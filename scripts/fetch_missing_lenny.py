#!/usr/bin/env python3
"""
Fetch missing Lenny's Podcast transcripts from YouTube auto-captions.
Batch 10 at a time, save as markdown with proper frontmatter.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime

RAW_DIR = Path.home() / ".hermes/podcast-wiki/raw/transcripts/lenny"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# The 87 missing video IDs with titles (from YouTube channel dump)
MISSING_FILE = Path("/tmp/checked-missing.txt")

# YouTube titles mapping (video_id -> title)
YT_TITLES = {}
if MISSING_FILE.exists():
    for line in MISSING_FILE.read_text().strip().split('\n'):
        if '|' in line:
            vid, title = line.split('|', 1)
            YT_TITLES[vid.strip()] = title.strip()


def get_transcript(video_id):
    """Fetch transcript using youtube_transcript_api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return None


def format_duration(seconds):
    """Format seconds to H:MM:SS or M:SS."""
    if seconds is None:
        return "0:00"
    seconds = int(seconds)
    h, m = divmod(seconds, 3600)
    m, s = divmod(m, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def extract_guest_name(title):
    """Extract guest name from YouTube title."""
    # Try "| Guest Name" pattern
    m = re.search(r'\|\s*(.+)$', title)
    if m:
        guest = m.group(1).strip()
        # Clean up common patterns
        guest = re.sub(r'\s*\(.*?\)\s*$', '', guest).strip()
        return guest
    
    # Try "with Guest Name" pattern
    m = re.search(r'with\s+(.+)$', title, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    
    return ""


def slugify(text):
    """Convert text to a filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].rstrip('-')


def transcript_to_text(transcript):
    """Convert YouTube transcript segments to plain text."""
    lines = []
    for seg in transcript:
        text = seg['text'].strip()
        timestamp = seg.get('start', 0)
        minutes = int(timestamp // 60)
        seconds = int(timestamp % 60)
        
        # Clean weird characters
        text = text.replace('&#39;', "'").replace('&amp;', '&').replace('&quot;', '"')
        
        # Format: [MM:SS] text
        lines.append(f"[{minutes:02d}:{seconds:02d}] {text}")
    
    return '\n'.join(lines)


def save_transcript(video_id, title, transcript, batch_num):
    """Save transcript as markdown file with frontmatter."""
    guest = extract_guest_name(title)
    slug = slugify(guest) if guest else slugify(title[:40])
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Build frontmatter
    fm = {
        'source': 'lenny',
        'guest': guest if guest else 'TBD',
        'title': title,
        'publish_date': date_str,
        'youtube_url': f'https://www.youtube.com/watch?v={video_id}',
        'video_id': video_id,
        'source_url': f'https://www.youtube.com/watch?v={video_id}',
        'wiki_slug': slug,
        'ingested_at': datetime.now().isoformat(),
    }
    
    # Full transcript text
    transcript_text = transcript_to_text(transcript)
    word_count = len(transcript_text.split())
    
    # If long transcript, also keep the JSON raw
    if word_count > 500:
        # Save full transcript with speaker-text format
        content_lines = []
        for seg in transcript:
            text = seg['text'].strip().replace('&#39;', "'").replace('&amp;', '&')
            content_lines.append(text)
        
        full_text = ' '.join(content_lines)
        
        body = f"""# {title}

Auto-generated transcript from YouTube auto-captions.
**Guest:** {guest if guest else 'Unknown'}
**Word count:** {word_count}
**Duration:** {len(transcript)} segments

## Transcript

{transcript_to_text(transcript)}
"""
    else:
        body = f"""# {title}

**Guest:** {guest if guest else 'Unknown'}
**Word count:** {word_count}

{transcript_to_text(transcript)}
"""
    
    # Write frontmatter + body as markdown
    content = "---\n" + yaml_safe(fm) + "---\n\n" + body
    
    filename = f"{slug}.md"
    filepath = RAW_DIR / filename
    
    # Avoid overwriting existing files
    counter = 1
    while filepath.exists():
        filename = f"{slug}-{counter}.md"
        filepath = RAW_DIR / filename
        counter += 1
    
    filepath.write_text(content, encoding='utf-8')
    
    return filename, word_count


def yaml_safe(data):
    """Simple YAML dumper that handles all types."""
    lines = []
    for key, value in data.items():
        if value is None:
            lines.append(f"{key}:")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        elif isinstance(value, str):
            escaped = value.replace('"', '\\"')
            if any(c in escaped for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']):
                lines.append(f'{key}: "{escaped}"')
            else:
                lines.append(f"{key}: {escaped}")
        else:
            lines.append(f"{key}: {repr(value)}")
    return '\n'.join(lines) + '\n'


def main():
    video_ids = list(YT_TITLES.keys())
    total = len(video_ids)
    print(f"Total missing transcripts to fetch: {total}")
    
    batch_size = 10
    success = 0
    failed = []
    skipped = []
    
    for batch_start in range(0, total, batch_size):
        batch = video_ids[batch_start:batch_start + batch_size]
        batch_num = (batch_start // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size
        
        print(f"\n{'='*60}")
        print(f"Batch {batch_num}/{total_batches} ({len(batch)} videos)")
        print(f"{'='*60}")
        
        for i, video_id in enumerate(batch):
            title = YT_TITLES.get(video_id, "Unknown")
            print(f"  [{batch_start + i + 1}/{total}] {video_id} — {title[:50]}...")
            
            transcript = get_transcript(video_id)
            if transcript is None:
                print(f"    ❌ No transcript available (no captions / private / age-restricted)")
                failed.append(video_id)
                continue
            
            if not transcript or len(transcript) < 5:
                print(f"    ❌ Too short ({len(transcript) if transcript else 0} segments)")
                failed.append(video_id)
                continue
            
            try:
                filename, wc = save_transcript(video_id, title, transcript, batch_num)
                print(f"    ✅ Saved: {filename} ({wc} words, {len(transcript)} segments)")
                success += 1
            except Exception as e:
                print(f"    ❌ Error saving: {e}")
                failed.append(video_id)
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
        
        # Report batch progress
        print(f"\n  Batch {batch_num} done. Running total: {success} success, {len(failed)} failed")
    
    # Final report
    print(f"\n{'='*60}")
    print(f"COMPLETE: {success} transcripts fetched, {len(failed)} failed")
    if failed:
        print(f"Failed videos ({len(failed)}):")
        for vid in failed:
            print(f"  {vid} — {YT_TITLES.get(vid, '?')[:60]}")
    
    # Save summary
    summary = {
        'total': total,
        'success': success,
        'failed': failed,
        'completed_at': datetime.now().isoformat(),
    }
    summary_path = RAW_DIR / '.fetch_summary.json'
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"\nSummary saved to {summary_path}")
    
    return 0 if len(failed) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
