'use client';

import React from 'react';
import { ASSETS } from './constants';

export default function HeroHeader() {
  return (
    <header className="hero-header">
      <div className="headline-wrap" role="heading" aria-level={1} aria-label="Vision in Motion">
        <div className="headline-inner" id="headlineInner">
          <div className="headline-words" id="headlineWords">
            {/* Populated dynamically in page.tsx */}
          </div>
          <div className="icon-layer" id="iconLayer">
            {/* 1. Camera / Lens */}
            <span className="pixel-icon" data-icon="lens">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
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
              </svg>
            </span>

            {/* 2. Film Reel / Clapper */}
            <span className="pixel-icon" data-icon="reel">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
                <rect x="1" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="2" y="1" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="4" y="1" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="5" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="6" y="1" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="7" y="1" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="1" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="2" y="2" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="3" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="4" y="2" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="5" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="6" y="2" width="1.02" height="1.02" fill="#CF6E4A" />
                <rect x="7" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="1" y="3" width="7" height="1.02" fill="#1D1815" />
                <rect x="1" y="4" width="7" height="3" fill="#E4A684" />
                <rect x="2" y="5" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="4" y="5" width="1.02" height="1.02" fill="#FFFFFF" />
                <rect x="6" y="5" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="1" y="7" width="7" height="1.02" fill="#1D1815" />
              </svg>
            </span>

            {/* 3. Studio Spotlight */}
            <span className="pixel-icon" data-icon="spotlight">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
                <rect x="4" y="0" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="1" width="3" height="1.02" fill="#1D1815" />
                <rect x="2" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="2" width="3" height="1.02" fill="#E5B876" />
                <rect x="6" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="1" y="3" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="2" y="3" width="5" height="1.02" fill="#FFFFFF" />
                <rect x="7" y="3" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="0" y="4" width="9" height="1.02" fill="#E5B876" />
                <rect x="1" y="5" width="7" height="1.02" fill="#E5B876" />
                <rect x="2" y="6" width="5" height="1.02" fill="#E5B876" />
                <rect x="3" y="7" width="3" height="1.02" fill="#E5B876" />
                <rect x="4" y="8" width="1.02" height="1.02" fill="#1D1815" />
              </svg>
            </span>

            {/* 4. Prism / Diamond */}
            <span className="pixel-icon" data-icon="prism">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
                <rect x="4" y="1" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="4" y="2" width="1.02" height="1.02" fill="#FFFFFF" />
                <rect x="5" y="2" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="2" y="3" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="3" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="4" y="3" width="1.02" height="1.02" fill="#FFFFFF" />
                <rect x="5" y="3" width="1.02" height="1.02" fill="#E4A684" />
                <rect x="6" y="3" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="1" y="4" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="2" y="4" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="3" y="4" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="4" y="4" width="1.02" height="1.02" fill="#FFFFFF" />
                <rect x="5" y="4" width="1.02" height="1.02" fill="#E4A684" />
                <rect x="6" y="4" width="1.02" height="1.02" fill="#E4A684" />
                <rect x="7" y="4" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="2" y="5" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="5" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="4" y="5" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="5" y="5" width="1.02" height="1.02" fill="#E4A684" />
                <rect x="6" y="5" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="3" y="6" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="4" y="6" width="1.02" height="1.02" fill="#DE9350" />
                <rect x="5" y="6" width="1.02" height="1.02" fill="#1D1815" />
                <rect x="4" y="7" width="1.02" height="1.02" fill="#1D1815" />
              </svg>
            </span>

            {/* 5. Director Viewfinder */}
            <span className="pixel-icon" data-icon="frame">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
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
              </svg>
            </span>

            {/* 6. Motion Waveform */}
            <span className="pixel-icon" data-icon="wave">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
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
              </svg>
            </span>

            {/* 7. Golden Spark */}
            <span className="pixel-icon" data-icon="spark">
              <svg viewBox="0 0 9 9" width="100%" height="100%" shapeRendering="crispEdges">
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
              </svg>
            </span>
          </div>
        </div>
      </div>
      <div
        className="plane-sprite"
        id="paperPlane"
        style={{ backgroundImage: `url(${ASSETS.sticker_plane})` }}
      />
    </header>
  );
}
