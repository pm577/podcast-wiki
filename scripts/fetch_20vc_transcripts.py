#!/usr/bin/env python3
"""
20VC YouTube Transcript Fetcher — grabs free auto-generated captions from YouTube.

Strategy:
1. Search YouTube for each 20VC episode title
2. If found, download the captions via youtube-transcript-api
3. Update the wiki episode page with the full transcript

YouTube captions are free. This pipeline runs on recent episodes first.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime
from urllib.parse import quote, urlencode
import urllib.request
import urllib.parse

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
EPISODES_DIR = WIKI_DIR / "episodes" / "20vc"

# YouTube Data API key (optional — without it we use web scraping)
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between YouTube requests


def fetch_youtube_captions(video_id):
    """Fetch captions from YouTube using youtube-transcript-api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        
        # Convert to text
        text_parts = []
        for snippet in transcript.snippets:
            text_parts.append(snippet.text)
        
        full_text = ' '.join(text_parts)
        
        # Also get the timestamped version
        timestamped = []
        for snippet in transcript.snippets:
            minutes = int(snippet.start // 60)
            seconds = int(snippet.start % 60)
            timestamped.append(f"[{minutes:02d}:{seconds:02d}] {snippet.text}")
        
        return {
            'success': True,
            'full_text': full_text,
            'timestamped': '\n'.join(timestamped),
            'language': transcript.language,
            'is_generated': transcript.is_generated,
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}


def search_youtube_video(query):
    """Search YouTube for a video by title. Returns video_id or None."""
    if YOUTUBE_API_KEY:
        # Use official API
        params = {
            'part': 'snippet',
            'q': query,
            'maxResults': 1,
            'type': 'video',
            'key': YOUTUBE_API_KEY,
        }
        url = f"https://www.googleapis.com/youtube/v3/search?{urlencode(params)}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Clio/1.0'})
            resp = urllib.request.urlopen(req, timeout=10)
            data = json.loads(resp.read())
            if data.get('items'):
                return data['items'][0]['id']['videoId']
        except:
            pass
        return None
    else:
        # Scrape search page (last resort)
        try:
            url = f"https://www.youtube.com/results?search_query={quote(query)}"
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            })
            resp = urllib.request.urlopen(req, timeout=10)
            html = resp.read().decode('utf-8', errors='replace')
            
            # Extract video IDs from search results
            # Pattern: /watch?v=VIDEO_ID
            matches = re.findall(r'/watch\?v=([a-zA-Z0-9_-]{11})', html)
            if matches:
                return matches[0]
        except:
            pass
        return None


def read_episode_frontmatter(filepath):
    """Read the YAML frontmatter from an episode file."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    fm = {}
    body = content
    if content.startswith('---'):
        parts = content.split('---', 3)
        if len(parts) >= 3:
            try:
                fm = json.loads(parts[1])
            except:
                pass
            body = parts[2] if len(parts) > 2 else ''
    return fm, body, content


def update_episode_with_transcript(filepath, transcript_data):
    """Update an episode page with the full transcript."""
    fm, body, content = read_episode_frontmatter(filepath)
    
    # Add transcript metadata to frontmatter
    fm['has_transcript'] = True
    fm['transcript_language'] = transcript_data['language']
    fm['transcript_source'] = 'youtube'
    fm['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    
    # Rebuild the file
    new_content = "---\n" + json.dumps(fm, indent=2) + "\n---\n"
    
    # Keep the original title and metadata
    new_content += body.rstrip() + "\n\n"
    
    # Add transcript section
    new_content += "## Full Transcript\n\n"
    new_content += transcript_data['timestamped'][:15000]  # Cap at 15K chars
    new_content += "\n\n"
    
    filepath.write_text(new_content, encoding='utf-8')
    return True


def process_episode(filepath):
    """Process a single 20VC episode: search YouTube, fetch captions, update wiki."""
    fm, body, _ = read_episode_frontmatter(filepath)
    
    # Skip if we already have a transcript
    if fm.get('has_transcript'):
        return {'status': 'skipped', 'reason': 'Already has transcript'}
    
    title = fm.get('title', '')
    episode_id = filepath.stem
    
    # Build search query
    search_query = f"20VC {title[:80]}"
    
    # Rate limit
    time.sleep(REQUEST_DELAY)
    
    # Search YouTube
    video_id = search_youtube_video(search_query)
    if not video_id:
        return {'status': 'not_found', 'episode': episode_id, 'title': title[:50]}
    
    # Fetch captions
    transcript = fetch_youtube_captions(video_id)
    if not transcript['success']:
        return {'status': 'no_captions', 'episode': episode_id, 'error': transcript['error']}
    
    # Update wiki page
    update_episode_with_transcript(filepath, transcript)
    
    word_count = len(transcript['full_text'].split())
    return {
        'status': 'transcribed',
        'episode': episode_id,
        'title': title[:50],
        'video_id': video_id,
        'words': word_count,
    }


def main():
    print("=== 20VC YouTube Transcript Fetcher ===\n")
    
    if not EPISODES_DIR.exists():
        print(f"Error: {EPISODES_DIR} not found")
        return 1
    
    episodes = sorted(EPISODES_DIR.glob("*.md"), reverse=True)
    print(f"Found {len(episodes)} 20VC episodes\n")
    
    # Process recent episodes first
    target = min(100, len(episodes))  # Start with 100
    results = {'transcribed': 0, 'not_found': 0, 'no_captions': 0, 'skipped': 0, 'errors': []}
    
    for i, ep_file in enumerate(episodes[:target]):
        result = process_episode(ep_file)
        status = result['status']
        results[status] = results.get(status, 0) + 1
        
        icon = {'transcribed': '✅', 'skipped': '⏭️', 'not_found': '❌', 'no_captions': '⚠️'}.get(status, '❓')
        print(f"  [{i+1}/{target}] {icon} {ep_file.stem[:40]}... — {status}")
        
        if status == 'transcribed':
            print(f"         {result['words']} words from video {result['video_id']}")
        
        if 'error' in result:
            results['errors'].append(result['error'])
    
    print(f"\n=== Results ===")
    print(f"  Transcribed: {results['transcribed']}")
    print(f"  Not found on YouTube: {results['not_found']}")
    print(f"  No captions available: {results['no_captions']}")
    print(f"  Already had transcript: {results['skipped']}")
    if results['errors']:
        print(f"  Errors: {len(results['errors'])} (see above)")


if __name__ == "__main__":
    main()
