#!/usr/bin/env python3
"""Build deck.html from slides.md.

Reads slides.md, inlines the artwork and app logos, and writes a single
self-contained deck.html that works offline.

Run:  python3 build_deck.py
"""

import base64
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
LOGOS = os.path.join(ASSETS, "logos")
OUT = os.path.join(ROOT, "deck.html")

# ---------------------------------------------------------------- palette
BG = "#0C0C0F"
INK = "#F5F5F3"
SAND = "#D8D8C8"
GOLD = "#E0A83F"
AMBER = "#F8B050"
ORANGE = "#C46A2C"
TERRA = "#B8602A"
RUST = "#8C3A22"
TEAL = "#3E7A84"

CHAPTERS = {
    "front": {"accent": GOLD, "label": "The Atmosphere"},
    "1": {"accent": GOLD, "label": "1 . Personal story"},
    "2": {"accent": "#D9883A", "label": "2 . The story so far"},
    "3": {"accent": "#C8724A", "label": "3 . The ecosystem today"},
    "4": {"accent": "#C86A52", "label": "4 . Young people"},
    "5": {"accent": "#58A0AA", "label": "5 . The future"},
    "close": {"accent": "#58A0AA", "label": "Close"},
}
WAVES = {
    "front": [GOLD, ORANGE, RUST, TEAL, SAND],
    "1": [GOLD, AMBER, ORANGE, TERRA, SAND],
    "2": [ORANGE, GOLD, TERRA, TEAL, SAND],
    "3": [TERRA, ORANGE, RUST, GOLD, TEAL],
    "4": [RUST, TERRA, ORANGE, GOLD, SAND],
    "5": [TEAL, "#4E8A94", GOLD, ORANGE, SAND],
    "close": [TEAL, GOLD, RUST, TERRA, SAND],
}

APP_LOGOS = {
    "eurosky.social": "eurosky.social.png",
    "mu.social": "mu.social.png",
    "popfeed.social": "popfeed.social.png",
    "sifa.id": "sifa.id.png",
    "tangled.org": "tangled.org.png",
    "margin.at": "margin.at.svg",
    "npmx.dev": "npmx.dev.png",
    "pckt.blog": "pckt.blog.png",
    "atstore.fyi": "atstore.fyi.svg",
    "blacksky.app": "blacksky.app.png",
    "atproto.eu": "atproto.eu.png",
    "atproto.barcelona": "atproto.barcelona.png",
}

# ---------------------------------------------------------------- parsing


def qr_svg(url):
    """Inline SVG QR for a URL, sized and coloured for the deck."""
    try:
        import segno
        q = segno.make(url, micro=False)
        svg = q.svg_inline(scale=1, dark=INK, light=None, border=0)
        m = re.match(r'<svg[^>]*width="(\d+)"[^>]*height="(\d+)"[^>]*>', svg)
        if m:
            svg = svg.replace(
                m.group(0),
                '<svg viewBox="0 0 %s %s" class="qr" width="200" height="200" '
                'shape-rendering="crispEdges">' % (m.group(1), m.group(2)),
                1)
        return svg
    except Exception as exc:      # pragma: no cover
        print("QR skipped:", url, exc)
        return ""


def parse_slides(path):
    text = open(path, encoding="utf-8").read()
    # only the part after the first '---' divider (skip the format notes)
    text = text.split("\n---\n", 1)[1]
    slides = []
    for block in re.split(r"\n### ", "\n" + text):
        block = block.strip()
        if not block:
            continue
        head, _, body = block.partition("\n")
        sid, _, title = head.partition(" — ")
        slide = {"id": sid.strip(), "title": title.strip(), "items": [], "en_items": [], "es_items": [],
                 "en_links": [], "es_links": []}
        for line in body.split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            key, _, val = line[2:].partition(": ")
            key, val = key.strip(), val.strip()
            if key == "en_item":
                slide["en_items"].append(val)
            elif key == "es_item":
                slide["es_items"].append(val)
            elif key == "link_en":
                slide["en_links"].append(val)
            elif key == "link_es":
                slide["es_links"].append(val)
            else:
                slide[key] = val
        slides.append(slide)
    return slides


# ---------------------------------------------------------------- helpers


def esc(s):
    return html.escape(s, quote=True)


def img_data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".svg": "image/svg+xml", ".webp": "image/webp"}[ext]
    with open(path, "rb") as fh:
        raw = base64.b64encode(fh.read()).decode("ascii")
    return "data:%s;base64,%s" % (mime, raw)


def split_stat(item):
    if " | " in item:
        n, _, label = item.partition(" | ")
        return n.strip(), label.strip()
    return item, ""


def split_app(item):
    parts = [p.strip() for p in item.split(" | ")]
    logo = parts[0] if parts else ""
    name = parts[1] if len(parts) > 1 else logo
    text = parts[2] if len(parts) > 2 else ""
    url = parts[3] if len(parts) > 3 else ""
    if len(parts) == 2 and parts[1].startswith("http"):
        url, text = parts[1], ""
    return logo, name, text, url


def split_link(item):
    if " | " in item:
        label, _, url = item.rpartition(" | ")
        return label.strip(), url.strip()
    return item, item


def waves_svg(colors, y=0):
    """A band of flowing lines, in the spirit of the cover artwork."""
    paths = []
    for i, c in enumerate(colors):
        off = i * 17
        w = 9 - i * 0.7
        o = 0.95 - i * 0.13
        paths.append(
            '<path d="M-40,%d C240,%d 480,%d 720,%d C960,%d 1200,%d 1480,%d" '
            'stroke="%s" stroke-width="%.1f" fill="none" stroke-linecap="round" opacity="%.2f"/>'
            % (30 + off + y, 4 + off, 66 + off, 36 + off, 6 + off, 76 + off, 30 + off, c, w, o)
        )
    return ('<svg class="waves" viewBox="0 0 1440 170" preserveAspectRatio="none" aria-hidden="true">'
            + "".join(paths) + "</svg>")


def render_items(slide):
    out = []
    for en, es in zip(slide.get("en_items", []), slide.get("es_items", [])):
        out.append(
            '<li><span class="en">%s</span><span class="es">%s</span></li>'
            % (esc(en), esc(es))
        )
    return '<ul class="points">%s</ul>' % "".join(out) if out else ""


def render_body(slide, logo_uri):
    kind = slide.get("type", "points")
    en_items, es_items = slide.get("en_items", []), slide.get("es_items", [])

    if kind in ("points", "agenda"):
        if slide.get("_img"):
            cap = ('<figcaption>%s</figcaption>' % esc(slide.get("img_credit", ""))) if slide.get("img_credit") else ""
            return ('<div class="withavatar"><figure class="av"><img src="%s" alt="">%s</figure>'
                    '<div class="avtext">%s</div></div>' % (slide["_img"], cap, render_items(slide)))
        return render_items(slide)

    if kind == "stats":
        cells = []
        for en, es in zip(en_items, es_items):
            n_en, l_en = split_stat(en)
            n_es, l_es = split_stat(es)
            cells.append(
                '<div class="stat"><div class="num">%s</div><div class="lab"><span class="en">%s</span>'
                '<span class="es">%s</span></div></div>'
                % (esc(n_en), esc(l_en), esc(l_es))
            )
        return '<div class="stats">%s</div>' % "".join(cells)

    if kind == "apps":
        cards = []
        for en, es in zip(en_items, es_items):
            slug, name, text, url = split_app(en)
            _, _, text_es, url_es = split_app(es)
            url = url or url_es
            uri = logo_uri.get(slug, "")
            if uri:
                logo_html = '<span class="chip"><img src="%s" alt=""></span>' % uri
            else:
                letter = (name or slug).strip()[:1].upper()
                logo_html = '<span class="chip letter">%s</span>' % esc(letter)
            name_html = ('<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(url), esc(name))) if url else esc(name)
            cards.append(
                '<div class="app">%s<div class="app-body"><div class="app-name">%s</div>'
                '<div class="app-text"><span class="en">%s</span><span class="es">%s</span></div></div></div>'
                % (logo_html, name_html, esc(text), esc(text_es))
            )
        cls = "apps two" if len(cards) >= 4 else "apps"
        return '<div class="%s">%s</div>' % (cls, "".join(cards))

    if kind == "party":
        url = slide.get("qr", "")
        qrblock = ""
        if slide.get("_qr"):
            qrblock = ('<div class="qrwrap tight">%s<div class="qrside"><a class="urlchip big" href="%s" '
                       'target="_blank" rel="noopener">%s</a></div></div>'
                       % (slide["_qr"], esc(url), esc(url.replace("https://", "").rstrip("/"))))
        shot = ('<div class="shot"><img src="%s" alt=""></div>' % slide["_img"]) if slide.get("_img") else ""
        return '<div class="party">%s<div class="pside">%s%s</div></div>' % (shot, render_items(slide), qrblock)

    if kind == "links":
        cells = []
        for en, es in zip(en_items, es_items):
            label, url = split_link(en)
            cells.append(
                '<a class="link" href="%s" target="_blank" rel="noopener"><span class="lbl">%s</span>'
                '<span class="url">%s</span></a>' % (esc(url), esc(label), esc(url.replace("https://", "").replace("http://", "")))
            )
        return '<div class="linkgrid">%s</div>' % "".join(cells)

    if kind == "quote":
        return (
            '<blockquote><p class="q"><span class="en">%s</span><span class="es">%s</span></p>'
            '<p class="attrib"><span class="en">%s</span><span class="es">%s</span></p></blockquote>%s'
            % (esc(slide.get("en_quote", "")), esc(slide.get("es_quote", "")),
               esc(slide.get("en_attrib", "")), esc(slide.get("es_attrib", "")), render_items(slide))
        )
    return render_items(slide)


def footer_links(slide):
    """Links of a slide as clickable chips: labelled link_en/link_es pairs first,
    then any bare URL left in the points."""
    if slide.get("type") in ("links", "party"):
        return ""
    pairs = []          # (label_en, label_es, url)
    for item in slide.get("en_links", []):
        label, _, url = item.partition(" | ")
        url = url.strip()
        if url.startswith("http"):
            pairs.append([label.strip(), "", url])
    for item in slide.get("es_links", []):
        label, _, url = item.partition(" | ")
        url = url.strip()
        for pair in pairs:
            if pair[2] == url and not pair[1]:
                pair[1] = label.strip()
    seen = {p[2] for p in pairs}
    for item in slide.get("en_items", []):
        for part in [q.strip() for q in item.split(" | ")]:
            if part.startswith("http") and part not in seen:
                seen.add(part)
                pairs.append(["", "", part])
    if not pairs:
        return ""
    chips = []
    for lbl_en, lbl_es, url in pairs:
        plain = esc(url.replace("https://", "").replace("http://", "").rstrip("/"))
        if lbl_en or lbl_es:
            text = ('<span class="en">%s</span><span class="es">%s</span>'
                    % (esc(lbl_en or lbl_es), esc(lbl_es or lbl_en)))
        else:
            text = plain
        chips.append('<a class="urlchip" href="%s" target="_blank" rel="noopener">%s</a>' % (esc(url), text))
    return '<div class="urls">%s</div>' % "".join(chips)


# ---------------------------------------------------------------- build


def build():
    slides = parse_slides(os.path.join(ROOT, "slides.md"))
    logo_uri = {k: img_data_uri(os.path.join(LOGOS, v)) for k, v in APP_LOGOS.items()
                if os.path.exists(os.path.join(LOGOS, v))}
    badge = img_data_uri(os.path.join(ASSETS, "atproto-barcelona-logo.jpg"))

    qr = qr_svg("https://mu.social/profile/didiermortier.eu")

    for s in slides:
        rel = s.get("img", "")
        if rel:
            path = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
            if os.path.exists(path):
                s["_img"] = img_data_uri(path)
            else:
                print("missing image:", rel)
        if s.get("qr"):
            s["_qr"] = qr_svg(s["qr"])

    parts = []
    for i, s in enumerate(slides):
        ch = s.get("chapter", "front")
        accent = CHAPTERS.get(ch, CHAPTERS["front"])["accent"]
        label = CHAPTERS.get(ch, CHAPTERS["front"])["label"]
        kind = s.get("type", "points")
        body = render_body(s, logo_uri)
        urls = footer_links(s)
        title_html = '<h2><span class="en">%s</span><span class="es">%s</span></h2>' % (
            esc(s.get("en_title", "")), esc(s.get("es_title", "")))
        sub = ""
        if s.get("en_sub") or s.get("es_sub"):
            sub = '<p class="sub"><span class="en">%s</span><span class="es">%s</span></p>' % (
                esc(s.get("en_sub", "")), esc(s.get("es_sub", "")))
        extra_top = extra_bottom = ""
        if kind == "title":
            extra_top = '<img class="badge" src="%s" alt="atproto BARCELONA">' % badge
        if kind == "cta":
            extra_bottom = (
                '<div class="qrwrap">%s'
                '<div class="qrside"><img class="badge small" src="%s" alt="">'
                '<a class="urlchip big" href="https://mu.social/profile/didiermortier.eu" '
                'target="_blank" rel="noopener">mu.social/profile/didiermortier.eu</a></div></div>'
                % (qr, badge))
        cls = "slide kind-%s ch-%s" % (kind, ch)
        kicker = "" if kind == "title" else '<p class="kicker">%s</p>' % esc(label)
        sec = (
            '<section class="%(cls)s" data-i="%(i)d" data-note-en="%(nen)s" data-note-es="%(nes)s" '
            'data-time="%(t)s" style="--accent:%(acc)s">'
            '<div class="chrome"><span class="badge-ch">%(sid)s</span></div>'
            '%(waves)s'
            '<div class="wrap">%(top)s%(kicker)s%(title)s%(sub)s%(body)s%(urls)s%(bottom)s</div>'
            '</section>'
        ) % {
            "cls": cls, "i": i, "nen": esc(s.get("note_en", "")), "nes": esc(s.get("note_es", "")),
            "t": esc(s.get("time", "")), "acc": accent, "sid": esc(s["id"]), "lab": esc(label),
            "waves": waves_svg(WAVES.get(ch, WAVES["front"])), "top": extra_top, "bottom": extra_bottom,
            "kicker": kicker, "title": title_html, "sub": sub, "body": body, "urls": urls,
        }
        parts.append(sec)

    deck = DECK_TEMPLATE.replace("/*SLIDES*/", "\n".join(parts)).replace("/*BADGE*/", badge)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(deck)
    print("wrote", OUT, "slides:", len(slides), "size:", os.path.getsize(OUT))


DECK_TEMPLATE = r"""<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Atmosphere . Building the open social web</title>
<style>
  :root{
    --bg:#0C0C0F; --ink:#F5F5F3; --sand:#D8D8C8; --gold:#E0A83F; --teal:#3E7A84;
    --line:rgba(255,255,255,.10); --panel:rgba(255,255,255,.045);
    --accent:var(--gold);
    --tscale:1;
    --font:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Helvetica,Arial,sans-serif;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;height:100%}
  body{background:var(--bg);color:var(--ink);font-family:var(--font);overflow:hidden}
  .en,.es{}
  html[data-lang="en"] .es{display:none}
  html[data-lang="es"] .en{display:none}

  .slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
    padding:7vh 8vw 12vh;opacity:0;visibility:hidden;transition:opacity .18s ease,transform .18s ease;
    transform:translateY(6px)}
  .slide.on{opacity:1;visibility:visible;transform:none}
  .slide .waves{position:absolute;left:-2vw;right:-2vw;top:0;width:104vw;height:23vh;
    opacity:.72;pointer-events:none}
  .slide.ch-5 .waves,.slide.ch-close .waves{top:auto;bottom:0}
  .wrap{position:relative;max-width:1080px;width:100%;margin:0 auto}

  .kicker{margin:0 0 14px;font-size:calc(13px * var(--tscale));letter-spacing:.17em;text-transform:uppercase;
    color:var(--accent);font-weight:600}
  h2{margin:0;font-size:calc(clamp(34px,4.6vw,68px) * var(--tscale));line-height:1.06;letter-spacing:-.015em;font-weight:700}
  .sub{margin:18px 0 0;font-size:calc(clamp(18px,1.9vw,28px) * var(--tscale));line-height:1.35;color:var(--sand);max-width:26em}

  ul.points{margin:30px 0 0;padding:0;list-style:none}
  ul.points li{position:relative;margin:0 0 16px;padding-left:34px;
    font-size:calc(clamp(17px,1.75vw,26px) * var(--tscale));line-height:1.35}
  ul.points li:before{content:"";position:absolute;left:8px;top:.62em;width:11px;height:11px;
    border-radius:50%;background:var(--accent);opacity:.85}
  .kind-agenda ul.points{counter-reset:ag}
  .kind-agenda ul.points li{counter-increment:ag;padding-left:60px;font-size:calc(clamp(18px,2vw,30px) * var(--tscale));
    margin-bottom:22px}
  .kind-agenda ul.points li:before{content:counter(ag);left:0;top:0;width:auto;height:auto;
    background:none;color:var(--accent);font-weight:700;font-size:.86em;opacity:1}

  .stats{display:flex;flex-wrap:wrap;gap:14px 54px;margin:34px 0 0}
  .stat .num{font-size:calc(clamp(40px,5.4vw,86px) * var(--tscale));font-weight:700;line-height:1;color:var(--accent)}
  .stat .lab{margin-top:8px;color:var(--sand);font-size:calc(clamp(15px,1.5vw,21px) * var(--tscale));max-width:18em}

  .apps{display:flex;flex-direction:column;gap:18px;margin:30px 0 0}
  .apps.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:26px 0 0}
  .apps.two .app{padding:13px 16px;gap:15px}
  .apps.two .app-text{font-size:calc(clamp(13px,1.2vw,16px) * var(--tscale))}
  .app{display:flex;gap:20px;align-items:center;background:var(--panel);border:1px solid var(--line);
    border-radius:16px;padding:16px 20px}
  .chip{flex:0 0 60px;width:60px;height:60px;border-radius:14px;background:#F0EEE7;
    display:grid;place-items:center;overflow:hidden}
  .chip img{width:42px;height:42px;object-fit:contain;display:block}
  .app-name{font-weight:700;font-size:calc(clamp(17px,1.6vw,22px) * var(--tscale))}
  .app-name a{color:var(--ink);text-decoration:none;border-bottom:1px solid rgba(224,168,63,.45)}
  .app-name a:hover{border-color:var(--gold)}
  .app-text{margin-top:5px;color:var(--sand);font-size:calc(clamp(14px,1.35vw,18px) * var(--tscale));line-height:1.4}

  blockquote{margin:26px 0 0;padding:0}
  blockquote .q{margin:0;font-size:calc(clamp(24px,3.1vw,46px) * var(--tscale));line-height:1.2;font-weight:600;color:var(--gold)}
  blockquote .attrib{margin:14px 0 0;color:var(--sand);font-size:calc(clamp(14px,1.4vw,19px) * var(--tscale))}

  .linkgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px 22px;margin:26px 0 0}
  .link{display:block;text-decoration:none;color:var(--ink);padding:9px 12px;border-radius:10px;
    border:1px solid var(--line);background:var(--panel);transition:border-color .15s}
  .link:hover{border-color:var(--teal)}
  .link .lbl{display:block;font-weight:600;font-size:calc(clamp(14px,1.3vw,17px) * var(--tscale))}
  .link .url{display:block;color:#7FBFC9;font-size:calc(12px * var(--tscale));margin-top:2px;word-break:break-all}

  .urls{position:relative;display:flex;gap:10px;flex-wrap:wrap;margin-top:34px}
  .urlchip{color:#7FBFC9;text-decoration:none;font-size:calc(13px * var(--tscale));border:1px solid rgba(127,191,201,.35);
    padding:5px 11px;border-radius:999px;background:rgba(62,122,132,.12)}
  .urlchip:hover{border-color:#7FBFC9}

  .badge{width:clamp(120px,13vw,190px);height:auto;border-radius:50%;display:block;margin-bottom:30px}
  .badge.small{width:74px;margin:0}
  .qrwrap{display:flex;align-items:center;gap:26px;margin:34px 0 0}
  .qrwrap.tight{margin:26px 0 0;gap:20px}
  .withavatar{display:flex;gap:34px;align-items:flex-start;margin-top:32px}
  .withavatar .av{margin:0;flex:0 0 clamp(140px,15vw,230px)}
  .withavatar .av img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:50%;border:2px solid var(--line)}
  .withavatar .av figcaption{margin-top:10px;color:var(--sand);font-size:calc(11px * var(--tscale));line-height:1.35}
  .withavatar .avtext{flex:1 1 auto}
  .withavatar .avtext ul.points{margin-top:0}
  .party{display:flex;gap:36px;align-items:flex-start;margin-top:24px}
  .party .shot{flex:0 0 44%;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--panel)}
  .party .shot img{display:block;width:100%;height:auto;max-height:54vh;object-fit:cover;object-position:top}
  .party .pside{flex:1 1 auto}
  .party .pside ul.points{margin-top:0}
  .party .qr{width:clamp(140px,13vw,180px);height:auto;padding:12px}
  .chip.letter{color:#2A2A31;font-weight:800;font-size:26px;letter-spacing:.5px}
  .qr{background:rgba(255,255,255,.06);padding:14px;border-radius:16px;display:block}
  .qrside{display:flex;flex-direction:column;align-items:flex-start;gap:16px}
  .urlchip.big{font-size:calc(15px * var(--tscale));padding:7px 14px}
  .qr path{fill:#F5F5F3}

  .chrome{position:absolute;top:18px;right:26px;display:flex;align-items:center;gap:14px;
    font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);opacity:.85}
  .chrome .badge-ch{font-weight:700}
  .chrome .chlab{color:var(--sand);opacity:.75;letter-spacing:.1em}

  .hud{position:fixed;left:0;right:0;bottom:0;height:44px;display:flex;align-items:center;
    justify-content:space-between;padding:0 22px;font-size:12px;color:var(--sand);
    background:linear-gradient(to top,rgba(0,0,0,.62),rgba(0,0,0,0));z-index:6}
  .hud .grp{display:flex;align-items:center;gap:16px}
  .hud button{font:inherit;color:var(--sand);background:none;border:1px solid var(--line);
    border-radius:999px;padding:3px 11px;cursor:pointer}
  .hud button.on{color:#0C0C0F;background:var(--gold);border-color:var(--gold);font-weight:700}
  .nav{position:fixed;left:50%;bottom:3px;transform:translateX(-50%);display:flex;gap:16px;z-index:7}
  .nav button{width:86px;height:38px;display:grid;place-items:center;font-size:20px;line-height:1;
    color:var(--ink);background:rgba(255,255,255,.09);border:1px solid var(--line);border-radius:11px;
    cursor:pointer;-webkit-tap-highlight-color:transparent;touch-action:manipulation}
  .nav button:active{background:var(--gold);border-color:var(--gold);color:#0C0C0F}
  .nav button:disabled{opacity:.3}
  .bar{position:fixed;left:0;bottom:0;height:3px;background:var(--accent);width:0;z-index:7;
    transition:width .18s ease;opacity:.9}
  .hint{position:fixed;left:50%;bottom:58px;transform:translateX(-50%);font-size:12px;color:var(--sand);
    background:rgba(0,0,0,.5);border:1px solid var(--line);border-radius:999px;padding:6px 14px;z-index:6}
  .note{position:fixed;left:0;right:0;bottom:44px;max-height:34vh;overflow:auto;z-index:8;
    background:rgba(10,10,12,.96);border-top:2px solid var(--accent);padding:14px 26px 18px;
    font-size:calc(15px * var(--tscale));line-height:1.5;color:var(--ink);display:none}
  .note.on{display:block}
  .note .lab{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:6px}
  .idx{position:fixed;inset:0;background:rgba(6,6,8,.96);z-index:9;display:none;padding:5vh 6vw;overflow:auto}
  .idx.on{display:block}
  .idx h3{margin:0 0 18px;font-size:15px;letter-spacing:.16em;text-transform:uppercase;color:var(--sand)}
  .idxgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px}
  .idxgrid a{display:block;text-decoration:none;color:var(--ink);border:1px solid var(--line);
    border-radius:10px;padding:10px 12px;font-size:13px;background:var(--panel)}
  .idxgrid a:hover{border-color:var(--gold)}
  .idxgrid .id{color:var(--gold);font-weight:700;font-size:11px;letter-spacing:.1em}

  .presenter .hint::after{content:' . presenter mode'}

  @media (max-width:1100px){
    .slide{padding:6vh 6vw 24vh}
    .hud{height:auto;flex-wrap:wrap;row-gap:6px;padding:6px 12px 8px;justify-content:center}
    .hud .grp{gap:8px;flex-wrap:wrap;justify-content:center}
    .hud .grp:first-child{width:100%}
    .hud button{padding:4px 10px}
    .nav{bottom:80px}
    .note{bottom:122px;max-height:30vh}
    .hint{bottom:168px}
  }
  @media print{
    body{overflow:visible}
    .slide{position:static;opacity:1;visibility:visible;transform:none;page-break-after:always;
      height:auto;min-height:60vh}
    .waves{opacity:.35}
    .hud,.nav,.bar,.note,.idx,.hint{display:none !important}
  }
</style>
</head>
<body>
/*SLIDES*/
<div class="note" id="note"><div class="lab" id="notelab">notes</div><div id="notetext"></div></div>
<div class="idx" id="idx"><h3>Slides</h3><div class="idxgrid" id="idxgrid"></div></div>
<div class="hint" id="hint">arrows or click to move . A+ / A- or + and - to resize text . T timer . F fullscreen . Esc index</div>
<div class="bar" id="bar"></div>
<div class="nav" id="nav">
  <button id="bprev" title="previous slide" aria-label="previous slide">&#8592;</button>
  <button id="bnext" title="next slide" aria-label="next slide">&#8594;</button>
</div>
<div class="hud">
  <div class="grp"><span id="counter">1 / 1</span><span id="timer">00:00</span><span id="budget"></span></div>
  <div class="grp">
    <button id="ben" class="on">EN</button><button id="bes">ES</button>
    <button id="bminus" title="smaller text">A-</button><button id="bplus" title="bigger text">A+</button>
    <button id="btimer">timer</button><button id="bfull">full</button>
  </div>
</div>
<script>
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var i=0, showed=false;
  var el=document.documentElement;
  function show(n){
    n=Math.max(0,Math.min(slides.length-1,n));
    slides[i].classList.remove('on'); i=n; slides[i].classList.add('on');
    document.getElementById('counter').textContent=(i+1)+' / '+slides.length;
    try{history.replaceState(null,'','#'+(i+1));}catch(e){}
    document.getElementById('bar').style.width=((i)/(slides.length-1)*100)+'%';
    document.getElementById('budget').textContent='target '+slides[i].dataset.time;
    document.getElementById('bprev').disabled=(i===0);
    document.getElementById('bnext').disabled=(i>=slides.length-1);
    if(noteOpen) renderNote();
    if(!showed){showed=true;setTimeout(function(){document.getElementById('hint').style.display='none';},4500);}
  }
  var PRESENTER=(function(){try{return /(^|[?&])notes=1(&|$)/.test(location.search)||location.hash==='#notes';}catch(e){return false;}})();
  if(PRESENTER){document.documentElement.classList.add('presenter');}
  var noteOpen=false;
  function renderNote(){
    var s=slides[i], lang=el.dataset.lang;
    document.getElementById('notelab').textContent=s.dataset[lang==='es'?'noteEs':'noteEn']?'notes . '+s.dataset.time:'notes';
    document.getElementById('notetext').textContent=lang==='es'?s.dataset.noteEs:s.dataset.noteEn;
    document.getElementById('note').classList.add('on');
  }
  function peek(on){
    if(!PRESENTER)return;
    var n=document.getElementById('note');
    if(on){renderNote();}else if(!noteOpen){n.classList.remove('on');}
  }
  var tsc=1;
  function setScale(v){
    tsc=Math.max(0.75,Math.min(1.9,Math.round(v*100)/100));
    el.style.setProperty('--tscale',tsc);
    try{localStorage.setItem('atmo-scale',tsc);}catch(e){}
  }
  function setLang(l){
    el.dataset.lang=l;
    document.getElementById('ben').classList.toggle('on',l==='en');
    document.getElementById('bes').classList.toggle('on',l==='es');
    try{localStorage.setItem('atmo-lang',l);}catch(e){}
    if(noteOpen) renderNote();
  }
  // timer
  var t0=null, acc=0, tick=null;
  function fmt(ms){var s=Math.floor(ms/1000);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');}
  function renderTimer(){document.getElementById('timer').textContent=fmt(acc+(t0?Date.now()-t0:0));}
  function toggleTimer(){
    var b=document.getElementById('btimer');
    if(t0){acc+=Date.now()-t0;t0=null;clearInterval(tick);tick=null;b.classList.remove('on');}
    else{t0=Date.now();b.classList.add('on');tick=setInterval(renderTimer,500);}
  }
  document.getElementById('ben').onclick=function(){setLang('en');};
  document.getElementById('bes').onclick=function(){setLang('es');};
  document.getElementById('btimer').onclick=toggleTimer;
  document.getElementById('bplus').onclick=function(){setScale(tsc+0.1);};
  document.getElementById('bminus').onclick=function(){setScale(tsc-0.1);};
  var bnote=document.getElementById('bnote');
  function toggleNote(){
    if(!PRESENTER)return;
    noteOpen=!noteOpen;if(bnote)bnote.classList.toggle('on',noteOpen);
    if(noteOpen){renderNote();}else{document.getElementById('note').classList.remove('on');}
  }
  if(bnote)bnote.onclick=toggleNote;
  document.getElementById('bfull').onclick=function(){
    if(document.fullscreenElement){document.exitFullscreen();}else{document.documentElement.requestFullscreen();}
  };
  document.getElementById('bprev').onclick=function(e){if(e)e.stopPropagation();show(i-1);};
  document.getElementById('bnext').onclick=function(e){if(e)e.stopPropagation();show(i+1);};
  // index
  var grid=document.getElementById('idxgrid');
  slides.forEach(function(s,n){
    var a=document.createElement('a');a.href='#';
    a.innerHTML='<div class="id">'+s.dataset.i+'</div>'+(s.querySelector('h2')?s.querySelector('h2').textContent:'');
    a.onclick=function(ev){ev.preventDefault();document.getElementById('idx').classList.remove('on');show(n);};
    grid.appendChild(a);
  });
  function idx(on){document.getElementById('idx').classList.toggle('on',on);}

  document.addEventListener('keydown',function(e){
    var k=e.key;
    if(k==='ArrowRight'||k===' '||k==='PageDown'||k==='ArrowDown'){e.preventDefault();show(i+1);}
    else if(k==='ArrowLeft'||k==='PageUp'||k==='ArrowUp'){e.preventDefault();show(i-1);}
    else if(k==='Home'){show(0);} else if(k==='End'){show(slides.length-1);}
    else if(k==='Escape'){idx(!document.getElementById('idx').classList.contains('on'));}
    else if(k==='f'||k==='F'){document.getElementById('bfull').click();}
    else if((k==='n'||k==='N')&&PRESENTER){peek(true);}
    else if((k==='s'||k==='S')&&PRESENTER){toggleNote();}
    else if(k==='t'||k==='T'){toggleTimer();}
    else if(k==='r'||k==='R'){acc=0;t0=null;clearInterval(tick);tick=null;
      document.getElementById('btimer').classList.remove('on');renderTimer();}
    else if(k==='1'){setLang('en');} else if(k==='2'){setLang('es');}
    else if(k==='+'||k==='='){setScale(tsc+0.1);} else if(k==='-'||k==='_'){setScale(tsc-0.1);}
    else if(k==='0'){setScale(1);}
  });
  document.addEventListener('keyup',function(e){if((e.key==='n'||e.key==='N')&&PRESENTER){peek(false);}});
  document.addEventListener('click',function(e){
    if(e.target.closest('a')||e.target.closest('.hud')||e.target.closest('.nav')||e.target.closest('.idx')||e.target.closest('.note'))return;
    show(i+1);
  });
  document.addEventListener('mousedown',function(e){if(e.button===2)show(i-1);});
  document.addEventListener('contextmenu',function(e){e.preventDefault();});
  var savedScale=null;try{savedScale=parseFloat(localStorage.getItem('atmo-scale'));}catch(e){}
  if(savedScale){setScale(savedScale);}
  var saved=null;try{saved=localStorage.getItem('atmo-lang');}catch(e){}
  setLang(saved||'en');
  var start=0, m=/^#(\d+)$/.exec(location.hash||'');
  if(m){start=parseInt(m[1],10)-1;}
  show(start); renderTimer();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
