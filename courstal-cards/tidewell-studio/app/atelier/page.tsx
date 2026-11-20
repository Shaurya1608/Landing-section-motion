'use client';

import React, { useState, useEffect } from 'react';
import SiteNav from '@/components/SiteNav';
import Link from 'next/link';

const GEAR_ITEMS = [
  { category: 'OPTICS & CAMERAS', items: ['ARRI Alexa 35 (4.6K Super 35)', 'ARRI Alexa Mini LF (Large Format)', 'Cooke Anamorphic /i Full Frame Primes', 'Cooke Speed Panchro Vintage Primes', 'Phantom Flex4K (1000fps High-Speed)'] },
  { category: 'LIGHTING & GRIP', items: ['ARRI SkyPanel S360-C & S60-C LED', 'Astera Titan & Helios Tubes', 'Koto 18KW HMI Daylight Fresnels', 'Chapman Leonard Hybrid Stage Crane', 'Motorized MoCo 6-Axis Motion Rig'] },
  { category: 'SOUND & SYNTHESIS', items: ['Custom 16-Panel Modular Eurorack Rig', 'Sequential Prophet-10 Analog Poly', 'Neumann U87 Ai & KM184 Stereo Pairs', 'Genelec 7.1.4 Dolby Atmos Reference', 'Sennheiser AMBEO VR Binaural Rig'] },
  { category: 'POST & GRADING', items: ['DaVinci Resolve Advanced Control Panel', 'Sony BVM-HX310 4K HDR Reference Master', 'Dual RTX 4090 Unreal 5.4 Render Nodes', '800TB Encrypted Fiber SAN Storage', 'DCP DCI Color Calibration Lab'] },
];

export default function AtelierPage() {
  const [parisTime, setParisTime] = useState('--:--:--');
  const [nyTime, setNyTime] = useState('--:--:--');
  const [tokyoTime, setTokyoTime] = useState('--:--:--');

  useEffect(() => {
    function tick() {
      const now = new Date();
      const getZone = (offsetHours: number) => {
        const utc = now.getTime() + now.getTimezoneOffset() * 60000;
        const d = new Date(utc + offsetHours * 3600000);
        return [
          String(d.getHours()).padStart(2, '0'),
          String(d.getMinutes()).padStart(2, '0'),
          String(d.getSeconds()).padStart(2, '0'),
        ].join(':');
      };
      setParisTime(getZone(1));
      setNyTime(getZone(-5));
      setTokyoTime(getZone(9));
    }
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  return (
    <main className="dedicated-page">
      <SiteNav />

      <section className="dedicated-hero">
        <div className="page-container">
          <div className="dedicated-tag">
            <span className="tag-dot" />
            <span>SOUNDSTAGES & APPARATUS</span>
          </div>
          <h1 className="dedicated-title">
            The Physical <span className="title-serif">Atelier & Equipment</span>
          </h1>
          <p className="dedicated-desc">
            Cinema is a physical medium. Across our studios in Paris, New York, and Tokyo, we house dedicated cyclorama stages, acoustic mixing rooms, and an exhaustive archive of vintage anamorphic and modern large-format optics.
          </p>

          <div className="hero-clocks-bar">
            <div className="clock-item">
              <span className="clock-city">PARIS</span>
              <span className="clock-digits">{parisTime}</span>
              <span className="clock-zone">CET (UTC+1)</span>
            </div>
            <div className="clock-divider" />
            <div className="clock-item">
              <span className="clock-city">NEW YORK</span>
              <span className="clock-digits">{nyTime}</span>
              <span className="clock-zone">EST (UTC-5)</span>
            </div>
            <div className="clock-divider" />
            <div className="clock-item">
              <span className="clock-city">TOKYO</span>
              <span className="clock-digits">{tokyoTime}</span>
              <span className="clock-zone">JST (UTC+9)</span>
            </div>
          </div>
        </div>
      </section>

      {/* Equipment Locker */}
      <section className="gear-section">
        <div className="page-container">
          <h2 className="section-subheading">PERMANENT PRODUCTION LOCKER</h2>
          <div className="gear-grid">
            {GEAR_ITEMS.map((cat) => (
              <div key={cat.category} className="gear-card">
                <h3 className="gear-cat-title">{cat.category}</h3>
                <ul className="gear-list">
                  {cat.items.map((item) => (
                    <li key={item} className="gear-item">
                      <span className="gear-bullet">▪</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer className="dedicated-footer">
        <div className="page-container">
          <div className="footer-row">
            <div>© 2024–2026 KROMA STUDIO INC.</div>
            <Link href="/" className="footer-link">
              ← Return to Main Scroll Experience
            </Link>
          </div>
        </div>
      </footer>
    </main>
  );
}
