import os
import urllib.parse
import json

prefix = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/'
def proxy(file, w):
    src = prefix + file
    encoded = urllib.parse.quote(src, safe='')
    return f'https://images.higgs.ai/?default=1&output=webp&url={encoded}&w={w}&q=85'

gridA = proxy('hf_20261118_061436_77e1a13d-60a0-4746-bf7b-53b2365609f5.png', 900)
gridB = proxy('hf_20261118_061435_8a1828bc-a149-44ea-80fd-c4c33eef7407.png', 900)
gridC = proxy('hf_20261118_061433_df51e37b-d8b8-40b1-9830-01ea6c20c83d.png', 900)
gridC_chip = proxy('hf_20261118_061433_df51e37b-d8b8-40b1-9830-01ea6c20c83d.png', 300)
sky_plate = proxy('hf_20261118_061434_a222c9d2-715b-44b7-873f-0548d1624211.png', 2400)
sky_video = prefix + 'hf_20261118_065029_a6ae2ebb-cd79-41fd-ae60-6b66fdda04ee.mp4'
camera_img = proxy('hf_20261118_061547_10365665-40d3-4390-944f-7bcb10dc6d4a.png', 1400)
sticker_plane = proxy('hf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png', 1200)
sticker_sheet = proxy('hf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png', 700)

font_url = 'https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2'

icons_data = {
    'plane': ['........k', '......kkb', '....kkwkb', '..kkwwkb.', 'kkwwwkbb.', '..kkkbb..', '....kb...', '....k....', '.........'],
    'shell': ['...kkk...', '..kbwbk..', '.kbwbwbk.', 'kbwbwbwbk', 'kwbwbwbwk', '.kbwbwbk.', '..kbbbk..', '...kkk...', '.........'],
    'boat':  ['....k....', '....kb...', '....kbb..', '...wkbbb.', '..wwkbbb.', '....k....', 'kkkkkkkkk', '.kpppppk.', '..kkkkk..'],
    'lighthouse': ['...kkk...', '..kbbbk..', '...kwk...', '...kbk...', '...kwk...', '...kbk...', '..kwwwk..', '..kbbbk..', '.kkkkkkk.'],
    'fish':  ['.........', '...kkk..k', '..kbbbkkk', '.kbwbbbbk', 'kbbbbbkkk', '.kbbbbk.k', '..kkkk...', '.........', '.........'],
    'wave':  ['.........', '...kkk...', '..kbbbk..', '.kbwwbbk.', 'kbw..kbbk', 'kb....kbk', 'bbbbbbbbb', 'kkkkkkkkk', '.........'],
    'sun':   ['....p....', '.p..k..p.', '...kpk...', '..kpppk..', 'pkpppppkp', '..kpppk..', '...kpk...', '.p..k..p.', '....p....']
}
colors = {'k': '#1F2430', 'b': '#7DA3BB', 'w': '#FFFFFF', 'p': '#DDAD95'}

pixel_icons_svg = {}
for name, rows in icons_data.items():
    rects = []
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char in colors:
                rects.append(f'<rect x="{x}" y="{y}" width="1.02" height="1.02" fill="{colors[char]}"/>')
    pixel_icons_svg[name] = f'<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">{"".join(rects)}</svg>'

# Cards art specification (12 cards)
card_art = [
    (gridB, '100% 100%'), # 0 B-BR
    (gridA, '100% 0%'),   # 1 A-TR
    (gridA, '0% 100%'),   # 2 A-BL
    (gridA, '100% 100%'), # 3 A-BR
    (gridB, '0% 0%'),     # 4 B-TL
    (gridB, '100% 0%'),   # 5 B-TR
    (gridC, '100% 0%'),   # 6 C-TR
    (gridC, '0% 0%'),     # 7 C-TL
    (gridB, '0% 100%'),   # 8 B-BL
    (gridA, '0% 0%'),     # 9 A-TL
    (gridC, '0% 100%'),   # 10 C-BL
    (gridC, '100% 100%'), # 11 C-BR
]

def mw(word, is_grey=False):
    cls = "manifesto-grey" if is_grey else ""
    chars = "".join(f'<span class="char {cls}" data-char-idx="{i}">{c}</span>' for i, c in enumerate(word))
    return f'<span class="manifesto-word {cls}">{chars}</span>'

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tidewell — Tides in Motion</title>
  <meta name="description" content="Tidewell is a coastal motion and digital product studio. Explore our scroll story from shore to product.">
  <style>
    @font-face {{
      font-family: 'Inter';
      font-style: normal;
      font-weight: 100 900;
      font-display: swap;
      src: url('{font_url}') format('woff2');
    }}

    :root {{
      --bg: #F1ECEA;
      --ink: #1F2430;
      --muted: #938B90;
      --dark: #12141B;
      --sky1: #C0C9D9;
      --sky2: #EFCEBE;
      --peach: #DDAD95;
      --lavender: #B0AEC6;
      --harbour: #7DA3BB;
      --sand: #EBC9AE;
      --rose: #BF9FA5;
      --slate: #4C6165;
      --ice: #BAD9E6;
      --sub-grey: #5B5A62;
      --sky-grey: #8D8893;
      --manifesto-grey: #6E7180;
      --cta-hover: #2E3546;

      --u: 1px;
      --n: 1;
      --hfs: 106px;
      --ic: 65px;
      --pfs: 48px;
      --sfs: 48px;
      --mfs: 72px;
      --camw: 270px;
      --cw: 218;
      --cw-px: 218px;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      width: 100%;
      height: 100%;
      background-color: var(--bg);
      color: var(--ink);
      font-family: 'Inter', system-ui, -apple-system, "Segoe UI", sans-serif;
      font-weight: 500;
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    body {{
      width: 100%;
      min-height: 100%;
      background-color: var(--bg);
      color: var(--ink);
      font-family: 'Inter', system-ui, -apple-system, "Segoe UI", sans-serif;
      font-weight: 500;
      overflow-x: clip;
      position: relative;
    }}

    a {{
      color: inherit;
      text-decoration: none;
    }}

    button {{
      font: inherit;
      border: none;
      background: none;
      cursor: pointer;
    }}

    /* NAV */
    .site-nav {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: calc(86px * var(--n));
      padding: 0 calc(40px * var(--n));
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 50;
      pointer-events: none;
      transition: color 0.4s ease;
    }}
    .site-nav > * {{
      pointer-events: auto;
    }}

    .nav-logo {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: calc(46px * var(--n));
      height: calc(46px * var(--n));
      color: var(--ink);
      transition: color 0.4s ease, opacity 0.3s ease;
      opacity: 0;
    }}
    .nav-logo svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: calc(28px * var(--n));
      font-size: calc(15px * var(--n));
      font-weight: 400;
      letter-spacing: -0.005em;
    }}
    @media (max-width: 819px) {{
      .nav-links {{
        display: none;
      }}
    }}
    .nav-link {{
      color: var(--muted);
      transition: color 0.25s ease, opacity 0.3s ease, transform 0.3s ease;
      opacity: 0;
      transform: translateY(6px);
    }}
    .nav-link:hover, .nav-link.active {{
      color: var(--ink);
    }}

    .nav-cta {{
      display: inline-flex;
      align-items: center;
      gap: calc(8px * var(--n));
      height: calc(42px * var(--n));
      padding: 0 calc(16px * var(--n)) 0 calc(20px * var(--n));
      border-radius: calc(12px * var(--n));
      background-color: var(--ink);
      color: var(--bg);
      font-size: calc(15px * var(--n));
      font-weight: 500;
      clip-path: inset(0 0 0 100% round calc(12px * var(--n)));
      transition: background-color 0.25s ease, color 0.25s ease, transform 0.2s ease;
    }}
    .nav-cta:hover {{
      background-color: var(--cta-hover);
    }}
    .nav-cta svg {{
      width: calc(16px * var(--n));
      height: calc(16px * var(--n));
      stroke: currentColor;
    }}

    /* DARK NAV OVERRIDE */
    body.dark-nav .nav-logo {{
      color: #ffffff;
    }}
    body.dark-nav .nav-link {{
      color: #8C8F9A;
    }}
    body.dark-nav .nav-link:hover, body.dark-nav .nav-link.active {{
      color: #ffffff;
    }}
    body.dark-nav .nav-cta {{
      background-color: #ffffff;
      color: var(--ink);
    }}
    body.dark-nav .nav-cta:hover {{
      background-color: #f0f0f0;
    }}

    /* STORY SECTION */
    #story {{
      position: relative;
      height: 1600vh;
      width: 100%;
    }}

    /* HERO */
    .hero-header {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      z-index: 9;
      pointer-events: none;
    }}
    .headline-wrap {{
      position: absolute;
      top: 41%;
      left: 0;
      width: 100%;
      height: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: var(--hfs);
      font-weight: 560;
      letter-spacing: -0.035em;
      line-height: 1;
      color: var(--ink);
    }}
    .headline-inner {{
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      white-space: nowrap;
      transform: translate3d(0, 0, 0);
      will-change: transform, opacity;
    }}
    .headline-words {{
      display: inline-flex;
      align-items: center;
    }}
    .headline-char {{
      display: inline-block;
      opacity: 0;
      clip-path: inset(0 100% 0 0);
      will-change: opacity, clip-path;
    }}
    .headline-char.space {{
      width: 0.28em;
    }}

    .icon-layer {{
      position: relative;
      display: inline-flex;
      align-items: center;
      gap: calc(var(--ic) * 0.2);
      margin-left: calc(var(--ic) * 0.32);
    }}
    .pixel-icon {{
      width: var(--ic);
      height: var(--ic);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transform: scale(0);
      transform-origin: 50% 50%;
      will-change: transform, opacity, filter;
    }}

    .plane-sprite {{
      position: absolute;
      width: calc(62px * var(--u));
      height: calc(62px * var(--u));
      background-image: url('{sticker_plane}');
      background-size: 336.7003% 492.6108%;
      background-position: 84.4950% 76.9134%;
      background-repeat: no-repeat;
      opacity: 0;
      pointer-events: none;
      z-index: 10;
      transform-origin: 50% 50%;
      will-change: transform, opacity;
    }}

    /* PINNED STAGE */
    .pinned-stage {{
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      height: 100svh;
      overflow: hidden;
      background-color: var(--bg);
      z-index: 1;
    }}

    /* PROCESS BLOCK */
    .process-block {{
      position: absolute;
      top: 20%;
      left: 50%;
      transform: translateX(-50%);
      width: 100%;
      max-width: 900px;
      padding: 0 16px;
      text-align: center;
      z-index: 4;
      pointer-events: none;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease;
    }}
    @media (max-width: 819px) {{
      .process-block {{
        top: 17%;
      }}
    }}
    .process-headline {{
      font-size: var(--pfs);
      font-weight: 500;
      line-height: 1.12;
      letter-spacing: -0.03em;
      color: var(--ink);
    }}
    .process-headline .word {{
      display: inline-block;
      opacity: 0;
      transform: translateY(0.35em);
      filter: blur(6px);
      will-change: transform, opacity, filter;
    }}
    .process-headline .word.bold {{
      color: var(--muted);
      font-weight: 500;
    }}
    .process-chip {{
      display: inline-block;
      width: 1.05em;
      height: 0.92em;
      border-radius: 0.16em;
      vertical-align: -0.12em;
      margin: 0 0.14em;
      box-shadow: 0 0.06em 0.18em rgba(31,36,48,.18);
      background-image: url('{gridC_chip}');
      background-size: 200% 200%;
      background-position: 100% 0%;
      background-repeat: no-repeat;
    }}

    .process-subline {{
      font-size: calc(var(--pfs) * 0.27);
      font-weight: 400;
      color: var(--sub-grey);
      margin-top: calc(var(--pfs) * 0.42);
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }}

    .process-btn-wrap {{
      margin-top: calc(var(--pfs) * 0.38);
      pointer-events: auto;
    }}
    .process-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.3em;
      height: calc(var(--pfs) * 0.64);
      font-size: calc(var(--pfs) * 0.25);
      padding: 0 calc(var(--pfs) * 0.28) 0 calc(var(--pfs) * 0.32);
      border-radius: calc(var(--pfs) * 0.2);
      background-color: var(--ink);
      color: var(--bg);
      font-weight: 500;
      opacity: 0;
      transform: translateY(8px);
      transition: background-color 0.25s ease, opacity 0.5s ease, transform 0.5s ease;
    }}
    .process-btn:hover {{
      background-color: var(--cta-hover);
    }}
    .process-btn svg {{
      width: 1em;
      height: 1em;
      stroke: currentColor;
    }}

    /* CARDS LAYER */
    .cards-layer {{
      position: absolute;
      inset: 0;
      z-index: 2;
      pointer-events: none;
    }}
    .art-card {{
      position: absolute;
      top: 0;
      left: 0;
      width: var(--cw-px);
      height: calc(var(--cw-px) * 1.32);
      border-radius: calc(var(--cw-px) * 0.075);
      margin-top: calc(var(--cw-px) * -0.66);
      margin-left: calc(var(--cw-px) * -0.5);
      transform-origin: 50% 50%;
      background-size: 200% 200%;
      background-repeat: no-repeat;
      box-shadow: 0 calc(var(--cw-px) * 0.03) calc(var(--cw-px) * 0.09) rgba(31,36,48,.16), inset 0 0 0 1px rgba(255,255,255,.35);
      will-change: transform, opacity;
      opacity: 0;
    }}

    /* SKY PANEL */
    .sky-panel {{
      position: absolute;
      inset: 0;
      z-index: 6;
      overflow: hidden;
      clip-path: inset(40% 41.5% 40% 41.5% round 14px);
      will-change: clip-path;
      opacity: 0;
      pointer-events: none;
    }}
    .sky-plate {{
      position: absolute;
      inset: -4%;
      background-image: url('{sky_plate}');
      background-size: cover;
      background-position: center;
      transform: scale(1.18);
      will-change: transform;
    }}
    .sky-video {{
      position: absolute;
      left: -4%;
      top: -4%;
      width: 108%;
      height: 108%;
      object-fit: cover;
      opacity: 0;
      transform: scale(1.18);
      transition: opacity 1.2s ease;
      will-change: transform, opacity;
    }}
    .sky-camera-wrap {{
      position: absolute;
      left: 50%;
      top: 51%;
      transform: translate(-50%, -50%);
      perspective: 900px;
      z-index: 2;
    }}
    .sky-camera {{
      width: var(--camw);
      aspect-ratio: 1.094;
      background-image: url('{camera_img}');
      background-size: 136.7989% 149.7006%;
      background-position: 55.0186% 42.4699%;
      background-repeat: no-repeat;
      filter: drop-shadow(0 calc(var(--camw) * 0.12) calc(var(--camw) * 0.08) rgba(60,52,70,.22));
      transform-origin: 54% 31%;
      will-change: transform;
    }}

    .sky-words {{
      position: absolute;
      font-size: var(--sfs);
      color: var(--ink);
      letter-spacing: -0.03em;
      line-height: 1.1;
      z-index: 3;
      pointer-events: none;
    }}
    .sky-words.top-left {{
      top: calc(104px * var(--n));
      left: calc(40px * var(--n));
    }}
    .sky-words.bottom-right {{
      bottom: calc(46px * var(--n));
      right: calc(40px * var(--n));
      text-align: right;
    }}
    @media (max-width: 819px) {{
      .sky-words.top-left {{
        top: 84px;
        left: 16px;
      }}
      .sky-words.bottom-right {{
        bottom: 28px;
        right: 16px;
      }}
    }}
    .sky-words .word {{
      display: inline-block;
      opacity: 0;
      transform: translateY(0.3em);
      filter: blur(6px);
      will-change: transform, opacity, filter;
    }}
    .sky-words .word.grey {{
      color: var(--sky-grey);
    }}

    /* BLACKOUT */
    .blackout-layer {{
      position: absolute;
      inset: 0;
      background-color: var(--dark);
      opacity: 0;
      z-index: 8;
      pointer-events: none;
      will-change: opacity;
    }}

    /* MANIFESTO SECTION */
    #manifesto {{
      position: relative;
      height: 950vh;
      background-color: var(--dark);
      width: 100%;
    }}
    .manifesto-stage {{
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }}
    .manifesto-track {{
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: calc(var(--mfs) * 0.32);
      white-space: nowrap;
      font-size: var(--mfs);
      letter-spacing: -0.03em;
      color: #ffffff;
      will-change: transform;
    }}

    .manifesto-track .char {{
      display: inline-block;
      opacity: 0;
      transform: translateY(0.55em) rotate(14deg);
      transform-origin: bottom left;
      transition: opacity 0.5s cubic-bezier(0.2, 0, 0.2, 1), transform 0.5s cubic-bezier(0.2, 0, 0.2, 1);
      will-change: transform, opacity;
    }}
    .manifesto-track .char.revealed {{
      opacity: 1;
      transform: translateY(0) rotate(0deg);
    }}

    .manifesto-grey {{
      color: var(--manifesto-grey);
    }}

    .badge-label {{
      display: inline-flex;
      align-items: center;
      padding: 0.28em 0.62em 0.3em;
      border-radius: 0.16em;
      font-size: 0.42em;
      font-weight: 560;
      color: var(--ink);
      line-height: 1;
      vertical-align: middle;
      opacity: 0;
      transform: scale(0) rotate(-14deg);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }}
    .badge-label.revealed {{
      opacity: 1;
      transform: scale(1) rotate(var(--rest-rot, 0deg));
    }}

    .small-badge {{
      position: absolute;
      font-size: calc(var(--mfs) * 0.24);
      padding: 0.3em 0.6em;
      border-radius: 0.16em;
      color: var(--ink);
      font-weight: 560;
      line-height: 1;
      box-shadow: 0 0.12em 0.3em rgba(0,0,0,.35);
      opacity: 0;
      transform: scale(0);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }}
    .small-badge.revealed {{
      opacity: 1;
      transform: scale(1) rotate(var(--rest-rot, 0deg));
    }}

    .trinket-obj {{
      display: inline-block;
      vertical-align: middle;
      opacity: 0;
      transform: scale(0) rotate(-14deg);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }}
    .trinket-obj.revealed {{
      opacity: 1;
      transform: scale(1) rotate(var(--rest-rot, 0deg));
    }}

    .trinket-conch {{
      width: 1.25em;
      height: 1.25em;
      background-image: url('{sticker_sheet}');
      background-size: 311.5265% 332.2259%;
      background-position: 16.0530% 17.3104%;
      background-repeat: no-repeat;
    }}
    .trinket-pearl {{
      width: 0.8em;
      height: 0.8em;
      background-image: url('{sticker_sheet}');
      background-size: 420.1681% 411.5226%;
      background-position: 82.0210% 20.0793%;
      background-repeat: no-repeat;
    }}
    .trinket-capsule {{
      width: 1.05em;
      height: 0.5em;
      background-image: url('{sticker_sheet}');
      background-size: 308.6420% 729.9270%;
      background-position: 13.9053% 76.0139%;
      background-repeat: no-repeat;
    }}

    .sparkle-icon {{
      display: inline-block;
      width: 0.34em;
      height: 0.34em;
      vertical-align: middle;
      opacity: 0;
      transform: scale(0);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .sparkle-icon.revealed {{
      opacity: 1;
      transform: scale(1);
    }}
    .sparkle-icon svg {{
      width: 100%;
      height: 100%;
      fill: #F4E3D3;
    }}

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }}
      #story, #manifesto {{
        height: auto !important;
      }}
      .pinned-stage, .manifesto-stage {{
        position: relative !important;
        height: auto !important;
        min-height: 100vh;
      }}
    }}
  </style>
</head>
<body>

  <!-- FIXED NAV -->
  <header class="site-nav" role="banner">
    <a href="#" class="nav-logo" aria-label="Tidewell home">
      <svg viewBox="0 0 48 48">
        <circle cx="24" cy="12.5" r="8.5" fill="currentColor"/>
        <path d="M6 27c6-5 13-5 18 0s12 5 18 0v6c-6 5-13 5-18 0S12 28 6 33z" fill="currentColor"/>
        <path d="M10 39c5-3.6 10-3.6 14 0s9 3.6 14 0" fill="none" stroke="currentColor" stroke-width="4.2" stroke-linecap="round"/>
      </svg>
    </a>

    <nav class="nav-links" aria-label="Main navigation">
      <a href="#" class="nav-link active">Home</a>
      <a href="#process" class="nav-link">Our Team</a>
      <a href="#process" class="nav-link">Cases</a>
      <a href="#product" class="nav-link">Features</a>
      <a href="#product" class="nav-link">Pricing</a>
      <a href="#manifesto" class="nav-link">Contact</a>
    </nav>

    <button class="nav-cta" type="button" aria-label="View Collections">
      <span>View Collections</span>
      <svg viewBox="0 0 16 16">
        <path d="M3 8h10M9 4l4 4-4 4"/>
      </svg>
    </button>
  </header>

  <!-- STORY SECTION (1600vh) -->
  <section id="story">
    <!-- HERO (100vh) -->
    <header class="hero-header">
      <div class="headline-wrap" role="heading" aria-level="1" aria-label="Tides in Motion">
        <div class="headline-inner" id="headlineInner">
          <div class="headline-words" id="headlineWords">
            <!-- Characters dynamically added/controlled in JS -->
          </div>
          <div class="icon-layer" id="iconLayer">
            <span class="pixel-icon" data-icon="plane">{pixel_icons_svg['plane']}</span>
            <span class="pixel-icon" data-icon="shell">{pixel_icons_svg['shell']}</span>
            <span class="pixel-icon" data-icon="boat">{pixel_icons_svg['boat']}</span>
            <span class="pixel-icon" data-icon="lighthouse">{pixel_icons_svg['lighthouse']}</span>
            <span class="pixel-icon" data-icon="fish">{pixel_icons_svg['fish']}</span>
            <span class="pixel-icon" data-icon="wave">{pixel_icons_svg['wave']}</span>
            <span class="pixel-icon" data-icon="sun">{pixel_icons_svg['sun']}</span>
          </div>
        </div>
      </div>
      <div class="plane-sprite" id="paperPlane"></div>
    </header>

    <!-- PINNED STAGE (100vh) -->
    <div class="pinned-stage" id="pinnedStage">
      <!-- PROCESS BLOCK -->
      <div class="process-block" id="processBlock">
        <h2 class="process-headline" id="processHeadline">
          <span class="line line1">
            <span class="word bold">From</span> <span class="word">shore</span> <span class="process-chip" aria-hidden="true"></span> <span class="word bold">to</span> <span class="word">product</span>
          </span><br>
          <span class="line line2">
            <span class="word">built</span> <span class="word bold">through</span> <span class="word">real</span> <span class="word">process</span>
          </span>
        </h2>
        <p class="process-subline" id="processSubline">Turning concepts into working digital products.</p>
        <div class="process-btn-wrap">
          <button class="process-btn" id="processBtn" type="button">
            <span>View All Collections</span>
            <svg viewBox="0 0 16 16">
              <path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- CARDS LAYER (12 cards) -->
      <div class="cards-layer" id="cardsLayer">
'''

for idx, (img_url, bg_pos) in enumerate(card_art):
    html_content += f'''        <div class="art-card" data-card="{idx}" style="background-image: url('{img_url}'); background-position: {bg_pos};"></div>\n'''

html_content += f'''      </div>

      <!-- SKY PANEL -->
      <div class="sky-panel" id="skyPanel">
        <div class="sky-plate" id="skyPlate"></div>
        <video class="sky-video" id="skyVideo" muted loop playsinline preload="auto">
          <source src="{sky_video}" type="video/mp4">
        </video>
        <div class="sky-camera-wrap" id="skyCamWrap">
          <div class="sky-camera" id="skyCamera"></div>
        </div>
        <div class="sky-words top-left" id="skyWordsTL">
          <span class="word grey">Not</span> <span class="word grey">just</span> <span class="word">visuals</span>
        </div>
        <div class="sky-words bottom-right" id="skyWordsBR">
          <span class="word grey">Real</span> <span class="word">products</span> <span class="word grey">that</span> <span class="word">run</span>
        </div>
      </div>

      <!-- BLACKOUT -->
      <div class="blackout-layer" id="blackout"></div>
    </div>
  </section>

  <!-- MANIFESTO SECTION (950vh) -->
  <section id="manifesto">
    <div class="manifesto-stage">
      <div class="manifesto-track" id="manifestoTrack">

        <!-- 1. Intro block -->
        <div style="position: relative; display: inline-flex; flex-direction: column; gap: 0.26em; font-size: 0.72em; margin-right: 0.6em;">
          <span class="small-badge" style="background-color: var(--sky2); top: -0.95em; left: 0; --rest-rot: -6deg;" data-m-item>motion studio</span>
          <span class="small-badge" style="background-color: var(--sand); top: -1.1em; left: 3.4em; --rest-rot: -4deg;" data-m-item>since the tide turned</span>
          <span class="small-badge" style="background-color: var(--ice); bottom: -1em; left: 0.6em; --rest-rot: 4deg;" data-m-item>coast to coast</span>
          <div>{mw("Designing", True)} {mw("motion")}</div>
          <div>{mw("that")} {mw("moves")} {mw("people.", True)}</div>
        </div>

        <!-- 2. Conch shell 1.25em -->
        <span class="trinket-obj trinket-conch" style="--rest-rot: -12deg;" data-m-item></span>

        <!-- 3. Crafting -->
        {mw("Crafting", True)}

        <!-- 4. Vertical stack -->
        <span style="display: inline-flex; flex-direction: column; gap: 0.2em; vertical-align: middle;">
          <span class="badge-label" style="background-color: var(--peach); position: relative; --rest-rot: -8deg;" data-m-item>
            tidal
            <span style="position: absolute; top: -2px; right: -2px; width: 4px; height: 4px; border-radius: 50%; background-color: var(--ink);"></span>
          </span>
          <span class="badge-label" style="background-color: var(--lavender); font-size: 0.32em; --rest-rot: 6deg;" data-m-item>and immersive</span>
        </span>

        <!-- 5. animation experiences. -->
        {mw("animation", True)}
        {mw("experiences.")}

        <!-- 6. Sparkle & Pearl -->
        <span class="sparkle-icon" data-m-item>
          <svg viewBox="0 0 20 20"><path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z"/></svg>
        </span>
        <span class="trinket-obj trinket-pearl" style="--rest-rot: 0deg;" data-m-item></span>

        <!-- 7. The ocean - is a -->
        {mw("The")}
        {mw("ocean")}
        {mw("–", True)}
        {mw("is", True)}
        {mw("a", True)}

        <!-- 8. Label tidal, conch, pearl, sparkle, coastal -->
        <span class="badge-label" style="background-color: var(--sky2); --rest-rot: -8deg;" data-m-item>tidal</span>
        <span class="trinket-obj trinket-conch" style="width: 1.05em; height: 1.05em; --rest-rot: 10deg;" data-m-item></span>
        <span class="trinket-obj trinket-pearl" style="width: 0.5em; height: 0.5em; --rest-rot: 0deg;" data-m-item></span>
        <span class="sparkle-icon" data-m-item>
          <svg viewBox="0 0 20 20"><path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z"/></svg>
        </span>
        <span class="badge-label" style="background-color: var(--lavender); --rest-rot: 3deg;" data-m-item>coastal</span>

        <!-- 9. and a, label drift, capsule -->
        {mw("and", True)}
        {mw("a", True)}
        <span class="badge-label" style="background-color: var(--ice); --rest-rot: -10deg;" data-m-item>drift</span>
        <span class="trinket-obj trinket-capsule" style="--rest-rot: -8deg;" data-m-item></span>

        <!-- 10. atelier that brings brands, stories, and experiences to life through art, design, and technology. -->
        {mw("atelier")}
        {mw("that")}
        {mw("brings")}
        {mw("brands,")}
        {mw("stories,")}
        {mw("and", True)}
        {mw("experiences")}
        {mw("to", True)}
        {mw("life", True)}
        {mw("through", True)}
        {mw("art,")}
        {mw("design,")}
        {mw("and", True)}
        {mw("technology.")}

        <!-- Spacer 30vw -->
        <div style="width: 30vw; height: 10px; flex-shrink: 0;"></div>
      </div>
    </div>
  </section>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    (function() {{
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      // Scaling state
      let W = window.innerWidth;
      let H = window.innerHeight;
      let isMobile = (W < 820 && W < H * 1.1);
      let cw = 218;

      function updateScale() {{
        W = window.innerWidth;
        H = window.innerHeight;
        isMobile = (W < 820 && W < H * 1.1);

        const u = Math.min(W / 1440, H / 800);
        const n = isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25);
        const hfs = isMobile ? Math.min(W * 0.12, H * 0.09) : Math.min(W * 0.074, H * 0.135);
        const ic = hfs * 0.62;
        const pfs = isMobile ? Math.min(W * 0.085, 40) : Math.min(W * 0.0335, H * 0.062);
        const sfs = isMobile ? Math.min(W * 0.09, 44) : Math.min(W * 0.042, H * 0.078);
        const mfs = isMobile ? Math.min(W * 0.11, H * 0.075) : Math.min(W * 0.05, H * 0.1);
        const camw = isMobile ? Math.min(W * 0.62, H * 0.34) : Math.min(W * 0.19, H * 0.36);

        cw = isMobile ? Math.min(W * 0.30, H * 0.20) : Math.min(W / 1440, H / 780) * 218;

        const root = document.documentElement;
        root.style.setProperty('--u', u + 'px');
        root.style.setProperty('--n', n);
        root.style.setProperty('--hfs', hfs + 'px');
        root.style.setProperty('--ic', ic + 'px');
        root.style.setProperty('--pfs', pfs + 'px');
        root.style.setProperty('--sfs', sfs + 'px');
        root.style.setProperty('--mfs', mfs + 'px');
        root.style.setProperty('--camw', camw + 'px');
        root.style.setProperty('--cw', cw);
        root.style.setProperty('--cw-px', cw + 'px');
      }}
      updateScale();
      window.addEventListener('resize', updateScale);

      // Elements
      const navLogo = document.querySelector('.nav-logo');
      const navLinks = document.querySelectorAll('.nav-link');
      const navCta = document.querySelector('.nav-cta');
      const paperPlane = document.getElementById('paperPlane');
      const iconLayer = document.getElementById('iconLayer');
      const pixelIcons = document.querySelectorAll('.pixel-icon');
      const headlineWords = document.getElementById('headlineWords');
      const processBlock = document.getElementById('processBlock');
      const processWords = document.querySelectorAll('#processHeadline .word');
      const processSubline = document.getElementById('processSubline');
      const processBtn = document.getElementById('processBtn');
      const cardsLayer = document.getElementById('cardsLayer');
      const cardEls = document.querySelectorAll('.art-card');
      const skyPanel = document.getElementById('skyPanel');
      const skyPlate = document.getElementById('skyPlate');
      const skyVideo = document.getElementById('skyVideo');
      const skyCamera = document.getElementById('skyCamera');
      const skyCamWrap = document.getElementById('skyCamWrap');
      const skyWordsTL = document.querySelectorAll('#skyWordsTL .word');
      const skyWordsBR = document.querySelectorAll('#skyWordsBR .word');
      const blackout = document.getElementById('blackout');
      const storyEl = document.getElementById('story');
      const manifestoEl = document.getElementById('manifesto');
      const manifestoTrack = document.getElementById('manifestoTrack');
      const headlineInner = document.getElementById('headlineInner');

      // Headline letters init
      const targetText = "Tides in Motion";
      const charSpans = [];
      for (let i = 0; i < targetText.length; i++) {{
        const span = document.createElement('span');
        span.className = 'headline-char' + (targetText[i] === ' ' ? ' space' : '');
        span.textContent = targetText[i] === ' ' ? '\\u00A0' : targetText[i];
        headlineWords.appendChild(span);
        charSpans.push(span);
      }}

      // Nav click handling
      document.querySelectorAll('.site-nav a[href^="#"]').forEach(anchor => {{
        anchor.addEventListener('click', e => {{
          e.preventDefault();
          const href = anchor.getAttribute('href');
          const storyHeight = storyEl.offsetHeight - H;
          if (href === '#') {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
          }} else if (href === '#process') {{
            window.scrollTo({{ top: storyEl.offsetTop + storyHeight * 0.20, behavior: 'smooth' }});
          }} else if (href === '#product') {{
            window.scrollTo({{ top: storyEl.offsetTop + storyHeight * 0.74, behavior: 'smooth' }});
          }} else if (href === '#manifesto') {{
            window.scrollTo({{ top: manifestoEl.offsetTop, behavior: 'smooth' }});
          }}
        }});
      }});

      // Card target poses and current poses
      const cardPoses = Array.from({{ length: 12 }}, () => ({{ x: W * 0.5, y: H * 1.5, rot: 8, scale: 1, opacity: 0 }}));
      const cardTargets = Array.from({{ length: 12 }}, () => ({{ x: W * 0.5, y: H * 1.5, rot: 8, scale: 1, opacity: 0 }}));

      function stepR(R) {{
        return 2 * Math.asin((1.05 * cw) / (2 * R));
      }}

      function getFanPose(i) {{
        if (i > 5) return {{ x: W * 0.5, y: H * 1.4, rot: 0, scale: 1, opacity: 0 }};
        if (!isMobile) {{
          const R = 1250 * W / 1440;
          const s = stepR(R);
          const theta = (i - 2.5) * s;
          const cx = W * 0.55;
          const cy = H * 0.86 + R;
          return {{
            x: cx + R * Math.sin(theta) - W * 0.02,
            y: cy - R * Math.cos(theta),
            rot: theta * (180 / Math.PI),
            scale: 1,
            opacity: 1
          }};
        }} else {{
          const R = W * 1.35;
          const s = stepR(R);
          const theta = (i - 2.5) * s;
          const cx = W * 0.5;
          const cy = H * 0.86 + R;
          return {{
            x: cx + R * Math.sin(theta),
            y: cy - R * Math.cos(theta) + cw * 0.2,
            rot: theta * (180 / Math.PI),
            scale: 1,
            opacity: 1
          }};
        }}
      }}

      function getScatterPose(i) {{
        if (i > 5) return {{ x: W * 0.5, y: H * 1.4, rot: 0, scale: 1, opacity: 0 }};
        let p;
        if (!isMobile) {{
          const poses = [
            [0.08, 0.46, -20],
            [0.20, 0.86, -12],
            [0.80, 0.84, 14],
            [0.38, 1.04, -8],
            [0.92, 0.42, 16],
            [0.62, 1.04, 9]
          ];
          p = poses[i];
        }} else {{
          const poses = [
            [0.06, 0.60, -20],
            [0.45, 0.66, 12],
            [0.94, 0.60, 16],
            [0.22, 0.93, -14],
            [0.72, 0.96, 9],
            [0.50, 1.30, 0]
          ];
          p = poses[i];
        }}
        let yFrac = p[1];
        if (H < 500 && yFrac < 0.1) yFrac += 0.08;
        return {{
          x: p[0] * W,
          y: yFrac * H,
          rot: p[2],
          scale: 1,
          opacity: 1
        }};
      }}

      function getPilePose(i) {{
        return {{
          x: W * 0.5 + ((i % 3) - 1) * cw * 0.08,
          y: H * 0.62 + (((i * 7) % 5) - 2) * cw * 0.04,
          rot: (i % 2 === 0 ? 1 : -1) * (4 + i * 1.3),
          scale: 1,
          opacity: 1
        }};
      }}

      function getWheelPose(i, rotVal) {{
        const R = !isMobile ? (900 * W / 1440) : (W * 1.2);
        const s = stepR(R);
        const slot = ((((i + rotVal) % 12) + 12) % 12) - 5.5;
        const angle = slot * s;
        const cx = W * 0.5;
        const cy = !isMobile ? (H * 0.82 + R) : (H * 0.76 + R);
        const deg = angle * (180 / Math.PI);
        const isVis = Math.abs(deg) < 62;
        return {{
          x: cx + R * Math.sin(angle),
          y: cy - R * Math.cos(angle),
          rot: deg,
          scale: 1,
          opacity: isVis ? 1 : 0
        }};
      }}

      function lerpPose(a, b, t) {{
        return {{
          x: a.x + (b.x - a.x) * t,
          y: a.y + (b.y - a.y) * t,
          rot: a.rot + (b.rot - a.rot) * t,
          scale: a.scale + (b.scale - a.scale) * t,
          opacity: a.opacity + (b.opacity - a.opacity) * t
        }};
      }}

      function easeInOutCubic(t) {{
        return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      }}

      function easeGlide(t) {{
        return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
      }}

      // Catmull-Rom spline points for plane
      const planePoints = [
        [0.33, -3, 73],
        [0.45, 4, 71],
        [0.60, 13, 65],
        [0.70, 22, 55],
        [0.80, 31, 44],
        [0.87, 32.5, 47.5],
        [0.93, 26, 48],
        [1.00, 21.5, 45],
        [1.07, 22.5, 51.5],
        [1.15, 27, 52],
        [1.27, 45, 41]
      ];

      function getCatmullRom(tVal) {{
        const pts = planePoints;
        const n = pts.length;
        if (tVal <= pts[0][0]) return {{ x: pts[0][1], y: pts[0][2], angle: 0 }};
        if (tVal >= pts[n - 1][0]) return {{ x: pts[n - 1][1], y: pts[n - 1][2], angle: 0 }};

        let i = 0;
        while (i < n - 1 && pts[i + 1][0] < tVal) i++;
        const p0 = pts[Math.max(0, i - 1)];
        const p1 = pts[i];
        const p2 = pts[Math.min(n - 1, i + 1)];
        const p3 = pts[Math.min(n - 1, i + 2)];

        const u = (tVal - p1[0]) / (p2[0] - p1[0]);
        const u2 = u * u;
        const u3 = u2 * u;

        const x = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * u + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * u2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * u3);
        const y = 0.5 * ((2 * p1[2]) + (-p0[2] + p2[2]) * u + (2 * p0[2] - 5 * p1[2] + 4 * p2[2] - p3[2]) * u2 + (-p0[2] + 3 * p1[2] - 3 * p2[2] + p3[2]) * u3);

        const dx = 0.5 * ((-p0[1] + p2[1]) + 2 * (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * u + 3 * (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * u2);
        const dy = 0.5 * ((-p0[2] + p2[2]) + 2 * (2 * p0[2] - 5 * p1[2] + 4 * p2[2] - p3[2]) * u + 3 * (-p0[2] + 3 * p1[2] - 3 * p2[2] + p3[2]) * u2);
        const angle = Math.atan2(dy * H, dx * W) * (180 / Math.PI) + 18;

        return {{ x, y, angle }};
      }}

      // Timing & animation state
      let startTime = null;
      let lastTime = performance.now();
      const cardOrder = [5, 2, 0, 1, 3, 4];
      const cardRises = [0.53, 0.60, 0.63, 0.70, 0.80, 0.86];

      // Smooth scroll state (desktop fine pointer)
      const hasFinePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
      let sy = window.scrollY || window.pageYOffset || 0;
      let ty = sy;
      let lastWheelTime = 0;

      if (hasFinePointer && !prefersReducedMotion) {{
        window.addEventListener('wheel', e => {{
          e.preventDefault();
          lastWheelTime = performance.now();
          const delta = e.deltaMode === 1 ? e.deltaY * 32 : e.deltaY;
          const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
          ty = Math.max(0, Math.min(ty + delta * 0.75, maxScroll));
          window.scrollTo(0, ty);
        }}, {{ passive: false }});
      }}

      window.addEventListener('scroll', () => {{
        if (!hasFinePointer || prefersReducedMotion || (performance.now() - lastWheelTime > 250)) {{
          ty = window.scrollY || window.pageYOffset || 0;
        }}
      }});

      // Gating & Sky state
      let wheelCompleted = false;
      let cardsSettled = false;
      let skyGateAllowed = false;
      let skyDisplayProgress = 0;
      let processWordsRevealed = false;
      let skyWordsRevealed = false;
      let videoStarted = false;

      function render(now) {{
        if (!startTime) startTime = now;
        const dt = Math.min(34, now - lastTime);
        lastTime = now;
        const t = (now - startTime) / 1000;

        // Smooth scroll interpolation
        if (hasFinePointer && !prefersReducedMotion) {{
          if (performance.now() - lastWheelTime > 250) {{
            ty = window.scrollY || window.pageYOffset || 0;
          }}
          const kScroll = 1 - Math.pow(1 - 0.06, dt / 16.67);
          sy += (ty - sy) * kScroll;
        }} else {{
          sy = window.scrollY || window.pageYOffset || 0;
        }}

        // Story progress
        const storyTop = storyEl.offsetTop;
        const storyHeight = storyEl.offsetHeight - H;
        const p = Math.max(0, Math.min(1, (sy - storyTop) / storyHeight));

        // 1. Hero headline position & exact fade formula
        const navHeight = 86 * (isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25));
        const hfs = isMobile ? Math.min(W * 0.12, H * 0.09) : Math.min(W * 0.074, H * 0.135);
        const currentHeadlineTop = 0.41 * H - sy;
        const fadeStart = navHeight + 1.9 * hfs;
        const fadeEnd = navHeight + 0.55 * hfs;

        if (currentHeadlineTop >= fadeStart) {{
          headlineInner.style.opacity = '1';
        }} else if (currentHeadlineTop <= fadeEnd) {{
          headlineInner.style.opacity = '0';
        }} else {{
          const fadeFrac = (currentHeadlineTop - fadeEnd) / (fadeStart - fadeEnd);
          headlineInner.style.opacity = Math.max(0, Math.min(1, fadeFrac));
        }}

        // Load sequence animations (first 6s)
        if (t < 6.5 && !prefersReducedMotion) {{
          // 0.15 - 0.35: Logo
          if (t >= 0.15 && t <= 0.35) {{
            const pVal = (t - 0.15) / 0.20;
            navLogo.style.opacity = Math.min(1, easeInOutCubic(pVal));
          }} else if (t > 0.35) {{
            navLogo.style.opacity = '1';
          }}

          // 0.20 + i*0.03: Nav links
          navLinks.forEach((link, idx) => {{
            const st = 0.20 + idx * 0.03;
            const ed = 0.42 + idx * 0.03;
            if (t >= st && t <= ed) {{
              const pVal = (t - st) / (ed - st);
              link.style.opacity = pVal;
              link.style.transform = `translateY(${{(1 - pVal) * 6}}px)`;
            }} else if (t > ed) {{
              link.style.opacity = '1';
              link.style.transform = 'translateY(0px)';
            }}
          }});

          // 0.23 - 0.42: Nav CTA
          if (t >= 0.23 && t <= 0.42) {{
            const pVal = (t - 0.23) / 0.19;
            const insetLeft = (1 - easeInOutCubic(pVal)) * 100;
            navCta.style.clipPath = `inset(0 0 0 ${{insetLeft}}% round calc(12px * var(--n)))`;
          }} else if (t > 0.42) {{
            navCta.style.clipPath = 'inset(0 0 0 0% round calc(12px * var(--n)))';
          }}

          // Slot 1 position for plane landing
          if (pixelIcons[0]) {{
            const rect = pixelIcons[0].getBoundingClientRect();
            planePoints[planePoints.length - 1][1] = (rect.left + rect.width * 0.5) / W * 100;
            planePoints[planePoints.length - 1][2] = (rect.top + rect.height * 0.5) / H * 100;
          }}

          // 0.33 - 1.27: Paper plane Catmull-Rom
          if (t >= 0.33 && t <= 1.27) {{
            paperPlane.style.opacity = '1';
            const pt = getCatmullRom(t);
            paperPlane.style.left = (pt.x * W / 100) + 'px';
            paperPlane.style.top = (pt.y * H / 100) + 'px';
            paperPlane.style.transform = `translate(-50%, -50%) rotate(${{pt.angle}}deg)`;
          }} else if (t > 1.27 && t <= 1.33) {{
            const pVal = (t - 1.27) / 0.06;
            const pt = getCatmullRom(1.27);
            paperPlane.style.left = (pt.x * W / 100) + 'px';
            paperPlane.style.top = (pt.y * H / 100) + 'px';
            paperPlane.style.opacity = (1 - pVal);
            paperPlane.style.transform = `translate(-50%, -50%) rotate(${{pt.angle}}deg) scale(${{1 - 0.4 * pVal}})`;
          }} else if (t > 1.33) {{
            paperPlane.style.opacity = '0';
          }}

          // 1.27: Plane icon appears
          if (t >= 1.27) {{
            pixelIcons[0].style.opacity = '1';
            pixelIcons[0].style.transform = 'scale(1)';
          }}

          // 1.27 + (0.03 + j*0.07): Icons 2-7 pop in
          for (let j = 1; j < 7; j++) {{
            const st = 1.27 + (0.03 + j * 0.07);
            if (t >= st && t <= st + 0.32) {{
              const pVal = (t - st) / 0.32;
              const s = 1 + 1.15 * Math.pow(pVal - 1, 3) + (pVal - 1) * Math.pow(pVal - 1, 2);
              pixelIcons[j].style.opacity = Math.min(1, pVal / 0.375);
              pixelIcons[j].style.transform = `scale(${{Math.max(0, s)}})`;
            }} else if (t > st + 0.32) {{
              pixelIcons[j].style.opacity = '1';
              pixelIcons[j].style.transform = 'scale(1)';
            }}
          }}

          // 0.53 - 1.56: Hero cards rise
          cardOrder.forEach((cIdx, orderIdx) => {{
            const st = cardRises[orderIdx];
            const endFan = getFanPose(cIdx);
            if (t < st) {{
              cardTargets[cIdx] = {{ x: endFan.x, y: H + cw * 1.2, rot: 8, scale: 1, opacity: 0 }};
              cardPoses[cIdx] = {{ ...cardTargets[cIdx] }};
            }} else if (t >= st && t <= st + 0.70) {{
              const pVal = (t - st) / 0.70;
              const overshoot = (x) => 1 + 2.15 * Math.pow(x - 1, 3) + 1.15 * Math.pow(x - 1, 2);
              const op = Math.min(1, pVal * 2);
              const py = H + cw * 1.2 + (endFan.y - (H + cw * 1.2)) * overshoot(pVal);
              const pr = 8 + (endFan.rot - 8) * overshoot(pVal);
              cardTargets[cIdx] = {{ x: endFan.x, y: py, rot: pr, scale: 1, opacity: op }};
              cardPoses[cIdx] = {{ ...cardTargets[cIdx] }};
            }}
          }});

          // 1.9 -> ~5.2: Icon-to-letter morph
          if (t >= 1.9) {{
            const morphT = t - 1.9;
            const stepDur = 0.22;
            const stepIdx = Math.floor(morphT / stepDur);

            for (let i = 0; i < targetText.length; i++) {{
              if (i < stepIdx) {{
                charSpans[i].style.opacity = '1';
                charSpans[i].style.clipPath = 'inset(0 0% 0 0)';
              }} else if (i === stepIdx && stepIdx < targetText.length) {{
                const stepFrac = (morphT % stepDur) / stepDur;
                if (stepFrac >= 0.32) {{
                  const wipe = Math.min(1, (stepFrac - 0.32) / 0.58);
                  charSpans[i].style.opacity = '1';
                  charSpans[i].style.clipPath = `inset(0 ${{ (1 - wipe) * 100 }}% 0 0)`;
                }} else {{
                  charSpans[i].style.opacity = '0';
                  charSpans[i].style.clipPath = 'inset(0 100% 0 0)';
                }}
              }} else {{
                charSpans[i].style.opacity = '0';
                charSpans[i].style.clipPath = 'inset(0 100% 0 0)';
              }}
            }}

            const lettersLeft = Math.max(0, targetText.length - stepIdx);
            const iconsRemaining = Math.min(7, Math.ceil(7 * lettersLeft / 13));

            for (let k = 0; k < 7; k++) {{
              if (k < 7 - iconsRemaining) {{
                pixelIcons[k].style.display = 'none';
              }} else if (k === 7 - iconsRemaining && stepIdx < targetText.length) {{
                pixelIcons[k].style.display = 'inline-flex';
                const stepFrac = (morphT % stepDur) / stepDur;
                if (stepFrac <= 0.45) {{
                  const u = stepFrac / 0.45;
                  const syVal = 1 - (1 - 0.16) * u;
                  const sxVal = 1 + 0.25 * u;
                  const r = -28 * u;
                  pixelIcons[k].style.transform = `scale(${{sxVal}}, ${{syVal}}) rotate(${{r}}deg)`;
                  pixelIcons[k].style.filter = `brightness(${{1 - u}})`;
                  pixelIcons[k].style.opacity = '1';
                }} else {{
                  const u = (stepFrac - 0.45) / 0.55;
                  const r = -28 - 62 * u;
                  pixelIcons[k].style.transform = `scale(1.25, 0.16) rotate(${{r}}deg)`;
                  pixelIcons[k].style.opacity = `${{1 - u}}`;
                }}
              }} else {{
                pixelIcons[k].style.display = 'inline-flex';
                pixelIcons[k].style.opacity = '1';
                pixelIcons[k].style.transform = 'scale(1) rotate(0deg)';
                pixelIcons[k].style.filter = 'none';
              }}
            }}
          }}
        }} else if (prefersReducedMotion) {{
          navLogo.style.opacity = '1';
          navLinks.forEach(l => {{ l.style.opacity = '1'; l.style.transform = 'none'; }});
          navCta.style.clipPath = 'none';
          charSpans.forEach(c => {{ c.style.opacity = '1'; c.style.clipPath = 'none'; }});
          iconLayer.style.display = 'none';
          paperPlane.style.display = 'none';
        }}

        // 2. Cards choreography driven by scroll progress p
        let wheelProg = 0;
        if (p < 0.004) {{
          for (let i = 0; i < 12; i++) cardTargets[i] = getFanPose(i);
        }} else if (p >= 0.004 && p < 0.085) {{
          const tVal = easeInOutCubic((p - 0.004) / 0.081);
          for (let i = 0; i < 12; i++) cardTargets[i] = lerpPose(getFanPose(i), getScatterPose(i), tVal);
        }} else if (p >= 0.085 && p < 0.21) {{
          for (let i = 0; i < 12; i++) cardTargets[i] = getScatterPose(i);
        }} else if (p >= 0.21 && p < 0.31) {{
          const tVal = easeInOutCubic((p - 0.21) / 0.10);
          for (let i = 0; i < 12; i++) cardTargets[i] = lerpPose(getScatterPose(i), getPilePose(i), tVal);
        }} else if (p >= 0.31 && p < 0.41) {{
          const tVal = easeGlide((p - 0.31) / 0.10);
          for (let i = 0; i < 12; i++) cardTargets[i] = lerpPose(getPilePose(i), getWheelPose(i, 0), tVal);
        }} else if (p >= 0.41 && p < 0.57) {{
          wheelProg = (p - 0.41) / 0.16;
          const rotVal = -3 * easeInOutCubic(wheelProg);
          for (let i = 0; i < 12; i++) cardTargets[i] = getWheelPose(i, rotVal);
        }} else if (p >= 0.57 && p < 0.62) {{
          wheelCompleted = true;
          for (let i = 0; i < 12; i++) cardTargets[i] = getWheelPose(i, -3);
        }} else {{
          wheelCompleted = true;
          for (let i = 0; i < 12; i++) cardTargets[i] = getWheelPose(i, -3);
        }}

        // Card inertia & settlement check
        cardsSettled = true;
        for (let i = 0; i < 12; i++) {{
          const tgt = cardTargets[i];
          const cur = cardPoses[i];
          const w = 0.055 + (i % 4) * 0.008;
          const k = (prefersReducedMotion || (t < 1.6 && sy < 10)) ? 1 : (1 - Math.pow(1 - w, dt / 16.67));

          cur.x += (tgt.x - cur.x) * k;
          cur.y += (tgt.y - cur.y) * k;
          cur.rot += (tgt.rot - cur.rot) * k;
          cur.scale += (tgt.scale - cur.scale) * k;
          cur.opacity += (tgt.opacity - cur.opacity) * k;

          if (Math.abs(tgt.x - cur.x) > 3 || Math.abs(tgt.rot - cur.rot) > 1) {{
            cardsSettled = false;
          }}

          const el = cardEls[i];
          if (el) {{
            el.style.transform = `translate3d(${{cur.x}}px, ${{cur.y}}px, 0) rotate(${{cur.rot}}deg) scale(${{cur.scale}})`;
            el.style.opacity = cur.opacity;
            el.style.display = cur.opacity < 0.01 ? 'none' : 'block';
          }}
        }}

        // 3. Process block reveal
        if (p >= 0.05 && p <= 0.075) {{
          processBlock.style.visibility = 'visible';
          processBlock.style.opacity = (p - 0.05) / 0.025;
        }} else if (p > 0.075) {{
          processBlock.style.visibility = 'visible';
          processBlock.style.opacity = '1';
          if (!processWordsRevealed) {{
            processWordsRevealed = true;
            processWords.forEach((w, idx) => {{
              setTimeout(() => {{
                w.style.transition = 'opacity 0.55s cubic-bezier(0.2,0,0.2,1), transform 0.55s cubic-bezier(0.2,0,0.2,1), filter 0.55s cubic-bezier(0.2,0,0.2,1)';
                w.style.opacity = '1';
                w.style.transform = 'translateY(0)';
                w.style.filter = 'blur(0)';
              }}, idx * 110);
            }});
            setTimeout(() => {{
              processSubline.style.opacity = '1';
              processSubline.style.transform = 'translateY(0)';
            }}, 700);
            setTimeout(() => {{
              processBtn.style.opacity = '1';
              processBtn.style.transform = 'translateY(0)';
            }}, 850);
          }}
        }} else {{
          processBlock.style.visibility = 'hidden';
          processBlock.style.opacity = '0';
          processWordsRevealed = false;
          processWords.forEach(w => {{
            w.style.transition = 'none';
            w.style.opacity = '0';
            w.style.transform = 'translateY(0.35em)';
            w.style.filter = 'blur(6px)';
          }});
          processSubline.style.opacity = '0';
          processSubline.style.transform = 'translateY(8px)';
          processBtn.style.opacity = '0';
          processBtn.style.transform = 'translateY(8px)';
        }}

        // 4. Sky Panel Gating (.62 -> .74)
        if (p >= 0.62 && wheelCompleted && cardsSettled) {{
          skyGateAllowed = true;
        }} else if (p < 0.57) {{
          skyGateAllowed = false;
        }}

        const targetSkyP = (skyGateAllowed && p >= 0.62) ? Math.min(1, (p - 0.62) / 0.12) : 0;
        skyDisplayProgress += (targetSkyP - skyDisplayProgress) * (prefersReducedMotion ? 1 : 0.09);

        if (skyDisplayProgress > 0.005) {{
          skyPanel.style.opacity = '1';
          skyPanel.style.pointerEvents = 'auto';

          const topInset = !isMobile ? (28 * (1 - skyDisplayProgress)) : (36 * (1 - skyDisplayProgress));
          const botInset = !isMobile ? (52 * (1 - skyDisplayProgress)) : (48 * (1 - skyDisplayProgress));
          const sideInset = !isMobile ? (41.5 * (1 - skyDisplayProgress)) : (29 * (1 - skyDisplayProgress));
          const rad = 14 * (1 - skyDisplayProgress);
          skyPanel.style.clipPath = `inset(${{topInset}}% ${{sideInset}}% ${{botInset}}% ${{sideInset}}% round ${{rad}}px)`;

          const sScale = 1.18 - 0.18 * skyDisplayProgress;
          skyPlate.style.transform = `scale(${{sScale}})`;
          skyVideo.style.transform = `scale(${{sScale}})`;

          if (!videoStarted) {{
            videoStarted = true;
            skyVideo.playbackRate = 0.6;
            skyVideo.play().then(() => {{
              skyVideo.style.opacity = '0.78';
            }}).catch(() => {{}});
          }}

          let camScale = 0.5 + 0.5 * skyDisplayProgress;
          let camYaw = 0;
          let camBob = 0;

          if (p >= 0.74 && p < 0.88) {{
            const yp = (p - 0.74) / 0.14;
            camYaw = -10 + 20 * yp;
            camBob = Math.sin(now * 0.0016) * (6 * (isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25)));
          }}

          let zoomScale = 1;
          if (p >= 0.88) {{
            const zp = Math.min(1, (p - 0.88) / 0.09);
            const gate = skyDisplayProgress >= 0.90 ? 1 : (skyDisplayProgress / 0.90);
            const q = Math.pow(zp, 1.6) * gate;
            zoomScale = 1 + q * q * 28;

            if (q >= 0.45) {{
              const bq = Math.min(1, (q - 0.45) / 0.40);
              blackout.style.opacity = bq;
            }} else {{
              blackout.style.opacity = '0';
            }}
          }} else {{
            blackout.style.opacity = '0';
          }}

          skyCamWrap.style.transform = `translate(-50%, calc(-50% + ${{camBob}}px)) scale(${{camScale}})`;
          skyCamera.style.transform = `rotateY(${{camYaw}}deg) scale(${{zoomScale}})`;

          if (skyDisplayProgress >= 0.92 && !skyWordsRevealed) {{
            skyWordsRevealed = true;
            skyWordsTL.forEach((w, idx) => {{
              setTimeout(() => {{
                w.style.transition = 'opacity 0.6s cubic-bezier(0.2,0,0.2,1), transform 0.6s cubic-bezier(0.2,0,0.2,1), filter 0.6s cubic-bezier(0.2,0,0.2,1)';
                w.style.opacity = '1';
                w.style.transform = 'translateY(0)';
                w.style.filter = 'blur(0)';
              }}, idx * 120);
            }});
            skyWordsBR.forEach((w, idx) => {{
              setTimeout(() => {{
                w.style.transition = 'opacity 0.6s cubic-bezier(0.2,0,0.2,1), transform 0.6s cubic-bezier(0.2,0,0.2,1), filter 0.6s cubic-bezier(0.2,0,0.2,1)';
                w.style.opacity = '1';
                w.style.transform = 'translateY(0)';
                w.style.filter = 'blur(0)';
              }}, 450 + idx * 120);
            }});
          }}
        }} else {{
          skyPanel.style.opacity = '0';
          skyPanel.style.pointerEvents = 'none';
          skyWordsRevealed = false;
          skyWordsTL.forEach(w => {{ w.style.opacity = '0'; w.style.transform = 'translateY(0.3em)'; w.style.filter = 'blur(6px)'; }});
          skyWordsBR.forEach(w => {{ w.style.opacity = '0'; w.style.transform = 'translateY(0.3em)'; w.style.filter = 'blur(6px)'; }});
        }}

        // Dark nav switch (p > 0.985 or in manifesto)
        if (p > 0.985 || sy >= manifestoEl.offsetTop - 100) {{
          document.body.classList.add('dark-nav');
        }} else {{
          document.body.classList.remove('dark-nav');
        }}

        // 5. Manifesto horizontal scroll
        const manTop = manifestoEl.offsetTop;
        const manHeight = manifestoEl.offsetHeight - H;
        const mp = Math.max(0, Math.min(1, (sy - manTop) / manHeight));

        const trackWidth = manifestoTrack.scrollWidth;
        const startX = isMobile ? W * 0.08 : W * 0.06;
        const endX = -(trackWidth - W * 0.90);
        const curX = startX + (endX - startX) * mp;
        manifestoTrack.style.transform = `translate3d(${{curX}}px, -50%, 0)`;

        if (sy >= manTop - H * 0.2) {{
          const triggerLine = isMobile ? W * 0.92 : W * 0.86;
          document.querySelectorAll('.manifesto-track .char').forEach(charEl => {{
            if (!charEl.classList.contains('revealed')) {{
              const rect = charEl.getBoundingClientRect();
              if (rect.left < triggerLine) {{
                const charIdx = parseInt(charEl.getAttribute('data-char-idx') || '0', 10);
                setTimeout(() => {{
                  charEl.classList.add('revealed');
                }}, charIdx * 35);
              }}
            }}
          }});

          document.querySelectorAll('[data-m-item]').forEach(item => {{
            const rect = item.getBoundingClientRect();
            if (rect.left < triggerLine && !item.classList.contains('revealed')) {{
              setTimeout(() => {{
                item.classList.add('revealed');
              }}, 120);
            }}
          }});
        }}

        requestAnimationFrame(render);
      }}

      requestAnimationFrame(render);

    }})();
  </script>
</body>
</html>
'''

output_path = r'c:\Users\Asus\websites-templates\courstal-cards\index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully! Size: {len(html_content)} bytes")
