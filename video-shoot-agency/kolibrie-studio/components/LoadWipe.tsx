'use client';

import React from 'react';

export default function LoadWipe() {
  return (
    <div className="load-wipe-overlay" aria-hidden="true">
      <svg className="load-wipe-svg" viewBox="0 0 1000 1000" preserveAspectRatio="none">
        <path
          className="load-wipe-path"
          d="M43 259C296 11.5688 994 -3 922.994 498.259C851.988 999.517 281.229 1004.28 123 767C-35.2287 529.721 179 259 472 259C765 259 792 498.259 659 654C526 809.741 319 755 285 669.001C251 583.001 299 452 496 452C693 452 876.073 639.171 935 937.001"
          fill="none"
          stroke="#2563eb"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="0"
        />
      </svg>
    </div>
  );
}
