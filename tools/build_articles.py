"""Builds the article pages of advjalajsharma.in from tools/articles_content.py.

Run from the repository root:  python3 tools/build_articles.py
Each article follows the same six questions so readers can scan it quickly.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from articles_content import ARTICLES  # noqa: E402

SITE = "https://advjalajsharma.in"

UI = {
    "en": {
        "skip": "Skip to content",
        "crumb": "← Legal guides",
        "back": "← Back to legal guides",
        "short": "In short",
        "faq": "Common questions",
        "note": "This guide is general information on the law as it stands in {month}. It is not legal advice; time limits and outcomes depend on the facts of each case.",
        "nav": [("index.html#practice", "Practice"), ("index.html#guidance", "Legal guides"), ("index.html#faq", "FAQ"), ("index.html#consult", "Contact")],
        "brand": "Jalaj Sharma",
        "read": "min read",
        "by": "Jalaj Sharma, Advocate",
    },
    "hi": {
        "skip": "सामग्री पर जाएँ",
        "crumb": "← कानूनी जानकारी",
        "back": "← कानूनी जानकारी पर वापस जाएँ",
        "short": "संक्षेप में",
        "faq": "आम सवाल",
        "note": "यह गाइड {month} तक के कानून पर सामान्य जानकारी है, कानूनी सलाह नहीं। समय-सीमा और परिणाम हर मामले के तथ्यों पर निर्भर करते हैं।",
        "nav": [("index.html#practice", "प्रैक्टिस"), ("index.html#guidance", "कानूनी जानकारी"), ("index.html#faq", "सवाल-जवाब"), ("index.html#consult", "संपर्क")],
        "brand": "जलज शर्मा",
        "read": "मिनट",
        "by": "जलज शर्मा, अधिवक्ता",
    },
}


def shared_parts():
    """Disclaimer, contact band and footer are taken from the home page so they stay in sync."""
    home = (ROOT / "index.html").read_text()
    gate = re.search(r'<div class="gate".*?\n</div>\n', home, re.S).group(0)
    gate = re.sub(r'\s*<div class="lang" role="group" aria-label="Language">.*?</div>', "", gate, count=1, flags=re.S)
    contact = re.search(r'<section class="contact".*?</section>', home, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", home, re.S).group(0)
    return gate, contact, footer


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def build(a, gate, contact, footer):
    lang = a["lang"]
    ui = UI[lang]
    slug = a["slug"]
    url = f"{SITE}/{slug}"

    alternates = ""
    lang_switch = ""
    if a.get("alt"):
        alt_slug, alt_lang = a["alt"]
        alternates = (
            f'<link rel="alternate" hreflang="{"en-IN" if lang == "en" else "hi-IN"}" href="{url}">\n'
            f'<link rel="alternate" hreflang="{"hi-IN" if alt_lang == "hi" else "en-IN"}" href="{SITE}/{alt_slug}">\n'
        )
        if lang == "en":
            lang_switch = (
                '      <div class="lang" role="group" aria-label="Language">\n'
                f'        <a aria-current="true" href="{slug}.html" data-set="en">English</a>\n'
                f'        <a href="{alt_slug}.html" data-set="hi" hreflang="hi" lang="hi">हिंदी</a>\n'
                "      </div>"
            )
        else:
            lang_switch = (
                '      <div class="lang" role="group" aria-label="भाषा">\n'
                f'        <a href="{alt_slug}.html" data-set="en" hreflang="en" lang="en">English</a>\n'
                f'        <a aria-current="true" href="{slug}.html" data-set="hi">हिंदी</a>\n'
                "      </div>"
            )

    nav = "\n".join(f'      <a href="{h}">{t}</a>' for h, t in ui["nav"])

    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["h1"],
        "description": a["description"],
        "datePublished": a["published"],
        "dateModified": a["modified"],
        "inLanguage": "en-IN" if lang == "en" else "hi-IN",
        "author": {"@type": "Person", "name": "Jalaj Sharma", "jobTitle": "Advocate", "url": SITE + "/"},
        "mainEntityOfPage": url,
        "image": SITE + "/assets/share.jpg",
        "keywords": a["keywords"],
    }
    faq_ld = None
    if a.get("faqs"):
        faq_ld = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)}}
                for q, ans in a["faqs"]
            ],
        }

    summary = "".join(f"      <li>{li}</li>\n" for li in a["summary"])
    sections = ""
    for i, (h2, body) in enumerate(a["sections"], 1):
        sections += f'    <h2 id="s{i}"><span class="qn">{i}.</span> {h2}</h2>\n{body.strip()}\n\n'
    faqs = ""
    if a.get("faqs"):
        faqs = f'    <h2 id="faq">{ui["faq"]}</h2>\n    <div class="faq">\n'
        for q, ans in a["faqs"]:
            faqs += f"      <details>\n        <summary>{q}</summary>\n        <p>{ans}</p>\n      </details>\n"
        faqs += "    </div>\n\n"
    other = ""
    if a.get("other_lang_note"):
        other = f'    <p class="lang-link">{a["other_lang_note"]}</p>\n\n'

    crumb_extra = ""
    if a.get("crumb_extra"):
        crumb_extra = " · " + a["crumb_extra"]

    page = f"""<!doctype html>
<html lang="{lang}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{a["title"]}</title>
<meta name="description" content="{esc_attr(a["description"])}">
<link rel="canonical" href="{url}">
{alternates}<meta property="og:type" content="article">
<meta property="og:title" content="{esc_attr(a["h1"])}">
<meta property="og:description" content="{esc_attr(a["description"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/share.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<script type="application/ld+json">
{json.dumps(article_ld, ensure_ascii=False, indent=2)}
</script>
{"" if not faq_ld else '<script type="application/ld+json">' + chr(10) + json.dumps(faq_ld, ensure_ascii=False, indent=2) + chr(10) + "</script>" + chr(10)}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body data-page="article">
{gate}
<a class="skip" href="#main">{ui["skip"]}</a>

<header>
  <div class="wrap bar">
    <a class="brand" href="index.html">{ui["brand"]}</a>
    <nav aria-label="Main">
{nav}
{lang_switch}
    </nav>
  </div>
</header>

<main id="main" class="wrap">
<article class="article">
  <p class="crumb"><a href="index.html#guidance">{ui["crumb"]}</a>{crumb_extra}</p>
  <p class="tag">{a["tag"]}</p>
  <h1>{a["h1"]}</h1>
  <p class="byline">{ui["by"]} · {a["month"]} · {a["minutes"]} {ui["read"]}</p>

  <div class="summary">
    <p class="sum-h">{ui["short"]}</p>
    <ol>
{summary}    </ol>
  </div>

  <div class="prose">
{sections}{faqs}{other}    <p class="note">{ui["note"].format(month=a["month"])}</p>
    <a class="back" href="index.html#guidance">{ui["back"]}</a>
  </div>
</article>
</main>

{contact}

{footer}

<script src="assets/site.js"></script>
</body>
</html>
"""
    (ROOT / f"{slug}.html").write_text(page)
    return slug


def main():
    gate, contact, footer = shared_parts()
    built = [build(a, gate, contact, footer) for a in ARTICLES]
    print("built:", ", ".join(built))


if __name__ == "__main__":
    main()
