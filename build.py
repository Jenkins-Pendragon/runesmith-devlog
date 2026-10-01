"""The Runesmith devlog sitesini üretir: posts/*.md -> docs/ (GitHub Pages /docs kaynağı).

Kullanım:
    python build.py            # docs/ klasörünü baştan üretir
    python build.py --serve    # üretip http://localhost:8000<base_url>/ adresinde önizler

Neden Jekyll değil: makinede Ruby yok, yerel önizleme yapılamıyordu. Bu script tek bağımlılıkla
(`pip install markdown`) aynı çıktıyı verir ve GitHub tarafında build adımı gerektirmez.
Alan adı değişince yalnız site.json'daki base_url / site_url güncellenip yeniden build alınır.
"""
import html
import json
import re
import shutil
import sys
from datetime import date
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
CFG = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = CFG["base_url"].rstrip("/")


def parse_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path.name}: front matter yok")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    for key in ("title", "date", "number", "summary", "cover"):
        if key not in meta:
            raise ValueError(f"{path.name}: '{key}' alanı eksik")
    body = m.group(2).replace("{{base}}", BASE)
    meta["html"] = markdown.markdown(body, extensions=["extra", "sane_lists", "attr_list"])
    meta["date_obj"] = date.fromisoformat(meta["date"])
    meta["slug"] = path.stem[11:] if re.match(r"\d{4}-\d{2}-\d{2}-", path.stem) else path.stem
    meta["url"] = f"{BASE}/posts/{meta['slug']}/"
    meta["number"] = int(meta["number"])
    meta["cover_url"] = f"{BASE}/assets/img/{meta['cover']}"
    return meta


def fmt_date(d: date) -> str:
    return d.strftime("%B %-d, %Y") if sys.platform != "win32" else d.strftime("%B %#d, %Y")


def layout(title: str, description: str, body: str, og_image: str = "", canonical: str = "") -> str:
    e = html.escape
    og_img = f'<meta property="og:image" content="{e(CFG["site_url"] + og_image)}">' if og_image else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
{og_img}
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{e(CFG['site_url'] + canonical)}">
<link rel="alternate" type="application/rss+xml" title="{e(CFG['title'])}" href="{BASE}/feed.xml">
<link rel="icon" href="{BASE}/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{BASE}/" aria-label="The Runesmith Devlog home">
      <img src="{BASE}/assets/img/logo.png" alt="The Runesmith" width="160" height="43">
    </a>
    <nav class="nav">
      <a href="{e(CFG['game_url'])}">The Game</a>
      <a href="{BASE}/" class="active">Devlog</a>
      <a class="btn btn-gold btn-sm" href="{e(CFG['steam_url'])}">Wishlist on Steam</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <span>&copy; {date.today().year} {e(CFG['studio'])}</span>
    <span class="footer-links">
      <a href="{e(CFG['game_url'])}">therunesmith.com</a>
      <a href="{e(CFG['steam_url'])}">Steam</a>
      <a href="{e(CFG['discord_url'])}">Discord</a>
      <a href="{BASE}/feed.xml">RSS</a>
    </span>
  </div>
</footer>
</body>
</html>
"""


def render_index(posts: list) -> str:
    e = html.escape
    cards = []
    for p in posts:
        cards.append(f"""
    <a class="card" href="{p['url']}">
      <div class="card-media"><img src="{p['cover_url']}" alt="" loading="lazy"></div>
      <div class="card-body">
        <div class="eyebrow">Devlog #{p['number']} &middot; {fmt_date(p['date_obj'])}</div>
        <h2>{e(p['title'])}</h2>
        <p>{e(p['summary'])}</p>
      </div>
      <span class="card-arrow" aria-hidden="true">&rarr;</span>
    </a>""")
    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="eyebrow">Development log</div>
    <h1>Devlog</h1>
    <p class="lead">Follow how The Runesmith takes shape: what I'm building, what I throw away, and what the next version of the game looks like.</p>
  </div>
</section>
<section class="wrap list">
{''.join(cards)}
</section>
"""
    return layout(CFG["title"], CFG["description"], body, posts[0]["cover_url"] if posts else "", f"{BASE}/")


def render_post(p: dict, newer: dict | None, older: dict | None) -> str:
    e = html.escape
    nav = []
    if older:
        nav.append(f'<a class="pn prev" href="{older["url"]}"><span>&larr; Previous</span>{e(older["title"])}</a>')
    else:
        nav.append('<span></span>')
    if newer:
        nav.append(f'<a class="pn next" href="{newer["url"]}"><span>Next &rarr;</span>{e(newer["title"])}</a>')
    period = f' &middot; {e(p["period"])}' if p.get("period") else ""
    body = f"""
<article class="post">
  <header class="post-head wrap-narrow">
    <a class="back" href="{BASE}/">&larr; All devlogs</a>
    <div class="eyebrow">Devlog #{p['number']} &middot; {fmt_date(p['date_obj'])}{period}</div>
    <h1>{e(p['title'])}</h1>
    <p class="lead">{e(p['summary'])}</p>
  </header>
  <figure class="post-cover wrap"><img src="{p['cover_url']}" alt="{e(p.get('cover_alt', ''))}"></figure>
  <div class="post-body wrap-narrow">
{p['html']}
  </div>
  <aside class="cta wrap-narrow">
    <div>
      <h3>Forge with us</h3>
      <p>The Runesmith is coming to Steam. A wishlist is the single best way to help a solo developer.</p>
    </div>
    <div class="cta-buttons">
      <a class="btn btn-gold" href="{e(CFG['steam_url'])}">Wishlist on Steam</a>
      <a class="btn btn-ghost" href="{e(CFG['discord_url'])}">Join the Discord</a>
    </div>
  </aside>
  <nav class="post-nav wrap-narrow">{''.join(nav)}</nav>
</article>
"""
    return layout(f"{p['title']} · The Runesmith Devlog", p["summary"], body, p["cover_url"], p["url"])


def render_feed(posts: list) -> str:
    e = html.escape
    items = []
    for p in posts[:20]:
        dt = datetime(p["date_obj"].year, p["date_obj"].month, p["date_obj"].day, 12, tzinfo=timezone.utc)
        link = CFG["site_url"] + p["url"]
        items.append(f"""  <item>
    <title>{e(p['title'])}</title>
    <link>{e(link)}</link>
    <guid>{e(link)}</guid>
    <pubDate>{format_datetime(dt)}</pubDate>
    <description>{e(p['summary'])}</description>
  </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{e(CFG['title'])}</title>
  <link>{e(CFG['site_url'] + BASE + '/')}</link>
  <description>{e(CFG['description'])}</description>
{chr(10).join(items)}
</channel>
</rss>
"""


def bust_cache(page: str) -> str:
    # GitHub Pages asset'leri max-age=600 ile sunuyor; aynı adla güncellenen görsel tarayıcıda
    # 10 dk eski kalıyordu. İçerik hash'i sorgu parametresi olarak eklenir — dosya değişince URL değişir.
    import hashlib

    def repl(m):
        rel = m.group(2)
        f = ROOT / "assets" / rel
        if not f.exists():
            return m.group(0)
        h = hashlib.md5(f.read_bytes()).hexdigest()[:8]
        return f'{m.group(1)}{BASE}/assets/{rel}?v={h}"'

    return re.sub(r'((?:src|href|content)=")' + re.escape(BASE) + r'/assets/([^"?]+)"', repl, page)


def build() -> list:
    posts = [parse_post(p) for p in sorted((ROOT / "posts").glob("*.md"))]
    posts.sort(key=lambda p: (p["date_obj"], p["number"]), reverse=True)
    nums = [p["number"] for p in posts]
    if len(nums) != len(set(nums)):
        raise ValueError(f"Devlog numaraları çakışıyor: {sorted(nums)}")
    for p in posts:
        img = ROOT / "assets" / "img" / p["cover"]
        if not img.exists():
            raise FileNotFoundError(f"{p['slug']}: kapak görseli yok -> {img}")
        for ref in re.findall(r'src="' + re.escape(BASE) + r'/assets/img/([^"]+)"', p["html"]):
            if not (ROOT / "assets" / "img" / ref).exists():
                raise FileNotFoundError(f"{p['slug']}: görsel yok -> {ref}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if (ROOT / "CNAME").exists():
        shutil.copy(ROOT / "CNAME", OUT / "CNAME")
    (OUT / "index.html").write_text(bust_cache(render_index(posts)), encoding="utf-8")
    (OUT / "feed.xml").write_text(render_feed(posts), encoding="utf-8")
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        d = OUT / "posts" / p["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(bust_cache(render_post(p, newer, older)), encoding="utf-8")
    print(f"{len(posts)} yazı -> {OUT}")
    return posts


def serve():
    # base_url altında servis etmek için docs/ klasörünü geçici bir kök altına bağlar.
    import http.server
    import tempfile

    tmp = Path(tempfile.mkdtemp())
    target = tmp / BASE.strip("/") if BASE else tmp
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(OUT, target, dirs_exist_ok=True)
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(tmp), **k)
    # Threading şart: tek iş parçacıklı sunucu, tarayıcının açık tuttuğu bağlantıda kilitleniyor.
    with http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler) as httpd:
        print(f"http://localhost:8000{BASE}/")
        httpd.serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
