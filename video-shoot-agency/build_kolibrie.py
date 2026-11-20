import json

with open('c:/Users/Asus/websites-templates/video-shoot-agency/fonts.json', encoding='utf-8') as f:
    fonts = json.load(f)

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kolibrie Studio</title>
  <meta name="description" content="Kolibrie: a small studio for scroll-stopping reels, films and motion.">
  <style>
    @font-face {
      font-family: 'Archivo';
      font-weight: 100 900;
      font-stretch: 62% 125%;
      font-style: normal;
      font-display: swap;
      src: url('__FONT_ARCHIVO__') format('woff2');
    }
    @font-face {
      font-family: 'Playfair';
      font-weight: 300 900;
      font-stretch: 87.5% 112.5%;
      font-style: normal;
      font-display: swap;
      src: url('__FONT_PLAYFAIR__') format('woff2');
    }
    @font-face {
      font-family: 'Yellowtail';
      font-weight: 400;
      font-style: normal;
      font-display: swap;
      src: url('__FONT_YELLOWTAIL__') format('woff2');
    }
    @font-face {
      font-family: 'Titan One';
      font-weight: 400;
      font-style: normal;
      font-display: swap;
      src: url('__FONT_TITANONE__') format('woff2');
    }

    :root {
      --cream: #faf3e4;
      --ink: #141110;
      --tomato: #ef4a23;
      --butter: #ffd46e;
      --sky: #8fc6e8;
      --pink: #f6a9c2;
      --sage: #b9c48a;
      --white: #ffffff;
      --night: #141110;
      --page: var(--cream);
    }

    html[data-theme="dark"] {
      --page: var(--night);
    }

    html {
      font-size: calc(100vw / 90);
      box-sizing: border-box;
    }

    @media (max-width: 991px) {
      html {
        font-size: calc(100vw / 60);
      }
    }

    @media (max-width: 600px) {
      html {
        font-size: calc(100vw / 24.375);
      }
    }

    *, *::before, *::after {
      box-sizing: inherit;
      margin: 0;
      padding: 0;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    img {
      display: block;
    }

    body {
      background-color: var(--page);
      color: var(--ink);
      font-family: 'Archivo', sans-serif;
      overflow-x: clip;
      transition: background-color .7s cubic-bezier(.65, .05, 0, 1);
      -webkit-font-smoothing: antialiased;
    }

    html.lenis, html.lenis body {
      height: auto;
    }

    .lenis.lenis-smooth {
      scroll-behavior: auto !important;
    }

    main {
      visibility: hidden;
    }

    html[data-page-ready] main {
      visibility: visible;
    }

    [data-text-reveal], [data-scroll-reveal] {
      visibility: hidden;
    }

    .line {
      overflow: hidden;
      display: block;
      padding-bottom: .06em;
      margin-bottom: -.06em;
    }

    .char {
      display: inline-block;
      will-change: transform;
    }

    /* Shared Type Styles */
    .hero-headline {
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      font-size: 9rem;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 0.8em;
    }

    .section-headline {
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      font-size: 8rem;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 0.8em;
    }

    .team-headline {
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      font-size: 7rem;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 0.8em;
    }

    .alt-serif {
      font-family: 'Playfair', serif;
      font-variation-settings: 'wght' 300, 'wdth' 87.5, 'opsz' 120;
      letter-spacing: -0.035em;
      text-transform: uppercase;
    }

    .eyebrow-m {
      font-family: 'Playfair', serif;
      font-variation-settings: 'wght' 500, 'wdth' 87.5, 'opsz' 40;
      font-size: 2.5rem;
      letter-spacing: -0.03em;
      line-height: 1em;
    }

    .eyebrow-s {
      font-family: 'Playfair', serif;
      font-variation-settings: 'wght' 500, 'wdth' 87.5, 'opsz' 40;
      font-size: 2rem;
      letter-spacing: -0.03em;
      line-height: 1em;
    }

    .paragraph {
      font-family: 'Playfair', serif;
      font-variation-settings: 'wght' 400, 'wdth' 100, 'opsz' 20;
      font-size: 1.25rem;
      line-height: 1.35;
      letter-spacing: -0.01em;
    }

    @media (max-width: 991px) {
      .hero-headline {
        font-size: 6.4rem;
      }
      .section-headline {
        font-size: 6rem;
      }
    }

    @media (max-width: 600px) {
      .hero-headline {
        font-size: 4rem;
      }
      .section-headline {
        font-size: 4.2rem;
      }
      .team-headline {
        font-size: 4.2rem;
      }
      .eyebrow-m {
        font-size: 1.75rem;
      }
      .eyebrow-s {
        font-size: 1.5rem;
      }
    }

    /* Crop Box System */
    .crop {
      container-type: size;
      overflow: hidden;
      position: relative;
    }

    .crop .cell {
      position: absolute;
      left: 50%;
      top: 50%;
      translate: -50% -50%;
      aspect-ratio: var(--ar);
      width: max(100cqw, calc(100cqh * var(--ar)));
      height: auto;
    }

    .crop .cell img {
      position: absolute;
      max-width: none;
      display: block;
    }

    /* 5.1 Load Wipe Overlay */
    .load-wipe-overlay {
      position: fixed;
      inset: 0;
      z-index: 1000;
      pointer-events: none;
      overflow: clip;
    }

    .load-wipe-overlay[data-transition-ready] {
      display: none !important;
    }

    .load-wipe-svg {
      width: 100%;
      height: 100%;
      display: block;
    }

    /* 5.2 Cursor Label */
    .cursor-label-wrapper {
      position: fixed;
      left: 0;
      top: 0;
      z-index: 100;
      pointer-events: none;
      transform: translate(-50%, -50%);
    }

    .cursor-label-card {
      width: 9.5rem;
      background-color: var(--butter);
      overflow: hidden;
      border-radius: 9999px;
      transform: scale(0);
      transform-origin: center center;
      transition: transform .4s cubic-bezier(.65, .05, 0, 1);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }

    .cursor-label-wrapper[data-cursor-marquee-status="active"] .cursor-label-card {
      transform: scale(1);
    }

    .cursor-label-track {
      display: flex;
      position: relative;
      width: 100%;
    }

    .cursor-label-text {
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      text-transform: uppercase;
      font-size: 1.3rem;
      padding: .375em .25em;
      white-space: nowrap;
      color: var(--ink);
      display: inline-block;
      animation: cursorMarqueeAnim var(--dur, 2s) linear infinite;
      animation-play-state: paused;
    }

    .cursor-label-text.clone {
      position: absolute;
      left: 100%;
      top: 0;
    }

    .cursor-label-wrapper[data-cursor-marquee-status="active"] .cursor-label-text {
      animation-play-state: running;
    }

    @keyframes cursorMarqueeAnim {
      0% { transform: translateX(0); }
      100% { transform: translateX(-100%); }
    }

    /* 5.3 Nav */
    .nav-bar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 50;
      padding: 1.25rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
    }

    .nav-bar > * {
      pointer-events: auto;
    }

    .nav-logo {
      font-family: 'Yellowtail', cursive;
      font-size: 3.6rem;
      line-height: 1;
      color: var(--tomato);
      transform-origin: left center;
      transform: rotate(-8deg);
      margin-top: .2rem;
      display: inline-block;
      cursor: pointer;
    }

    .nav-center {
      position: absolute;
      left: 50%;
      top: 1.25rem;
      transform: translateX(-50%);
      background-color: var(--white);
      height: 3rem;
      padding: 0 1.25rem;
      gap: 1.5rem;
      border-radius: 9999px;
      display: flex;
      align-items: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
    }

    .nav-link {
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      font-size: 1.05rem;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      color: var(--ink);
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
    }

    .underline-box {
      position: absolute;
      left: 0;
      width: 100%;
      top: 100%;
      height: .5em;
      color: var(--tomato);
      pointer-events: none;
    }

    .nav-contact {
      background-color: var(--white);
      height: 3rem;
      padding: 0 1.25rem;
      display: flex;
      align-items: center;
      gap: .5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
      cursor: pointer;
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      font-size: 1.05rem;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      color: var(--ink);
    }

    .nav-dot {
      width: .45rem;
      height: .45rem;
      background-color: var(--tomato);
      border-radius: 50%;
      flex-shrink: 0;
    }

    @media (max-width: 991px) {
      .nav-center {
        display: none;
      }
    }

    @media (max-width: 600px) {
      .nav-bar {
        padding: 1rem;
      }
      .nav-logo {
        font-size: 2.6rem;
      }
      .nav-contact {
        height: 2.5rem;
        font-size: .95rem;
        padding: 0 .9rem;
      }
    }

    /* 5.4 Hero */
    .hero-section {
      height: 100vh;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .hero-video {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 50%;
      z-index: 0;
      pointer-events: none;
    }

    @media (max-width: 600px) {
      .hero-video {
        object-position: 6% 50%;
      }
    }

    .hero-cursor-card {
      width: 16rem;
      height: 16rem;
      position: absolute;
      left: 50%;
      top: 50%;
      translate: -50% -50%;
      overflow: hidden;
      z-index: 1;
      pointer-events: none;
      border-radius: 1.25rem;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }

    .hero-cursor-card .media-layer {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      transform: scale(1.2);
    }

    .hero-cursor-card .crop {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      visibility: hidden;
      transition: opacity .25s ease;
    }

    .hero-cursor-card .crop.on {
      opacity: 1;
      visibility: visible;
    }

    @media (max-width: 600px) {
      .hero-cursor-card {
        width: 7.5rem;
        height: 7.5rem;
        top: 13% !important;
        left: 50% !important;
        translate: -50% 0 !important;
        transform: rotate(-5deg) !important;
        opacity: 1 !important;
        visibility: visible !important;
      }
      .hero-cursor-card .crop:first-child {
        opacity: 1;
        visibility: visible;
      }
    }

    .hero-content {
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2rem;
      margin-top: -3rem;
      text-align: center;
      pointer-events: auto;
    }

    @media (max-width: 600px) {
      .hero-content {
        gap: 1.4rem;
        margin-top: 5rem;
        padding: 0 1rem;
      }
    }

    .hero-link {
      font-family: 'Playfair', serif;
      font-variation-settings: 'wght' 500, 'wdth' 87.5, 'opsz' 40;
      font-size: 2.1rem;
      letter-spacing: -0.03em;
      line-height: 1;
      gap: .375em;
      display: inline-flex;
      align-items: center;
      position: relative;
      cursor: pointer;
    }

    .hero-link .underline-box {
      top: 118%;
      height: .6em;
    }

    .hero-arrow-box {
      width: 1em;
      height: 1em;
      background-color: var(--tomato);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
      vertical-align: middle;
      border-radius: 0.18em;
      flex-shrink: 0;
    }

    .hero-arrow-inner {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: transform .525s cubic-bezier(.175, .885, .32, 1.275);
    }

    .hero-link:hover .hero-arrow-inner {
      transform: translateY(100%);
    }

    .hero-arrow-inner svg {
      width: 65%;
      height: 65%;
      fill: var(--white);
      position: absolute;
    }

    .hero-arrow-inner svg.clone {
      top: -100%;
    }

    @media (max-width: 600px) {
      .hero-link {
        font-size: 1.6rem;
      }
    }

    .marquee-outer {
      position: absolute;
      bottom: 1.5rem;
      left: 0;
      width: 100%;
      z-index: 2;
      overflow: hidden;
      pointer-events: none;
    }

    .marquee-scroll-wrapper {
      margin-left: -10%;
      width: 120%;
    }

    .marquee-track {
      display: flex;
      width: max-content;
    }

    .marquee-collection {
      display: flex;
      align-items: center;
      flex-shrink: 0;
    }

    .marquee-item {
      width: 9rem;
      height: 7rem;
      margin: 0 2.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .marquee-item svg {
      width: 60%;
      height: 60%;
      color: var(--tomato);
      fill: currentColor;
    }

    @media (max-width: 600px) {
      .marquee-item {
        width: 5.5rem;
        height: 5rem;
        margin: 0 1rem;
      }
    }

    /* 5.5 Latest Drops */
    .section-drops {
      position: relative;
      background-color: var(--page);
    }

    .drops-pin-element {
      height: 100vh;
      display: grid;
      grid-template-columns: 38fr 62fr;
      gap: 2rem;
      padding: 0 3rem 0 5rem;
      align-items: center;
      overflow: hidden;
      position: relative;
    }

    .drops-left-col {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      justify-content: center;
    }

    .drops-left-col .eyebrow-s {
      max-width: 26rem;
    }

    .drops-stage {
      position: relative;
      height: 100%;
      perspective: 1400px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .drops-stack-root {
      transform-style: preserve-3d;
      position: relative;
      width: 100%;
      height: 100%;
    }

    .drop-card {
      position: absolute;
      aspect-ratio: 1.75;
      width: min(80vh, 52vw);
      left: 50%;
      top: calc(50% - 5vh);
      translate: -50% -50%;
      display: block;
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.18);
      padding: 1.75vh;
      transform-style: preserve-3d;
    }

    .drop-card .crop {
      position: absolute;
      inset: 1.75vh;
      border-radius: 1rem;
      overflow: hidden;
    }

    .drop-card .gradient-overlay {
      position: absolute;
      inset: 1.75vh;
      border-radius: 1rem;
      background: linear-gradient(#0000 55%, #0006);
      pointer-events: none;
      z-index: 2;
    }

    .drop-card-title {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 2.4em;
      text-align: center;
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 800, 'wdth' 72;
      text-transform: uppercase;
      font-size: 7.5vh;
      line-height: .8;
      letter-spacing: -0.02em;
      color: var(--cream);
      text-shadow: 0 .05em .3em rgba(0, 0, 0, .25);
      z-index: 3;
    }

    .drops-badge {
      position: absolute;
      right: 1rem;
      bottom: 1rem;
      width: 9rem;
      height: 9rem;
      z-index: 5;
    }

    @media (max-width: 991px) {
      .drops-pin-element {
        height: auto !important;
        display: flex;
        flex-direction: column;
        padding: 6rem 1.5rem 4rem;
        gap: 3rem;
        overflow: visible;
      }
      .drops-stage {
        width: 100%;
        height: auto;
        perspective: none;
      }
      .drops-stack-root {
        transform-style: flat;
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        width: 100%;
        height: auto;
      }
      .drop-card {
        position: relative;
        width: 100%;
        left: auto;
        top: auto;
        translate: none;
        aspect-ratio: 1.75;
        padding: 1rem;
        border-radius: 1rem;
      }
      .drop-card .crop, .drop-card .gradient-overlay {
        inset: 1rem;
        border-radius: .75rem;
      }
      .drop-card-title {
        font-size: 3.4rem;
        bottom: 1.6em;
      }
      .drops-badge {
        display: none;
      }
    }

    @media (max-width: 600px) {
      .drop-card-title {
        font-size: 2rem;
      }
    }

    /* 5.6 Meet the Flock */
    .section-flock {
      position: relative;
      height: 340vh;
      background-color: var(--page);
      color: var(--flock-text, #141110);
      transition: background-color .7s cubic-bezier(.65, .05, 0, 1), color .7s cubic-bezier(.65, .05, 0, 1);
    }

    html[data-theme="dark"] .section-flock {
      --flock-text: var(--cream);
    }

    @media (max-width: 991px) {
      .section-flock {
        height: 260vh;
      }
    }

    .sticky-title-wrap {
      position: sticky;
      top: 0;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1;
      pointer-events: none;
    }

    .sticky-title-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.4rem;
      text-align: center;
      position: relative;
      pointer-events: auto;
    }

    .sticky-title-content .paragraph {
      max-width: 26rem;
    }

    .stamp-sticker {
      position: absolute;
      width: 10rem;
      left: -3rem;
      top: -8rem;
      transform: rotate(-10deg);
      cursor: pointer;
      z-index: 4;
    }

    .photo-layer {
      position: absolute;
      inset: 0;
      z-index: 2;
      pointer-events: none;
    }

    .team-photo-card {
      position: absolute;
      pointer-events: auto;
      border-radius: 0.75rem;
      overflow: visible;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
      cursor: pointer;
      will-change: transform;
    }

    .team-photo-card .crop {
      width: 100%;
      aspect-ratio: 4 / 5;
      border-radius: 0.75rem;
      overflow: hidden;
      background-color: #e9dcc6;
    }

    .name-sticker {
      font-family: 'Titan One', sans-serif;
      font-size: 3.4rem;
      color: var(--tomato);
      -webkit-text-stroke: .32rem var(--cream);
      paint-order: stroke fill;
      position: absolute;
      bottom: -0.9rem;
      left: 50%;
      translate: -50% 0;
      white-space: nowrap;
      pointer-events: none;
      z-index: 3;
    }

    .caption-tag {
      position: absolute;
      bottom: .7rem;
      left: .7rem;
      background-color: var(--cream);
      color: var(--ink);
      font-family: 'Archivo', sans-serif;
      font-variation-settings: 'wght' 700, 'wdth' 72;
      text-transform: uppercase;
      font-size: .9rem;
      padding: .25rem .5rem;
      border-radius: .2rem;
      pointer-events: none;
      z-index: 3;
    }

    @media (max-width: 600px) {
      .stamp-sticker {
        width: 6rem;
        left: 0;
        top: -5rem;
      }
      .sticky-title-content {
        padding: 0 1.5rem;
      }
      .team-photo-card {
        width: 8rem !important;
      }
      .caption-tag {
        display: none;
      }
      .name-sticker {
        font-size: 1.9rem;
        -webkit-text-stroke: .22rem var(--cream);
      }

      /* Staggered alternating phone positions for 12 cards */
      .team-photo-card[data-index="0"] { top: 1% !important; left: -1rem !important; right: auto !important; }
      .team-photo-card[data-index="6"] { top: 9% !important; right: -1rem !important; left: auto !important; }
      .team-photo-card[data-index="1"] { top: 17% !important; left: 4rem !important; right: auto !important; }
      .team-photo-card[data-index="7"] { top: 25% !important; right: 4rem !important; left: auto !important; }
      .team-photo-card[data-index="2"] { top: 33% !important; left: -1rem !important; right: auto !important; }
      .team-photo-card[data-index="8"] { top: 41% !important; right: -1rem !important; left: auto !important; }
      .team-photo-card[data-index="3"] { top: 49% !important; left: 4rem !important; right: auto !important; }
      .team-photo-card[data-index="9"] { top: 57% !important; right: 4rem !important; left: auto !important; }
      .team-photo-card[data-index="4"] { top: 65% !important; left: -1rem !important; right: auto !important; }
      .team-photo-card[data-index="10"] { top: 73% !important; right: -1rem !important; left: auto !important; }
      .team-photo-card[data-index="5"] { top: 81% !important; left: 4rem !important; right: auto !important; }
      .team-photo-card[data-index="11"] { top: 89% !important; right: 4rem !important; left: auto !important; }
    }

    /* 7. Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      .load-wipe-overlay {
        display: none !important;
      }
      main {
        visibility: visible !important;
      }
      [data-text-reveal], [data-scroll-reveal] {
        visibility: visible !important;
      }
      .section-flock {
        height: auto !important;
      }
      .section-flock .sticky-title-wrap {
        position: relative !important;
        height: auto !important;
        padding-top: 8rem !important;
        padding-bottom: 4rem !important;
      }
      .section-flock .photo-layer {
        position: relative !important;
        inset: auto !important;
        display: grid !important;
        grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr)) !important;
        gap: 2rem !important;
        padding: 2rem !important;
        height: auto !important;
      }
      .section-flock .team-photo-card {
        position: relative !important;
        left: auto !important;
        right: auto !important;
        top: auto !important;
        width: 100% !important;
        transform: none !important;
      }
    }
  </style>
</head>
<body>

  <!-- 5.1 Load Wipe Overlay -->
  <div class="load-wipe-overlay" aria-hidden="true">
    <svg class="load-wipe-svg" viewBox="0 0 1000 1000" preserveAspectRatio="none">
      <path class="load-wipe-path" d="M43 259C296 11.5688 994 -3 922.994 498.259C851.988 999.517 281.229 1004.28 123 767C-35.2287 529.721 179 259 472 259C765 259 792 498.259 659 654C526 809.741 319 755 285 669.001C251 583.001 299 452 496 452C693 452 876.073 639.171 935 937.001" fill="none" stroke="#ef4a23" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" />
    </svg>
  </div>

  <!-- 5.2 Cursor Label -->
  <div class="cursor-label-wrapper" data-cursor-marquee-status="inactive" aria-hidden="true">
    <div class="cursor-label-card">
      <div class="cursor-label-track">
        <span class="cursor-label-text">View case →</span>
        <span class="cursor-label-text clone">View case →</span>
      </div>
    </div>
  </div>

  <!-- 5.3 Nav -->
  <nav class="nav-bar" aria-label="Main navigation">
    <a href="#" class="nav-logo" aria-label="Kolibrie home">Kolibrie</a>
    
    <div class="nav-center">
      <a href="#flock" class="nav-link" data-draw-line>
        <span>About</span>
        <span class="underline-box"></span>
      </a>
      <a href="#drops" class="nav-link" data-draw-line>
        <span>Work</span>
        <span class="underline-box"></span>
      </a>
      <a href="#drops" class="nav-link" data-draw-line>
        <span>Services</span>
        <span class="underline-box"></span>
      </a>
    </div>

    <a href="#flock" class="nav-contact">
      <span class="nav-dot"></span>
      <span>Contact</span>
    </a>
  </nav>

  <main>
    <!-- 5.4 Hero Section -->
    <section class="hero-section" data-cursor-cards>
      <video class="hero-video" muted loop playsinline preload="auto" aria-hidden="true" poster="https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224241_f6feccd5-1c45-4d22-b369-f927916f9973.png&w=2048&q=85">
        <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261110_231342_88260d66-aa30-4612-9157-d7f1b5a66d8c.mp4" type="video/mp4">
      </video>

      <!-- Cursor Card (behind text) -->
      <div class="hero-cursor-card" aria-hidden="true">
        <div class="media-layer">
          <div class="crop on" data-crop="work2:1"></div>
          <div class="crop" data-crop="work1:0"></div>
          <div class="crop" data-crop="work2:3"></div>
          <div class="crop" data-crop="work1:1"></div>
          <div class="crop" data-crop="work2:2"></div>
          <div class="crop" data-crop="work1:2"></div>
          <div class="crop" data-crop="work2:0"></div>
          <div class="crop" data-crop="work1:3"></div>
        </div>
      </div>

      <!-- Hero Content -->
      <div class="hero-content">
        <h1 class="hero-headline" data-text-reveal="chars" data-font-weight-hover data-rest="700" data-near="200" data-radius="400">
          STORIES THAT<br>GET <span class="alt-serif" data-font-weight-hover data-rest="300" data-near="800" data-radius="400">SHARED</span>
        </h1>

        <a href="#drops" class="hero-link" data-draw-line="always">
          <span class="hero-link-text">See the reel</span>
          <span class="underline-box"></span>
          <span class="hero-arrow-box" aria-hidden="true">
            <span class="hero-arrow-inner">
              <svg viewBox="0 0 14 13"><path d="M12.94 5.7 9.95 8 6.9 10.37l.84 1.86V0h-2.55v12.23l.85-1.86L3 8 0 5.7V9.05l6.47 4.95 6.47-4.95z"/></svg>
              <svg viewBox="0 0 14 13" class="clone"><path d="M12.94 5.7 9.95 8 6.9 10.37l.84 1.86V0h-2.55v12.23l.85-1.86L3 8 0 5.7V9.05l6.47 4.95 6.47-4.95z"/></svg>
            </span>
          </span>
        </a>
      </div>

      <!-- Client Marquee -->
      <div class="marquee-outer" aria-hidden="true">
        <div class="marquee-scroll-wrapper">
          <div class="marquee-track">
            <div class="marquee-collection">
              <!-- 1. Asterisk -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#ef4a23" stroke-width="12" stroke-linecap="round"><line x1="50" y1="15" x2="50" y2="85"/><line x1="19.7" y1="32.5" x2="80.3" y2="67.5"/><line x1="19.7" y1="67.5" x2="80.3" y2="32.5"/></svg>
              </div>
              <!-- 2. Two capsule D shapes -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="#ef4a23"><path d="M18 25 h16 a25 25 0 0 1 0 50 h-16 z M54 25 h16 a25 25 0 0 1 0 50 h-16 z"/></svg>
              </div>
              <!-- 3. Three wavy lines -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#ef4a23" stroke-width="8" stroke-linecap="round"><path d="M15 32 Q 32.5 22 50 32 T 85 32"/><path d="M15 50 Q 32.5 40 50 50 T 85 50"/><path d="M15 68 Q 32.5 58 50 68 T 85 68"/></svg>
              </div>
              <!-- 4. Four diamonds in diamond pattern -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="#ef4a23"><polygon points="50,15 62,30 50,45 38,30"/><polygon points="50,55 62,70 50,85 38,70"/><polygon points="28,35 40,50 28,65 16,50"/><polygon points="72,35 84,50 72,65 60,50"/></svg>
              </div>
              <!-- 5. Half sun over three bars -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="#ef4a23" stroke="#ef4a23"><path d="M25 45 A 25 25 0 0 1 75 45 Z" stroke="none"/><line x1="25" y1="56" x2="75" y2="56" stroke-width="6" stroke-linecap="round"/><line x1="25" y1="68" x2="75" y2="68" stroke-width="6" stroke-linecap="round"/><line x1="25" y1="80" x2="75" y2="80" stroke-width="6" stroke-linecap="round"/></svg>
              </div>
              <!-- 6. Two arches -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#ef4a23" stroke-width="10" stroke-linecap="round"><path d="M18 80 V 45 A 16 16 0 0 1 50 45 V 80"/><path d="M50 80 V 45 A 16 16 0 0 1 82 45 V 80"/></svg>
              </div>
              <!-- 7. Four-point sparkle star -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="#ef4a23"><path d="M50 12 Q 50 50 12 50 Q 50 50 50 88 Q 50 50 88 50 Q 50 50 50 12 Z"/></svg>
              </div>
              <!-- 8. Circle with cross inside -->
              <div class="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#ef4a23" stroke-width="8" stroke-linecap="round"><circle cx="50" cy="50" r="35"/><line x1="50" y1="25" x2="50" y2="75"/><line x1="25" y1="50" x2="75" y2="50"/></svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5.5 Latest Drops -->
    <section class="section-drops" id="drops" data-featured-stack>
      <div class="drops-pin-element">
        <!-- Left Column -->
        <div class="drops-left-col" data-scroll-reveal-group>
          <p class="eyebrow-s" data-scroll-reveal="lines">
            Made to be watched twice. A handful of what left our edit desk lately.
          </p>
          <h2 class="section-headline" data-scroll-reveal="chars" data-font-weight-hover data-rest="700" data-near="200" data-radius="400">
            LATEST<br><span class="alt-serif" data-font-weight-hover data-rest="300" data-near="800" data-radius="400">DROPS</span>
          </h2>
        </div>

        <!-- Right Column Stage -->
        <div class="drops-stage">
          <div class="drops-stack-root">
            <!-- Card 1 -->
            <a href="#" class="drop-card" style="background-color: var(--tomato);" data-cursor-marquee-text="View case →">
              <div class="crop" data-crop="work1:0"></div>
              <div class="gradient-overlay"></div>
              <div class="drop-card-title">SQUEEZE THE SUN</div>
            </a>
            <!-- Card 2 -->
            <a href="#" class="drop-card" style="background-color: var(--sky);" data-cursor-marquee-text="View case →">
              <div class="crop" data-crop="work1:1"></div>
              <div class="gradient-overlay"></div>
              <div class="drop-card-title">DEEP END DAYS</div>
            </a>
            <!-- Card 3 -->
            <a href="#" class="drop-card" style="background-color: var(--butter);" data-cursor-marquee-text="View case →">
              <div class="crop" data-crop="work1:2"></div>
              <div class="gradient-overlay"></div>
              <div class="drop-card-title">FLAKE & BAKE</div>
            </a>
            <!-- Card 4 -->
            <a href="#" class="drop-card" style="background-color: var(--sage);" data-cursor-marquee-text="View case →">
              <div class="crop" data-crop="work1:3"></div>
              <div class="gradient-overlay"></div>
              <div class="drop-card-title">CURB APPEAL</div>
            </a>
            <!-- Card 5 -->
            <a href="#" class="drop-card" style="background-color: var(--pink);" data-cursor-marquee-text="View case →">
              <div class="crop" data-crop="work2:0"></div>
              <div class="gradient-overlay"></div>
              <div class="drop-card-title">NIGHT BITES</div>
            </a>
          </div>

          <!-- Badge -->
          <div class="drops-badge" aria-hidden="true">
            <svg viewBox="0 0 200 200" style="width: 100%; height: 100%; display: block;">
              <circle cx="100" cy="100" r="98" fill="#ef4a23"/>
              <path id="badgePath" d="M 100, 30 a 70,70 0 1,1 -0.01,0" fill="none"/>
              <text fill="#faf3e4" font-family="'Archivo', sans-serif" font-variation-settings="'wght' 800, 'wdth' 80" font-size="24">
                <textPath href="#badgePath" textLength="436" lengthAdjust="spacing">SCROLL · SAVE · SHARE · REPEAT ·</textPath>
              </text>
              <circle cx="100" cy="100" r="17" fill="none" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="100" y1="73" x2="100" y2="65" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="100" y1="127" x2="100" y2="135" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="73" y1="100" x2="65" y2="100" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="127" y1="100" x2="135" y2="100" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="81" y1="81" x2="75" y2="75" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="119" y1="119" x2="125" y2="125" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="119" y1="81" x2="125" y2="75" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
              <line x1="81" y1="119" x2="75" y2="125" stroke="#faf3e4" stroke-width="5" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- 5.6 Meet the Flock -->
    <section class="section-flock" id="flock" data-page-theme="dark">
      <!-- Sticky Title -->
      <div class="sticky-title-wrap">
        <div class="sticky-title-content" data-scroll-reveal-group>
          <!-- Stamp Sticker -->
          <div class="stamp-sticker" data-momentum-hover>
            <svg viewBox="0 0 228 136" style="width: 100%; height: auto; display: block;">
              <ellipse cx="114" cy="68" rx="104" ry="58" fill="#faf3e4" stroke="#ef4a23" stroke-width="10"/>
              <text x="114" y="78" text-anchor="middle" font-family="'Yellowtail', cursive" font-size="54" fill="#ef4a23" transform="rotate(-8 114 68)">Kolibrie</text>
            </svg>
          </div>

          <p class="eyebrow-m" data-scroll-reveal="lines">The people behind the frames</p>
          <h2 class="team-headline" data-scroll-reveal="chars" data-font-weight-hover data-rest="700" data-near="200" data-radius="400">
            <span class="alt-serif" data-font-weight-hover data-rest="300" data-near="800" data-radius="400">MEET </span>THE <span class="alt-serif" data-font-weight-hover data-rest="300" data-near="800" data-radius="400">FLOCK</span>
          </h2>
          <p class="paragraph" data-scroll-reveal="lines">
            Twelve makers, one group chat. We shoot, cut and animate before the coffee goes cold.
          </p>
        </div>
      </div>

      <!-- Photo Layer -->
      <div class="photo-layer">
        <!-- Left 1: Noor -->
        <div class="team-photo-card" data-index="0" data-speed="1" data-momentum-hover style="left: 2.5vw; top: 3%; width: 14rem; transform: rotate(-4deg);">
          <div class="crop" data-crop="team1:0"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(-7deg);">Noor</span>
        </div>
        <!-- Left 2: ON SET -->
        <div class="team-photo-card" data-index="1" data-speed="0.6" data-momentum-hover style="left: 21vw; top: 19%; width: 11rem; transform: rotate(3deg);">
          <div class="crop" data-crop="bts:0"></div>
          <span class="caption-tag">ON SET</span>
        </div>
        <!-- Left 3: Sem -->
        <div class="team-photo-card" data-index="2" data-speed="1.3" data-momentum-hover style="left: 3vw; top: 33%; width: 13rem; transform: rotate(5deg);">
          <div class="crop" data-crop="team1:1"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(4deg);">Sem</span>
        </div>
        <!-- Left 4: Mila -->
        <div class="team-photo-card" data-index="3" data-speed="0.8" data-momentum-hover style="left: 23vw; top: 49%; width: 13.5rem; transform: rotate(-3deg);">
          <div class="crop" data-crop="team2:3"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(-5deg);">Mila</span>
        </div>
        <!-- Left 5: DINNER, IN 9:16 -->
        <div class="team-photo-card" data-index="4" data-speed="1.15" data-momentum-hover style="left: 2vw; top: 64%; width: 11.5rem; transform: rotate(-6deg);">
          <div class="crop" data-crop="bts:2"></div>
          <span class="caption-tag">DINNER, IN 9:16</span>
        </div>
        <!-- Left 6: Daan -->
        <div class="team-photo-card" data-index="5" data-speed="0.7" data-momentum-hover style="left: 20vw; top: 79%; width: 14rem; transform: rotate(4deg);">
          <div class="crop" data-crop="team1:2"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(6deg);">Daan</span>
        </div>

        <!-- Right 1: Lotte -->
        <div class="team-photo-card" data-index="6" data-speed="0.75" data-momentum-hover style="right: 3vw; top: 2%; width: 13.5rem; transform: rotate(4deg);">
          <div class="crop" data-crop="team2:0"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(5deg);">Lotte</span>
        </div>
        <!-- Right 2: TAKE ONE -->
        <div class="team-photo-card" data-index="7" data-speed="1.25" data-momentum-hover style="right: 22vw; top: 17%; width: 11rem; transform: rotate(-5deg);">
          <div class="crop" data-crop="bts:1"></div>
          <span class="caption-tag">TAKE ONE</span>
        </div>
        <!-- Right 3: Jules -->
        <div class="team-photo-card" data-index="8" data-speed="0.9" data-momentum-hover style="right: 2.5vw; top: 32%; width: 14rem; transform: rotate(-3deg);">
          <div class="crop" data-crop="team2:1"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(-6deg);">Jules</span>
        </div>
        <!-- Right 4: Yara -->
        <div class="team-photo-card" data-index="9" data-speed="1.4" data-momentum-hover style="right: 23vw; top: 48%; width: 13rem; transform: rotate(5deg);">
          <div class="crop" data-crop="team1:3"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(4deg);">Yara</span>
        </div>
        <!-- Right 5: GOLDEN HOUR -->
        <div class="team-photo-card" data-index="10" data-speed="0.65" data-momentum-hover style="right: 3vw; top: 63%; width: 11.5rem; transform: rotate(6deg);">
          <div class="crop" data-crop="bts:3"></div>
          <span class="caption-tag">GOLDEN HOUR</span>
        </div>
        <!-- Right 6: Kenji -->
        <div class="team-photo-card" data-index="11" data-speed="1.05" data-momentum-hover style="right: 20vw; top: 78%; width: 14rem; transform: rotate(-4deg);">
          <div class="crop" data-crop="team2:2"></div>
          <span class="name-sticker" style="transform: translateX(-50%) rotate(-4deg);">Kenji</span>
        </div>
      </div>
    </section>
  </main>

  <!-- 1. Libraries (in exact order) -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/DrawSVGPlugin.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/InertiaPlugin.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.17/dist/lenis.min.js"></script>

  <!-- Inline Script -->
  <script>
    (function() {
      // Crop metadata
      const SHEETS = {
        work1: {
          url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_b0899b4d-5876-4c63-98d3-8608d8dbe790.png&w=2400&q=85',
          w: 2688, h: 1520,
          cells: [
            [0, 0, 1336, 752],
            [1352, 0, 1336, 752],
            [0, 768, 1336, 752],
            [1352, 768, 1336, 752]
          ]
        },
        work2: {
          url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_aee93a53-873f-470f-afb3-6395c22ab639.png&w=2400&q=85',
          w: 2688, h: 1520,
          cells: [
            [0, 0, 1335, 749],
            [1356, 0, 1332, 749],
            [0, 770, 1335, 750],
            [1356, 770, 1332, 750]
          ]
        },
        team1: {
          url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224239_be9bd6b1-debb-4a95-aadf-1a36e4d2f557.png&w=1600&q=85',
          w: 1744, h: 2336,
          cells: [
            [0, 0, 864, 1156],
            [881, 0, 863, 1156],
            [0, 1175, 864, 1161],
            [881, 1175, 863, 1161]
          ]
        },
        team2: {
          url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_bfc657e7-cbc1-43fb-a726-e8be5dd42302.png&w=1600&q=85',
          w: 1744, h: 2336,
          cells: [
            [0, 0, 864, 1159],
            [880, 0, 864, 1159],
            [0, 1176, 864, 1160],
            [880, 1176, 864, 1160]
          ]
        },
        bts: {
          url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_bf8567fa-9d67-4f1e-b4e0-5662c0bf70e4.png&w=1600&q=85',
          w: 1744, h: 2336,
          cells: [
            [0, 0, 865, 1160],
            [881, 0, 863, 1160],
            [0, 1176, 865, 1160],
            [881, 1176, 863, 1160]
          ]
        }
      };

      // Fill crop elements
      document.querySelectorAll('.crop[data-crop]').forEach(box => {
        const [sheetKey, cellIdxStr] = box.getAttribute('data-crop').split(':');
        const sheet = SHEETS[sheetKey];
        if (!sheet) return;
        const cellIdx = parseInt(cellIdxStr, 10);
        const [rawX, rawY, rawW, rawH] = sheet.cells[cellIdx];
        const insetX = rawX + 4;
        const insetY = rawY + 4;
        const insetW = rawW - 8;
        const insetH = rawH - 8;
        const ar = insetW / insetH;

        const cellDiv = document.createElement('div');
        cellDiv.className = 'cell';
        cellDiv.style.setProperty('--ar', ar);

        const img = document.createElement('img');
        img.src = sheet.url;
        img.loading = 'lazy';
        img.decoding = 'async';
        img.alt = '';
        img.style.width = ((sheet.w / insetW) * 100) + '%';
        img.style.height = ((sheet.h / insetH) * 100) + '%';
        img.style.left = (-(insetX / insetW) * 100) + '%';
        img.style.top = (-(insetY / insetH) * 100) + '%';

        cellDiv.appendChild(img);
        box.appendChild(cellDiv);
      });

      // Reduced motion check
      const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      let isReducedMotion = motionQuery.matches;
      motionQuery.addEventListener('change', e => {
        isReducedMotion = e.matches;
        updateHeroVideo();
      });

      // Video poster vs stream
      const heroVideo = document.querySelector('.hero-video');
      function updateHeroVideo() {
        if (!heroVideo) return;
        if (isReducedMotion) {
          heroVideo.pause();
          heroVideo.removeAttribute('src');
          heroVideo.load();
        } else {
          if (!heroVideo.currentSrc && !heroVideo.querySelector('source')) {
            const src = document.createElement('source');
            src.src = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261110_231342_88260d66-aa30-4612-9157-d7f1b5a66d8c.mp4';
            src.type = 'video/mp4';
            heroVideo.appendChild(src);
            heroVideo.load();
          }
          heroVideo.play().catch(() => {});
        }
      }
      updateHeroVideo();

      // Failsafe reveal function
      function revealEverythingFailsafe() {
        if (!document.documentElement.hasAttribute('data-page-ready')) {
          document.documentElement.setAttribute('data-page-ready', '');
          const overlay = document.querySelector('.load-wipe-overlay');
          if (overlay) overlay.setAttribute('data-transition-ready', '');
          document.querySelectorAll('[data-text-reveal], [data-scroll-reveal]').forEach(el => {
            el.style.visibility = 'visible';
          });
        }
      }

      // 4-second failsafe
      setTimeout(revealEverythingFailsafe, 4000);

      // Check GSAP availability
      if (typeof gsap === 'undefined') {
        revealEverythingFailsafe();
        return;
      }

      // Register Plugins
      if (typeof ScrollTrigger !== 'undefined') gsap.registerPlugin(ScrollTrigger);
      if (typeof SplitText !== 'undefined') gsap.registerPlugin(SplitText);
      if (typeof DrawSVGPlugin !== 'undefined') gsap.registerPlugin(DrawSVGPlugin);
      if (typeof InertiaPlugin !== 'undefined') gsap.registerPlugin(InertiaPlugin);

      // Smooth scroll (Lenis)
      let lenis = null;
      if (!isReducedMotion && typeof Lenis !== 'undefined') {
        lenis = new Lenis({ lerp: 0.165, wheelMultiplier: 1.25 });
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => {
          lenis.raf(time * 1000);
        });
        gsap.ticker.lagSmoothing(0);
      }

      // Smooth in-page navigation links
      document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
          const href = link.getAttribute('href');
          if (href === '#') return;
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            if (lenis && !isReducedMotion) {
              lenis.scrollTo(target, { duration: 1.4 });
            } else {
              target.scrollIntoView({ behavior: 'smooth' });
            }
          }
        });
      });

      // 6.5 Draw Underline Variants
      const UNDERLINE_PATHS = [
        'M5 20.9999C26.7762 16.2245 49.5532 11.5572 71.7979 14.6666C84.9553 16.5057 97.0392 21.8432 109.987 24.3888C116.413 25.6523 123.012 25.5143 129.042 22.6388C135.981 19.3303 142.586 15.1422 150.092 13.3333C156.799 11.7168 161.702 14.6225 167.887 16.8333C181.562 21.7212 194.975 22.6234 209.252 21.3888C224.678 20.0548 239.912 17.991 255.42 18.3055C272.027 18.6422 288.409 18.867 305 17.9999',
        'M5 24.2592C26.233 20.2879 47.7083 16.9968 69.135 13.8421C98.0469 9.5853 128.407 4.02322 158.059 5.14674C172.583 5.69708 187.686 8.66104 201.598 11.9696C207.232 13.3093 215.437 14.9471 220.137 18.3619C224.401 21.4596 220.737 25.6575 217.184 27.6168C208.309 32.5097 197.199 34.281 186.698 34.8486C183.159 35.0399 147.197 36.2657 155.105 26.5837C158.11 22.9053 162.993 20.6229 167.764 18.7924C178.386 14.7164 190.115 12.1115 201.624 10.3984C218.367 7.90626 235.528 7.06127 252.521 7.49276C258.455 7.64343 264.389 7.92791 270.295 8.41825C280.321 9.25056 296 10.8932 305 13.0242',
        'M5 29.5014C9.61174 24.4515 12.9521 17.9873 20.9532 17.5292C23.7742 17.3676 27.0987 17.7897 29.6575 19.0014C33.2644 20.7093 35.6481 24.0004 39.4178 25.5014C48.3911 29.0744 55.7503 25.7731 63.3048 21.0292C67.9902 18.0869 73.7668 16.1366 79.3721 17.8903C85.1682 19.7036 88.2173 26.2464 94.4121 27.2514C102.584 28.5771 107.023 25.5064 113.276 20.6125C119.927 15.4067 128.83 12.3333 137.249 15.0014C141.418 16.3225 143.116 18.7528 146.581 21.0014C149.621 22.9736 152.78 23.6197 156.284 24.2514C165.142 25.8479 172.315 17.5185 179.144 13.5014C184.459 10.3746 191.785 8.74853 195.868 14.5292C199.252 19.3205 205.597 22.9057 211.621 22.5014C215.553 22.2374 220.183 17.8356 222.979 15.5569C225.4 13.5845 227.457 11.1105 230.742 10.5292C232.718 10.1794 234.784 12.9691 236.164 14.0014C238.543 15.7801 240.717 18.4775 243.356 19.8903C249.488 23.1729 255.706 21.2551 261.079 18.0014C266.571 14.6754 270.439 11.5202 277.146 13.6125C280.725 14.7289 283.221 17.209 286.393 19.0014C292.321 22.3517 298.255 22.5014 305 22.5014',
        'M17.0039 32.6826C32.2307 32.8412 47.4552 32.8277 62.676 32.8118C67.3044 32.807 96.546 33.0555 104.728 32.0775C113.615 31.0152 104.516 28.3028 102.022 27.2826C89.9573 22.3465 77.3751 19.0254 65.0451 15.0552C57.8987 12.7542 37.2813 8.49399 44.2314 6.10216C50.9667 3.78422 64.2873 5.81914 70.4249 5.96641C105.866 6.81677 141.306 7.58809 176.75 8.59886C217.874 9.77162 258.906 11.0553 300 14.4892',
        'M4.99805 20.9998C65.6267 17.4649 126.268 13.845 187.208 12.8887C226.483 12.2723 265.751 13.2796 304.998 13.9998',
        'M5 29.8857C52.3147 26.9322 99.4329 21.6611 146.503 17.1765C151.753 16.6763 157.115 15.9505 162.415 15.6551C163.28 15.6069 165.074 15.4123 164.383 16.4275C161.704 20.3627 157.134 23.7551 153.95 27.4983C153.209 28.3702 148.194 33.4751 150.669 34.6605C153.638 36.0819 163.621 32.6063 165.039 32.2029C178.55 28.3608 191.49 23.5968 204.869 19.5404C231.903 11.3436 259.347 5.83254 288.793 5.12258C294.094 4.99476 299.722 4.82265 305 5.45025'
      ];

      let underlineVariantIdx = Math.floor(Math.random() * UNDERLINE_PATHS.length);

      function createUnderlineSvg(d) {
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 310 40');
        svg.setAttribute('preserveAspectRatio', 'none');
        svg.style.width = '100%';
        svg.style.height = '100%';
        svg.style.display = 'block';

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', d);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', 'currentColor');
        path.setAttribute('stroke-width', '10');
        path.setAttribute('stroke-linecap', 'round');
        svg.appendChild(path);
        return { svg, path };
      }

      // Hook hover underlines
      document.querySelectorAll('[data-draw-line]:not([data-draw-line="always"])').forEach(el => {
        const box = el.querySelector('.underline-box');
        if (!box) return;

        let activePath = null;
        let activeSvg = null;
        let isDrawing = false;
        let pendingLeave = false;

        el.addEventListener('mouseenter', () => {
          if (isReducedMotion) return;
          pendingLeave = false;
          box.innerHTML = '';
          const d = UNDERLINE_PATHS[underlineVariantIdx % UNDERLINE_PATHS.length];
          underlineVariantIdx++;
          const { svg, path } = createUnderlineSvg(d);
          box.appendChild(svg);
          activePath = path;
          activeSvg = svg;
          isDrawing = true;

          gsap.fromTo(path, { drawSVG: '0%' }, {
            drawSVG: '100%',
            duration: 0.5,
            ease: 'power2.inOut',
            onComplete: () => {
              isDrawing = false;
              if (pendingLeave && activePath) {
                gsap.to(activePath, {
                  drawSVG: '100% 100%',
                  duration: 0.5,
                  ease: 'power2.inOut',
                  onComplete: () => {
                    if (activeSvg && activeSvg.parentNode) activeSvg.remove();
                    activeSvg = null;
                    activePath = null;
                  }
                });
                pendingLeave = false;
              }
            }
          });
        });

        el.addEventListener('mouseleave', () => {
          if (isReducedMotion) return;
          if (isDrawing) {
            pendingLeave = true;
          } else if (activePath) {
            gsap.to(activePath, {
              drawSVG: '100% 100%',
              duration: 0.5,
              ease: 'power2.inOut',
              onComplete: () => {
                if (activeSvg && activeSvg.parentNode) activeSvg.remove();
                activeSvg = null;
                activePath = null;
              }
            });
          }
        });
      });

      // Always-on hero underline
      function drawHeroUnderline() {
        const heroLink = document.querySelector('[data-draw-line="always"]');
        if (!heroLink) return;
        const box = heroLink.querySelector('.underline-box');
        if (!box) return;
        box.innerHTML = '';
        const d = UNDERLINE_PATHS[underlineVariantIdx % UNDERLINE_PATHS.length];
        underlineVariantIdx++;
        const { svg, path } = createUnderlineSvg(d);
        box.appendChild(svg);
        if (isReducedMotion) {
          gsap.set(path, { drawSVG: '100%' });
        } else {
          gsap.fromTo(path, { drawSVG: '0%' }, {
            drawSVG: '100%',
            duration: 0.6,
            ease: 'power2.inOut'
          });
        }
      }

      // 6.6 Font weight follows cursor
      const isTouch = window.matchMedia('(hover: none), (pointer: coarse)').matches;
      let hoverChars = [];
      let pointerPageX = window.innerWidth / 2;
      let pointerPageY = window.innerHeight / 2;

      function setupFontWeightHover(targetEl, splitChars) {
        if (isTouch || isReducedMotion) return;

        splitChars.forEach(char => {
          const host = char.closest('[data-font-weight-hover]') || targetEl;
          const rest = parseFloat(host.dataset.rest || 700);
          const near = parseFloat(host.dataset.near || 200);
          const radius = parseFloat(host.dataset.radius || 400);

          char.style.setProperty('--wght', rest);
          const isSerif = char.closest('.alt-serif') !== null;
          if (isSerif) {
            char.style.fontVariationSettings = `'wght' var(--wght, ${rest}), 'wdth' 87.5, 'opsz' 120`;
          } else {
            char.style.fontVariationSettings = `'wght' var(--wght, ${rest}), 'wdth' 72`;
          }

          hoverChars.push({
            el: char,
            rest,
            near,
            radius,
            current: rest,
            quickTo: gsap.quickTo(char, '--wght', { duration: 0.4, ease: 'power2.out' }),
            x: 0,
            y: 0
          });
        });
        updateCharCenters();
      }

      function updateCharCenters() {
        for (let i = 0; i < hoverChars.length; i++) {
          const c = hoverChars[i];
          const r = c.el.getBoundingClientRect();
          c.x = r.left + r.width / 2 + window.scrollX;
          c.y = r.top + r.height / 2 + window.scrollY;
        }
      }

      window.addEventListener('pointermove', (e) => {
        pointerPageX = e.pageX;
        pointerPageY = e.pageY;
      });

      window.addEventListener('resize', updateCharCenters);
      window.addEventListener('scroll', updateCharCenters, { passive: true });

      gsap.ticker.add(() => {
        if (isReducedMotion || isTouch || hoverChars.length === 0) return;
        for (let i = 0; i < hoverChars.length; i++) {
          const c = hoverChars[i];
          const d = Math.hypot(pointerPageX - c.x, pointerPageY - c.y);
          const f = d >= c.radius ? 0 : 1 - d / c.radius;
          let target = c.rest + (c.near - c.rest) * f;
          const minVal = Math.min(c.rest, c.near);
          const maxVal = Math.max(c.rest, c.near);
          target = Math.max(minVal, Math.min(maxVal, target));
          if (Math.abs(target - c.current) >= 1) {
            c.current = target;
            c.quickTo(target);
          }
        }
      });

      // Text Reveal Setup
      function initTextReveals() {
        // Hero headline load reveal
        const heroH1 = document.querySelector('.hero-headline[data-text-reveal]');
        if (heroH1) {
          if (isReducedMotion) {
            heroH1.style.visibility = 'visible';
            heroH1.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
          } else {
            const split = new SplitText(heroH1, {
              type: 'chars,words,lines',
              linesClass: 'line',
              charsClass: 'char',
              mask: 'lines',
              autoSplit: false
            });

            gsap.set(heroH1, { visibility: 'visible' });
            gsap.from(split.chars, {
              yPercent: 135,
              duration: 1,
              ease: 'expo.out',
              stagger: 0.0175,
              delay: 0.6,
              onComplete: () => {
                heroH1.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
                setupFontWeightHover(heroH1, split.chars);
              }
            });
          }
        }

        // Scroll reveals
        document.querySelectorAll('[data-scroll-reveal-group]').forEach(group => {
          if (isReducedMotion) {
            group.querySelectorAll('[data-scroll-reveal]').forEach(el => {
              el.style.visibility = 'visible';
              el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
            });
            return;
          }

          const elements = group.querySelectorAll('[data-scroll-reveal]');
          const tl = gsap.timeline({
            scrollTrigger: {
              trigger: group,
              start: 'top 85%',
              once: true
            }
          });

          elements.forEach((el, idx) => {
            const mode = el.getAttribute('data-scroll-reveal');
            const startTime = idx * 0.12;

            if (mode === 'chars') {
              const split = new SplitText(el, {
                type: 'chars,words,lines',
                linesClass: 'line',
                charsClass: 'char',
                mask: 'lines',
                autoSplit: false
              });

              tl.set(el, { visibility: 'visible' }, startTime);
              tl.from(split.chars, {
                yPercent: 135,
                duration: 1,
                ease: 'expo.out',
                stagger: 0.0175,
                onComplete: () => {
                  el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
                  if (el.hasAttribute('data-font-weight-hover')) {
                    setupFontWeightHover(el, split.chars);
                  }
                }
              }, startTime);
            } else if (mode === 'lines') {
              const split = new SplitText(el, {
                type: 'lines,words',
                linesClass: 'line',
                mask: 'lines'
              });

              tl.set(el, { visibility: 'visible' }, startTime);
              tl.from(split.lines, {
                yPercent: 135,
                duration: 1,
                ease: 'expo.out',
                stagger: 0.07,
                onComplete: () => {
                  el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
                }
              }, startTime);
            } else if (mode === 'element') {
              tl.set(el, { visibility: 'visible' }, startTime);
              tl.fromTo(el, { y: 24, autoAlpha: 0 }, {
                y: 0,
                autoAlpha: 1,
                duration: 0.8,
                ease: 'expo.out',
                onComplete: () => {
                  el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
                }
              }, startTime);
            }
          });
        });
      }

      // 6.7 Hero cursor card
      function initHeroCursorCard() {
        if (isReducedMotion || isTouch || window.innerWidth <= 600) return;

        const hero = document.querySelector('.hero-section');
        const card = document.querySelector('.hero-cursor-card');
        if (!hero || !card) return;

        const mediaLayer = card.querySelector('.media-layer');
        const photos = card.querySelectorAll('.crop');

        const cardX = gsap.quickTo(card, 'x', { duration: 1, ease: 'power4' });
        const cardY = gsap.quickTo(card, 'y', { duration: 1, ease: 'power4' });
        const cardRot = gsap.quickTo(card, 'rotation', { duration: 1, ease: 'power4' });
        const mediaX = gsap.quickTo(mediaLayer, 'xPercent', { duration: 0.6, ease: 'power2' });
        const mediaY = gsap.quickTo(mediaLayer, 'yPercent', { duration: 0.7, ease: 'power2' });

        gsap.set(card, { autoAlpha: 0 });

        let firstMove = true;
        let lastX = 0, lastY = 0;
        let travel = 0;
        let photoIdx = 0;
        let timer = null;
        let isCardVisible = false;

        hero.addEventListener('mousemove', (e) => {
          if (e.target.closest('a, button')) {
            gsap.to(card, { autoAlpha: 0, duration: 0.25, ease: 'power2.out' });
            isCardVisible = false;
            return;
          }

          if (!isCardVisible) {
            gsap.to(card, { autoAlpha: 1, duration: 0.3 });
            isCardVisible = true;
          }

          const heroRect = hero.getBoundingClientRect();
          const targetX = e.clientX - window.innerWidth / 2;
          const targetY = e.clientY - window.innerHeight / 2 - heroRect.top;

          if (firstMove) {
            gsap.set(card, { x: targetX, y: targetY });
            cardX(targetX);
            cardY(targetY);
            lastX = targetX;
            lastY = targetY;
            firstMove = false;
            return;
          }

          const dx = (targetX - lastX) / 2;
          const dy = (targetY - lastY) / 2;
          const rot = (targetX - lastX) / 4;
          lastX = targetX;
          lastY = targetY;

          cardX(targetX);
          cardY(targetY);
          cardRot(rot);

          const driftX = -Math.max(-8, Math.min(8, dx));
          const driftY = -Math.max(-8, Math.min(8, dy));
          mediaX(driftX);
          mediaY(driftY);

          travel += Math.abs(dx) + Math.abs(dy);
          if (travel >= 300) {
            travel = 0;
            photoIdx = (photoIdx + 1) % photos.length;
            photos.forEach((p, i) => p.classList.toggle('on', i === photoIdx));
          }

          clearTimeout(timer);
          timer = setTimeout(() => {
            cardRot(0);
            mediaX(0);
            mediaY(0);
          }, 66);
        });

        hero.addEventListener('mouseleave', () => {
          firstMove = true;
          travel = 0;
          cardRot(0);
          mediaX(0);
          mediaY(0);
          gsap.to(card, { autoAlpha: 0, duration: 0.3 });
          isCardVisible = false;
        });
      }

      // 6.8 Client Marquee
      function initClientMarquee() {
        const marqueeOuter = document.querySelector('.marquee-outer');
        const scrollWrapper = document.querySelector('.marquee-scroll-wrapper');
        const track = document.querySelector('.marquee-track');
        const collection = document.querySelector('.marquee-collection');
        if (!marqueeOuter || !scrollWrapper || !track || !collection) return;

        // Duplicate collection 2 times (3 total)
        const clone1 = collection.cloneNode(true);
        const clone2 = collection.cloneNode(true);
        track.appendChild(clone1);
        track.appendChild(clone2);

        if (isReducedMotion) return;

        const f = window.innerWidth <= 479 ? 0.25 : window.innerWidth <= 991 ? 0.5 : 1;
        const colWidth = collection.offsetWidth || (window.innerWidth * 1.5);
        const loopDuration = 30 * (colWidth / window.innerWidth) * f;

        const allCols = track.querySelectorAll('.marquee-collection');
        gsap.set(allCols, { xPercent: -100 });

        const marqueeTween = gsap.to(allCols, {
          xPercent: 0,
          repeat: -1,
          duration: loopDuration,
          ease: 'none'
        });
        marqueeTween.totalProgress(0.5);

        ScrollTrigger.create({
          trigger: marqueeOuter,
          start: 'top bottom',
          end: 'bottom top',
          onUpdate: (self) => {
            const dir = self.direction; // 1 = scrolling down, -1 = scrolling up
            marqueeTween.timeScale(dir === 1 ? 1 : -1);
          }
        });

        gsap.fromTo(scrollWrapper, { x: '10vw' }, {
          x: '-10vw',
          ease: 'none',
          scrollTrigger: {
            trigger: marqueeOuter,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0
          }
        });
      }

      // 6.9 "Latest drops" 3D stack
      function initDropsStack() {
        const dropsSection = document.querySelector('.section-drops');
        const pinElement = dropsSection?.querySelector('.drops-pin-element');
        const stackRoot = dropsSection?.querySelector('.drops-stack-root');
        const slides = dropsSection?.querySelectorAll('.drop-card');
        const badge = dropsSection?.querySelector('.drops-badge');

        if (!dropsSection || !pinElement || !stackRoot || !slides || slides.length === 0) return;

        const count = slides.length;

        // Media query: only pin on desktop (>=992px)
        const mm = gsap.matchMedia();

        mm.add('(min-width: 992px)', () => {
          slides.forEach((slide, b) => {
            gsap.set(slide, {
              z: -b * 120,
              y: -b * 40,
              zIndex: count - b,
              autoAlpha: 1
            });
          });

          const tl = gsap.timeline({ paused: true });

          for (let b = 0; b < count - 1; b++) {
            tl.to(slides[b], {
              y: '+=' + (window.innerHeight * 0.9),
              ease: 'power2.in',
              duration: 1
            }, b);

            tl.to(slides[b], {
              autoAlpha: 0,
              ease: 'none',
              duration: 0.25
            }, b + 0.7);

            for (let c = b + 1; c < count; c++) {
              const newC = c - (b + 1);
              tl.to(slides[c], {
                z: -newC * 120,
                y: -newC * 40,
                ease: 'none',
                duration: 1
              }, b);
            }
          }

          if (badge) {
            tl.to(badge, {
              rotation: 180,
              ease: 'none',
              duration: count - 1
            }, 0);
          }

          ScrollTrigger.create({
            trigger: dropsSection,
            start: 'top top',
            end: () => '+=' + (window.innerHeight * 1.2 * (count - 1)),
            pin: pinElement,
            pinSpacing: true,
            scrub: 0.3,
            refreshPriority: 1,
            invalidateOnRefresh: true,
            onUpdate: (self) => {
              tl.progress(self.progress);
            }
          });

          // Mouse tilt
          if (!isReducedMotion) {
            const tiltX = gsap.quickTo(stackRoot, 'rotationX', { duration: 0.6, ease: 'power3' });
            const tiltY = gsap.quickTo(stackRoot, 'rotationY', { duration: 0.6, ease: 'power3' });

            const onMouseMove = (e) => {
              const rect = pinElement.getBoundingClientRect();
              const rx = -((e.clientY - rect.top) / rect.height - 0.5) * 6;
              const ry = ((e.clientX - rect.left) / rect.width - 0.5) * 10;
              tiltX(rx);
              tiltY(ry);
            };

            const onMouseLeave = () => {
              tiltX(0);
              tiltY(0);
            };

            pinElement.addEventListener('mousemove', onMouseMove);
            pinElement.addEventListener('mouseleave', onMouseLeave);

            return () => {
              pinElement.removeEventListener('mousemove', onMouseMove);
              pinElement.removeEventListener('mouseleave', onMouseLeave);
            };
          }
        });
      }

      // 6.10 Cursor Label ("View case →")
      function initCursorLabel() {
        if (isTouch) return;

        const labelWrapper = document.querySelector('.cursor-label-wrapper');
        if (!labelWrapper) return;

        const textEls = labelWrapper.querySelectorAll('.cursor-label-text');
        const quickX = gsap.quickTo(labelWrapper, 'x', { duration: 0.4, ease: 'power3' });
        const quickY = gsap.quickTo(labelWrapper, 'y', { duration: 0.4, ease: 'power3' });

        let firstMove = true;
        let lastTarget = null;
        let pauseTimeout = null;

        function updateHover(clientX, clientY) {
          const hovered = document.elementFromPoint(clientX, clientY)?.closest('[data-cursor-marquee-text]');
          if (hovered && hovered !== lastTarget) {
            lastTarget = hovered;
            clearTimeout(pauseTimeout);
            const text = hovered.getAttribute('data-cursor-marquee-text') || 'View case →';
            textEls.forEach(el => {
              el.textContent = text;
              el.style.setProperty('--dur', (text.length / 5) + 's');
            });
            labelWrapper.setAttribute('data-cursor-marquee-status', 'active');
          } else if (!hovered && lastTarget) {
            lastTarget = null;
            labelWrapper.setAttribute('data-cursor-marquee-status', 'inactive');
            pauseTimeout = setTimeout(() => {
              // paused state handled via CSS
            }, 400);
          }
        }

        window.addEventListener('pointermove', (e) => {
          if (firstMove) {
            gsap.set(labelWrapper, { x: e.clientX, y: e.clientY });
            quickX(e.clientX);
            quickY(e.clientY);
            firstMove = false;
          } else {
            quickX(e.clientX);
            quickY(e.clientY);
          }
          updateHover(e.clientX, e.clientY);
        });

        window.addEventListener('scroll', () => {
          if (!firstMove) {
            updateHover(pointerPageX - window.scrollX, pointerPageY - window.scrollY);
          }
        }, { passive: true });
      }

      // 6.11 Team photo parallax
      function initTeamParallax() {
        const flock = document.querySelector('.section-flock');
        const cards = flock?.querySelectorAll('.team-photo-card');
        if (!flock || !cards) return;

        const mm = gsap.matchMedia();

        const createTriggers = (k) => {
          cards.forEach(card => {
            const speed = parseFloat(card.getAttribute('data-speed') || 1);
            const dist = 320 * k * speed;
            gsap.fromTo(card, { y: dist }, {
              y: -dist,
              ease: 'none',
              scrollTrigger: {
                trigger: flock,
                start: 'clamp(top bottom)',
                end: 'clamp(bottom top)',
                scrub: true,
                invalidateOnRefresh: true,
                refreshPriority: -1
              }
            });
          });
        };

        mm.add('(min-width: 992px) and (prefers-reduced-motion: no-preference)', () => {
          createTriggers(1);
        });
        mm.add('(min-width: 480px) and (max-width: 991px) and (prefers-reduced-motion: no-preference)', () => {
          createTriggers(0.5);
        });
        mm.add('(max-width: 479px) and (prefers-reduced-motion: no-preference)', () => {
          createTriggers(0.3);
        });
      }

      // 6.12 Momentum hover (InertiaPlugin)
      function initMomentumHover() {
        if (isTouch || isReducedMotion || typeof InertiaPlugin === 'undefined') return;

        const targets = document.querySelectorAll('[data-momentum-hover]');
        let prevX = 0, prevY = 0;
        let vx = 0, vy = 0;

        window.addEventListener('pointermove', (e) => {
          vx = e.clientX - prevX;
          vy = e.clientY - prevY;
          prevX = e.clientX;
          prevY = e.clientY;
        });

        // Decay velocity per frame
        gsap.ticker.add(() => {
          vx *= 0.8;
          vy *= 0.8;
        });

        targets.forEach(target => {
          target.addEventListener('mouseenter', (e) => {
            const rect = target.getBoundingClientRect();
            const F = e.clientX - rect.left - rect.width / 2;
            const R = e.clientY - rect.top - rect.height / 2;
            const hyp = Math.hypot(F, R) || 1;
            const torque = (F * vy - R * vx) / hyp;

            const clampVal = (val, max) => Math.max(-max, Math.min(max, val));

            gsap.to(target, {
              inertia: {
                x: { velocity: clampVal(vx * 30, 1080), end: 0 },
                y: { velocity: clampVal(vy * 30, 1080), end: 0 },
                rotation: { velocity: clampVal(torque * 20, 60), end: 0 },
                resistance: 200
              }
            });
          });
        });
      }

      // 6.13 Page theme switch
      function initThemeSwitch() {
        document.querySelectorAll('[data-page-theme]').forEach(el => {
          const theme = el.getAttribute('data-page-theme');
          ScrollTrigger.create({
            trigger: el,
            start: 'top 55%',
            end: 'bottom 45%',
            refreshPriority: -1,
            onEnter: () => document.documentElement.setAttribute('data-theme', theme),
            onEnterBack: () => document.documentElement.setAttribute('data-theme', theme),
            onLeave: () => document.documentElement.removeAttribute('data-theme'),
            onLeaveBack: () => document.documentElement.removeAttribute('data-theme')
          });
        });
      }

      // Master Page Init
      function initPage() {
        initTextReveals();
        initHeroCursorCard();
        initClientMarquee();
        initDropsStack();
        initCursorLabel();
        initTeamParallax();
        initMomentumHover();
        initThemeSwitch();
      }

      // 6.2 Load Sequence Timeline
      function startLoadSequence() {
        document.documentElement.setAttribute('data-page-ready', '');
        const overlay = document.querySelector('.load-wipe-overlay');
        const wipePath = document.querySelector('.load-wipe-path');

        if (isReducedMotion) {
          if (overlay) overlay.setAttribute('data-transition-ready', '');
          const main = document.querySelector('main');
          if (main) gsap.set(main, { autoAlpha: 1 });
          initPage();
          drawHeroUnderline();
          return;
        }

        const main = document.querySelector('main');
        const tl = gsap.timeline();

        // 0s: main autoAlpha: 0, scribble wipe covering screen
        tl.set(main, { autoAlpha: 0 }, 0);
        tl.set(wipePath, { drawSVG: '0% 100%', strokeWidth: '30%' }, 0);

        // 0.4s ("reveal" label)
        tl.addLabel('reveal', 0.4);
        tl.set(main, { autoAlpha: 1 }, 'reveal');
        tl.call(() => {
          initPage();
        }, null, 'reveal');

        tl.to(wipePath, {
          drawSVG: '100% 100%',
          strokeWidth: '5%',
          duration: 1.25,
          ease: 'power1.inOut',
          onComplete: () => {
            if (overlay) overlay.setAttribute('data-transition-ready', '');
          }
        }, 'reveal');

        // ~1.3s after init: draw hero link underline
        tl.call(() => {
          drawHeroUnderline();
        }, null, 1.7);
      }

      // Start when fonts ready or after 1.5s
      const fontsPromise = document.fonts ? document.fonts.ready : Promise.resolve();
      const timeoutPromise = new Promise(resolve => setTimeout(resolve, 1500));

      Promise.race([fontsPromise, timeoutPromise]).then(() => {
        startLoadSequence();
      }).catch(() => {
        startLoadSequence();
      });

    })();
  </script>
</body>
</html>
"""

template = template.replace('__FONT_ARCHIVO__', fonts['archivo'])
template = template.replace('__FONT_PLAYFAIR__', fonts['playfair'])
template = template.replace('__FONT_YELLOWTAIL__', fonts['yellowtail'])
template = template.replace('__FONT_TITANONE__', fonts['titanone'])

with open('c:/Users/Asus/websites-templates/video-shoot-agency/index.html', 'w', encoding='utf-8') as f:
    f.write(template)

print('Successfully generated index.html')
