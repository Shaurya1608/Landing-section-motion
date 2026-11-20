# Tidewell — "Tides in Motion" (Next.js App Router)

A high-fidelity Next.js implementation of the **Tidewell** coastal motion studio scroll-story landing page.

## Getting Started

Inside `tidewell-studio`:

```bash
# Development server (runs on port 3005)
npm run dev

# Production build
npm run build
npm start
```

Then visit:
```text
http://localhost:3005
```

## Features & Architecture

- **Next.js 14 App Router** with TypeScript and React 18.
- **Hero Section**:
  - Catmull-Rom spline flight path for the paper plane sprite.
  - 7 SVG pixel icons dynamically morphing into the "Tides in Motion" headline.
  - Physical distance-based fade tracking ensuring the headline never overlaps the navigation bar.
- **Pinned Stage (`1600vh`)**:
  - CSS sticky viewport stage with `overflow-x: clip` to ensure seamless pinning.
  - 12 art cards loaded from Higgsfield sprite sheets with exact cropping.
  - Card choreography phases: **Fan $\to$ Scatter $\to$ Pile $\to$ Rotating 3-Slot Wheel** with per-card spring inertia.
  - "From shore to product" process headline with animated word blur reveal and sailboat chip.
- **Gated Sky Panel & Camera**:
  - Strictly gated until wheel rotation completes and cards settle ($\le 3\text{px} / 1^\circ$).
  - Expanding rounded clip-path window to full bleed with looping dawn sky timelapse.
  - 3D cream instant camera with sinusoidal bob, perspective yaw ($\pm 10^\circ$), and deep lens zoom.
- **Horizontal Manifesto (`950vh`)**:
  - Sideways scrolling text track with character drop-ins ($\text{translateY} + \text{rotate}$).
  - 3D trinkets (conch shell, pearl, capsule, 4-point star sparkles) and pastel badge chips.
  - Automatic dark navigation transition on deep scroll.
