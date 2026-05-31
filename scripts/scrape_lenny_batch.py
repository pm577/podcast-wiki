#!/usr/bin/env python3
"""
Batch scrape Lenny's missing episode transcripts from Substack.
Uses _preloads JSON blob for full article content.
"""
import sys, re, json, os, time
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
import html as html_mod

RAW_DIR = Path.home() / ".hermes/podcast-wiki/raw/transcripts/lenny"
SITEMAP_FILE = "/tmp/lenny-sitemap-urls.txt"
MISSING_FILE = "/tmp/lenny-missing-scrape-v2.txt"

# Known URL mappings
KNOWN = {
    "4D3hDmGhFhA": "https://www.lennysnewsletter.com/p/the-ai-paradox-dan-shipper",
    "6XMUDEYf2OE": "https://www.lennysnewsletter.com/p/thinking-beyond-frameworks-casey",
    "-7Yol5vX5xw": "https://www.lennysnewsletter.com/p/snapchat-ceo-why-distribution-is",
    "8TpakBfsmcQ": "https://www.lennysnewsletter.com/p/the-quiet-architect-peter-deng",
    "93fCvFkY1Lg": "https://www.lennysnewsletter.com/p/product-management-is-dead-what-are-we-doing",
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
    "CvC_ZJGNW8c": "https://www.lennysnewsletter.com/p/crafting-a-compelling-product-vision",
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
    "-ljxHsuwz98": "https://www.lennysnewsletter.com/p/rituals-of-great-decision-making",
    "-LywX3T5Scc": "https://www.lennysnewsletter.com/p/the-making-of-canva",
    "mCO-D3pkviM": "https://www.lennysnewsletter.com/p/why-cultivating-agency-matters-more",
    "mOY159TlYXM": "https://www.lennysnewsletter.com/p/the-ultimate-guide-to-seo-ethan-smith",
    "oItg64eaRlc": "https://www.lennysnewsletter.com/p/simplify-to-win",
    "omk7ZUXveHw": "https://www.lennysnewsletter.com/p/young-product-managers",
    "PAF7KPxhvs0": "https://www.lennysnewsletter.com/p/the-kind-of-surprise",
    "PDobJV8wh1g": "https://www.lennysnewsletter.com/p/how-to-win-in-the-ai-era",
    "-PDsvl2WCZU": "https://www.lennysnewsletter.com/p/when-to-invest-in-new-acquisition",
    "pEis2CBomVA": "https://www.lennysnewsletter.com/p/the-ultimate-guide-to-negotiating",
    "PoJ1vTdHpks": "https://www.lennysnewsletter.com/p/how-to-build-a-company-that-withstands",
    "PplmzlgE0kg": "https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves",
    "puY_dxVKEwU": "https://www.lennysnewsletter.com/p/mercadolibre-18k-engineers",
    "PzTTum1gkGs": "https://www.lennysnewsletter.com/p/product-led-growth-b2b-companies-succeed",
    "Q5PX2DpRqEI": "https://www.lennysnewsletter.com/p/how-to-craft-an-elite-career",
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
    "W1coI_d9MsQ": "https://www.lennysnewsletter.com/p/how-to-do-the-product-review-right",
    "wc8FBhQtdsA": "https://www.lennysnewsletter.com/p/an-ai-state-of-the-union",
    "We7BZVKbCVw": "https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens",
    "wFhurV1l6Jk": "https://www.lennysnewsletter.com/p/the-super-ic-pm-tal-raviv",
    "wprxOrDpB0U": "https://www.lennysnewsletter.com/p/sriram-krishnan-does-not-like",
    "WWoyWNhx2XU": "https://www.lennysnewsletter.com/p/anthropic-co-founder-benjamin-mann",
    "xCd9ykretlg": "https://www.lennysnewsletter.com/p/hard-truths-about-building-in-the-ai-era",
    "XYMvtmPGcmU": "https://www.lennysnewsletter.com/p/making-and-leading-products-people-love",
    "YErOtGMgTNg": "https://www.lennysnewsletter.com/p/what-most-people-miss-about-marketing",
    "ylNKlBlkFas": "https://www.lennysnewsletter.com/p/ai-is-critical-for-humanitys-survival",
    "YLsxHa1dhSw": "https://www.lennysnewsletter.com/p/overcome-imposter-syndrome-julie-zhuo",
    "YrUq8JUkQls": "https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms",
    "yUohoaC8_Hs": "https://www.lennysnewsletter.com/p/why-half-of-product-managers-are-in-trouble",
    "ywkwUvJlFn0": "https://www.lennysnewsletter.com/p/just-evil-enough-subversive-marketing",
    "z1ISq9Ty4Cg": "https://www.lennysnewsletter.com/p/inside-openai-2026-is-the-year",
    "ZG3iNH4vvMA": "https://www.lennysnewsletter.com/p/brian-balfour-10-lessons-on-career",
}


def fetch(url):
    """Fetch a URL."""
    import urllib.request
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('utf-8', errors='replace')
        except Exception as e:
            if i < 2:
                time.sleep(2 ** i)
    return None


def extract_json(html):
    """Extract and parse the _preloads JSON blob."""
    jp = html.find('JSON.parse("', html.find('window._preloads'))
    if jp < 0:
        return None
    start = jp + 12
    chars = []
    i = start
    while i < len(html):
        c = html[i]
        if c == '\\' and i+1 < len(html):
            n = html[i+1]
            if n == '\\': chars.append('\\'); i += 2
            elif n == '"': chars.append('"'); i += 2
            elif n == 'n': chars.append('\n'); i += 2
            elif n == 't': chars.append('\t'); i += 2
            elif n == 'u': 
                hex_str = html[i+2:i+6]
                if len(hex_str) == 4: chars.append(chr(int(hex_str, 16)))
                i += 6
            else: chars.append(n); i += 2
            continue
        if c == '"' and html[i+1:i+2] == ')':
            break
        chars.append(c)
        i += 1
    try:
        return json.loads(''.join(chars))
    except:
        return None


def strip_html(content):
    """Strip HTML tags and clean whitespace."""
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    text = html_mod.unescape(text)
    return text


def extract_guest(title):
    m = re.search(r'\|\s*(.+)$', title)
    return m.group(1).strip() if m else ""


def slugify(t):
    t = t.lower().strip()
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    t = re.sub(r'[\s_]+', '-', t)
    return re.sub(r'-+', '-', t)[:60].rstrip('-')


def main():
    print("=" * 60)
    print("Lenny Substack Batch Scraper")
    print("=" * 60)

    # Load missing videos
    videos = []
    for line in open(MISSING_FILE):
        if '|' in line:
            v, t = line.strip().split('|', 1)
            videos.append((v.strip(), t.strip()))
    
    print(f"Total: {len(videos)}")
    
    success = 0
    failed = []
    
    for i, (vid, title) in enumerate(videos):
        url = KNOWN.get(vid)
        if not url:
            failed.append((vid, title, "NO_URL"))
            continue
        
        # Check if this video already has a good transcript
        guest = extract_guest(title)
        slug = slugify(guest) if guest else slugify(title[:40])
        existing = list(RAW_DIR.glob(f"{slug}*.md"))
        if existing:
            # Check if any existing file has real content (>100 words)
            has_good = False
            for ef in existing:
                content = ef.read_text(encoding='utf-8', errors='replace')
                # Count words in the body (after the frontmatter)
                body_start = content.find('\n\n')
                if body_start > 0:
                    body = content[body_start:]
                    if len(body.split()) > 100:
                        has_good = True
                        break
            if has_good:
                print(f"\n[{i+1}/{len(videos)}] ⏭️  Already scraped: {title[:50]}...")
                continue
        
        print(f"\n[{i+1}/{len(videos)}] {title[:50]}...")
        
        html = fetch(url)
        if not html:
            print(f"  ❌ Fetch failed")
            failed.append((vid, title, "FETCH"))
            continue
        
        data = extract_json(html)
        if not data:
            print(f"  ❌ JSON extract failed")
            failed.append((vid, title, "JSON"))
            continue
        
        post = data.get('post', {})
        body_html = post.get('body_html', '')
        
        if not body_html or len(body_html) < 100:
            print(f"  ❌ No body_html ({len(body_html)} chars)")
            failed.append((vid, title, f"NO_BODY:{len(body_html)}"))
            continue
        
        content = strip_html(body_html)
        wc = len(content.split())
        
        guest = extract_guest(title)
        slug = slugify(guest) if guest else slugify(title[:40])
        
        # Get post date from preloads
        post_date = post.get('post_date', '')[:10]
        if not post_date:
            post_date = datetime.now().strftime('%Y-%m-%d')
        
        # Save
        body = f"""---
source: lenny
guest: "{guest}"
title: "{title}"
publish_date: "{post_date}"
source_url: "{url}"
wiki_slug: "{slug}"
ingested_at: "{datetime.now().isoformat()}"
source_type: "substack"
---

# {title}

**Source:** [Substack article]({url})
**Guest:** {guest}
**Date:** {post_date}
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
        
        fp.write_text(body, encoding='utf-8', errors='replace')
        print(f"  ✅ {fp.name} ({wc} words)")
        success += 1
        
        if (i + 1) % 10 == 0:
            print(f"\n-- Checkpoint: {success}/{i+1} --")
        
        time.sleep(1.5)
    
    print(f"\n{'='*60}")
    print(f"Done: {success} scraped, {len(failed)} failed")
    if failed:
        print("Failed:")
        for v, t, reason in failed:
            print(f"  {v} — {t[:50]} → {reason}")
    
    return 0 if not failed else 1


if __name__ == '__main__':
    sys.exit(main())
