import os
import urllib.parse

# Assets
cards_images = [
    'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1518770660439-4636190af475?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=900&q=85&fit=crop',
    'https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?w=900&q=85&fit=crop',
]
chip_img = 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=300&q=85&fit=crop'
sky_plate = 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=2400&q=85&fit=crop'
sky_video = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261118_065029_a6ae2ebb-cd79-41fd-ae60-6b66fdda04ee.mp4'

prefix = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/'
def proxy(file, w):
    src = prefix + file
    encoded = urllib.parse.quote(src, safe='')
    return f'https://images.higgs.ai/?default=1&output=webp&url={encoded}&w={w}&q=85'

camera_img = proxy('hf_20261118_061547_10365665-40d3-4390-944f-7bcb10dc6d4a.png', 1400)
sticker_plane = proxy('hf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png', 1200)
sticker_sheet = proxy('hf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png', 700)

font_url = 'https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2'

# 7 Warm Studio Pixel Icons
pixel_icons_svg = {
    'lens': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="2" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="1" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="4" y="1" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="5" y="1" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="6" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="1" y="2" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="2" y="2" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="3" y="2" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="4" y="2" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="5" y="2" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="6" y="2" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="7" y="2" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="1" y="3" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="2" y="3" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="3" y="3" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="4" y="3" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="5" y="3" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="6" y="3" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="7" y="3" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="1" y="4" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="2" y="4" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="3" y="4" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="4" y="4" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="5" y="4" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="6" y="4" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="7" y="4" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="1" y="5" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="2" y="5" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="3" y="5" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="4" y="5" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="5" y="5" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="6" y="5" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="7" y="5" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="1" y="6" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="2" y="6" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="3" y="6" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="4" y="6" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="5" y="6" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="6" y="6" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="7" y="6" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="2" y="7" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="7" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="4" y="7" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="5" y="7" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="6" y="7" width="1.02" height="1.02" fill="#1D1815" />
    </svg>''',
    'reel': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="1" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="2" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="4" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="5" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="6" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="7" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="1" y="2" width="7" height="1.02" fill="#1D1815" />
      <rect x="1" y="3" width="7" height="5" fill="#DE9350" />
      <rect x="3" y="4" width="3" height="3" fill="#1D1815" />
      <rect x="4" y="5" width="1.02" height="1.02" fill="#FFFFFF" />
    </svg>''',
    'spotlight': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="1" y="1" width="3" height="3" fill="#1D1815" />
      <rect x="2" y="2" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="2" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="3" y="4" width="1.02" height="1.02" fill="#CF6E4A" />
      <rect x="5" y="3" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="5" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="6" y="4" width="2" height="2" fill="#E5B876" />
      <rect x="5" y="6" width="2" height="2" fill="#E5B876" />
      <rect x="7" y="6" width="2" height="2" fill="#FFFFFF" />
    </svg>''',
    'prism': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="4" y="1" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="3" y="2" width="3" height="1.02" fill="#DE9350" />
      <rect x="2" y="3" width="5" height="1.02" fill="#DE9350" />
      <rect x="2" y="4" width="5" height="1.02" fill="#CF6E4A" />
      <rect x="1" y="5" width="7" height="1.02" fill="#CF6E4A" />
      <rect x="1" y="6" width="7" height="1.02" fill="#1D1815" />
      <rect x="0" y="7" width="9" height="1.02" fill="#1D1815" />
      <rect x="4" y="3" width="1.02" height="2" fill="#FFFFFF" />
    </svg>''',
    'viewfinder': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="1" y="1" width="3" height="1.02" fill="#1D1815" />
      <rect x="1" y="1" width="1.02" height="3" fill="#1D1815" />
      <rect x="5" y="1" width="3" height="1.02" fill="#1D1815" />
      <rect x="7" y="1" width="1.02" height="3" fill="#1D1815" />
      <rect x="1" y="5" width="1.02" height="3" fill="#1D1815" />
      <rect x="1" y="7" width="3" height="1.02" fill="#1D1815" />
      <rect x="7" y="5" width="1.02" height="3" fill="#1D1815" />
      <rect x="5" y="7" width="3" height="1.02" fill="#1D1815" />
      <rect x="4" y="3" width="1.02" height="3" fill="#CF6E4A" />
      <rect x="3" y="4" width="3" height="1.02" fill="#CF6E4A" />
      <rect x="4" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
    </svg>''',
    'wave': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="0" y="4" width="1.02" height="1.02" fill="#DE9350" />
      <rect x="1" y="3" width="1.02" height="3" fill="#DE9350" />
      <rect x="2" y="2" width="1.02" height="5" fill="#DE9350" />
      <rect x="3" y="1" width="1.02" height="7" fill="#CF6E4A" />
      <rect x="4" y="0" width="1.02" height="9" fill="#1D1815" />
      <rect x="4" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="1" width="1.02" height="7" fill="#CF6E4A" />
      <rect x="6" y="2" width="1.02" height="5" fill="#DE9350" />
      <rect x="7" y="3" width="1.02" height="3" fill="#DE9350" />
      <rect x="8" y="4" width="1.02" height="1.02" fill="#DE9350" />
    </svg>''',
    'spark': '''<svg viewBox="0 0 9 9" width="100%" height="100%" shape-rendering="crispEdges">
      <rect x="4" y="0" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="1" y="1" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="1" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="7" y="1" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="3" y="2" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="4" y="2" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="2" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="2" y="3" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="3" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="3" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="3" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="6" y="3" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="0" y="4" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="1" y="4" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="2" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="3" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="4" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="6" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="7" y="4" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="8" y="4" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="2" y="5" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="5" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="5" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="5" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="6" y="5" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="3" y="6" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="4" y="6" width="1.02" height="1.02" fill="#FFFFFF" />
      <rect x="5" y="6" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="1" y="7" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="7" width="1.02" height="1.02" fill="#1D1815" />
      <rect x="7" y="7" width="1.02" height="1.02" fill="#E5B876" />
      <rect x="4" y="8" width="1.02" height="1.02" fill="#E5B876" />
    </svg>'''
}

def mw(word, is_grey=False):
    cls = "manifesto-grey" if is_grey else ""
    chars = "".join(f'<span class="char {cls}" data-char-idx="{i}">{c}</span>' for i, c in enumerate(word))
    return f'<span class="manifesto-word {cls}">{chars}</span>'

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>KROMA — Vision in Motion</title>
  <meta name="description" content="KROMA is a global creative and motion studio directing cinema, brand identities, and visual culture.">
  <style>
    @font-face {{
      font-family: 'Inter';
      font-style: normal;
      font-weight: 100 900;
      font-display: swap;
      src: url('{font_url}') format('woff2');
    }}

    :root {{
      --bg: #F8F4EE;
      --ink: #1D1815;
      --muted: #94887E;
      --dark: #14100D;
      --sky1: #F0E6D8;
      --sky2: #E8D3C0;
      --peach: #DE9350;
      --lavender: #C28E6E;
      --harbour: #CF6E4A;
      --sand: #DFC2A5;
      --rose: #B8785E;
      --slate: #5E5047;
      --ice: #E8D8C8;
      --sub-grey: #6B5E55;
      --sky-grey: #A39488;
      --manifesto-grey: #85776E;
      --cta-hover: #362B24;
      --amber: #DE9350;
      --terracotta: #CF6E4A;
      --honey: #E5B876;

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
      background: linear-gradient(to bottom, rgba(248, 244, 238, 0.94) 0%, rgba(248, 244, 238, 0.72) 70%, transparent 100%);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      transition: color 0.4s ease, background 0.4s ease;
    }}
    .site-nav > * {{
      pointer-events: auto;
    }}

    .nav-logo {{
      display: flex;
      align-items: center;
      gap: calc(10px * var(--n));
      color: var(--ink);
      transition: color 0.4s ease, opacity 0.3s ease;
      opacity: 0;
      font-size: calc(19px * var(--n));
      font-weight: 600;
      letter-spacing: -0.03em;
    }}
    .nav-logo svg {{
      width: calc(36px * var(--n));
      height: calc(36px * var(--n));
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
      padding: 0 calc(18px * var(--n)) 0 calc(22px * var(--n));
      border-radius: calc(12px * var(--n));
      background-color: var(--ink);
      color: var(--bg);
      font-size: calc(14.5px * var(--n));
      font-weight: 560;
      clip-path: inset(0 0 0 100% round calc(12px * var(--n)));
      transition: background-color 0.25s ease, color 0.25s ease, transform 0.2s ease;
    }}
    .nav-cta:hover {{
      background-color: var(--cta-hover);
    }}
    .nav-cta svg {{
      width: calc(15px * var(--n));
      height: calc(15px * var(--n));
      stroke: currentColor;
    }}

    /* DARK NAV OVERRIDE */
    body.dark-nav .site-nav {{
      background: linear-gradient(to bottom, rgba(20, 16, 13, 0.94) 0%, rgba(20, 16, 13, 0.72) 70%, transparent 100%);
    }}
    body.dark-nav .nav-logo {{
      color: #ffffff;
    }}
    body.dark-nav .nav-link {{
      color: #A3968C;
    }}
    body.dark-nav .nav-link:hover, body.dark-nav .nav-link.active {{
      color: #ffffff;
    }}
    body.dark-nav .nav-cta {{
      background-color: #ffffff;
      color: var(--ink);
    }}
    body.dark-nav .nav-cta:hover {{
      background-color: #F8F4EE;
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
      gap: calc(var(--ic) * 0.22);
      margin-left: calc(var(--ic) * 0.35);
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
      filter: sepia(0.35) saturate(1.3) hue-rotate(-15deg);
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
      box-shadow: 0 0.06em 0.18em rgba(29,24,21,.18);
      background-image: url('{chip_img}');
      background-size: cover;
      background-position: center;
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
      padding: 0 calc(var(--pfs) * 0.32) 0 calc(var(--pfs) * 0.36);
      border-radius: calc(var(--pfs) * 0.2);
      background-color: var(--ink);
      color: var(--bg);
      font-weight: 560;
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
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      box-shadow: 0 calc(var(--cw-px) * 0.04) calc(var(--cw-px) * 0.12) rgba(29,24,21,.18), inset 0 0 0 1px rgba(255,255,255,.3);
      will-change: transform, opacity;
      opacity: 0;
      overflow: hidden;
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
      filter: drop-shadow(0 25px 50px rgba(29, 24, 21, 0.24));
    }}
    .sky-plate {{
      position: absolute;
      inset: -4%;
      background-image: url('{sky_plate}');
      background-size: cover;
      background-position: center;
      transform: scale(1.18);
      filter: brightness(0.96) saturate(1.1);
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
      filter: drop-shadow(0 calc(var(--camw) * 0.12) calc(var(--camw) * 0.1) rgba(45,35,30,.28)) sepia(0.2) saturate(1.15);
      transform-origin: 54% 31%;
      will-change: transform;
    }}

    .sky-words {{
      position: absolute;
      font-size: var(--sfs);
      color: var(--ink);
      letter-spacing: -0.03em;
      line-height: 1.1;
      font-weight: 560;
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
      color: #F8F4EE;
      will-change: transform;
    }}

    .manifesto-word {{
      display: inline-block;
      white-space: nowrap;
    }}

    .manifesto-track .char {{
      display: inline-block;
      opacity: 0;
      transform: translateY(0.55em) rotate(14deg);
      transform-origin: bottom left;
      transition: opacity 0.5s cubic-bezier(0.2, 0, 0.2, 1), transform 0.5s cubic-bezier(0.2, 0, 0.2, 1);
      will-change: transform, opacity;
      color: #F8F4EE;
    }}
    .manifesto-track .char.revealed {{
      opacity: 1;
      transform: translateY(0) rotate(0deg);
    }}

    .manifesto-grey {{
      color: var(--manifesto-grey) !important;
    }}

    .badge-label {{
      display: inline-flex;
      align-items: center;
      font-size: 0.42em;
      padding: 0.28em 0.62em 0.3em;
      border-radius: 0.16em;
      color: var(--ink);
      font-weight: 560;
      opacity: 0;
      transform: scale(0) rotate(-14deg);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      white-space: nowrap;
      vertical-align: middle;
      will-change: transform, opacity;
    }}
    .badge-label.revealed {{
      opacity: 1;
      transform: scale(1) rotate(var(--rest-rot, 0deg));
    }}

    .small-badge {{
      position: absolute;
      font-size: 0.35em;
      padding: 0.24em 0.55em;
      border-radius: 0.16em;
      color: var(--ink);
      font-weight: 560;
      opacity: 0;
      transform: scale(0) rotate(-14deg);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      white-space: nowrap;
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
    <a href="#" class="nav-logo" id="navLogo" aria-label="KROMA Atelier">
      <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="18" cy="18" r="16" stroke="currentColor" stroke-width="2" />
        <circle cx="18" cy="18" r="7" fill="currentColor" />
        <path d="M18 2V8M18 28V34M2 18H8M28 18H34" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
      </svg>
      <span>KROMA</span>
    </a>

    <nav class="nav-links" aria-label="Main navigation">
      <a href="#" class="nav-link active">Atelier</a>
      <a href="#process" class="nav-link">Works</a>
      <a href="#process" class="nav-link">Services</a>
      <a href="#product" class="nav-link">Showreel</a>
      <a href="#manifesto" class="nav-link">Manifesto</a>
    </nav>

    <button class="nav-cta" id="navCta" type="button" aria-label="Book Studio">
      <span>Book Studio</span>
      <svg viewBox="0 0 16 16">
        <path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </header>

  <!-- STORY SECTION (1600vh) -->
  <section id="story">
    <!-- HERO (100vh) -->
    <header class="hero-header">
      <div class="headline-wrap" role="heading" aria-level="1" aria-label="Vision in Motion">
        <div class="headline-inner" id="headlineInner">
          <div class="headline-words" id="headlineWords">
            <!-- Characters dynamically added/controlled in JS -->
          </div>
          <div class="icon-layer" id="iconLayer">
            <span class="pixel-icon" data-icon="lens">{pixel_icons_svg['lens']}</span>
            <span class="pixel-icon" data-icon="reel">{pixel_icons_svg['reel']}</span>
            <span class="pixel-icon" data-icon="spotlight">{pixel_icons_svg['spotlight']}</span>
            <span class="pixel-icon" data-icon="prism">{pixel_icons_svg['prism']}</span>
            <span class="pixel-icon" data-icon="viewfinder">{pixel_icons_svg['viewfinder']}</span>
            <span class="pixel-icon" data-icon="wave">{pixel_icons_svg['wave']}</span>
            <span class="pixel-icon" data-icon="spark">{pixel_icons_svg['spark']}</span>
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
            <span class="word bold">From</span> <span class="word">concept</span> <span class="process-chip" aria-hidden="true"></span> <span class="word bold">to</span> <span class="word">screen,</span>
          </span><br>
          <span class="line line2">
            <span class="word">crafted</span> <span class="word bold">through</span> <span class="word">pure</span> <span class="word">direction.</span>
          </span>
        </h2>
        <p class="process-subline" id="processSubline">Partnering with visionary brands to direct iconic films, identities, and visual culture.</p>
        <div class="process-btn-wrap">
          <button class="process-btn" id="processBtn" type="button">
            <span>Explore Portfolio</span>
            <svg viewBox="0 0 16 16">
              <path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- CARDS LAYER (12 cards) -->
      <div class="cards-layer" id="cardsLayer">
'''

for idx, img_url in enumerate(cards_images):
    html_content += f'''        <div class="art-card" data-card="{idx}" style="background-image: url('{img_url}');"></div>\n'''

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
          <span class="word grey">Not</span> <span class="word grey">just</span> <span class="word">frames</span>
        </div>
        <div class="sky-words bottom-right" id="skyWordsBR">
          <span class="word grey">Real</span> <span class="word">stories</span> <span class="word grey">that</span> <span class="word">move</span>
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
          <span class="small-badge" style="background-color: var(--peach); top: -0.95em; left: 0; --rest-rot: -6deg;" data-m-item>creative studio</span>
          <span class="small-badge" style="background-color: var(--sand); top: -1.1em; left: 3.4em; --rest-rot: -4deg;" data-m-item>est. twenty twenty-four</span>
          <span class="small-badge" style="background-color: var(--ice); bottom: -1em; left: 0.6em; --rest-rot: 4deg;" data-m-item>global atelier</span>
          <div>{mw("Directing", True)} {mw("cinema")}</div>
          <div>{mw("that")} {mw("shapes")} {mw("culture.", True)}</div>
        </div>

        <!-- 2. Conch -->
        <span class="trinket-obj trinket-conch" style="--rest-rot: -12deg;" data-m-item></span>

        <!-- 3. Crafting -->
        {mw("Crafting", True)}

        <!-- 4. Vertical badge stack -->
        <div style="display: inline-flex; flex-direction: column; gap: 0.3em; vertical-align: middle; margin: 0 0.2em;">
          <div style="display: inline-flex; align-items: center; gap: 0.35em;">
            <span class="badge-label" style="background-color: var(--peach); --rest-rot: -8deg;" data-m-item>visual</span>
            <span style="display: inline-block; width: 0.22em; height: 0.22em; border-radius: 50%; background: #4D5366; vertical-align: middle;"></span>
          </div>
          <span class="badge-label" style="background-color: var(--lavender); font-size: 0.32em; --rest-rot: 6deg;" data-m-item>and immersive</span>
        </div>

        <!-- 5. cinematic worlds. -->
        {mw("cinematic", True)}
        {mw("worlds.")}

        <!-- 6. Sparkle & Pearl -->
        <span class="sparkle-icon" data-m-item><svg viewBox="0 0 20 20"><path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z"/></svg></span>
        <span class="trinket-obj trinket-pearl" style="--rest-rot: 0deg;" data-m-item></span>

        <!-- 7. The studio — is a -->
        {mw("The")} {mw("studio")} {mw("—", True)} {mw("is", True)} {mw("a", True)}

        <!-- 8. Badge creative, Conch, Pearl, Sparkle, Badge collective -->
        <span class="badge-label" style="background-color: var(--peach); --rest-rot: -8deg;" data-m-item>creative</span>
        <span class="trinket-obj trinket-conch" style="width: 1.05em; height: 1.05em; --rest-rot: 10deg;" data-m-item></span>
        <span class="trinket-obj trinket-pearl" style="width: 0.5em; height: 0.5em; --rest-rot: 0deg;" data-m-item></span>
        <span class="sparkle-icon" data-m-item><svg viewBox="0 0 20 20"><path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z"/></svg></span>
        <span class="badge-label" style="background-color: var(--lavender); --rest-rot: 3deg;" data-m-item>collective</span>

        <!-- 9. and a, visionary, capsule -->
        {mw("and", True)} {mw("a", True)}
        <span class="badge-label" style="background-color: var(--sand); --rest-rot: -10deg;" data-m-item>visionary</span>
        <span class="trinket-obj trinket-capsule" style="--rest-rot: -8deg;" data-m-item></span>

        <!-- 10. space that brings brands, artists, and stories to life through film, design, and technology. -->
        {mw("space")} {mw("that")} {mw("brings")} {mw("brands,")} {mw("artists,")} {mw("and", True)}
        {mw("stories")} {mw("to", True)} {mw("life", True)} {mw("through", True)}
        {mw("film,")} {mw("design,")} {mw("and", True)} {mw("technology.")}

        <!-- 11. Spacer -->
        <span style="display: inline-block; width: 30vw; flex-shrink: 0;"></span>
      </div>
    </div>
  </section>

  <!-- SCRIPTS -->
  <script>
    (function() {{
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      // Plane Catmull-Rom spline trajectory
      const PLANE_POINTS = [
        {{ x: -0.15, y: 1.08, z: 0.35, pitch: -36, yaw: 12, roll: 28 }},
        {{ x: 0.12,  y: 0.72, z: 0.65, pitch: -24, yaw: 18, roll: 22 }},
        {{ x: 0.38,  y: 0.44, z: 0.95, pitch: -12, yaw: 24, roll: 14 }},
        {{ x: 0.58,  y: 0.32, z: 1.15, pitch: -2,  yaw: 28, roll: 6 }},
        {{ x: 0.76,  y: 0.28, z: 1.25, pitch: 6,   yaw: 32, roll: -4 }},
        {{ x: 0.92,  y: 0.31, z: 1.10, pitch: 14,  yaw: 34, roll: -12 }},
        {{ x: 1.12,  y: 0.42, z: 0.70, pitch: 22,  yaw: 32, roll: -18 }}
      ];

      function catmullRom(p0, p1, p2, p3, t) {{
        const t2 = t * t;
        const t3 = t2 * t;
        return 0.5 * (
          (2 * p1) +
          (-p0 + p2) * t +
          (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 +
          (-p0 + 3 * p1 - 3 * p2 + p3) * t3
        );
      }}

      function getSplinePoint(points, u) {{
        const n = points.length - 1;
        const p = Math.max(0, Math.min(1, u)) * (n - 2) + 1;
        const i0 = Math.floor(p);
        const t = p - i0;
        const p0 = points[Math.max(0, i0 - 1)];
        const p1 = points[i0];
        const p2 = points[Math.min(n, i0 + 1)];
        const p3 = points[Math.min(n, i0 + 2)];

        return {{
          x: catmullRom(p0.x, p1.x, p2.x, p3.x, t),
          y: catmullRom(p0.y, p1.y, p2.y, p3.y, t),
          z: catmullRom(p0.z, p1.z, p2.z, p3.z, t),
          pitch: catmullRom(p0.pitch, p1.pitch, p2.pitch, p3.pitch, t),
          yaw: catmullRom(p0.yaw, p1.yaw, p2.yaw, p3.yaw, t),
          roll: catmullRom(p0.roll, p1.roll, p2.roll, p3.roll, t)
        }};
      }}

      // Card initial entrance timings & stacking
      const CARD_RISES = [
        {{ idx: 0,  start: 0.55 }},
        {{ idx: 1,  start: 0.60 }},
        {{ idx: 2,  start: 0.66 }},
        {{ idx: 3,  start: 0.72 }},
        {{ idx: 4,  start: 0.79 }},
        {{ idx: 5,  start: 0.86 }},
        {{ idx: 6,  start: 0.94 }},
        {{ idx: 7,  start: 1.02 }},
        {{ idx: 8,  start: 1.11 }},
        {{ idx: 9,  start: 1.20 }},
        {{ idx: 10, start: 1.30 }},
        {{ idx: 11, start: 1.41 }}
      ];

      const CARD_ORDER = [10, 8, 9, 7, 6, 11, 4, 5, 2, 3, 0, 1];

      function easeInOutCubic(x) {{
        return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
      }}
      function easeGlide(x) {{
        return Math.pow(x, 1.25);
      }}
      function stepR(p, p0, p1) {{
        return Math.max(0, Math.min(1, (p - p0) / (p1 - p0)));
      }}

      // DOM Elements
      let W = window.innerWidth;
      let H = window.innerHeight;
      let isMobile = W < 820 || W < H * 1.1;
      let cw = 218;

      const htmlEl = document.documentElement;
      const bodyEl = document.body;
      const storyEl = document.getElementById('story');
      const manifestoEl = document.getElementById('manifesto');
      const navLogo = document.getElementById('navLogo');
      const navLinks = document.querySelectorAll('.nav-link');
      const navCta = document.getElementById('navCta');
      const headlineInner = document.getElementById('headlineInner');
      const headlineWords = document.getElementById('headlineWords');
      const iconLayer = document.getElementById('iconLayer');
      const paperPlane = document.getElementById('paperPlane');
      const pixelIcons = document.querySelectorAll('.pixel-icon');
      const processBlock = document.getElementById('processBlock');
      const processHeadline = document.getElementById('processHeadline');
      const processSubline = document.getElementById('processSubline');
      const processBtn = document.getElementById('processBtn');
      const cardEls = document.querySelectorAll('.art-card');
      const skyPanel = document.getElementById('skyPanel');
      const skyPlate = document.getElementById('skyPlate');
      const skyVideo = document.getElementById('skyVideo');
      const skyCamWrap = document.getElementById('skyCamWrap');
      const skyCamera = document.getElementById('skyCamera');
      const skyWordsTL = document.getElementById('skyWordsTL');
      const skyWordsBR = document.getElementById('skyWordsBR');
      const blackout = document.getElementById('blackout');
      const manifestoTrack = document.getElementById('manifestoTrack');
      const manifestoItems = document.querySelectorAll('[data-m-item]');

      // Build Hero Headline characters
      const targetText = 'Vision in Motion';
      for (let i = 0; i < targetText.length; i++) {{
        const char = targetText[i];
        const span = document.createElement('span');
        span.className = 'headline-char' + (char === ' ' ? ' space' : '');
        span.textContent = char === ' ' ? '\\u00A0' : char;
        headlineWords.appendChild(span);
      }}
      const charSpans = document.querySelectorAll('.headline-char');
      const processWords = document.querySelectorAll('.process-headline .word');
      const skyWords = document.querySelectorAll('.sky-words .word');

      function updateScale() {{
        W = window.innerWidth;
        H = window.innerHeight;
        isMobile = W < 820 || W < H * 1.1;

        const n = isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25);
        const hfs = isMobile ? Math.min(W * 0.074, H * 0.055, 34) : Math.min(W * 0.074, H * 0.135);
        const ic = isMobile ? Math.min(hfs * 0.58, 20) : hfs * 0.61;
        const pfs = isMobile ? Math.min(W * 0.082, H * 0.052) : Math.min(W * 0.033, 48);
        const sfs = isMobile ? Math.min(W * 0.078, 38) : Math.min(W * 0.033, 48);
        const mfs = isMobile ? Math.min(W * 0.13, 56) : Math.min(W * 0.05, 72);
        const camw = isMobile ? Math.min(W * 0.62, 280) : Math.min(W * 0.28, 400);

        cw = !isMobile ? Math.min(W * 0.151, H * 0.27) : Math.min(W * 0.32, 170);

        htmlEl.style.setProperty('--n', n.toString());
        htmlEl.style.setProperty('--u', (isMobile ? W / 390 : W / 1440) + 'px');
        htmlEl.style.setProperty('--hfs', hfs + 'px');
        htmlEl.style.setProperty('--ic', ic + 'px');
        htmlEl.style.setProperty('--pfs', pfs + 'px');
        htmlEl.style.setProperty('--sfs', sfs + 'px');
        htmlEl.style.setProperty('--mfs', mfs + 'px');
        htmlEl.style.setProperty('--camw', camw + 'px');
        htmlEl.style.setProperty('--cw', cw.toString());
        htmlEl.style.setProperty('--cw-px', cw + 'px');
      }}
      window.addEventListener('resize', updateScale);
      updateScale();

      // Card coordinate math (Bottom Fan & Carousel)
      function getFanPose(idx, isMob, w, h, cardW) {{
        const rIndex = 11 - idx;
        const count = 12;
        const fraction = rIndex / (count - 1);
        const cardH = cardW * 1.32;

        if (!isMob) {{
          const spanW = w * 0.94;
          const startX = (w - spanW) / 2 + cardW * 0.5;
          const endX = w - (w - spanW) / 2 - cardW * 0.5;
          const px = startX + fraction * (endX - startX);
          const archApex = -Math.sin(fraction * Math.PI) * (cardH * 0.32);
          const py = h - cardH * 0.18 + archApex;
          const prot = -14 + fraction * 28;
          return {{ x: px, y: py, rot: prot }};
        }} else {{
          const spanW = w * 1.28;
          const startX = -w * 0.14 + cardW * 0.5;
          const endX = w * 1.14 - cardW * 0.5;
          const px = startX + fraction * (endX - startX);
          const archApex = -Math.sin(fraction * Math.PI) * (cardH * 0.24);
          const py = h - cardH * 0.16 + archApex;
          const prot = -18 + fraction * 36;
          return {{ x: px, y: py, rot: prot }};
        }}
      }}

      function getWheelPose(idx, phiDeg, isMob, w, h, cardW) {{
        const thetaDeg = idx * 30 + phiDeg;
        const thetaRad = thetaDeg * Math.PI / 180;
        const cosT = Math.cos(thetaRad);
        const sinT = Math.sin(thetaRad);

        const cardH = cardW * 1.32;
        const cx = w * 0.5;
        const cy = !isMob ? h * 0.58 + cardH * 0.42 : h * 0.60 + cardH * 0.38;
        const rx = !isMob ? w * 0.44 : w * 0.52;
        const ry = !isMob ? h * 0.24 : h * 0.20;

        const px = cx + rx * sinT;
        const py = cy + ry * cosT;
        const prot = -sinT * 22;
        const depth = (cosT + 1) / 2;
        const pscale = 0.74 + 0.34 * depth;
        const popacity = Math.max(0.08, Math.min(1, 0.18 + 0.82 * depth));
        const pz = Math.round(depth * 100);

        return {{ x: px, y: py, rot: prot, scale: pscale, opacity: popacity, z: pz }};
      }}

      // Animation State Variables
      let startTime = performance.now();
      let lastTime = performance.now();
      let sy = 0;
      let ty = 0;
      let isSmoothScrolling = false;

      // Cards smoothed poses
      const cardPoses = [];
      const cardTargets = [];
      for (let i = 0; i < 12; i++) {{
        cardPoses.push({{ x: W / 2, y: H + cw * 1.5, rot: 0, scale: 1, opacity: 0, z: i + 1 }});
        cardTargets.push({{ ...cardPoses[i] }});
      }}

      let skyDisplayProgress = 0;
      let skyGateAllowed = false;
      let videoStarted = false;
      let processWordsRevealed = false;
      let skyWordsRevealed = false;
      let curYawDeg = 0;
      let curCamScale = 0.75;
      let curZoomScale = 1;
      let curBobY = 0;

      // Smooth wheel interpolation
      window.addEventListener('wheel', (e) => {{
        if (Math.abs(e.deltaY) > 0) {{
          isSmoothScrolling = true;
          ty = Math.max(0, Math.min(document.documentElement.scrollHeight - window.innerHeight, ty + e.deltaY));
        }}
      }}, {{ passive: true }});

      window.addEventListener('scroll', () => {{
        if (!isSmoothScrolling) {{
          ty = window.scrollY || window.pageYOffset || 0;
          sy = ty;
        }}
      }}, {{ passive: true }});

      function render(now) {{
        const dt = Math.min(32, now - lastTime);
        lastTime = now;
        const t = (now - startTime) / 1000;

        // Smooth scroll damping
        if (isSmoothScrolling) {{
          if (Math.abs(ty - sy) < 0.5) {{
            sy = ty;
            isSmoothScrolling = false;
          }}
          const kScroll = 1 - Math.pow(1 - 0.06, dt / 16.67);
          sy += (ty - sy) * kScroll;
        }} else {{
          sy = window.scrollY || window.pageYOffset || 0;
        }}

        const storyTop = storyEl.offsetTop;
        const storyHeight = storyEl.offsetHeight - H;
        const p = Math.max(0, Math.min(1, (sy - storyTop) / storyHeight));

        // 1. Hero headline position & exact fade formula
        const navHeight = 86 * (isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25));
        const hfs = isMobile ? Math.min(W * 0.12, H * 0.09) : Math.min(W * 0.074, H * 0.135);
        const currentHeadlineTop = 0.41 * H - 0.5 * hfs - sy;
        const fadeStart = navHeight + 2.0 * hfs;
        const fadeEnd = navHeight + 0.6 * hfs;

        if (headlineInner) {{
          if (currentHeadlineTop >= fadeStart) {{
            headlineInner.style.opacity = '1';
          }} else if (currentHeadlineTop <= fadeEnd) {{
            headlineInner.style.opacity = '0';
          }} else {{
            const fadeFrac = (currentHeadlineTop - fadeEnd) / (fadeStart - fadeEnd);
            headlineInner.style.opacity = Math.max(0, Math.min(1, fadeFrac));
          }}
        }}

        // Load sequence animations (first 6.5s)
        if (t < 6.5 && !prefersReducedMotion) {{
          // 0.15 - 0.35: Logo
          if (t >= 0.15 && t <= 0.35) {{
            const pVal = (t - 0.15) / 0.20;
            navLogo.style.opacity = Math.min(1, easeInOutCubic(pVal));
          }} else if (t > 0.35) {{
            navLogo.style.opacity = '1';
          }}

          // 0.25 - 0.45: Nav Links
          navLinks.forEach((link, idx) => {{
            const st = 0.25 + idx * 0.03;
            if (t >= st && t <= st + 0.25) {{
              const pVal = (t - st) / 0.25;
              link.style.opacity = Math.min(1, pVal);
              link.style.transform = `translateY(${{6 * (1 - easeInOutCubic(pVal))}}px)`;
            }} else if (t > st + 0.25) {{
              link.style.opacity = '1';
              link.style.transform = 'translateY(0)';
            }}
          }});

          // 0.35 - 0.70: CTA wipe
          if (t >= 0.35 && t <= 0.70) {{
            const pVal = (t - 0.35) / 0.35;
            const wipe = easeInOutCubic(pVal);
            navCta.style.clipPath = `inset(0 0 0 ${{ (1 - wipe) * 100 }}% round calc(12px * var(--n)))`;
          }} else if (t > 0.70) {{
            navCta.style.clipPath = 'inset(0 0 0 0% round calc(12px * var(--n)))';
          }}

          // 0.50 - 1.95: Paper plane flight
          if (t >= 0.50 && t <= 1.95) {{
            paperPlane.style.opacity = '1';
            const u = (t - 0.50) / 1.45;
            const pt = getSplinePoint(PLANE_POINTS, u);
            const px = pt.x * W;
            const py = pt.y * H;
            paperPlane.style.transform = `translate3d(${{px}}px, ${{py}}px, 0) rotateX(${{pt.pitch}}deg) rotateY(${{pt.yaw}}deg) rotateZ(${{pt.roll}}deg) scale(${{pt.z}})`;
          }} else if (t > 1.95) {{
            paperPlane.style.opacity = '0';
          }}

          // 0.85 - 1.90: Pixel icons spring in
          const iconArrivals = [0.85, 1.02, 1.20, 1.38, 1.55, 1.72, 1.90];
          pixelIcons.forEach((icon, idx) => {{
            const st = iconArrivals[idx];
            if (t >= st && t <= st + 0.40) {{
              const pVal = (t - st) / 0.40;
              const overshoot = (x) => 1 + 2.70 * Math.pow(x - 1, 3) + 1.70 * Math.pow(x - 1, 2);
              const s = overshoot(pVal);
              icon.style.opacity = '1';
              icon.style.transform = `scale(${{s}})`;
            }} else if (t > st + 0.40 && t < 1.90) {{
              icon.style.opacity = '1';
              icon.style.transform = 'scale(1)';
            }}
          }});

          // 0.55 - 2.11: Cards rise into fan
          CARD_RISES.forEach(cr => {{
            const cIdx = cr.idx;
            const st = cr.start;
            const endFan = getFanPose(cIdx, isMobile, W, H, cw);

            if (t < st) {{
              cardTargets[cIdx] = {{ x: endFan.x, y: H + cw * 1.5, rot: 8, scale: 1, opacity: 0 }};
              cardPoses[cIdx] = {{ ...cardTargets[cIdx] }};
            }} else if (t >= st && t <= st + 0.70) {{
              const pVal = (t - st) / 0.70;
              const overshoot = (x) => 1 + 2.15 * Math.pow(x - 1, 3) + 1.15 * Math.pow(x - 1, 2);
              const op = Math.min(1, pVal * 2);
              const py = (H + cw * 1.2) + (endFan.y - (H + cw * 1.2)) * overshoot(pVal);
              const pr = 8 + (endFan.rot - 8) * overshoot(pVal);
              cardTargets[cIdx] = {{ x: endFan.x, y: py, rot: pr, scale: 1, opacity: op }};
              cardPoses[cIdx] = {{ ...cardTargets[cIdx] }};
            }}
          }});

          // 1.90 -> ~5.2s: Icon to letter morph
          if (t >= 1.90) {{
            const morphT = t - 1.90;
            const stepDur = 0.22;
            const stepIdx = Math.floor(morphT / stepDur);

            for (let i = 0; i < targetText.length; i++) {{
              if (charSpans[i]) {{
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
            }}

            const lettersLeft = Math.max(0, targetText.length - stepIdx);
            const iconsRemaining = Math.min(7, Math.ceil(7 * lettersLeft / targetText.length));

            for (let k = 0; k < 7; k++) {{
              if (pixelIcons[k]) {{
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
          }}
        }} else {{
          // Reduced motion or settled load
          navLogo.style.opacity = '1';
          navLinks.forEach(l => {{ l.style.opacity = '1'; l.style.transform = 'none'; }});
          navCta.style.clipPath = 'inset(0 0 0 0% round calc(12px * var(--n)))';
          paperPlane.style.opacity = '0';
          pixelIcons.forEach(i => i.style.display = 'none');
          charSpans.forEach(c => {{ c.style.opacity = '1'; c.style.clipPath = 'inset(0 0 0 0)'; }});
        }}

        // 2. Scroll Choreography Stages (p: 0 -> 1)
        if (p > 0 || t >= 2.11 || prefersReducedMotion) {{
          // Process block visibility & word stagger with clean fade-out before Sky Panel
          if (p >= 0.08 && p <= 0.53) {{
            processBlock.style.visibility = 'visible';
            processBlock.style.opacity = '1';

            if (!processWordsRevealed && p >= 0.14) {{
              processWordsRevealed = true;
              const wordOrder = [0, 1, 2, 3, 4, 5, 6, 7];
              wordOrder.forEach((wIdx, orderIdx) => {{
                setTimeout(() => {{
                  if (processWords[wIdx]) {{
                    processWords[wIdx].style.transition = 'opacity 0.6s cubic-bezier(0.2,0,0.2,1), transform 0.6s cubic-bezier(0.2,0,0.2,1), filter 0.6s cubic-bezier(0.2,0,0.2,1)';
                    processWords[wIdx].style.opacity = '1';
                    processWords[wIdx].style.transform = 'translateY(0)';
                    processWords[wIdx].style.filter = 'blur(0px)';
                  }}
                }}, orderIdx * 45);
              }});

              setTimeout(() => {{
                processSubline.style.opacity = '1';
                processSubline.style.transform = 'translateY(0)';
              }}, 360);

              setTimeout(() => {{
                processBtn.style.opacity = '1';
                processBtn.style.transform = 'translateY(0)';
              }}, 440);
            }}
          }} else if (p < 0.08) {{
            processBlock.style.opacity = '0';
            processBlock.style.visibility = 'hidden';
            processWordsRevealed = false;
            processWords.forEach(w => {{
              w.style.opacity = '0';
              w.style.transform = 'translateY(0.35em)';
              w.style.filter = 'blur(6px)';
            }});
            processSubline.style.opacity = '0';
            processSubline.style.transform = 'translateY(8px)';
            processBtn.style.opacity = '0';
            processBtn.style.transform = 'translateY(8px)';
          }} else if (p > 0.53 && p <= 0.59) {{
            const fade = Math.max(0, 1 - (p - 0.53) / 0.06);
            processBlock.style.opacity = fade.toString();
            if (fade <= 0.01) processBlock.style.visibility = 'hidden';
          }} else if (p > 0.59) {{
            processBlock.style.visibility = 'hidden';
            processBlock.style.opacity = '0';
          }}

          // Card Choreography Calculations
          const fan0 = [];
          for (let i = 0; i < 12; i++) {{
            fan0.push(getFanPose(i, isMobile, W, H, cw));
          }}

          for (let i = 0; i < 12; i++) {{
            let target = {{ ...fan0[i], scale: 1, opacity: 1, z: i + 1 }};

            if (p <= 0.06) {{
              target = {{ ...fan0[i], scale: 1, opacity: 1, z: i + 1 }};
            }} else if (p > 0.06 && p <= 0.20) {{
              // Scatter
              const q = (p - 0.06) / 0.14;
              const eq = easeGlide(q);
              const rIndex = 11 - i;
              const scatterX = (rIndex - 5.5) * (W * 0.12);
              const scatterY = Math.sin((rIndex / 11) * Math.PI) * (H * 0.14);
              const scatterRot = (rIndex - 5.5) * 8.5;
              target = {{
                x: fan0[i].x + scatterX * eq,
                y: fan0[i].y + scatterY * eq,
                rot: fan0[i].rot + scatterRot * eq,
                scale: 1,
                opacity: 1,
                z: i + 1
              }};
            }} else if (p > 0.20 && p <= 0.32) {{
              // Pile Up behind bottom-center
              const q = (p - 0.20) / 0.12;
              const eq = easeInOutCubic(q);
              const orderIdx = CARD_ORDER.indexOf(i);
              const pileX = W * 0.5 + (orderIdx - 5.5) * 2.2;
              const pileY = H - cw * 0.35 + orderIdx * 1.5;
              const pileRot = (orderIdx - 5.5) * 1.2;

              const rIndex = 11 - i;
              const scatterX = (rIndex - 5.5) * (W * 0.12);
              const scatterY = Math.sin((rIndex / 11) * Math.PI) * (H * 0.14);
              const scatterRot = (rIndex - 5.5) * 8.5;
              const fromX = fan0[i].x + scatterX;
              const fromY = fan0[i].y + scatterY;
              const fromRot = fan0[i].rot + scatterRot;

              target = {{
                x: fromX + (pileX - fromX) * eq,
                y: fromY + (pileY - fromY) * eq,
                rot: fromRot + (pileRot - fromRot) * eq,
                scale: 1 - 0.08 * eq,
                opacity: 1,
                z: orderIdx + 1
              }};
            }} else if (p > 0.32 && p <= 0.44) {{
              // Wheel Formation
              const q = (p - 0.32) / 0.12;
              const eq = easeInOutCubic(q);
              const orderIdx = CARD_ORDER.indexOf(i);
              const pileX = W * 0.5 + (orderIdx - 5.5) * 2.2;
              const pileY = H - cw * 0.35 + orderIdx * 1.5;
              const pileRot = (orderIdx - 5.5) * 1.2;

              const wheelPose = getWheelPose(i, 0, isMobile, W, H, cw);

              target = {{
                x: pileX + (wheelPose.x - pileX) * eq,
                y: pileY + (wheelPose.y - pileY) * eq,
                rot: pileRot + (wheelPose.rot - pileRot) * eq,
                scale: 0.92 + (wheelPose.scale - 0.92) * eq,
                opacity: 1 + (wheelPose.opacity - 1) * eq,
                z: wheelPose.z
              }};
            }} else if (p > 0.44 && p <= 0.56) {{
              // Wheel Rotation (360 deg)
              const q = (p - 0.44) / 0.12;
              const phi = q * 360;
              const wheelPose = getWheelPose(i, phi, isMobile, W, H, cw);
              target = wheelPose;
            }} else if (p > 0.56 && p <= 0.66) {{
              // Smoothly sink and fade down before Sky Panel
              const q = (p - 0.56) / 0.10;
              const eq = easeInOutCubic(q);
              const wheelPose = getWheelPose(i, 360, isMobile, W, H, cw);
              target = {{
                ...wheelPose,
                y: wheelPose.y + eq * (H * 0.32),
                scale: wheelPose.scale * (1 - 0.12 * eq),
                opacity: Math.max(0, wheelPose.opacity * (1 - eq))
              }};
            }} else if (p > 0.66) {{
              const wheelPose = getWheelPose(i, 360, isMobile, W, H, cw);
              target = {{ ...wheelPose, y: wheelPose.y + H * 0.32, opacity: 0 }};
            }}

            cardTargets[i] = target;
          }}
        }}

        // 3. Smooth Cards towards Targets
        const kCard = 1 - Math.pow(1 - 0.08, dt / 16.67);
        let maxCardDist = 0;
        for (let i = 0; i < 12; i++) {{
          const cur = cardPoses[i];
          const tgt = cardTargets[i];
          const dx = tgt.x - cur.x;
          const dy = tgt.y - cur.y;
          const dr = tgt.rot - cur.rot;
          const ds = tgt.scale - cur.scale;
          const dop = tgt.opacity - cur.opacity;

          cur.x += dx * kCard;
          cur.y += dy * kCard;
          cur.rot += dr * kCard;
          cur.scale += ds * kCard;
          cur.opacity += dop * kCard;
          cur.z = tgt.z || cur.z;

          maxCardDist = Math.max(maxCardDist, Math.abs(dx), Math.abs(dy));

          if (cardEls[i]) {{
            cardEls[i].style.transform = `translate3d(${{cur.x}}px, ${{cur.y}}px, 0) rotate(${{cur.rot}}deg) scale(${{cur.scale}})`;
            cardEls[i].style.opacity = Math.max(0, Math.min(1, cur.opacity));
            cardEls[i].style.zIndex = cur.z;
          }}
        }}

        // 4. Smooth Sky Panel & Steadicam Camera (0.58 -> 0.74)
        const targetSkyProgress = Math.max(0, Math.min(1, (p - 0.58) / 0.15));
        const kSky = 1 - Math.pow(1 - 0.08, dt / 16.67);
        skyDisplayProgress += (targetSkyProgress - skyDisplayProgress) * kSky;

        if (skyDisplayProgress > 0.005) {{
          skyPanel.style.display = 'block';
          skyPanel.style.opacity = Math.min(1, skyDisplayProgress / 0.08);

          const easedSky = easeInOutCubic(skyDisplayProgress);
          const topInset = !isMobile ? 38 * (1 - easedSky) : 40 * (1 - easedSky);
          const bottomInset = !isMobile ? 38 * (1 - easedSky) : 40 * (1 - easedSky);
          const leftInset = !isMobile ? 38 * (1 - easedSky) : 26 * (1 - easedSky);
          const rightInset = !isMobile ? 38 * (1 - easedSky) : 26 * (1 - easedSky);
          const rad = 16 * (1 - easedSky);

          skyPanel.style.clipPath = `inset(${{topInset}}% ${{rightInset}}% ${{bottomInset}}% ${{leftInset}}% round ${{rad}}px)`;

          const plateScale = 1.18 - 0.18 * easedSky;
          skyPlate.style.transform = `scale(${{plateScale}})`;
          skyVideo.style.transform = `scale(${{plateScale}})`;

          // Video playback handling
          if (!videoStarted) {{
            videoStarted = true;
            skyVideo.playbackRate = 0.6;
            skyVideo.play().catch(() => {{}});
            setTimeout(() => {{
              skyVideo.style.opacity = '0.78';
            }}, 100);
          }}

          // Camera Target Scale
          const tgtCamScale = 0.75 + 0.25 * easedSky;

          // Camera Bob & Yaw (Smooth continuous floating motion, no angle snaps)
          let tgtYawDeg = 0;
          let tgtBobY = 0;
          if (p >= 0.64 && p < 0.74) {{
            const u = (p - 0.64) / 0.10;
            const eu = easeInOutCubic(u);
            tgtYawDeg = -8 * eu;
            tgtBobY = Math.sin(t * 1.5) * 6 * eu * (isMobile ? 0.75 : 1);
          }} else if (p >= 0.74 && p <= 0.88) {{
            const u = (p - 0.74) / 0.14;
            const eu = easeInOutCubic(u);
            tgtYawDeg = -8 + 16 * eu;
            tgtBobY = Math.sin(t * 1.5) * 6 * (isMobile ? 0.75 : 1);
          }} else if (p > 0.88 && p <= 0.95) {{
            const u = (p - 0.88) / 0.07;
            const eu = easeInOutCubic(u);
            tgtYawDeg = 8 * (1 - eu);
            tgtBobY = Math.sin(t * 1.5) * 6 * (1 - eu) * (isMobile ? 0.75 : 1);
          }} else if (p > 0.95) {{
            tgtYawDeg = 0;
            tgtBobY = 0;
          }}

          // Camera Deep Zoom into Lens (0.88 -> 0.97)
          let tgtZoomScale = 1;
          let blackoutOp = 0;
          if (p >= 0.88 && p <= 0.97) {{
            const rawQ = (p - 0.88) / 0.09;
            const gateMul = skyDisplayProgress >= 0.85 ? 1 : skyDisplayProgress / 0.85;
            const q = Math.pow(rawQ, 1.7) * gateMul;
            tgtZoomScale = 1 + q * q * 28;

            if (q >= 0.38) {{
              blackoutOp = Math.min(1, (q - 0.38) / 0.45);
            }}
          }} else if (p > 0.97) {{
            tgtZoomScale = 29;
            blackoutOp = 1;
          }}

          // Smooth Camera Steadicam Interpolation
          const kCam = 1 - Math.pow(1 - 0.10, dt / 16.67);
          curYawDeg += (tgtYawDeg - curYawDeg) * kCam;
          curCamScale += (tgtCamScale - curCamScale) * kCam;
          curZoomScale += (tgtZoomScale - curZoomScale) * kCam;
          curBobY += (tgtBobY - curBobY) * kCam;

          skyCamWrap.style.transform = `translate(-50%, -50%) translateY(${{curBobY}}px) scale(${{curCamScale}})`;
          skyCamera.style.transform = `rotateY(${{curYawDeg}}deg) scale(${{curZoomScale}})`;
          blackout.style.opacity = blackoutOp;

          // Sky Words Reveal
          if (skyDisplayProgress > 0.95 && !skyWordsRevealed) {{
            skyWordsRevealed = true;
            const times = [0, 120, 240, 450, 570, 690, 810];
            skyWords.forEach((sw, sIdx) => {{
              setTimeout(() => {{
                sw.style.transition = 'opacity 0.6s cubic-bezier(0.2,0,0.2,1), transform 0.6s cubic-bezier(0.2,0,0.2,1), filter 0.6s cubic-bezier(0.2,0,0.2,1)';
                sw.style.opacity = '1';
                sw.style.transform = 'translateY(0)';
                sw.style.filter = 'blur(0px)';
              }}, times[sIdx] || 0);
            }});
          }}
        }} else {{
          skyPanel.style.display = 'none';
          if (videoStarted) {{
            skyVideo.pause();
            videoStarted = false;
            skyVideo.style.opacity = '0';
          }}
          skyWordsRevealed = false;
          skyWords.forEach(sw => {{
            sw.style.opacity = '0';
            sw.style.transform = 'translateY(0.3em)';
            sw.style.filter = 'blur(6px)';
          }});
        }}

        // 5. Dark Navigation Toggle
        if (p > 0.985 || sy >= manifestoEl.offsetTop - 100) {{
          bodyEl.classList.add('dark-nav');
        }} else {{
          bodyEl.classList.remove('dark-nav');
        }}

        // 6. Horizontal Manifesto Track Scroll (950vh)
        const manTop = manifestoEl.offsetTop;
        const manHeight = manifestoEl.offsetHeight - H;
        const mp = Math.max(0, Math.min(1, (sy - manTop) / manHeight));

        if (sy >= manTop - H * 0.2) {{
          const startX = !isMobile ? W * 0.06 : W * 0.08;
          const trackWidth = manifestoTrack.scrollWidth;
          const endX = -(trackWidth - W * 0.9);
          const curX = startX + (endX - startX) * mp;
          manifestoTrack.style.transform = `translate3d(${{curX}}px, -50%, 0)`;

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

          manifestoItems.forEach(item => {{
            if (!item.classList.contains('revealed')) {{
              const rect = item.getBoundingClientRect();
              if (rect.left < triggerLine) {{
                setTimeout(() => {{
                  item.classList.add('revealed');
                }}, 120);
              }}
            }}
          }});
        }}

        requestAnimationFrame(render);
      }}

      requestAnimationFrame(render);

      // Smooth anchor clicks
      document.querySelectorAll('.nav-link').forEach(link => {{
        link.addEventListener('click', (e) => {{
          e.preventDefault();
          const target = link.getAttribute('href');
          if (target === '#') {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
          }} else if (target === '#process') {{
            window.scrollTo({{ top: storyEl.offsetTop + (storyEl.offsetHeight - H) * 0.20, behavior: 'smooth' }});
          }} else if (target === '#product') {{
            window.scrollTo({{ top: storyEl.offsetTop + (storyEl.offsetHeight - H) * 0.74, behavior: 'smooth' }});
          }} else if (target === '#manifesto') {{
            window.scrollTo({{ top: manifestoEl.offsetTop, behavior: 'smooth' }});
          }}
        }});
      }});

      if (processBtn) {{
        processBtn.addEventListener('click', () => {{
          window.scrollTo({{ top: manifestoEl.offsetTop, behavior: 'smooth' }});
        }});
      }}
    }})();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully!")
