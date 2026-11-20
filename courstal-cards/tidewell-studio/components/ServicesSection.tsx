'use client';

import React from 'react';

export interface ServiceItem {
  num: string;
  title: string;
  headline: string;
  description: string;
  lensSpec: string;
  pipeline: string[];
  deliverables: string[];
}

export const SERVICES: ServiceItem[] = [
  {
    num: '01',
    title: 'Direction & Cinematography',
    headline: 'Narrative cinema crafted with large-format optics and deliberate choreography.',
    description: 'We direct narrative commercials, brand documentaries, and original visual essays. Our in-house cinematography kit spans ARRI Alexa 35, Cooke Anamorphic primes, and vintage Super 16mm glass.',
    lensSpec: 'Cooke Anamorphic /i Full Frame Plus • 40mm T2.3',
    pipeline: ['Treatment & Concept Directing', 'Storyboarding & Pre-vis', 'Location & Talent Casting', 'Large-Format Production', 'Custom Master Grading'],
    deliverables: ['DCI 4K Master ProRes 4444 XQ', 'Theatrical Cinemascope 2.39:1', 'Dolby Vision HDR Pass', 'Social 9:16 Editorial Cutdowns'],
  },
  {
    num: '02',
    title: 'World-Building & Realtime CGI',
    headline: 'Simulating impossible physics, spatial environments, and tactile digital matter.',
    description: 'From photo-real raytraced materials to real-time Unreal Engine 5.4 installations, we craft spatial worlds that obey their own physics while remaining grounded in sensory truth.',
    lensSpec: 'Virtual Camera Rig • 18mm Ultra-Wide Optical Simulation',
    pipeline: ['Procedural Geometry & Houdini FX', 'Photogrammetry & Gaussian Splats', 'Unreal Engine 5 Virtual Production', 'Volumetric Lighting & Atmosphere'],
    deliverables: ['Real-time 60fps Interactive Builds', 'Lossless 32-bit OpenEXR Plates', 'Spatial Display Masters', 'Custom Asset Libraries'],
  },
  {
    num: '03',
    title: 'Sound Architecture & Score',
    headline: 'Sonic landscapes engineered to vibrate through physical space.',
    description: 'Sound is half the image. We compose bespoke modular synthesizer scores, tactile foley recordings, and spatial Dolby Atmos soundbeds that guide subconscious emotion.',
    lensSpec: 'Stereo Pair Neumann KM184 • Binaural Head Rig',
    pipeline: ['Analog Synthesizer Scoring', 'Custom Foley & Location Ambience', 'Spatial Sound Design', 'Dolby Atmos 7.1.4 Mastering'],
    deliverables: ['Dolby Atmos ADM BWF Master', 'Stereo 96kHz 24-bit Lossless Score', 'Stems & Instrumental Mixes', 'Interactive WebAudio Packs'],
  },
  {
    num: '04',
    title: 'Brand Systems & Digital Artifacts',
    headline: 'Visual identities and kinetic design languages that move with intention.',
    description: 'We develop bespoke motion guidelines, title sequences, typographic systems, and physical limited-edition packaging that extend film narratives into enduring cultural artifacts.',
    lensSpec: 'Macro 100mm T2.8 • Precision Typographic Focus',
    pipeline: ['Visual Identity & Kinetic Rules', 'Custom Type Design & Variable Fonts', 'Motion Design Guidelines', 'Editorial Print & Packaging'],
    deliverables: ['Comprehensive Motion System Guidelines', 'Custom Variable Font Files (.woff2)', 'Interactive Web Experience Kit', 'Collector Boxset Packaging'],
  },
];

export default function ServicesSection() {
  return (
    <section id="services" className="services-section">
      <div className="services-stage" id="servicesStage">
        <div className="services-header">
          <div className="services-tag">
            <span className="tag-dot" />
            <span>STUDIO CAPABILITIES & APPARATUS</span>
          </div>
          <h2 className="services-title">
            Engineering Sensation Through <span className="title-serif">Direction</span>
          </h2>
        </div>

        <div className="services-grid">
          {/* Left Column: Capability List */}
          <div className="services-list" id="servicesList">
            {SERVICES.map((srv, idx) => (
              <div
                key={srv.num}
                className={`service-item ${idx === 0 ? 'active' : ''}`}
                data-service-idx={idx}
                id={`serviceItem-${idx}`}
              >
                <div className="service-item-head">
                  <span className="service-num">{srv.num}</span>
                  <h3 className="service-name">{srv.title}</h3>
                  <span className="service-arrow">
                    <svg viewBox="0 0 16 16">
                      <path d="M4 12l8-8M4 4h8v8" stroke="currentColor" strokeWidth="1.8" fill="none" />
                    </svg>
                  </span>
                </div>
                <div className="service-item-body">
                  <p className="service-headline">{srv.headline}</p>
                  <p className="service-desc">{srv.description}</p>
                  <div className="service-spec-badge">
                    <span className="spec-label">OPTICAL SPEC:</span>
                    <span className="spec-value">{srv.lensSpec}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Right Column: Interactive 3D Technical Viewport */}
          <div className="services-viewport">
            <div className="viewport-hud">
              <div className="hud-line">
                <span>PIPELINE APPARATUS // ONLINE</span>
                <span className="hud-status">FPS: 60.00 • 4K DCI</span>
              </div>
              <div className="hud-crosshair center" />
              <div className="hud-crosshair top-left" />
              <div className="hud-crosshair bottom-right" />
            </div>

            {/* Dynamic Geometry Prism Wireframe */}
            <div className="viewport-canvas-container" id="serviceCanvasWrap">
              <svg
                className="prism-wireframe"
                id="prismSvg"
                viewBox="0 0 400 400"
                fill="none"
              >
                <circle cx="200" cy="200" r="150" stroke="rgba(222, 147, 80, 0.25)" strokeWidth="1" strokeDasharray="4 4" />
                <circle cx="200" cy="200" r="100" stroke="rgba(207, 110, 74, 0.35)" strokeWidth="1" />
                <polygon
                  id="prismPoly1"
                  points="200,60 320,280 80,280"
                  stroke="#DE9350"
                  strokeWidth="1.8"
                  fill="rgba(222, 147, 80, 0.05)"
                />
                <polygon
                  id="prismPoly2"
                  points="200,340 320,120 80,120"
                  stroke="#E5B876"
                  strokeWidth="1.2"
                  strokeDasharray="6 6"
                />
                <circle cx="200" cy="200" r="6" fill="#E5B876" />
                <line x1="50" y1="200" x2="350" y2="200" stroke="rgba(255,255,255,0.15)" strokeWidth="0.8" />
                <line x1="200" y1="50" x2="200" y2="350" stroke="rgba(255,255,255,0.15)" strokeWidth="0.8" />
              </svg>

              <div className="viewport-readout" id="serviceReadout">
                <div className="readout-title" id="readoutTitle">
                  01 // ARRI LARGE FORMAT CINEMATOGRAPHY
                </div>
                <div className="readout-tags" id="readoutTags">
                  <span className="spec-chip">35mm SENSOR</span>
                  <span className="spec-chip">4.6K RAW</span>
                  <span className="spec-chip">EI 800 - 3200</span>
                  <span className="spec-chip">T1.5 - T22</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
