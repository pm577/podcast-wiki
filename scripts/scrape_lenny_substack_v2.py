#!/usr/bin/env python3
"""
Improved Lenny Substack scraper. Matches YouTube episode titles to Substack URLs
by extracting guest names + key title words, then fetches article content.
"""

import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

RAW_DIR = Path.home() / ".hermes/podcast-wiki/raw/transcripts/lenny"
SITEMAP_FILE = "/tmp/lenny-sitemap-urls.txt"
MISSING_FILE = "/tmp/lenny-missing-for-scraper.txt"

# Known exact mappings for tricky titles
KNOWN_MAPPINGS = {
    "-7Yol5vX5xw": "https://www.lennysnewsletter.com/p/snapchat-ceo-why-distribution-is",
    "8TpakBfsmcQ": "https://www.lennysnewsletter.com/p/the-quiet-architect-peter-deng",
    "adyIaTopO6g": "https://www.lennysnewsletter.com/p/naming-expert-david-placek",
    "apfL7ULrQ-I": "https://www.lennysnewsletter.com/p/embracing-chaos-vlad-loktev",
    "atS060bNpE0": "https://www.lennysnewsletter.com/p/4-questions-shreyas-wishes",
    "B26CwKm5C1k": "https://www.lennysnewsletter.com/p/engineers-are-becoming-sorcerers",
    "B6Dt1sgGmLI": "https://www.lennysnewsletter.com/p/identify-your-bullseye-customer",
    "BD3vLtWhT5A": "https://www.lennysnewsletter.com/p/a-rational-conversation-on-where",
    "bhnfZhJWCWY": "https://www.lennysnewsletter.com/p/how-to-consistently-go-viral-nikita-bier",
    "BIvVGhy_VxU": "https://www.lennysnewsletter.com/p/become-a-better-communicator-specific",
    "ciBdPH88C4c": "https://www.lennysnewsletter.com/p/10-contrarian-leadership-truths",
    "Cj4ORGGEJcA": "https://www.lennysnewsletter.com/p/46b-of-hard-truths-from-ben-horowitz",
    "cJo2Yf5UOEU": "https://www.lennysnewsletter.com/p/the-gitlab-way",
    "DBomzCnUDd8": "https://www.lennysnewsletter.com/p/the-common-mistake-most-managers-make",
    "DIa0MYJzM5I": "https://www.lennysnewsletter.com/p/how-openclaw-changed-my-life-claire-vo",
    "DkKGGfORHqw": "https://www.lennysnewsletter.com/p/a-field-guide-for-introverts-susan-cain",
    "dP8NmcEkxJI": "https://www.lennysnewsletter.com/p/how-to-measure-and-improve-developer-productivity",
    "e1R_-esuO9o": "https://www.lennysnewsletter.com/p/how-ai-is-reshaping-the-product-role",
    "eh8bcBIAAFo": "https://www.lennysnewsletter.com/p/the-design-process-is-dead",
    "eMe_FWldQF0": "https://www.lennysnewsletter.com/p/building-a-world-class-sales-org",
    "E_rNotqs--I": "https://www.lennysnewsletter.com/p/becoming-an-ai-pm-aman-khan",
    "FCxkT8ULrVg": "https://www.lennysnewsletter.com/p/how-to-create-a-winning-product-strategy",
    "Fves5chVZRA": "https://www.lennysnewsletter.com/p/the-creator-of-wordpress-opens-up-matt-mullenweg",
    "G5WTgB87rYQ": "https://www.lennysnewsletter.com/p/why-were-at-the-beginning-of-the",
    "HEqrvF7ztBE": "https://www.lennysnewsletter.com/p/a-behind-the-scenes-interview-with-lenny-rachitsky",
    "h-KVGHoQ_98": "https://www.lennysnewsletter.com/p/the-nature-of-product-marty-cagan",
    "HL7PS0fy1Ho": "https://www.lennysnewsletter.com/p/inside-gong-how-teams-work",
    "HzDLWKI6mnI": "https://www.lennysnewsletter.com/p/how-to-launch-and-grow-your-product-ryan-hoover",
    "IxkvVZua28k": "https://www.lennysnewsletter.com/p/a-conversation-with-openais-cpo-kevin-weil",
    "k-H4nsOTuxU": "https://www.lennysnewsletter.com/p/head-of-growth-anthropic",
    "-kHkWgjGD7U": "https://www.lennysnewsletter.com/p/storytelling-with-nancy-duarte-how",
    "-kN8Agqee4w": "https://www.lennysnewsletter.com/p/managing-nerves-anxiety-and-burnout",
    "-kPpd21bFrE": "https://www.lennysnewsletter.com/p/how-revolut-trains-world-class-pms",
    "L9KvV_UOs3A": "https://www.lennysnewsletter.com/p/the-base44-bootstrapped-startup-success-story-maor-shlomo",
    "L9qqwV8_rvY": "https://www.lennysnewsletter.com/p/inside-monday-coms-transformation",
    "-LywX3T5Scc": "https://www.lennysnewsletter.com/p/the-making-of-canva",
    "mCO-D3pkviM": "https://www.lennysnewsletter.com/p/why-cultivating-agency-matters-more",
    "mOY159TlYXM": "https://www.lennysnewsletter.com/p/the-ultimate-guide-to-seo-ethan-smith",
    "omk7ZUXveHw": "https://www.lennysnewsletter.com/p/young-product-managers",
    "PAF7KPxhvs0": "https://www.lennysnewsletter.com/p/the-kind-of-surprise",
    "PDobJV8wh1g": "https://www.lennysnewsletter.com/p/how-to-win-in-the-ai-era",
    "-PDsvl2WCZU": "https://www.lennysnewsletter.com/p/when-to-invest-in-new-acquisition",
    "pEis2CBomVA": "https://www.lennysnewsletter.com/p/the-ultimate-guide-to-negotiating",
    "PoJ1vTdHpks": "https://www.lennysnewsletter.com/p/how-to-build-a-company-that-withstands",
    "PplmzlgE0kg": "https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves",
    "puY_dxVKEwU": "https://www.lennysnewsletter.com/p/mercadolibre-18k-engineers",
    "PzTTum1gkGs": "https://www.lennysnewsletter.com/p/product-led-growth-b2b-companies-succeed",
    "-QsTmu2CqhA": "https://www.lennysnewsletter.com/p/anyone-can-cook-how-v0-is-bringing",
    "qU9ihr-kppo": "https://www.lennysnewsletter.com/p/my-favorite-interview-questions-from",
    "R5_ypwiRIyo": "https://www.lennysnewsletter.com/p/brian-cheskys-contrarian-approach",
    "R8uPpsDqJWk": "https://www.lennysnewsletter.com/p/shreyas-doshi-live",
    "_rcniEb9bLw": "https://www.lennysnewsletter.com/p/the-real-ai-revolution-isnt-software",
    "rMqElZhqeRg": "https://www.lennysnewsletter.com/p/the-interview-question-that-challenges",
    "RP4vJeIb7WU": "https://www.lennysnewsletter.com/p/the-art-of-influence-jessica-fain",
    "sOyFpSW1Vls": "https://www.lennysnewsletter.com/p/behind-the-product-notebooklm",
    "T4LGBZ0uO_4": "https://www.lennysnewsletter.com/p/imposter-syndrome-and-5-tips",
    "-tUIGpgmsZw": "https://www.lennysnewsletter.com/p/behind-the-scenes-of-calendlys-rapid",
    "tX6nwT1Bsuo": "https://www.lennysnewsletter.com/p/a-4-step-framework-for-building-delightful-products",
    "UbjAOCzpNWc": "https://www.lennysnewsletter.com/p/the-foundation-sprint-jake-knapp-and-john-zeratsky",
    "UhASMW6X4AY": "https://www.lennysnewsletter.com/p/my-favorite-interview-questions-from",
    "UTmFuSZfJ9U": "https://www.lennysnewsletter.com/p/10-growth-tactics-that-never-work-elena-verna",
    "V7tnbx-6Ayc": "https://www.lennysnewsletter.com/p/radical-candor-from-theory-to-practice",
    "Vlph3dn4jnU": "https://www.lennysnewsletter.com/p/breaking-the-rules-of-growth-shopify",
    "-VqmFI9vY7w": "https://www.lennysnewsletter.com/p/a-step-by-step-guide-to-crafting",
    "wc8FBhQtdsA": "https://www.lennysnewsletter.com/p/an-ai-state-of-the-union",
    "We7BZVKbCVw": "https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens",
    "wFhurV1l6Jk": "https://www.lennysnewsletter.com/p/the-super-ic-pm-tal-raviv",
    "wprxOrDpB0U": "https://www.lennysnewsletter.com/p/sriram-krishnan-does-not-like",
    "WWoyWNhx2XU": "https://www.lennysnewsletter.com/p/anthropic-co-founder-benjamin-mann",
    "xCd9ykretlg": "https://www.lennysnewsletter.com/p/hard-truths-about-building-in-the-ai-era",
    "YErOtGMgTNg": "https://www.lennysnewsletter.com/p/what-most-people-miss-about-marketing",
    "ylNKlBlkFas": "https://www.lennysnewsletter.com/p/ai-is-critical-for-humanitys-survival",
    "YLsxHa1dhSw": "https://www.lennysnewsletter.com/p/overcome-imposter-syndrome-julie-zhuo",
    "YrUq8JUkQls": "https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms",
    "yUohoaC8_Hs": "https://www.lennysnewsletter.com/p/why-half-of-product-managers-are-in-trouble",
    "ywkwUvJlFn0": "https://www.lennysnewsletter.com/p/just-evil-enough-subversive-marketing",
    "z1ISq9Ty4Cg": "https://www.lennysnewsletter.com/p/inside-openai-2026-is-the-year",
    "ZG3iNH4vvMA": "https://www.lennysnewsletter.com/p/brian-balfour-10-lessons-on-career",
    "6XMUDEYf2OE": "https://www.lennysnewsletter.com/p/thinking-beyond-frameworks-casey",
    "93fCvFkY1Lg": "https://www.lennysnewsletter.com/p/product-management-is-dead-what-are-we-doing",
    "CvC_ZJGNW8c": "https://www.lennysnewsletter.com/p/crafting-a-compelling-product-vision",
    "-ljxHsuwz98": "https://www.lennysnewsletter.com/p/rituals-of-great-decision-making",
    "oItg64eaRlc": "https://www.lennysnewsletter.com/p/simplify-to-win",
    "Q5PX2DpRqEI": "https://www.lennysnewsletter.com/p/how-to-craft-an-elite-career",
    "W1coI_d9MsQ": "https://www.lennysnewsletter.com/p/how-to-do-the-product-review-right",
    "XYMvtmPGcmU": "https://www.lennysnewsletter.com/p/making-and-leading-products-people-love",
}


class SubstackExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self._title = ""
        self._text = []
        self._in_title = False
        self._in_content = False
        self._depth = 0
        self._skip = 0
        self._in_script = False
        self._in_style = False
    
    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        if tag in ('script', 'style'):
            self._skip += 1
            return
        if tag == 'title':
            self._in_title = True
        if tag == 'body':
            self._in_content = True
        if tag == 'header':
            self._in_content = False
        if tag in ('div', 'section', 'article') and self._in_content:
            cls = ad.get('class', '')
            if any(x in cls for x in ['post-content', 'body', 'article-body', 'available-content']):
                self._in_content = True
                self._depth += 1
    
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            if self._skip > 0:
                self._skip -= 1
            return
        if tag == 'title':
            self._in_title = False
        if tag in ('div', 'section', 'article') and self._depth > 0:
            self._depth -= 1
    
    def handle_data(self, data):
        if self._skip > 0:
            return
        if self._in_title:
            self._title += data
        elif self._in_content and self._depth > 0:
            d = data.strip()
            if d:
                self._text.append(d)
    
    @property
    def title(self):
        return self._title.strip()
    
    @property
    def content(self):
        return ' '.join(self._text)


def fetch(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('utf-8', errors='replace')
        except Exception as e:
            if i < retries - 1:
                time.sleep(2 ** i)
    return None


def extract_guest(title):
    m = re.search(r'\|\s*(.+)$', title)
    return m.group(1).strip() if m else ""


def slugify(t):
    t = t.lower().strip()
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    t = re.sub(r'[\s_]+', '-', t)
    t = re.sub(r'-+', '-', t)
    return t[:60].rstrip('-')


def match_url(title, video_id, sitemap_urls):
    """Find best matching URL for a title."""
    # Check known mappings first
    if video_id in KNOWN_MAPPINGS:
        return KNOWN_MAPPINGS[video_id]
    
    # Try guest name
    guest = extract_guest(title)
    if guest:
        for part in re.split(r'[,&]', guest):
            part = part.strip()
            slug = slugify(part)
            if len(slug) > 3:
                for url in sitemap_urls:
                    if slug in url.lower():
                        return url
    
    # Try title keywords
    words = set(re.findall(r'[a-zA-Z]{4,}', title.lower()))
    stopwords = {'that', 'this', 'with', 'from', 'what', 'when', 'your', 'more', 'they', 'their'}
    words = words - stopwords
    
    best_url, best_score = None, 0
    for url in sitemap_urls:
        ul = url.lower()
        score = sum(1 for w in words if w in ul)
        if score > best_score:
            best_score = score
            best_url = url
    
    return best_url if best_score >= 2 else None


def main():
    print("=" * 60)
    
    # Load data
    sitemap_urls = set(open(SITEMAP_FILE).read().strip().split('\n'))
    print(f"Sitemap: {len(sitemap_urls)} URLs")
    
    videos = []
    for line in open(MISSING_FILE):
        if '|' in line:
            v, t = line.strip().split('|', 1)
            videos.append((v.strip(), t.strip()))
    
    print(f"Missing: {len(videos)} videos")
    
    # Match URLs
    mapped = []
    unmapped = []
    for vid, title in videos:
        url = match_url(title, vid, sitemap_urls)
        if url:
            mapped.append((vid, title, url))
        else:
            unmapped.append((vid, title))
    
    print(f"Matched: {len(mapped)}, Unmatched: {len(unmapped)}")
    
    if unmapped:
        print("\nUnmatched:")
        for v, t in unmapped:
            print(f"  {v} — {t[:60]}")
    
    # Scrape in batches
    batch_size = 10
    total = len(mapped)
    success, failed = 0, []
    
    for i, (vid, title, url) in enumerate(mapped):
        print(f"\n[{i+1}/{total}] {title[:55]}...")
        
        html = fetch(url)
        if not html:
            print(f"  ❌ Fetch failed")
            failed.append((vid, title, url))
            continue
        
        ext = SubstackExtractor()
        try:
            ext.feed(html)
        except:
            pass
        
        content = ext.content
        page_title = ext.title
        
        if not content or len(content) < 80:
            # Try finding content in meta description
            m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', html)
            if m:
                content = m.group(1)
            else:
                # Try finding tweet or article body text
                body = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
                if body:
                    text = re.sub(r'<[^>]+>', ' ', body.group(1))
                    text = re.sub(r'\s+', ' ', text).strip()
                    content = text
        
        if not content or len(content) < 50:
            print(f"  ❌ No content")
            failed.append((vid, title, url))
            continue
        
        # Save
        guest = extract_guest(title)
        slug = slugify(guest) if guest else slugify(title[:40])
        
        date_str = datetime.now().strftime('%Y-%m-%d')
        wc = len(content.split())
        
        body = f"""---
source: lenny
guest: "{guest}"
title: "{title}"
publish_date: "{date_str}"
source_url: "{url}"
wiki_slug: "{slug}"
ingested_at: "{datetime.now().isoformat()}"
source_type: "substack"
---

# {title}

**Source:** [Substack article]({url})
**Guest:** {guest}
**Word count:** {wc}

---

{content}
"""
        filename = f"{slug}.md"
        fp = RAW_DIR / filename
        c = 1
        while fp.exists():
            fp = RAW_DIR / f"{slug}-{c}.md"
            c += 1
        
        fp.write_text(body)
        print(f"  ✅ {fp.name} ({wc} words)")
        success += 1
        
        if (i + 1) % batch_size == 0:
            print(f"\n--- Batch checkpoint: {success}/{i+1} successful ---")
        
        time.sleep(1.5)  # polite rate limit
    
    print(f"\n{'='*60}")
    print(f"Done: {success} scraped, {len(failed)} failed")
    if failed:
        print("Failed:", [(v, u) for v, _, u in failed])
    if unmapped:
        print(f"Unmapped: {len(unmapped)}")
    
    return 0 if not failed else 1


if __name__ == '__main__':
    sys.exit(main())
