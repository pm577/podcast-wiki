#!/usr/bin/env python3
"""
Scrape Lenny's Podcast missing episodes from Substack newsletter articles.
Matches missing YouTube videos to Substack posts and extracts content.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

RAW_DIR = Path.home() / ".hermes/podcast-wiki/raw/transcripts/lenny"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Load sitemap URLs
SITEMAP_FILE = "/tmp/lenny-sitemap-urls.txt"
# Load missing videos
MISSING_FILE = "/tmp/lenny-missing-for-scraper.txt"


class SubstackExtractor(HTMLParser):
    """Extract article content from Substack HTML."""
    def __init__(self):
        super().__init__()
        self.reset_state()
        self.title = ""
        self.body_text = []
        self.in_body = False
        self.in_title = False
        self.in_header = False
        self.in_script = False
        self.in_style = False
        self.skip_tags = {'script', 'style', 'nav', 'footer', 'header', 'aside'}
        self.skip_depth = 0
        self.content_div_depth = 0
        self.in_content_div = False
        self.content_div_class = ""
        
    def reset_state(self):
        self.title = ""
        self.body_text = []
        self.in_body = False
        self.in_title = False
        self.in_header = False
        self.in_script = False
        self.in_style = False
        self.skip_depth = 0
        self.content_div_depth = 0
        self.in_content_div = False
        self.content_div_class = ""
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag in self.skip_tags:
            self.skip_depth += 1
            return
            
        if tag == 'title':
            self.in_title = True
        
        if tag == 'body':
            self.in_body = True
            
        if tag == 'header':
            self.in_header = True
            
        # Find the main content div
        if tag == 'div' and self.in_body and not self.in_header:
            classes = attrs_dict.get('class', '')
            if 'body' in classes or 'content' in classes or 'article' in classes or 'post' in classes:
                if not self.in_content_div:
                    self.in_content_div = True
                    self.content_div_depth = 1
            if self.in_content_div:
                self.content_div_depth += 1
                
        if tag == 'h1' and self.in_content_div:
            self.in_title = True
        elif tag == 'h2' and self.in_content_div:
            self.body_text.append('\n\n')
        elif tag == 'p' and self.in_content_div:
            pass  # we'll add text content
        elif tag == 'br' and self.in_content_div:
            self.body_text.append('\n')
        elif tag in ('ul', 'ol') and self.in_content_div:
            self.body_text.append('\n')
        elif tag == 'li' and self.in_content_div:
            self.body_text.append('\n• ')
        elif tag == 'blockquote' and self.in_content_div:
            pass
        elif tag in ('strong', 'b') and self.in_content_div:
            pass
        elif tag in ('em', 'i') and self.in_content_div:
            pass
        elif tag == 'a' and self.in_content_div:
            href = attrs_dict.get('href', '')
            if href and not href.startswith('#'):
                pass  # we'll add the text, not the link
    
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return
            
        if tag == 'title':
            self.in_title = False
            
        if tag == 'h1' and self.in_content_div:
            self.body_text.append('\n\n')
            self.in_title = False
            
        if tag == 'p' and self.in_content_div:
            self.body_text.append('\n\n')
            
        if tag == 'div' and self.in_content_div:
            self.content_div_depth -= 1
            if self.content_div_depth <= 0:
                self.in_content_div = False
    
    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        if self.in_title:
            self.title += data.strip()
            return
        if self.in_content_div:
            text = data.strip()
            if text:
                # Clean up whitespace
                text = re.sub(r'\s+', ' ', text)
                self.body_text.append(text)
    
    def get_content(self):
        body = ' '.join(self.body_text)
        # Clean up excessive whitespace
        body = re.sub(r'\n{3,}', '\n\n', body)
        body = re.sub(r' {2,}', ' ', body)
        body = re.sub(r'•\s+', '• ', body)
        return body.strip()


def fetch_page(url, retries=3):
    """Fetch a URL with retries."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req, timeout=30)
            html = resp.read().decode('utf-8', errors='replace')
            return html
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None


def extract_guest_name(title):
    """Extract guest name from YouTube title."""
    m = re.search(r'\|\s*(.+)$', title)
    if m:
        guest = m.group(1).strip()
        guest = re.sub(r'\s*\(.*?\)\s*$', '', guest).strip()
        return guest
    return ""


def extract_content_from_html(html):
    """Extract title and body content from Substack HTML."""
    extractor = SubstackExtractor()
    try:
        extractor.feed(html)
        title = extractor.title
        content = extractor.get_content()
        return title, content
    except Exception as e:
        return "", ""


def clean_content(content):
    """Clean up extracted content."""
    # Remove common Substack noise
    noise_patterns = [
        r'Listen to this episode.*?(?=\n|$)',
        r'Share this discussion.*',
        r'Ready for more.*',
        r'Substack.*',
        r'Comments.*',
        r'Reply.*',
    ]
    for pat in noise_patterns:
        content = re.sub(pat, '', content, flags=re.IGNORECASE | re.DOTALL)
    
    return content.strip()


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].rstrip('-')


def find_matching_url(title, sitemap_urls):
    """Find the best matching Substack URL for a given episode title."""
    # Extract key parts from title
    title_lower = title.lower()
    
    # Try exact guest name match first (after |)
    guest = extract_guest_name(title).lower()
    if guest:
        guest_slug = slugify(guest)
        for url in sitemap_urls:
            if guest_slug in url.lower() and len(guest_slug) > 3:
                return url
    
    # Try matching key unique words
    words = set(re.findall(r'[a-z]{4,}', title_lower))
    important = {'ai', 'product', 'growth', 'building', 'future', 'guide', 
                 'inside', 'secrets', 'leadership', 'interview', 'ceo', 'founder'}
    words = {w for w in words if len(w) > 3 or w in important}
    
    best_url = None
    best_score = 0
    
    for url in sitemap_urls:
        url_lower = url.lower()
        score = sum(1 for w in words if w in url_lower and len(w) > 3)
        if score > best_score:
            best_score = score
            best_url = url
    
    if best_score >= 2:  # at least 2 key words match
        return best_url
    
    return None


def save_transcript(video_id, title, substack_url, raw_content):
    """Save extracted content as a transcript markdown file."""
    guest = extract_guest_name(title)
    slug = slugify(guest) if guest else slugify(title[:40])
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Build word count
    word_count = len(raw_content.split())
    
    # Build frontmatter
    fm_lines = [
        '---',
        f'source: lenny',
        f'guest: "{guest}"' if guest else 'guest: TBD',
        f'title: "{title}"',
        f'publish_date: "{date_str}"',
        f'source_url: "{substack_url}"',
        f'wiki_slug: "{slug}"',
        f'ingested_at: "{datetime.now().isoformat()}"',
        f'source_type: "substack"',
        '---',
        '',
        f'# {title}',
        '',
        f'Source: [Substack article]({substack_url})',
        f'**Guest:** {guest}' if guest else '',
        f'**Word count:** {word_count}',
        '',
        '---',
        '',
        raw_content,
    ]
    
    content = '\n'.join(fm_lines)
    
    filename = f"{slug}.md"
    filepath = RAW_DIR / filename
    
    counter = 1
    while filepath.exists():
        filename = f"{slug}-{counter}.md"
        filepath = RAW_DIR / filename
        counter += 1
    
    filepath.write_text(content, encoding='utf-8')
    return filename, word_count


def load_sitemap_urls():
    """Load sitemap URLs from file or fetch."""
    if os.path.exists(SITEMAP_FILE):
        urls = open(SITEMAP_FILE).read().strip().split('\n')
        return sorted(set(urls))
    
    # Fetch and cache
    print("Fetching sitemap...")
    html = fetch_page("https://www.lennysnewsletter.com/sitemap.xml")
    if html:
        urls = re.findall(r'https://www\.lennysnewsletter\.com/p/[^<]+', html)
        urls = sorted(set(urls))
        Path(SITEMAP_FILE).write_text('\n'.join(urls))
        print(f"Found {len(urls)} sitemap URLs")
        return urls
    return []


def main():
    print("=" * 60)
    print("Lenny's Podcast → Substack Scraper")
    print("=" * 60)
    
    # Load missing videos
    if not os.path.exists(MISSING_FILE):
        print(f"ERROR: Missing file not found: {MISSING_FILE}")
        return 1
    
    videos = []
    for line in open(MISSING_FILE).read().strip().split('\n'):
        if '|' in line:
            vid, title = line.split('|', 1)
            videos.append((vid.strip(), title.strip()))
    
    print(f"Total missing videos: {len(videos)}")
    
    # Load sitemap URLs
    sitemap_urls = load_sitemap_urls()
    print(f"Sitemap URLs: {len(sitemap_urls)}")
    
    # Match each missing video to a Substack URL
    matched = []
    unmatched = []
    
    for vid, title in videos:
        url = find_matching_url(title, sitemap_urls)
        if url:
            matched.append((vid, title, url))
        else:
            unmatched.append((vid, title))
    
    print(f"\nMatched to Substack: {len(matched)}")
    print(f"Unmatched: {len(unmatched)}")
    
    if unmatched:
        print("\nUnmatched episodes (no Substack URL found):")
        for vid, title in unmatched:
            print(f"  {vid} — {title[:60]}")
    
    # Fetch and extract content
    print(f"\n{'='*60}")
    print(f"Fetching {len(matched)} Substack articles...")
    print(f"{'='*60}")
    
    success = 0
    failed = []
    
    for i, (vid, title, url) in enumerate(matched):
        print(f"\n[{i+1}/{len(matched)}] {title[:60]}...")
        
        html = fetch_page(url)
        if not html:
            print(f"  ❌ Failed to fetch {url}")
            failed.append((vid, title, url))
            continue
        
        page_title, content = extract_content_from_html(html)
        
        if not content or len(content) < 100:
            # Try alternate extraction
            print(f"  ⚠️  Short content ({len(content)} chars), trying alternate...")
            # Fallback: use page description if content too short
            meta_desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', html)
            if meta_desc:
                content = meta_desc.group(1)
                print(f"  Using meta description instead")
        
        if not content or len(content) < 50:
            print(f"  ❌ No content extracted")
            failed.append((vid, title, url))
            continue
        
        content = clean_content(content)
        
        try:
            filename, wc = save_transcript(vid, title, url, content)
            print(f"  ✅ Saved: {filename} ({wc} words)")
            success += 1
        except Exception as e:
            print(f"  ❌ Error saving: {e}")
            failed.append((vid, title, url))
        
        time.sleep(1)  # Rate limit
    
    # Summary
    print(f"\n{'='*60}")
    print(f"COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully scraped: {success}")
    print(f"Failed: {len(failed)}")
    
    if failed:
        print("\nFailed:")
        for vid, title, url in failed:
            print(f"  {vid} — {url}")
    
    if unmatched:
        print(f"\nNo Substack match for {len(unmatched)} episodes:")
        for vid, title in unmatched:
            print(f"  {vid} — {title[:60]}")
    
    return 0 if len(failed) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
