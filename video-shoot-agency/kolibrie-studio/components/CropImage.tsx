'use client';

import React from 'react';

const SHEETS: Record<string, { url: string; w: number; h: number; cells: [number, number, number, number][] }> = {
  work1: {
    url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_b0899b4d-5876-4c63-98d3-8608d8dbe790.png&w=2400&q=85',
    w: 2688,
    h: 1520,
    cells: [
      [0, 0, 1336, 752],
      [1352, 0, 1336, 752],
      [0, 768, 1336, 752],
      [1352, 768, 1336, 752]
    ]
  },
  work2: {
    url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_aee93a53-873f-470f-afb3-6395c22ab639.png&w=2400&q=85',
    w: 2688,
    h: 1520,
    cells: [
      [0, 0, 1335, 749],
      [1356, 0, 1332, 749],
      [0, 770, 1335, 750],
      [1356, 770, 1332, 750]
    ]
  },
  team1: {
    url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224239_be9bd6b1-debb-4a95-aadf-1a36e4d2f557.png&w=1600&q=85',
    w: 1744,
    h: 2336,
    cells: [
      [0, 0, 864, 1156],
      [881, 0, 863, 1156],
      [0, 1175, 864, 1161],
      [881, 1175, 863, 1161]
    ]
  },
  team2: {
    url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_bfc657e7-cbc1-43fb-a726-e8be5dd42302.png&w=1600&q=85',
    w: 1744,
    h: 2336,
    cells: [
      [0, 0, 864, 1159],
      [880, 0, 864, 1159],
      [0, 1176, 864, 1160],
      [880, 1176, 864, 1160]
    ]
  },
  bts: {
    url: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224238_bf8567fa-9d67-4f1e-b4e0-5662c0bf70e4.png&w=1600&q=85',
    w: 1744,
    h: 2336,
    cells: [
      [0, 0, 865, 1160],
      [881, 0, 863, 1160],
      [0, 1176, 865, 1160],
      [881, 1176, 863, 1160]
    ]
  }
};

interface CropImageProps {
  crop: string;
  className?: string;
  style?: React.CSSProperties;
}

export default function CropImage({ crop, className = '', style }: CropImageProps) {
  const [sheetKey, cellIdxStr] = crop.split(':');
  const sheet = SHEETS[sheetKey];
  if (!sheet) return null;

  const cellIdx = parseInt(cellIdxStr, 10);
  const [rawX, rawY, rawW, rawH] = sheet.cells[cellIdx];
  const insetX = rawX + 4;
  const insetY = rawY + 4;
  const insetW = rawW - 8;
  const insetH = rawH - 8;
  const ar = insetW / insetH;

  const widthPct = (sheet.w / insetW) * 100;
  const heightPct = (sheet.h / insetH) * 100;
  const leftPct = -(insetX / insetW) * 100;
  const topPct = -(insetY / insetH) * 100;

  return (
    <div className={`crop ${className}`} data-crop={crop} style={style}>
      <div className="cell" style={{ ['--ar' as any]: ar }}>
        <img
          src={sheet.url}
          alt=""
          loading="lazy"
          decoding="async"
          style={{
            width: `${widthPct}%`,
            height: `${heightPct}%`,
            left: `${leftPct}%`,
            top: `${topPct}%`,
          }}
        />
      </div>
    </div>
  );
}
