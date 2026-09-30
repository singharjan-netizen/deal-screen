#!/usr/bin/env python3
"""deal-screen: one-command first-pass diligence brief for an early-stage company.

Usage:
    python screen.py https://www.zeroeyes.com
    python screen.py https://hadrian.co --pages about careers

Pulls the company's public site, hands it to Claude (via the `claude` CLI),
and writes a structured one-pager to briefs/<domain>.md.
"""
import argparse, re, subprocess, sys, textwrap
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (deal-screen; student research tool)"}
DEFAULT_PAGES = ["", "about", "about-us", "company", "product", "products", "technology", "careers", "team", "news"]
MAX_CHARS = 60_000  # keep the prompt bounded

PROMPT = """You are a venture analyst preparing a first-pass screen for a partner who invests in
AI, aerospace, defense, proprietary data and other frontier-technology companies.
Below is text scraped from the company's public website. Using ONLY what is in the text
(say "not stated" where the site is silent), write a one-page brief in this exact structure:

# {name} — first-pass screen

**Source:** {url} (public site only, scraped {pages_n} pages)

## What they build
2–3 sentences. Product, customer, and the job it does.

## Sector and category
One line. Is this a new category or a better version of an existing one?

## Stage signals
Bullet list. Anything on the site that hints at traction: customers named, deployments,
contracts, funding announcements, headcount / open roles, certifications, partnerships.

## Claimed technical advantage
Bullet list. What the company says makes it hard to copy. Flag each claim as
[verifiable from site] or [unverified marketing].

## Risks and open questions
Bullet list of 3–5. Regulatory, go-to-market, concentration, technical.

## Five questions for the founder
Numbered. Specific to this company, not generic.

## Screen verdict
One line: PASS / LOOK CLOSER / PRIORITY, and the single reason.

--- SITE TEXT ---
{text}
"""


def fetch(url: str) -> str:
    try:
        r = requests.get(url, headers=UA, timeout=15)
        if r.status_code != 200 or "text/html" not in r.headers.get("content-type", ""):
            return ""
    except requests.RequestException:
        return ""
    soup = BeautifulSoup(r.text, "html.parser")
    for t in soup(["script", "style", "noscript", "svg", "nav", "footer"]):
        t.decompose()
    text = soup.get_text("\n")
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def scrape(base: str, pages: list[str]) -> tuple[str, int]:
    chunks, n = [], 0
    for p in pages:
        u = urljoin(base if base.endswith("/") else base + "/", p)
        t = fetch(u)
        if len(t) > 100:
            chunks.append(f"\n\n===== {u} =====\n{t}")
            n += 1
    blob = "".join(chunks)
    return blob[:MAX_CHARS], n


def ask_claude(prompt: str) -> str:
    try:
        out = subprocess.run(["claude", "-p", prompt], capture_output=True, text=True, timeout=300)
    except FileNotFoundError:
        sys.exit("`claude` CLI not found. Install Claude Code or set up an API path.")
    if out.returncode != 0:
        sys.exit(f"claude failed:\n{out.stderr}")
    return out.stdout.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--pages", nargs="*", default=DEFAULT_PAGES, help="paths to try under the domain")
    ap.add_argument("--out", default="briefs")
    ap.add_argument("--dry", action="store_true", help="print scraped text, skip Claude")
    a = ap.parse_args()

    base = a.url if a.url.startswith("http") else "https://" + a.url
    domain = urlparse(base).netloc.replace("www.", "")
    name = domain.split(".")[0].capitalize()

    print(f"[deal-screen] scraping {domain} …", file=sys.stderr)
    text, n = scrape(base, a.pages)
    if not text:
        sys.exit("Nothing fetched. Site may block scrapers; try --pages with specific paths.")
    print(f"[deal-screen] {n} pages, {len(text):,} chars → Claude", file=sys.stderr)
    if a.dry:
        print(text); return

    brief = ask_claude(PROMPT.format(name=name, url=base, pages_n=n, text=text))
    out = Path(a.out); out.mkdir(exist_ok=True)
    path = out / f"{domain}.md"
    path.write_text(brief + "\n")
    print(f"[deal-screen] wrote {path}", file=sys.stderr)
    print(brief)


if __name__ == "__main__":
    main()
