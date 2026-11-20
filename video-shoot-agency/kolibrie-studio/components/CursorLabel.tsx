'use client';

import React from 'react';

export default function CursorLabel() {
  return (
    <div className="cursor-label-wrapper" data-cursor-marquee-status="inactive" aria-hidden="true">
      <div className="cursor-label-card">
        <div className="cursor-label-track">
          <span className="cursor-label-text">View case →</span>
          <span className="cursor-label-text clone">View case →</span>
        </div>
      </div>
    </div>
  );
}
