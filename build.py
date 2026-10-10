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
    meta["series"] = meta.get("series", "devlog")
    if meta["series"] not in ("devlog", "archive"):
        raise ValueError(f"{path.name}: unknown series {meta['series']}")
    story_ids = [sid.strip() for sid in meta.get("stories", "").split(",") if sid.strip()]
    if any(not re.fullmatch(r"S\d{4}", sid) for sid in story_ids) or len(story_ids) != len(set(story_ids)):
        raise ValueError(f"{path.name}: invalid or repeated story IDs")
    if story_ids and not re.fullmatch(r"[0-9a-f]{40}", meta.get("source_snapshot", "")):
        raise ValueError(f"{path.name}: stories require a full source_snapshot SHA")
    meta["story_ids"] = story_ids
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


def layout(title: str, description: str, body: str, og_image: str = "", canonical: str = "", series: str = "devlog") -> str:
    e = html.escape
    devlog_state = ' class="active" aria-current="page"' if series == "devlog" else ""
    archive_state = ' class="active" aria-current="page"' if series == "archive" else ""
    media_state = ' class="active" aria-current="page"' if series == "media" else ""
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
      <a class="game-link" href="{e(CFG['game_url'])}">The Game</a>
      <a href="{BASE}/"{devlog_state}>Devlog</a>
      <a href="{BASE}/archive/"{archive_state}>Development Archive</a>
      <a href="{BASE}/media/"{media_state}>Media</a>
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


def render_index(posts: list, series: str = "devlog") -> str:
    e = html.escape
    is_archive = series == "archive"
    heading = "Development Archive" if is_archive else "Devlog"
    eyebrow = "Early development" if is_archive else "Development log"
    lead = ("A look back at how The Runesmith took shape, from its first landscapes to crafting, runes and the demo journey. Each retrospective follows a theme across its development period; later images are labeled."
            if is_archive else "Follow how The Runesmith takes shape: what I'm building, what I throw away, and what the next version of the game looks like.")
    label = "Archive" if is_archive else "Devlog"
    index_path = f"{BASE}/archive/" if is_archive else f"{BASE}/"
    cards = []
    for p in posts:
        cards.append(f"""
    <a class="card" href="{p['url']}">
      <div class="card-media"><img src="{p['cover_url']}" alt="" loading="lazy"></div>
      <div class="card-body">
        <div class="eyebrow">{label} #{p['number']} &middot; {fmt_date(p['date_obj'])}</div>
        <h2>{e(p['title'])}</h2>
        <p>{e(p['summary'])}</p>
      </div>
      <span class="card-arrow" aria-hidden="true">&rarr;</span>
    </a>""")
    if not cards:
        cards.append('<p class="lead archive-empty">The early development entries are being prepared. <a href="' + BASE + '/">Read the current devlogs</a> in the meantime.</p>')
    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{heading}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
<section class="wrap list">
{''.join(cards)}
</section>
"""
    return layout(f"{heading} · The Runesmith", lead, body, posts[0]["cover_url"] if posts else "", index_path, series)


MEDIA_JSON = ROOT / "media.json"
THUMB_W = 720


def ensure_thumbs(media: dict) -> None:
    # Galeri 50+ görseli tek sayfada gösteriyor; 1600 px asıllarla sayfa ~20 MB oluyordu.
    # Önizlemeler assets/thumbs altında bir kez üretilir ve commit'lenir: Pages'te build adımı yok.
    # Pillow yalnız önizleme eksik ya da kaynaktan eskiyse gerekir.
    todo = []
    for sec in media_sections(media):
        for it in sec["items"]:
            name = it.get("image") or it.get("poster")
            src = ROOT / "assets" / "img" / name
            dst = ROOT / "assets" / "thumbs" / name
            if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                todo.append((src, dst))
    if not todo:
        return
    from PIL import Image
    for src, dst in todo:
        dst.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(src).convert("RGB")
        if im.width > THUMB_W:
            im = im.resize((THUMB_W, round(im.height * THUMB_W / im.width)), Image.LANCZOS)
        im.save(dst, quality=82, optimize=True)


def media_sections(media: dict) -> list:
    return media["sections"] + (media["outtakes"]["sections"] if "outtakes" in media else [])


def validate_media(media: dict, slugs: set) -> None:
    for sec in media_sections(media):
        for it in sec["items"]:
            files = [("img", it["image"])] if "image" in it else [("video", it["video"]), ("img", it["poster"])]
            for folder, name in files:
                if not (ROOT / "assets" / folder / name).exists():
                    raise FileNotFoundError(f"media.json: dosya yok -> {folder}/{name}")
            if it.get("post") and it["post"] not in slugs:
                raise ValueError(f"media.json: yazı yok -> {it['post']}")


def render_media(media: dict, posts_by_slug: dict, outtakes: bool = False) -> str:
    e = html.escape
    page = media["outtakes"] if outtakes else media
    sections = []
    first_image = ""
    for sec in page["sections"]:
        tiles = []
        for it in sec["items"]:
            post = posts_by_slug.get(it.get("post", ""))
            source = f'<a class="media-source" href="{post["url"]}">{e(post["title"])}</a>' if post else ""
            cap = e(it["caption"])
            if "video" in it:
                tiles.append(f"""
      <figure class="media-tile media-video">
        <video src="{BASE}/assets/video/{e(it['video'])}" poster="{BASE}/assets/thumbs/{e(it['poster'])}" controls muted loop playsinline preload="none" aria-label="{cap}"></video>
        <figcaption><span>{cap}</span>{source}</figcaption>
      </figure>""")
            else:
                first_image = first_image or it["image"]
                tiles.append(f"""
      <figure class="media-tile">
        <a class="media-open" href="{BASE}/assets/img/{e(it['image'])}" data-caption="{cap}">
          <img src="{BASE}/assets/thumbs/{e(it['image'])}" alt="{cap}" loading="lazy">
        </a>
        <figcaption><span>{cap}</span>{source}</figcaption>
      </figure>""")
        cls = "media-grid media-grid-video" if any("video" in it for it in sec["items"]) else "media-grid"
        sections.append(f"""
<section class="wrap media-section">
  <h2>{e(sec['title'])}</h2>
  <div class="{cls}">{''.join(tiles)}
  </div>
</section>""")
    lead = page["intro"]
    tabs = ""
    if "outtakes" in media:
        g_state = "" if outtakes else ' class="active" aria-current="page"'
        o_state = ' class="active" aria-current="page"' if outtakes else ""
        tabs = f"""
    <nav class="media-tabs" aria-label="Media sections">
      <a href="{BASE}/media/"{g_state}>Gallery</a>
      <a href="{BASE}/media/outtakes/"{o_state}>{e(media['outtakes']['title'])}</a>
    </nav>"""
    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="eyebrow">Screenshots and clips</div>
    <h1>{e(page['title'])}</h1>
    <p class="lead">{e(lead)}</p>{tabs}
  </div>
</section>
{''.join(sections)}
<dialog class="lightbox" id="lightbox" aria-label="Image viewer">
  <button class="lightbox-close" type="button" aria-label="Close">&times;</button>
  <img alt="">
  <p class="lightbox-caption"></p>
</dialog>
<script>
(() => {{
  const box = document.getElementById('lightbox');
  if (!box || !box.showModal) return;
  const img = box.querySelector('img'), cap = box.querySelector('.lightbox-caption');
  document.querySelectorAll('.media-open').forEach(a => a.addEventListener('click', ev => {{
    ev.preventDefault();
    img.src = a.href; img.alt = a.dataset.caption; cap.textContent = a.dataset.caption;
    box.showModal();
  }}));
  box.addEventListener('click', ev => {{ if (ev.target === box || ev.target.closest('.lightbox-close')) box.close(); }});
}})();
</script>
"""
    og = f"{BASE}/assets/img/{first_image}" if first_image else ""
    url = f"{BASE}/media/outtakes/" if outtakes else f"{BASE}/media/"
    return layout(f"{page['title']} · The Runesmith", lead, body, og, url, "media")


def render_post(p: dict, newer: dict | None, older: dict | None) -> str:
    e = html.escape
    nav = []
    if older:
        nav.append(f'<a class="pn prev" href="{older["url"]}"><span>&larr; Previous</span>{e(older["title"])}</a>')
    else:
        nav.append('<span></span>')
    if newer:
        nav.append(f'<a class="pn next" href="{newer["url"]}"><span>Next &rarr;</span>{e(newer["title"])}</a>')
    series = p["series"]
    index_path = f"{BASE}/archive/" if series == "archive" else f"{BASE}/"
    label = "Archive" if series == "archive" else "Devlog"
    back_label = "Development Archive" if series == "archive" else "All devlogs"
    archive_note = '<p class="archive-note">From the development archive. This entry describes the game at the time of the work.</p>' if series == "archive" else ""
    period = f' &middot; {e(p["period"])}' if p.get("period") else ""
    body = f"""
<article class="post">
  <header class="post-head wrap-narrow">
    <a class="back" href="{index_path}">&larr; {back_label}</a>
    <div class="eyebrow">{label} #{p['number']} &middot; {fmt_date(p['date_obj'])}{period}</div>
    <h1>{e(p['title'])}</h1>
    <p class="lead">{e(p['summary'])}</p>
    {archive_note}
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
    return layout(f"{p['title']} · The Runesmith Devlog", p["summary"], body, p["cover_url"], p["url"], series)


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

    return re.sub(r'((?:src|href|content|poster)=")' + re.escape(BASE) + r'/assets/([^"?]+)"', repl, page)


def build() -> list:
    posts = [parse_post(p) for p in sorted((ROOT / "posts").glob("*.md"))]
    posts.sort(key=lambda p: (p["date_obj"], p["number"]), reverse=True)
    nums = [(p["series"], p["number"]) for p in posts]
    if len(nums) != len(set(nums)):
        raise ValueError(f"Devlog numaraları çakışıyor: {sorted(nums)}")
    for p in posts:
        img = ROOT / "assets" / "img" / p["cover"]
        if not img.exists():
            raise FileNotFoundError(f"{p['slug']}: kapak görseli yok -> {img}")
        for ref in re.findall(r'src="' + re.escape(BASE) + r'/assets/img/([^"]+)"', p["html"]):
            if not (ROOT / "assets" / "img" / ref).exists():
                raise FileNotFoundError(f"{p['slug']}: görsel yok -> {ref}")
        # Video yazıya ham HTML olarak girer (<video src=... poster=...>); yukarıdaki denetim onu kapsamaz.
        for ref in re.findall(r'(?:src|poster)="' + re.escape(BASE) + r'/assets/((?:video|img)/[^"]+)"', p["html"]):
            if not (ROOT / "assets" / ref).exists():
                raise FileNotFoundError(f"{p['slug']}: video/poster yok -> {ref}")

    urls = [p["url"] for p in posts]
    if len(urls) != len(set(urls)):
        raise ValueError("Post URL collision")
    media = json.loads(MEDIA_JSON.read_text(encoding="utf-8")) if MEDIA_JSON.exists() else None
    if media:
        validate_media(media, {p["slug"] for p in posts})
        ensure_thumbs(media)
    # Generated output must stay inside this checkout even if docs is replaced with a link.
    if OUT.is_symlink() or OUT.resolve().parent != ROOT.resolve():
        raise ValueError("Unsafe generated output path")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if (ROOT / "CNAME").exists():
        shutil.copy(ROOT / "CNAME", OUT / "CNAME")
    current = [p for p in posts if p["series"] == "devlog"]
    archive = sorted((p for p in posts if p["series"] == "archive"), key=lambda p: (p["date_obj"], p["number"]))
    (OUT / "index.html").write_text(bust_cache(render_index(current)), encoding="utf-8")
    (OUT / "archive").mkdir()
    (OUT / "archive" / "index.html").write_text(bust_cache(render_index(archive, "archive")), encoding="utf-8")
    (OUT / "feed.xml").write_text(render_feed(current), encoding="utf-8")
    if media:
        (OUT / "media").mkdir()
        by_slug = {p["slug"]: p for p in posts}
        (OUT / "media" / "index.html").write_text(bust_cache(render_media(media, by_slug)), encoding="utf-8")
        if "outtakes" in media:
            (OUT / "media" / "outtakes").mkdir()
            (OUT / "media" / "outtakes" / "index.html").write_text(bust_cache(render_media(media, by_slug, outtakes=True)), encoding="utf-8")
    for p in posts:
        neighbors = [other for other in posts if other["series"] == p["series"]]
        i = neighbors.index(p)
        newer = neighbors[i - 1] if i > 0 else None
        older = neighbors[i + 1] if i + 1 < len(neighbors) else None
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
