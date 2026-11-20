'use client';

import React from 'react';
import CropImage from './CropImage';

export default function LatestDropsSection() {
  return (
    <section className="section-drops" id="drops" data-featured-stack>
      <div className="drops-pin-element">
        {/* Left Column */}
        <div className="drops-left-col" data-scroll-reveal-group>
          <p className="eyebrow-s" data-scroll-reveal="lines">
            Made to be watched twice. A handful of what left our edit desk lately.
          </p>
          <h2
            className="section-headline"
            data-scroll-reveal="chars"
            data-font-weight-hover
            data-rest="700"
            data-near="200"
            data-radius="400"
          >
            LATEST<br />
            <span
              className="alt-serif"
              data-font-weight-hover
              data-rest="300"
              data-near="800"
              data-radius="400"
            >
              DROPS
            </span>
          </h2>
        </div>

        {/* Right Column Stage */}
        <div className="drops-stage">
          <div className="drops-stack-root">
            {/* Card 1 */}
            <a href="#" className="drop-card" style={{ backgroundColor: 'var(--tomato)' }} data-cursor-marquee-text="View case →">
              <CropImage crop="work1:0" />
              <div className="gradient-overlay"></div>
              <div className="drop-card-title">TUSCAN SUNRISE</div>
            </a>
            {/* Card 2 */}
            <a href="#" className="drop-card" style={{ backgroundColor: 'var(--sky)' }} data-cursor-marquee-text="View case →">
              <CropImage crop="work1:1" />
              <div className="gradient-overlay"></div>
              <div className="drop-card-title">AZURE DRIFT</div>
            </a>
            {/* Card 3 */}
            <a href="#" className="drop-card" style={{ backgroundColor: 'var(--butter)' }} data-cursor-marquee-text="View case →">
              <CropImage crop="work1:2" />
              <div className="gradient-overlay"></div>
              <div className="drop-card-title">GOLDEN CRUST</div>
            </a>
            {/* Card 4 */}
            <a href="#" className="drop-card" style={{ backgroundColor: 'var(--sage)' }} data-cursor-marquee-text="View case →">
              <CropImage crop="work1:3" />
              <div className="gradient-overlay"></div>
              <div className="drop-card-title">COASTAL RUN</div>
            </a>
            {/* Card 5 */}
            <a href="#" className="drop-card" style={{ backgroundColor: 'var(--pink)' }} data-cursor-marquee-text="View case →">
              <CropImage crop="work2:0" />
              <div className="gradient-overlay"></div>
              <div className="drop-card-title">MIDNIGHT MARKET</div>
            </a>
          </div>

          {/* Badge */}
          <div className="drops-badge" aria-hidden="true">
            <svg viewBox="0 0 200 200" style={{ width: '100%', height: '100%', display: 'block' }}>
              <circle cx="100" cy="100" r="98" fill="#2563eb" />
              <path id="badgePath" d="M 100, 30 a 70,70 0 1,1 -0.01,0" fill="none" />
              <text fill="#f0f5fa" fontFamily="'Archivo', sans-serif" style={{ fontVariationSettings: "'wght' 800, 'wdth' 80" }} fontSize="24">
                <textPath href="#badgePath" textLength="436" lengthAdjust="spacing">
                  SOLARIA · SCROLL · SAVE · REPEAT ·
                </textPath>
              </text>
              <circle cx="100" cy="100" r="17" fill="none" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="100" y1="73" x2="100" y2="65" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="100" y1="127" x2="100" y2="135" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="73" y1="100" x2="65" y2="100" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="127" y1="100" x2="135" y2="100" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="81" y1="81" x2="75" y2="75" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="119" y1="119" x2="125" y2="125" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="119" y1="81" x2="125" y2="75" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
              <line x1="81" y1="119" x2="75" y2="125" stroke="#f0f5fa" strokeWidth="5" strokeLinecap="round" />
            </svg>
          </div>
        </div>
      </div>
    </section>
  );
}
