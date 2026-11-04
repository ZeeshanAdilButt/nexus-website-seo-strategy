"""NEXUS v3.1: Mark's brief (sections, copy, rules) in the brand-led v3 look.

Copy is the client's prototype copy and case-study text, unchanged except where marked.
"""
import os
import sys

OUT = sys.argv[1]
LOGO = "/_blob/384f10695d602865bdd54b973fa5c57c"
WEBUILD = "/_blob/3b48310bcd6634d5b4750f8c7e090c2f"
B1 = "/_blob/277d5c1e63cd017d7765e5e482fdc6eb"
B2 = "/_blob/7977c027cc23909ae8bf30f10fba4b0f"
B3 = "/_blob/51f3fa72fb2676848ac011ebc42e30d7"

H = "Home31.dc.html"
INST = "Institutions31.dc.html"
INTL = "International31.dc.html"
SCALE = "ScaleUps31.dc.html"
ASIA = "Asia31.dc.html"

X_CLIP = "polygon(0 0, 50% 32.5%, 100% 0, 100% 32.7%, 73.1% 50.3%, 100% 67.7%, 100% 100%, 50% 67.1%, 0 100%, 0 67.7%, 26.9% 50.3%, 0 32.7%)"

HELMET = """<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&amp;family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&amp;display=swap">
<style>
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:#000}
a{color:inherit}
.h{font-family:'Archivo',Arial,sans-serif;font-weight:900;text-transform:uppercase;letter-spacing:-0.02em}
.wrap{max-width:1264px;margin:0 auto;padding-left:32px;padding-right:32px}
.ul{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px;text-decoration-color:#DFFF13}
.lt .ul{text-decoration-color:#000}
.row{transition:background .2s}.row:hover .go{color:#DFFF13}.lt .row:hover{background:#F4F4F4}.lt .row:hover .go{color:#000}
.chip{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:999px;border:1px solid #000;font-weight:500;font-size:16px}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #DFFF13;outline-offset:4px}
.lt a:focus-visible,.lt summary:focus-visible,.lt button:focus-visible,.lt input:focus-visible,.lt select:focus-visible,.lt textarea:focus-visible{outline-color:#000}
summary{list-style:none;cursor:pointer}summary::-webkit-details-marker{display:none}
details[open] .pl{transform:rotate(45deg)}
@media (prefers-reduced-motion:no-preference){.pl{transition:transform .2s}}
@media (max-width:1100px){.navl{display:none !important}.mbtn{display:inline-flex !important}}
@media (max-width:640px){.wrap{padding-left:20px;padding-right:20px}.hidem{display:none !important}}
</style>
</helmet>"""

NAV = [(INST, "Institutions"), (INTL, "International companies"), (SCALE, "UK scale-ups"), (ASIA, "Asia corridor"),
       (H + "#insights", "Insights"), (H + "#events", "Events"), (H + "#about", "About")]


def btn(label, href, kind="primary", light=False):
    if kind == "primary":
        st = "background: #DFFF13; color: #000000"
    else:
        st = "border: 2px solid " + ("#000000; color: #000000" if light else "#FFFFFF; color: #FFFFFF")
    return ('<a href="' + href + '" style="display: inline-flex; align-items: center; min-height: 52px; padding: 0 28px; border-radius: 999px; ' + st +
            '; font-weight: 700; font-size: 17px; text-decoration: none">' + label + '</a>')


def chrome_top(current):
    links = "\n        ".join(
        '<a href="' + h + '" style="text-decoration: ' + ('underline; text-decoration-color: #DFFF13; text-decoration-thickness: 2px; text-underline-offset: 8px" aria-current="page"' if h == current else 'none"') + '>' + t + '</a>'
        for h, t in NAV)
    return """  <div style="border-bottom: 1px solid #262626">
    <p class="wrap" style="margin: 0 auto; padding-top: 10px; padding-bottom: 10px; font-size: 15px; text-align: center; color: #D1D1D1"><span style="color: #DFFF13; font-weight: 700">Global Innovator Awards</span> · 16 November 2026 · <a href=\"""" + H + """#events" class="ul" style="color: #FFFFFF">Get tickets</a></p>
  </div>
  <header class="wrap" style="padding-top: 24px; padding-bottom: 24px; display: flex; align-items: center; justify-content: space-between; gap: 24px">
    <a href=\"""" + H + """\" aria-label="NEXUS home" style="display: flex; flex: none"><img src=\"""" + LOGO + """\" alt="NEXUS" style="height: 22px; width: auto; display: block"></a>
    <nav aria-label="Main" class="navl" style="display: flex; gap: 24px; font-size: 15px; font-weight: 500">
        """ + links + """
    </nav>
    <div style="display: flex; align-items: center; gap: 20px; flex: none">
      <a href=\"""" + H + """#partner" class="navl" style="font-size: 15px; font-weight: 700; text-decoration: none">Partner with NEXUS</a>
      <a href="#contact" style="display: inline-flex; align-items: center; min-height: 48px; padding: 0 22px; border-radius: 999px; background: #DFFF13; color: #000000; font-weight: 700; font-size: 15px; text-decoration: none">Talk to us</a>
      <button type="button" class="mbtn" aria-expanded="false" style="display: none; align-items: center; min-height: 48px; padding: 0 18px; border: 1px solid #FFFFFF; border-radius: 999px; background: transparent; color: #FFFFFF; font: inherit; font-weight: 700; cursor: pointer">Menu</button>
    </div>
  </header>
"""


FOOTER = """  <footer style="border-top: 1px solid #262626">
    <div class="wrap" style="padding-top: 72px; padding-bottom: 40px">
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 48px">
        <div style="flex: 1 1 300px; min-width: 0">
          <img src=\"""" + WEBUILD + """\" alt="NEXUS. We build businesses." style="height: 56px; width: auto; display: block">
          <p style="margin: 24px 0 0; max-width: 340px; color: #BDBDBD; font-size: 16px">Helping technology businesses land, grow and scale in the UK, with China as our flagship corridor.</p>
        </div>
        <nav aria-label="Footer" style="flex: 2 1 560px; min-width: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(160px, 100%), 1fr)); gap: 32px; font-size: 16px">
          <div style="display: flex; flex-direction: column; gap: 10px"><span style="font-weight: 700; color: #DFFF13">Who we help</span><a href=\"""" + INST + """\" style="text-decoration: none">Institutions</a><a href=\"""" + INTL + """\" style="text-decoration: none">International companies</a><a href=\"""" + SCALE + """\" style="text-decoration: none">UK scale-ups</a><a href=\"""" + H + """#partner" style="text-decoration: none">Partner with NEXUS</a></div>
          <div style="display: flex; flex-direction: column; gap: 10px"><span style="font-weight: 700; color: #DFFF13">Explore</span><a href=\"""" + ASIA + """\" style="text-decoration: none">Asia corridor</a><a href=\"""" + H + """#results" style="text-decoration: none">Results</a><a href=\"""" + H + """#insights" style="text-decoration: none">Insights</a><a href=\"""" + H + """#events" style="text-decoration: none">Events</a><a href=\"""" + H + """#about" style="text-decoration: none">About and team</a><a href=\"""" + H + """#questions" style="text-decoration: none">Endorsing role (UKES)</a><a href=\"""" + H + """#insights" style="text-decoration: none">NEXUS Startup Diaries</a></div>
          <div style="display: flex; flex-direction: column; gap: 10px"><span style="font-weight: 700; color: #DFFF13">Contact</span><a href="#contact" style="text-decoration: none">Talk to us →</a><span style="color: #9E9E9E">[Email address to be confirmed]</span><a href="#" style="text-decoration: none">LinkedIn</a><a href="#" style="text-decoration: none">Instagram</a><a href="#" style="text-decoration: none">X</a><a href="#" style="text-decoration: none">Facebook</a></div>
        </nav>
      </div>
      <div style="margin-top: 64px; padding-top: 24px; border-top: 1px solid #262626; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; font-size: 14px; color: #9E9E9E">
        <span>© 2026 NEXUS Creative HQ Ltd · Company number 12667243 · [Registered office to be confirmed]</span>
        <span><a href="#">Privacy</a> · <a href="#">Cookies</a> · <a href="#">Terms</a> · <a href="#">Accessibility</a></span>
      </div>
    </div>
  </footer>
"""


def page(title, current, body, height):
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<title>" + title +
            "</title>\n<script src=\"./support.js\"></script>\n</head>\n<body>\n<x-dc>\n" + HELMET +
            "\n<div style=\"font-family: 'DM Sans', Arial, sans-serif; font-size: 17px; line-height: 1.6; color: #FFFFFF; background: #000000\">\n" +
            chrome_top(current) + body + FOOTER + "</div>\n</x-dc>\n<script type=\"text/x-dc\" data-dc-script data-props='{\"$preview\":{\"width\":1440,\"height\":" +
            str(height) + "}}'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n")


def ph(text, h="100%", dark=True):
    return ('<div role="img" aria-label="' + text.strip('[]') + '" style="width: 100%; height: ' + h + '; background: ' + ('#1C1C1C' if dark else '#D1D1D1') +
            '; display: flex; align-items: center; justify-content: center; text-align: center; padding: 24px; font-size: 15px; color: ' + ('#9E9E9E' if dark else '#333333') + '">' + text + '</div>')


def x_photo(label, caption, sphere=True):
    s = ('<img src="' + B1 + '" alt="" aria-hidden="true" style="position: absolute; right: -6%; top: -4%; width: 30%; max-width: 160px; height: auto">' if sphere else '')
    return ('<figure style="margin: 0; position: relative">'
            '<div role="img" aria-label="' + label.strip('[]') + '" style="position: relative; width: 100%; aspect-ratio: 1080 / 1070; clip-path: ' + X_CLIP + '; background: #2E2E2E"></div>' + s +
            '<figcaption style="margin-top: 14px; font-size: 14px; color: #9E9E9E">' + label + ' · ' + caption + '</figcaption></figure>')


def eyebrow(text, light=False):
    return '<p style="margin: 0 0 20px; font-weight: 700; font-size: 15px; letter-spacing: 0.02em; color: ' + ('#000000' if light else '#DFFF13') + '">' + text + '</p>'


def h2(text, size="clamp(36px, 4.4vw, 60px)", mb="24px"):
    return '<h2 class="h" style="margin: 0 0 ' + mb + '; font-size: ' + size + '; line-height: 0.95; max-width: 960px">' + text + '</h2>'


def sec(inner, sid=None, bg="#000000", light=False, top_rule=False, pad="104px"):
    style = "background: " + bg + ("; color: #000000" if light else "") + ("; border-top: 8px solid #DFFF13" if top_rule else "")
    return ('  <section' + (' id="' + sid + '"' if sid else '') + (' class="lt"' if light else '') + ' style="' + style + '">\n'
            '    <div class="wrap" style="padding-top: ' + pad + '; padding-bottom: ' + pad + '">\n' + inner + '\n    </div>\n  </section>\n')


def quote(text, who, light=False):
    return ('<figure style="margin: 0; max-width: 980px"><blockquote class="h" style="margin: 0; font-size: clamp(26px, 3vw, 40px); line-height: 1.08">“' + text + '”</blockquote>'
            '<figcaption style="margin-top: 20px; font-size: 16px; font-weight: 700; color: ' + ('#333333' if light else '#BDBDBD') + '">' + who + '</figcaption></figure>')


def case_card(sector, name, headline, outcome, q=None, who=None, light=True):
    sub = '#333333' if light else '#BDBDBD'
    line = '#D1D1D1' if light else '#333333'
    out = ('<article style="display: flex; flex-direction: column; gap: 12px; padding: 32px 0; border-top: 2px solid ' + ('#000000' if light else '#FFFFFF') + '">'
           '<span style="font-size: 14px; font-weight: 700; color: ' + sub + '">' + sector + '</span>'
           '<h3 class="h" style="margin: 0; font-size: 28px; line-height: 1">' + name + '</h3>'
           '<p style="margin: 0; font-weight: 700; font-size: 19px; line-height: 1.35">' + headline + '</p>'
           '<p style="margin: 0; color: ' + sub + '">' + outcome + '</p>')
    if q:
        out += ('<p style="margin: 8px 0 0; padding-top: 16px; border-top: 1px solid ' + line + '; font-style: italic; color: ' + sub + '">“' + q + '”<br><span style="font-style: normal; font-weight: 700; font-size: 15px">' + who + '</span></p>')
    return out + '<a href="#" class="ul" style="margin-top: auto; padding-top: 8px; font-weight: 700">Read the case study →</a></article>'


def grid(items, minw=300, gap="32px 40px"):
    return ('<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(' + str(minw) + 'px, 100%), 1fr)); gap: ' + gap + '">' + "".join(items) + '</div>')


def faq(items, light=False):
    line = '#D1D1D1' if light else '#333333'
    sub = '#333333' if light else '#D1D1D1'
    return ('<div style="border-top: 2px solid ' + ('#000000' if light else '#FFFFFF') + '">' + "".join(
        '<details style="border-bottom: 1px solid ' + line + '"' + (' open' if i == 0 else '') + '><summary style="display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 22px 0; font-weight: 700; font-size: 19px">' + q +
        '<span class="pl" aria-hidden="true" style="font-size: 30px; line-height: 1; font-weight: 400; color: ' + ('#000000' if light else '#DFFF13') + '">+</span></summary><p style="margin: 0 0 24px; max-width: 760px; color: ' + sub + '">' + a + '</p></details>'
        for i, (q, a) in enumerate(items)) + '</div>')


INP = "min-height: 52px; background: transparent; color: #FFFFFF; border: 0; border-bottom: 1px solid #9E9E9E; padding: 0 2px; font: inherit"


def fld(fid, label, kind="text", auto=None, opts=None, full=False):
    w = '<div style="display: flex; flex-direction: column; gap: 4px' + ('; grid-column: 1 / -1' if full else '') + '"><label for="' + fid + '" style="font-size: 14px; font-weight: 700; color: #D1D1D1">' + label + '</label>'
    if opts:
        c = '<select id="' + fid + '" style="' + INP.replace("background: transparent", "background: #000000") + '"><option value="" selected disabled>Choose one</option>' + "".join('<option>' + o + '</option>' for o in opts) + '</select>'
    elif kind == "textarea":
        c = '<textarea id="' + fid + '" rows="3" style="' + INP.replace("min-height: 52px; ", "").replace("padding: 0 2px", "padding: 10px 2px") + '; resize: vertical"></textarea>'
    else:
        c = '<input id="' + fid + '" type="' + kind + '"' + (' autocomplete="' + auto + '"' if auto else '') + ' style="' + INP + '">'
    return w + c + '</div>'


def enquiry(sid, title, intro, nexts, fields, button):
    nx = "".join('<li style="display: flex; gap: 14px; padding: 12px 0; border-top: 1px solid #333333"><span class="h" style="color: #DFFF13; font-size: 18px">' + str(i + 1) + '</span><span>' + n + '</span></li>' for i, n in enumerate(nexts))
    return sec('<div style="display: flex; flex-wrap: wrap; gap: 56px 80px">'
               '<div style="flex: 1 1 360px; min-width: 0">' + h2(title, "clamp(36px, 4.2vw, 56px)") + '<p style="margin: 0 0 32px; font-size: 19px; color: #D1D1D1">' + intro + '</p>'
               '<p style="margin: 0 0 4px; font-weight: 700">What happens next</p><ol style="list-style: none; margin: 0; padding: 0; color: #D1D1D1">' + nx + '</ol></div>'
               '<form style="flex: 1 1 480px; min-width: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 28px 32px; align-content: start">' + "".join(fields) +
               '<div style="grid-column: 1 / -1; display: flex; align-items: flex-start; gap: 12px"><input id="' + sid + '-consent" type="checkbox" style="width: 22px; height: 22px; margin: 2px 0 0; accent-color: #DFFF13"><label for="' + sid + '-consent" style="font-size: 15px; color: #D1D1D1">Send me occasional updates from NEXUS. We use your details only to respond to this request. <a href="#" class="ul">[Privacy notice link]</a></label></div>'
               '<div style="grid-column: 1 / -1"><button type="button" style="min-height: 56px; padding: 0 32px; border: 0; border-radius: 999px; background: #DFFF13; color: #000000; font: inherit; font-weight: 700; font-size: 17px; cursor: pointer">' + button + '</button></div></form></div>',
               sid=sid)


def hero(crumb, kicker, h1, intro, b1, b1h, b2, b2h, art):
    bc = ('<nav aria-label="Breadcrumb" style="font-size: 14px; color: #9E9E9E; margin-bottom: 40px"><a href="' + H + '">Home</a> / <span aria-current="page" style="color: #FFFFFF">' + crumb + '</span></nav>') if crumb else ''
    return ('  <section>\n    <div class="wrap" style="padding-top: ' + ('40px' if crumb else '64px') + '; padding-bottom: 104px">' + bc +
            '<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 56px">'
            '<div style="flex: 999 1 560px; min-width: 0">' + eyebrow(kicker) +
            '<h1 class="h" style="margin: 0; font-size: clamp(46px, 6.2vw, 88px); line-height: 0.93">' + h1 + '</h1>'
            '<p style="margin: 32px 0 0; max-width: 600px; font-size: 20px; color: #D1D1D1">' + intro + '</p>'
            '<div style="display: flex; flex-wrap: wrap; gap: 16px; margin-top: 40px">' + btn(b1, b1h) + (btn(b2, b2h, "secondary") if b2 else '') + '</div></div>'
            '<div class="hidem" style="flex: 1 1 380px; min-width: 0; max-width: 480px">' + art + '</div>'
            '</div>\n    </div>\n  </section>\n  <div aria-hidden="true" style="height: 8px; background: #DFFF13"></div>\n')


def offer_rows(items, light=False):
    line = '#D1D1D1' if light else '#333333'
    sub = '#333333' if light else '#BDBDBD'
    out = '<div style="border-top: 2px solid ' + ('#000000' if light else '#FFFFFF') + '">'
    for tag, name, intro, bullets, price in items:
        out += ('<div style="display: flex; flex-wrap: wrap; gap: 20px 56px; padding: 40px 0; border-bottom: 1px solid ' + line + '">'
                '<div style="flex: 1 1 340px; min-width: 0"><p style="margin: 0 0 10px; font-weight: 700; font-size: 15px; color: ' + ('#000000' if light else '#DFFF13') + '">' + tag + '</p>'
                '<h3 class="h" style="margin: 0; font-size: clamp(28px, 3vw, 40px); line-height: 1">' + name + '</h3>'
                '<p style="margin: 14px 0 0; color: ' + sub + '">' + intro + '</p></div>'
                '<div style="flex: 1 1 380px; min-width: 0"><ul style="margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 6px">' + "".join('<li>' + b + '</li>' for b in bullets) + '</ul>'
                '<p style="margin: 18px 0 0; font-weight: 700">' + price + '</p></div></div>')
    return out + '</div>'


def steps(items):
    return ('<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(190px, 100%), 1fr)); gap: 32px">' + "".join(
        '<li style="border-top: 2px solid #DFFF13; padding-top: 18px"><span class="h" style="display: block; font-size: 44px; line-height: 1; color: #DFFF13">' + str(i + 1) + '</span>'
        '<span class="h" style="display: block; margin-top: 14px; font-size: 22px">' + t + '</span><span style="display: block; margin-top: 6px; color: #BDBDBD">' + d + '</span></li>'
        for i, (t, d) in enumerate(items)) + '</ol>')


def fit(yes, no):
    return grid(['<div style="border-top: 2px solid #000000; padding-top: 20px"><h3 class="h" style="margin: 0 0 12px; font-size: 26px">This is for you if</h3><p style="margin: 0; font-size: 19px">' + yes + '</p></div>',
                 '<div style="border-top: 2px solid #D1D1D1; padding-top: 20px"><h3 class="h" style="margin: 0 0 12px; font-size: 26px; color: #555555">This is not for you if</h3><p style="margin: 0; font-size: 19px; color: #333333">' + no + '</p></div>'], 380, "32px 64px")


def why(items):
    return grid(['<div style="border-top: 2px solid #FFFFFF; padding-top: 20px"><h3 class="h" style="margin: 0 0 10px; font-size: 24px; line-height: 1.05">' + t + '</h3><p style="margin: 0; color: #BDBDBD">' + d + '</p></div>' for t, d in items], 300)


# ============================================================ HOME (brief 4.2)
home = hero(None, "UK growth partner · China flagship corridor", "Land, grow and scale technology businesses in the UK.",
            "NEXUS works with international technology companies, the institutions that back them, and UK scale-ups ready for their next stage. One accountable team in the UK, with partners on the ground in China.",
            "Find your route", "#routes", "Talk to our team", "#contact",
            x_photo("[Photo: signing ceremony, Tianjin]", "Signing ceremony, Tianjin. [Caption to be confirmed]"))
# proof strip
home += ('  <section aria-label="Proof"><div class="wrap" style="padding-top: 72px; padding-bottom: 72px">' +
         grid(['<div><div class="h" style="font-size: 64px; line-height: 1">' + n + '</div><div style="margin-top: 8px; color: #BDBDBD">' + l + '</div></div>' for n, l in
               [("100+", "Businesses actively supported"), ("16", "Carefully curated global partnerships"), ("1,400+", "Business plans assessed")]] +
              ['<div><div class="h" style="font-size: 30px; line-height: 1.05; padding-top: 8px">Supplier and security cleared</div><div style="margin-top: 8px; color: #BDBDBD">UK Government supplier</div></div>'], 220) +
         '<div style="margin-top: 56px; padding-top: 24px; border-top: 1px solid #333333; display: flex; flex-wrap: wrap; align-items: center; gap: 16px 40px"><span style="font-weight: 700; font-size: 15px; color: #9E9E9E">Partners and memberships</span>' +
         "".join('<span class="h" style="font-size: 20px; color: #9E9E9E">' + n + '</span>' for n in ["City of London", "TEDA", "S-Tron", "CBBC"]) +
         '<span style="font-size: 13px; color: #9E9E9E">[Logos once each permission is confirmed]</span></div></div></section>\n')
# who we work with
routes = [("For institutions", "A UK operating partner for your companies", "For science parks, innovation zones, hubs and funds. We act as your UK presence: showcase events, a deal-flow pipeline and landing support for your portfolio.", "Explore institutional partnership", INST),
          ("For international companies", "Reach UK customers sooner", "For technology companies entering the UK. Market intelligence, qualified introductions, soft landing support and vetted legal, finance and banking partners.", "See market entry support", INTL),
          ("For UK scale-ups", "Solve the growth problem in front of you", "For frontier-tech companies already trading. A focused diagnostic, then specialist delivery through our partner network, managed by NEXUS.", "Book a growth diagnostic", SCALE)]
rows = '<div style="border-top: 2px solid #000000">' + "".join(
    '<a href="' + href + '" class="row" style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 36px 0; border-bottom: 1px solid #D1D1D1; text-decoration: none">'
    '<span style="flex: 1 1 380px; min-width: 0"><span style="display: block; font-weight: 700; font-size: 15px; color: #555555">' + tag + '</span><span class="h" style="display: block; margin-top: 8px; font-size: clamp(28px, 3vw, 40px); line-height: 1">' + title + '</span></span>'
    '<span style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 14px"><span style="color: #333333">' + text + '</span><span class="go" style="font-weight: 700">' + link + ' →</span></span></a>'
    for tag, title, text, link, href in routes) + '</div>'
home += sec(eyebrow("Who we work with", True) + h2("Three ways in. One team behind them.", mb="48px") + rows, "routes", "#FFFFFF", True)
# how we work
home += sec('<div style="display: flex; flex-wrap: wrap; gap: 56px 72px; align-items: flex-end; margin-bottom: 64px"><div style="flex: 999 1 520px; min-width: 0">' + eyebrow("How we work") + h2("Hands-on, with one point of accountability.") +
            '<p style="margin: 0; max-width: 620px; font-size: 19px; color: #D1D1D1">We stay with you from the first conversation to results, and bring in specialists only when you need them. No generic programmes and no hand-offs you have to manage yourself.</p></div>'
            '<div class="hidem" style="flex: 1 1 320px; min-width: 0; height: 240px">' + ph("[Photo: NEXUS team at work]") + '</div></div>' +
            steps([("Diagnose", "We pinpoint what you need to achieve in the UK, and what stands in the way."), ("Plan", "A clear plan with owners, timings and costs."),
                   ("Connect", "Introductions to the customers, partners, investors and advisers that matter."), ("Deliver", "We manage the work, including specialist partners, as your single contact."),
                   ("Grow", "We review results with you and plan the next stage.")]))
# Asia corridor (white, yellow top rule)
partners = [("China", "RidgeCore Ventures", "A reciprocal partnership. We represent their clients in the UK; they represent ours in China."),
            ("Hong Kong", "Alibaba Entrepreneurs Fund", "A route for growth-stage companies expanding overseas through Hong Kong. [In discussion. Name used only with written approval]"),
            ("Tianjin", "Tianjin", "Two signed MOUs, building a pipeline of Tianjin companies into the UK."),
            ("Shanghai", "S-Tron", "Two years together at S-Tron Shanghai, exhibiting and speaking."),
            ("Shanghai · Switzerland", "Swiss Bluefaer Innovation Centre", "Connecting European and Chinese innovators. [Relationship wording to be approved]")]
home += sec('<div style="display: flex; flex-wrap: wrap; gap: 32px 72px; align-items: flex-end; margin-bottom: 56px"><div style="flex: 999 1 520px; min-width: 0">' + eyebrow("Our Asia corridor, led by China", True) + h2("A working corridor in both directions.", mb="0") + '</div>'
            '<p style="flex: 1 1 380px; min-width: 0; margin: 0; color: #333333">China is our flagship international market, and Hong Kong is our gateway to the wider region. We have built what many UK organisations spend years trying to establish: an operating corridor between the UK and Asia, with partners on the ground.</p></div>' +
            grid(['<div style="border-top: 2px solid #000000; padding-top: 18px"><span style="font-size: 14px; font-weight: 700; color: #555555">' + w + '</span><h3 class="h" style="margin: 8px 0 10px; font-size: 22px; line-height: 1.05">' + n + '</h3><p style="margin: 0; font-size: 16px; color: #333333">' + d + '</p></div>' for w, n, d in partners], 190, "32px 28px") +
            '<div style="display: flex; flex-wrap: wrap; gap: 16px; margin-top: 56px">' + btn("Explore the Asia corridor", ASIA) + btn("Register interest in 2027 delegations", ASIA + "#delegations", "secondary", True) + '</div>',
            "corridor", "#FFFFFF", True, True)
# results
home += sec('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 56px">' + '<div>' + eyebrow("Results", True) + h2("What we have delivered for clients.", mb="0") + '</div><a href="#results" class="ul" style="font-weight: 700">All case studies →</a></div>' +
            quote("NEXUS did not just give us advice, it helped us get closer to the people and opportunities that could move the business forward.", "Ash Ganesan Indra and Adip Ranjan Das, Co-Founders, GI Healthcare", True) +
            '<div style="margin-top: 64px">' + grid([case_card("Aerospace and deep tech", "Sentian Aerospace", "From a garage to an international acquisition", "Technology acquired by Volatus Aerospace, a publicly listed company, in under two years from UK incorporation."),
                                                     case_card("Deep tech and robotics", "GI Healthcare", "From an early prototype to customer-backed pilots", "From no customers to a customer-funded proof of concept and a follow-on programme."),
                                                     case_card("AI compute infrastructure", "Auto Impartial", "New silicon for the age of private AI", "Core architecture independently validated; a UK and Asia research consortium in formation with Innovate UK.")]) + '</div>',
            "results", "#D1D1D1", True)
# events
home += sec(eyebrow("Events") + h2("The right people in the right room.", mb="56px") +
            grid(['<div style="border: 2px solid #DFFF13; padding: 40px; display: flex; flex-direction: column; gap: 14px; height: 100%"><span style="font-weight: 700; color: #DFFF13">16 November 2026</span><h3 class="h" style="margin: 0; font-size: 36px; line-height: 1">Global Innovator Awards</h3><p style="margin: 0; color: #D1D1D1">Created and delivered by NEXUS. Celebrating overseas founders building businesses in the UK.</p><div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: auto; padding-top: 12px">' + btn("Get tickets", "#events") + btn("About the awards", "#events", "secondary") + '</div></div>',
                  '<div style="border: 1px solid #333333; padding: 40px; display: flex; flex-direction: column; gap: 14px; height: 100%"><span style="font-weight: 700; color: #BDBDBD">[Working name]</span><h3 class="h" style="margin: 0; font-size: 36px; line-height: 1">NEXUS Sessions</h3><p style="margin: 0; color: #D1D1D1">Monthly sessions with the people you need to meet. In-person sessions on a set topic, at partner venues around the UK. Each one brings together founders, institutions and specialists. [Venue partner and launch date to be confirmed]</p><div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: auto; padding-top: 12px">' + btn("Register interest", "#events", "secondary") + btn("Sponsor a session", "#partner", "secondary") + '</div></div>'], 380),
            "events")
# partner network
home += sec('<div style="display: flex; flex-wrap: wrap; gap: 40px 80px; align-items: center"><div style="flex: 1 1 380px; min-width: 0">' + eyebrow("Our partner network", True) + h2("Specialists join when you need them.", "clamp(32px, 3.6vw, 48px)") +
            '<p style="margin: 0 0 24px; color: #333333">NEXUS stays your single point of contact.</p><a href="#partner" class="ul" style="font-weight: 700">Professional firm? Partner with NEXUS →</a></div>'
            '<div style="flex: 1 1 480px; min-width: 0"><div style="display: flex; flex-wrap: wrap; gap: 10px">' + "".join('<span class="chip">' + c + '</span>' for c in ["Accountancy", "Corporate finance", "Banking and payments", "Legal", "IP and patents", "AI strategy", "R&amp;D tax", "Venues"]) +
            '</div><p style="margin: 18px 0 0; font-size: 14px; color: #555555">[Named partners and logos appear only once each partner confirms in writing]</p></div></div>', "partner", "#FFFFFF", True)
# team
team = [("Mark Sarfo-Kantanka", "CEO and Co-Founder"), ("Mauria Fransishku", "NEXUS Manager"), ("Grace Mander", "Operations Manager"), ("Kolos Sipos", "Business and Finance Analyst"),
        ("Jonny Quirk", "Head of Community"), ("Sheleene Sealy", "Social Media Manager"), ("Zee West", "Head of Development")]
home += sec(eyebrow("The team") + quote("[Founder quote: one or two sentences on why NEXUS exists, to be approved]", "Mark Sarfo-Kantanka, CEO and Co-Founder") +
            '<ul style="list-style: none; margin: 64px 0 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(150px, 100%), 1fr)); gap: 28px 20px">' + "".join(
                '<li><div role="img" aria-label="Portrait of ' + n + ' to come" style="aspect-ratio: 4 / 5; background: #1C1C1C; display: flex; align-items: flex-end; padding: 14px"><span class="h" style="font-size: 30px; color: #3A3A3A">' + "".join(w[0] for w in n.split()[:2]) + '</span></div>'
                '<div style="margin-top: 12px; font-weight: 700">' + n + '</div><div style="font-size: 15px; color: #9E9E9E">' + r + '</div></li>' for n, r in team) + '</ul>'
            '<p style="margin: 20px 0 0; font-size: 14px; color: #9E9E9E">[Black and white portraits to come]</p>', "about")
# insights
arts = [("Insight", "The Next £10bn Opportunities in Creative-Tech: Where We're Seeing Signals"), ("Insight", "IP as an Asset: How Creative Founders Can Make Their Work Investable"),
        ("Insight", "Partnerships as Growth: How to Secure Collabs That Move Revenue")]
home += sec('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 48px"><div>' + eyebrow("Insights", True) + h2("Intelligence from the UK and Asia innovation corridor.", mb="0") + '</div><a href="#insights" class="ul" style="font-weight: 700">All insights →</a></div>' +
            grid(['<a href="#insights" class="row" style="display: flex; flex-direction: column; gap: 12px; padding: 24px 0; border-top: 2px solid #000000; text-decoration: none; height: 100%"><span style="font-weight: 700; font-size: 14px; color: #555555">' + t + '</span><span class="h" style="font-size: 22px; line-height: 1.1">' + n + '</span><span class="go" style="margin-top: auto; font-weight: 700">Read →</span></a>' for t, n in arts] +
                 ['<div style="background: #000000; color: #FFFFFF; padding: 28px; display: flex; flex-direction: column; gap: 12px"><span style="font-weight: 700; font-size: 14px; color: #DFFF13">Report</span><span class="h" style="font-size: 24px; line-height: 1.05">Doing Business in China 2027</span><span style="font-size: 15px; color: #BDBDBD">[Report in development: content and publication date to be confirmed]</span>'
                  '<label for="rep" style="font-size: 14px; font-weight: 700; margin-top: 8px">Work email</label><input id="rep" type="email" autocomplete="email" style="' + INP + '"><button type="button" style="align-self: flex-start; margin-top: 8px; min-height: 48px; padding: 0 22px; border: 0; border-radius: 999px; background: #DFFF13; color: #000000; font: inherit; font-weight: 700; cursor: pointer">Get the report</button></div>'], 240),
            "insights", "#FFFFFF", True)
# questions
home += sec('<div style="display: flex; flex-wrap: wrap; gap: 40px 80px"><div style="flex: 1 1 300px; min-width: 0">' + h2("Common questions", "clamp(32px, 3.6vw, 48px)") + '</div><div style="flex: 2 1 560px; min-width: 0">' + faq([
    ("What does NEXUS do?", "NEXUS helps technology businesses land, grow and scale in the UK. We work with international technology companies entering the UK, the innovation institutions that back them, and UK scale-ups ready for their next stage. China is our flagship corridor."),
    ("Who do you work with?", "Science parks, innovation zones, hubs and funds; international technology companies; UK frontier-tech companies that are already trading; and professional firms that partner with us or sponsor our events."),
    ("How do you work with institutions outside the UK?", "We act as their operational presence in the UK. We represent them, run showcase events, build a pipeline of opportunities and support their companies as they land. Our MOU with Binhai Zhongguancun Science Park in Tianjin is one example."),
    ("Do you endorse visa applications?", "NEXUS reviews and endorses Innovator Founder applicants as a consortium partner of UK Endorsing Services (UKES). Applications are made through UKES, and endorsement decisions are entirely separate from our commercial services."),
    ("How do I start, and what does it cost?", "Companies and scale-ups start with a paid diagnostic: a focused session and a written plan, with the fee credited against further work [fee to be confirmed]. Institutions start with a partnership call.")]) + '</div></div>', "questions")
# contact routes
tiles = [("Institutions", "Discuss a UK partnership", "Representation and landing programmes for your companies.", "Book a partnership call", INST + "#start"),
         ("Companies and scale-ups", "Start with a diagnostic", "A focused session and written plan for your next stage.", "Book a paid diagnostic", INTL + "#start"),
         ("Firms and sponsors", "Reach our audience", "Session and awards sponsorship, and referral partnerships.", "Request the sponsor pack", "#partner")]
home += sec('<div style="text-align: center; margin-bottom: 64px"><h2 class="h" style="margin: 0 auto; font-size: clamp(44px, 5.6vw, 84px); line-height: 0.92; max-width: 960px">Tell us where you want to grow.</h2><p style="margin: 24px auto 0; max-width: 560px; font-size: 19px; color: #D1D1D1">Choose the route that fits. Each one goes straight to the right person on our team.</p></div>' +
            grid(['<div style="border-top: 2px solid #DFFF13; padding-top: 24px; display: flex; flex-direction: column; gap: 10px; height: 100%"><span style="font-weight: 700; font-size: 15px; color: #DFFF13">' + a + '</span><h3 class="h" style="margin: 0; font-size: 28px; line-height: 1">' + b + '</h3><p style="margin: 0; color: #BDBDBD">' + c + '</p><div style="margin-top: auto; padding-top: 12px">' + btn(d, e) + '</div></div>' for a, b, c, d, e in tiles], 300) +
            '<p style="margin: 48px 0 0; text-align: center; color: #9E9E9E">General enquiries: [email address to be confirmed]</p>', "contact")


# ============================================================ AUDIENCE PAGES (brief 4.3)
def audience(crumb, kicker, h1, intro, cta, sphere_art, chal_quote, chal_text, offers_title, offers, why_title, whys, cases_html, fit_yes, fit_no, how_steps, qs, form):
    p = hero(crumb, kicker, h1, intro, cta, "#start", "How it works", "#how", sphere_art)
    p += sec('<div style="display: flex; flex-wrap: wrap; gap: 40px 80px; align-items: flex-start"><div style="flex: 999 1 560px; min-width: 0">' + eyebrow("The challenge") + quote(chal_quote, "") + '</div>'
             '<div style="flex: 1 1 360px; min-width: 0; display: flex; flex-direction: column; gap: 16px; color: #D1D1D1; font-size: 18px">' + "".join('<p style="margin: 0">' + t + '</p>' for t in chal_text) + '</div></div>')
    p += sec(eyebrow("How we can help", True) + h2(offers_title, mb="48px") + offer_rows(offers, True), "offers", "#FFFFFF", True)
    p += sec(eyebrow(why_title) + '<div style="margin-bottom: 72px">' + why(whys) + '</div>' + cases_html)
    p += sec(fit(fit_yes, fit_no), None, "#FFFFFF", True)
    p += sec(eyebrow("How it works") + h2("How it works", mb="48px") + steps(how_steps), "how")
    p += sec('<div style="display: flex; flex-wrap: wrap; gap: 40px 80px"><div style="flex: 1 1 300px; min-width: 0">' + h2("Questions", "clamp(32px, 3.6vw, 48px)") + '</div><div style="flex: 2 1 560px; min-width: 0">' + faq(qs, True) + '</div></div>', "questions", "#FFFFFF", True)
    p += enquiry("start", *form)
    return p


SPH = ('<div style="position: relative; aspect-ratio: 1 / 1"><img src="' + B1 + '" alt="" aria-hidden="true" style="position: absolute; right: 0; top: 0; width: 82%; height: auto">'
       '<img src="' + B3 + '" alt="" aria-hidden="true" style="position: absolute; left: 0; bottom: 6%; width: 34%; height: auto"><img src="' + B2 + '" alt="" aria-hidden="true" style="position: absolute; right: 12%; bottom: 0; width: 16%; height: auto"></div>')


def cases_block(title, cards):
    return '<h3 class="h" style="margin: 0 0 32px; font-size: clamp(28px, 3vw, 40px)">' + title + '</h3>' + grid(cards, 320)


inst_page = audience(
    "For institutions", "For science parks, innovation zones, hubs and funds", "Your operating partner in the UK.",
    "Give your companies a UK presence without opening a UK office. We represent you, run showcase events, build a deal-flow pipeline and support your companies as they land.",
    "Book a partnership call", x_photo("[Photo: NEXUS with an institutional delegation]", "[Photo and caption to be confirmed]"),
    "We need international outcomes for our companies, but a UK team takes years to build.",
    ["Innovation institutions are expected to show results abroad: companies landing, partnerships signed, investment won. Doing that from a distance is slow, and opening an overseas office is expensive and hard to justify.",
     "NEXUS gives you an operational presence in the UK from day one, run by a team that already works on both sides of the UK and China corridor."],
    "What we provide",
    [("Annual", "UK Representation", "We act as your UK presence for the year, representing your institution and your companies.",
      ["A named UK point of contact for your institution", "Showcase events and exhibition presence in the UK", "A pipeline of qualified UK partners, customers and investors", "Landing support for companies you refer to us", "Regular reporting on activity and outcomes"], "Annual retainer, on application"),
     ("Per cohort", "UK Landing Programme", "A group of your companies lands in the UK together, with a programme built around their sectors.",
      ["Pre-arrival market briefing for each company", "A curated UK programme of meetings and site visits [format to be confirmed]", "A showcase event with UK buyers, partners and investors", "Introductions to legal, banking and accountancy partners", "Follow-up support after the programme"], "Priced per cohort, on application")],
    "Why institutions work with us",
    [("Already operating in China", "A signed MOU with Binhai Zhongguancun Science Park in Tianjin, and a reciprocal partnership with RidgeCore Ventures in Hainan."),
     ("We know what UK success requires", "More than 1,400 business plans assessed within the UK endorsement system, and 100+ businesses actively supported."),
     ("Connected in the UK", "Members of the China-Britain Business Council, with 16 carefully curated global partnerships and the Global Innovator Awards.")],
    quote("[Partner testimonial from an institution: approval required]", "[Name, role, institution]") +
    '<div style="margin-top: 48px; height: 160px">' + ph("[Institution case study: results from a representation or landing programme, approval required]") + '</div>',
    "You lead a government-linked innovation zone, science park, incubator or corporate venture fund, and your companies are ready to grow internationally.",
    "You are looking for a one-off introduction or a speaking slot without a programme behind it.",
    [("Partnership call", "We learn about your goals, your companies and your timelines."), ("Proposal", "A scoped plan with deliverables, reporting and price."),
     ("Agreement", "We agree terms and onboard your team and first companies."), ("Delivery", "Events, introductions and landing support, with regular reports."),
     ("Review", "We review outcomes together and plan the following year.")],
    [("Do you only work with institutions in China?", "China is our flagship corridor and where our partnerships are strongest. We also work with institutions elsewhere where there is a clear UK opportunity."),
     ("How are payments from mainland China handled?", "[Answer to be confirmed: payment arrangements for clients in mainland China]"),
     ("How long does a programme run?", "UK Representation runs annually. Landing programme timings are agreed with each institution [typical duration to be confirmed].")],
    ("Book a partnership call", "Tell us about your institution and what you want to achieve in the UK.",
     ["We reply within two working days [service level to be confirmed]", "A 30-minute call with our partnerships lead", "A written proposal if there is a fit"],
     [fld("io", "Organisation", auto="organization"), fld("ic", "Country", auto="country-name"), fld("it", "Type of institution", opts=["Science park", "Innovation zone", "Incubator or accelerator", "Fund", "Other"]),
      fld("ii", "Main interest", opts=["UK Representation", "UK Landing Programme", "Not sure yet"]), fld("in", "Your name and role", auto="name"), fld("ie", "Work email", "email", "email"),
      fld("im", "What would you like to achieve?", "textarea", full=True)], "Request a call"))

intl_page = audience(
    "For international companies", "For technology companies entering the UK", "Enter the UK with a team already on the ground.",
    "We help you reach your first UK customers and partners sooner, with less risk. Market intelligence, the right introductions, soft landing support and vetted specialist partners, managed by one team.",
    "Book a paid diagnostic", SPH,
    "We are ready for the UK, but we do not know the market, the rules or the right people.",
    ["Entering a new market from a distance is slow. Companies lose months finding the right partners, setting up correctly and getting in front of real buyers.",
     "NEXUS works as your team on the ground: we qualify opportunities, open the right doors and bring in the specialists you need, so your leadership can focus on winning business."],
    "Three ways in",
    [("Start here", "Market-Entry Diagnostic", "A focused session and a written UK entry plan for your company.",
      ["Your UK opportunity, priorities and risks", "Recommended route to market and set-up", "The introductions and partners you will need", "A costed plan for the next stage"], "Fixed fee [to be confirmed], credited against further work"),
     ("Ongoing", "UK Soft Landing", "Hands-on support while you establish your UK presence.",
      ["A named UK point of contact", "Qualified customer and partner introductions", "Introductions to legal, banking and accountancy partners", "Conference and event representation"], "Set-up fee plus monthly retainer, on application"),
     ("One-off", "Market Intelligence Report", "A sector and competitor briefing for a specific UK decision.",
      ["Market size and demand signals", "Competitors, buyers and channels", "Regulation and standards to plan for", "Recommended next steps"], "Fixed fee, on application")],
    "Why companies choose NEXUS",
    [("We know what UK success requires", "More than 1,400 business plans assessed within the UK endorsement system, and 100+ businesses actively supported."),
     ("On the ground in both markets", "Our partner RidgeCore Ventures represents clients in China while we represent them in the UK, so nothing is lost between the two."),
     ("One team, specialist partners", "Legal, banking, accountancy and IP specialists from our curated network, coordinated by NEXUS.")],
    cases_block("Companies we have helped land in the UK", [
        case_card("AI enterprise software", "DarkhorseOne", "AI native software for the enterprise", "UK patent filed and a commercial collaboration secured through the NEXUS network.",
                  "NEXUS helped me build DarkhorseOne not only as a technology project, but as a UK business.", "Jian Ma, Founder", False),
        case_card("CreaTech", "Eco2Life (EcoDo)", "Global brands, local stories, powered by AI", "From consultancy to a live AI platform with early revenue, and a UK patent in progress.",
                  "NEXUS helped me build Eco2Life with real structure, confidence and connection to the UK innovation ecosystem.", "Qingwen (Joy) Li, Founder", False),
        case_card("Legal tech", "Smart Patent", "IP strategy made accessible by AI", "A live platform, a national AI programme finalist, and a UK and China raise in preparation.",
                  "NEXUS gave me a supportive community, practical guidance and the perspective to develop Smart Patent.", "Jack Zhu, Founder", False)]),
    "You are a technology company with a product in market, funding or revenue, and a decision-maker committed to UK growth.",
    "You are looking only for a visa route. Innovator Founder applications are made through UK Endorsing Services, separately from our commercial services.",
    [("Diagnose", "A focused session and a written UK entry plan."), ("Plan", "We agree priorities, partners, timings and costs."),
     ("Land", "Set-up support, introductions and representation."), ("Grow", "We track results and plan your next stage.")],
    [("Do I need a UK company to start selling?", "It depends on your business model and customers. The diagnostic covers this, and our legal and accountancy partners advise on the right structure."),
     ("Can you help with visas?", "We can introduce immigration law specialists. NEXUS's endorsement work is separate and handled through UK Endorsing Services."),
     ("Do you only work with Chinese companies?", "No. China is our flagship corridor, and we work with technology companies from other markets that are serious about the UK."),
     ("Why is the diagnostic paid?", "Because it produces a real plan you can act on. The fee is credited against further work if you continue with us.")],
    ("Book a paid diagnostic", "Tell us about your company and your UK plans. We will confirm fit before you pay.",
     ["We review your details and confirm fit within two working days [service level to be confirmed]", "You choose a session time and pay securely [booking and payment tool to be confirmed]", "Your written plan follows the session"],
     [fld("cc", "Company", auto="organization"), fld("ch", "Headquarters country", auto="country-name"),
      fld("cs", "Sector", opts=["AI and robotics", "Consumer tech", "Climate", "Deep tech", "Life sciences", "Advanced manufacturing", "Other"]),
      fld("cg", "Stage", opts=["Revenue under £1m", "Revenue £1m to £10m", "Revenue over £10m", "Pre-revenue, funded"]),
      fld("cw", "When do you plan to enter the UK?", opts=["Within 6 months", "6 to 12 months", "Over 12 months"]), fld("cn", "Your name", auto="name"),
      fld("ce", "Work email", "email", "email", full=True)], "Check availability"))

scale_page = audience(
    "For UK scale-ups", "For UK frontier-tech companies already trading", "Your next stage, with the right specialists.",
    "We pinpoint what is holding your growth back, then bring in the right partners to fix it. NEXUS stays your single point of contact throughout.",
    "Book a growth diagnostic", SPH,
    "We know something is holding us back. We do not have time to find and manage five different advisers.",
    ["Growing companies hit specific problems: an unclear route to market, investment that will not close, AI they have not yet put to work, tax and finance that need fixing.",
     "We start with a focused diagnostic, agree the priority, and bring in a specialist from our partner network to deliver. You deal with one team, not five."],
    "Start with a diagnostic",
    [("Start here", "Growth Diagnostic", "A focused session with a senior NEXUS adviser and a written plan.",
      ["Where growth is stalling, and why", "The one or two priorities that matter most", "Who should deliver the work, and what it should cost", "Clear next steps you can act on immediately"], "Fixed fee [to be confirmed], credited against further work"),
     ("Then", "Partner-delivered projects", "Specialist work, scoped and coordinated by NEXUS.",
      ["Go-to-market", "Investment readiness", "AI strategy and adoption", "R&amp;D tax credits", "Accountancy", "Legal and IP"], "Priced per project, on application"),
     ("After a project", "Ongoing access", "Continued access to our partner network, roundtables and peer sessions as you grow.",
      ["[Name, format and price of the ongoing offer to be confirmed]"], "[To be confirmed]")],
    "Why scale-ups work with us",
    [("Hands-on, not generic", "We work on your specific problem, not a one-size programme."),
     ("Experienced mentors and advisers", "Our network includes founders, investors and specialists with experience at Google, Microsoft, NBCUniversal, Sky, Disney and Apple."),
     ("A wider network when you are ready", "International connections through our Asia corridor and events, when you look beyond the UK.")],
    cases_block("Results from founders we support", [
        case_card("Deep tech and robotics", "GI Healthcare", "From no customers to a customer-funded proof of concept", "A paid proof of concept and follow-on programme, moving the technology towards TRL 7.",
                  "NEXUS did not just give us advice, it helped us get closer to the people and opportunities that could move the business forward.", "Ash Ganesan Indra and Adip Ranjan Das, Co-Founders", False),
        case_card("Aerospace", "Sentian Aerospace", "From UK incorporation to exit in under two years", "Acquired by Volatus Aerospace, a publicly listed company, with the founders retained.",
                  "NEXUS gave us structure, accountability and an independent perspective.", "Edmund Moyo and Dalumuzi Dube, Co-Founders", False)]),
    "You run a UK technology company that is already trading and facing a specific growth challenge.",
    "You are at idea stage and looking for free general advice. Our events and insights are a better place to start.",
    [("Diagnose", "A focused session and a written plan."), ("Recommend", "We agree the priority and the right specialist."),
     ("Deliver", "Our partner delivers; we manage scope, timing and quality."), ("Review", "We check results with you and plan what comes next.")],
    [("Why is the diagnostic paid?", "Because it gives you a plan you can act on, not a sales pitch. The fee is credited against further work if you continue with us."),
     ("Who delivers the work?", "Specialists from our curated partner network, chosen for your problem. NEXUS scopes the work, manages delivery and remains your point of contact."),
     ("Do you take equity?", "[Answer to be confirmed]")],
    ("Book a growth diagnostic", "Tell us where you are and what is in the way. We will confirm fit before you pay.",
     ["We confirm fit within two working days [service level to be confirmed]", "You choose a session time and pay securely [booking and payment tool to be confirmed]", "Your written plan follows the session"],
     [fld("sc", "Company", auto="organization"), fld("sr", "Annual revenue", opts=["Under £500k", "£500k to £2m", "£2m to £10m", "Over £10m"]),
      fld("sm", "Main challenge", opts=["Go-to-market and sales", "Raising investment", "AI strategy and adoption", "Tax, finance or legal", "Not sure yet"]),
      fld("sn", "Your name", auto="name"), fld("se", "Work email", "email", "email", full=True), fld("sx", "Anything else we should know?", "textarea", full=True)], "Check availability"))

# ============================================================ ASIA CORRIDOR (brief 4.4)
asia_page = hero("Asia corridor", "Asia corridor · China is our flagship market", "Our Asia corridor, led by China.",
                 "China is one of the most active innovation economies in the world and the heart of our Asia corridor. Hong Kong gives companies a gateway in both directions. We have built an operating corridor with partners on the ground and a record of delegations and events.",
                 "Register for 2027 delegations", "#delegations", "Partner with us as an institution", INST,
                 x_photo("[Photo: NEXUS at S-Tron Shanghai]", "[Photo and caption to be confirmed]"))
apartners = [("China", "RidgeCore Ventures", "A reciprocal partnership. We handle UK representation for their clients; they handle China representation for ours. Together we open access to investment, knowledge transfer and franchise opportunities."),
             ("Hong Kong", "Alibaba Entrepreneurs Fund", "A route for growth-stage companies from Hong Kong and mainland China expanding overseas through Hong Kong, and for UK companies looking to Asia. [Partnership in discussion. Name, wording and logo used only with written approval from the Alibaba Entrepreneurs Fund]"),
             ("Tianjin", "Tianjin", "Two signed MOUs, building UK showcase events and a pipeline of Tianjin companies into the UK. Tianjin co-exhibited with NEXUS at S-Tron Shanghai. [Confirm partner names and MOU dates]"),
             ("Shanghai", "S-Tron", "Our partner at S-Tron Shanghai for two years: exhibiting with UK companies in 2025 and speaking on stage in 2026."),
             ("Shanghai · Switzerland", "Swiss Bluefaer Innovation Centre", "A Swiss innovation centre in Shanghai's Yangpu district, connecting European and Chinese innovators. [Describe the NEXUS relationship. Wording and logo to be approved by the partner]")]
asia_page += sec(eyebrow("Our partners across Asia", True) + h2("Partners on the ground.", mb="48px") +
                 grid(['<div style="border-top: 2px solid #000000; padding-top: 18px"><span style="font-size: 14px; font-weight: 700; color: #555555">' + w + '</span><h3 class="h" style="margin: 8px 0 10px; font-size: 26px; line-height: 1.05">' + n + '</h3><p style="margin: 0; color: #333333">' + d + '</p></div>' for w, n, d in apartners] +
                      ['<div style="background: #000000; color: #FFFFFF; padding: 28px"><span style="font-size: 14px; font-weight: 700; color: #DFFF13">Hong Kong</span><h3 class="h" style="margin: 8px 0 10px; font-size: 26px; line-height: 1.05">Why Hong Kong</h3><p style="margin: 0; color: #D1D1D1">Hong Kong is a familiar, international base for UK companies taking their first step into Asia, and a launch point for Chinese companies heading to the UK and Europe.</p></div>'], 320, "40px 48px") +
                 '<div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid #D1D1D1; display: flex; flex-wrap: wrap; align-items: center; gap: 16px 40px"><span style="font-weight: 700; font-size: 15px; color: #555555">Partners and memberships</span><span class="h" style="font-size: 20px; color: #555555">RidgeCore Ventures</span><span class="h" style="font-size: 20px; color: #555555">S-Tron</span><span class="h" style="font-size: 20px; color: #555555">CBBC</span><span style="font-size: 13px; color: #555555">[Logos once each permission is confirmed]</span></div>',
                 "partners", "#FFFFFF", True, True)
timeline = [("2025", "First MOU with Tianjin", "The agreement behind our UK representation work for Tianjin. [Month and partner name to be confirmed]"),
            ("2025", "S-Tron Shanghai", "NEXUS and Tianjin co-exhibited, bringing UK companies to exhibit in Shanghai."),
            ("March 2026", "NEXUS opens in China", "A NEXUS company in China, with partners in Beijing and Shanghai. [Wording to be confirmed]"),
            ("April 2026", "CBBC delegation to Hangzhou", "Matchmaking sessions focused on AI, robotics and life sciences."),
            ("2026", "S-Tron Shanghai", "Our second year with S-Tron, speaking on stage."),
            ("2026", "Second MOU with Tianjin", "Extending the partnership with a committed programme to bring Tianjin companies to the UK. [Date to be confirmed]")]
asia_page += sec(eyebrow("Where we have been") + h2("Delegations, conferences and agreements that built the corridor.", "clamp(32px, 3.8vw, 52px)", "48px") +
                 '<ol style="list-style: none; margin: 0; padding: 0; border-top: 2px solid #FFFFFF">' + "".join(
                     '<li style="display: flex; flex-wrap: wrap; gap: 8px 40px; padding: 26px 0; border-bottom: 1px solid #333333"><span class="h" style="flex: 0 0 160px; font-size: 22px; color: #DFFF13">' + y + '</span><span class="h" style="flex: 1 1 280px; min-width: 0; font-size: 24px; line-height: 1.05">' + t + '</span><span style="flex: 2 1 360px; min-width: 0; color: #BDBDBD">' + d + '</span></li>'
                     for y, t, d in timeline) + '</ol>', "timeline")
asia_page += sec(eyebrow("Founders building across the corridor", True) + h2("Results across the corridor.", mb="48px") + grid([
    case_card("AI compute infrastructure", "Auto Impartial", "New silicon for the age of private AI", "Core architecture independently validated; a UK and Asia research consortium in formation with Innovate UK.",
              "NEXUS has been helping us build international partnerships and advance our technology towards real-world deployment.", "Dr Xiusun Huang, Founder"),
    case_card("CreaTech", "Eco2Life (EcoDo)", "Global brands, local stories, powered by AI", "From consultancy to a live AI platform with early revenue, with a market route from Britain into Shanghai and Singapore.",
              "NEXUS helped me build Eco2Life with real structure, confidence and connection to the UK innovation ecosystem.", "Qingwen (Joy) Li, Founder"),
    case_card("Legal tech", "Smart Patent", "World-class IP strategy, made accessible by AI", "A live platform, a finalist in a national AI venture programme in China, and preparing a UK and China fundraise.",
              "NEXUS gave me a supportive community, practical guidance and the perspective to develop Smart Patent.", "Jack Zhu, Founder")]), "results", "#D1D1D1", True)
asia_page += enquiry("delegations", "Join a NEXUS delegation to Asia",
                     "Meet buyers, partners and investors in China and Hong Kong, with our team and our partners arranging the programme. We build relationships that last beyond the trip, including short working stays and ongoing knowledge exchange with companies in the region. [Destinations, dates, sectors and price range for 2027 to be confirmed]",
                     ["Register interest now; there is no commitment", "We share the programme and costs when confirmed", "Places are limited for each trip"],
                     [fld("dn", "Your name", auto="name"), fld("dc", "Company", auto="organization"),
                      fld("ds", "Sector", opts=["AI and robotics", "Consumer tech", "Climate", "Deep tech", "Life sciences", "Advanced manufacturing", "Creative and immersive", "Other"]),
                      fld("dd", "Destination", opts=["Mainland China", "Hong Kong", "Both", "Not sure yet"]),
                      fld("dw", "What do you want from the trip?", opts=["Customers and distributors", "Manufacturing or supply partners", "Investment", "Research partnerships"]),
                      fld("de", "Work email", "email", "email")], "Register interest")

pages = {
    H: ("NEXUS | UK–China Tech Market Entry & Scale-Up Partner", "", home, 10150),
    INST: ("NEXUS | UK representation for science parks and innovation zones", INST, inst_page, 6100),
    INTL: ("NEXUS | UK market entry for technology companies", INTL, intl_page, 6430),
    SCALE: ("NEXUS | Growth support for UK scale-ups", SCALE, scale_page, 6300),
    ASIA: ("NEXUS | Our Asia corridor, led by China", ASIA, asia_page, 5360),
}
for name, (t, cur, body, hgt) in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(page(t, cur, body, hgt))
    print("wrote", name)
