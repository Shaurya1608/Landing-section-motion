'use client';

import React, { useState, useEffect } from 'react';

interface StudioLocation {
  city: string;
  zone: string;
  utcOffset: number; // in hours from UTC
  address: string;
  focus: string;
  image: string;
}

const LOCATIONS: StudioLocation[] = [
  {
    city: 'PARIS',
    zone: 'CET / UTC+1',
    utcOffset: 1,
    address: '14 Rue de Turenne, 3e Arrondissement',
    focus: 'Direction, Color Grading & Soundstage',
    image: 'https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=900&q=85&fit=crop',
  },
  {
    city: 'NEW YORK',
    zone: 'EST / UTC-5',
    utcOffset: -5,
    address: '88 Franklin Street, Tribeca',
    focus: 'Motion Design, Virtual Production & Executive Production',
    image: 'https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=900&q=85&fit=crop',
  },
  {
    city: 'TOKYO',
    zone: 'JST / UTC+9',
    utcOffset: 9,
    address: '6-10-1 Ginza, Chuo-ku',
    focus: 'Realtime Unreal Engine R&D & Spatial Audio Labs',
    image: 'https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=900&q=85&fit=crop',
  },
];

export default function AtelierSection() {
  const [times, setTimes] = useState<{ [city: string]: string }>({
    PARIS: '--:--:--',
    'NEW YORK': '--:--:--',
    TOKYO: '--:--:--',
  });

  useEffect(() => {
    function updateClocks() {
      const now = new Date();
      const updated: { [city: string]: string } = {};

      LOCATIONS.forEach((loc) => {
        const utcMs = now.getTime() + now.getTimezoneOffset() * 60000;
        const targetDate = new Date(utcMs + loc.utcOffset * 3600000);
        const hh = String(targetDate.getHours()).padStart(2, '0');
        const mm = String(targetDate.getMinutes()).padStart(2, '0');
        const ss = String(targetDate.getSeconds()).padStart(2, '0');
        updated[loc.city] = `${hh}:${mm}:${ss}`;
      });

      setTimes(updated);
    }

    updateClocks();
    const interval = setInterval(updateClocks, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <section id="atelier" className="atelier-section">
      <div className="atelier-stage">
        <div className="atelier-header">
          <div className="atelier-tag">
            <span className="atelier-dot" />
            <span>GLOBAL FOOTPRINT & PRODUCTION SPACES</span>
          </div>
          <h2 className="atelier-title">
            Three Soundstages. <span className="title-italic">One Unified Vision.</span>
          </h2>
          <p className="atelier-intro">
            Operating synchronously across time zones, KROMA links master cinematographers in Paris, motion engineers in New York, and real-time world-builders in Tokyo.
          </p>
        </div>

        {/* Global Studio Clocks Grid */}
        <div className="atelier-grid">
          {LOCATIONS.map((loc) => (
            <div key={loc.city} className="atelier-card">
              <div
                className="atelier-card-bg"
                style={{ backgroundImage: `url(${loc.image})` }}
              />
              <div className="atelier-card-overlay" />
              <div className="atelier-card-content">
                <div className="clock-row">
                  <div className="city-pill">
                    <span className="live-dot" />
                    <span>{loc.city}</span>
                  </div>
                  <div className="digital-clock" aria-label={`Current time in ${loc.city}`}>
                    {times[loc.city]}
                  </div>
                </div>

                <div className="location-info">
                  <div className="location-zone">{loc.zone}</div>
                  <div className="location-address">{loc.address}</div>
                  <div className="location-focus">{loc.focus}</div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Studio Tenets / Colophon */}
        <div className="atelier-tenets">
          <div className="tenet-col">
            <span className="tenet-num">01 // RESTRAINT</span>
            <p className="tenet-desc">
              Every cut, focal transition, and sonic layer must earn its place. We reject superfluous digital noise in favor of enduring weight and visual cadence.
            </p>
          </div>
          <div className="tenet-col">
            <span className="tenet-num">02 // SENSORY TRUTH</span>
            <p className="tenet-desc">
              Even when directing purely synthetic CGI environments, we simulate optical imperfection: anamorphic breathing, lens flare dispersion, and tactile grain.
            </p>
          </div>
          <div className="tenet-col">
            <span className="tenet-num">03 // SYNCHRONICITY</span>
            <p className="tenet-desc">
              Sound and vision are conceived simultaneously from the earliest treatment stage, never as an afterthought glued to locked picture.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
