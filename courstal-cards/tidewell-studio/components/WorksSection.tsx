'use client';

import React from 'react';

export interface Project {
  id: string;
  num: string;
  title: string;
  subtitle: string;
  client: string;
  year: string;
  aspect: string;
  tags: string[];
  image: string;
  synopsis: string;
}

export const PROJECTS: Project[] = [
  {
    id: 'aether',
    num: '01',
    title: 'AETHER: The Silent Chronicles',
    subtitle: 'Cinematic 35mm Brand Direction & Film',
    client: 'Aether Mobility / Zurich',
    year: '2026',
    aspect: '2.39:1 Cinemascope',
    tags: ['Direction', '35mm Film', 'Spatial Audio'],
    image: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&q=85&fit=crop',
    synopsis: 'An atmospheric four-chapter cinematic film capturing the intersection of autonomous architecture and human serenity in the Swiss Alps.',
  },
  {
    id: 'solstice',
    num: '02',
    title: 'SOLSTICE 04: Architectural Memory',
    subtitle: '3D Simulation & Spatial Exhibition',
    client: 'Venice Biennale of Architecture',
    year: '2025',
    aspect: '16:9 4K Master',
    tags: ['Unreal Engine 5', 'CGI Worlds', 'Sound Design'],
    image: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1400&q=85&fit=crop',
    synopsis: 'Sculptural concrete monoliths suspended in shifting dawn light, exploring memory and permanence through real-time raytraced physics.',
  },
  {
    id: 'vanguard',
    num: '03',
    title: 'VANGUARD: Optical Resonance',
    subtitle: 'Avant-Garde Synthesizer Launch & Identity',
    client: 'Vanguard Instruments / Berlin',
    year: '2025',
    aspect: '2.35:1 Anamorphic',
    tags: ['Creative Direction', 'Macro Optics', 'Score'],
    image: 'https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=1400&q=85&fit=crop',
    synopsis: 'Macro optical lens flares, dispersion prisms, and tactile analog knobs choreographed to a custom modular synthesizer score.',
  },
  {
    id: 'lumiere',
    num: '04',
    title: 'LUMIÈRE ATELIER: Pure Contrast',
    subtitle: 'Haute Couture Motion & Spatial Installation',
    client: 'Lumière Paris / Fashion Week',
    year: '2024',
    aspect: '4:3 35mm Analog',
    tags: ['Editorial Film', 'Direction', 'Color Grading'],
    image: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1400&q=85&fit=crop',
    synopsis: 'High-contrast black-and-amber portraiture following draped raw silk through kinetic wind tunnels in an industrial Parisian foundry.',
  },
];

export default function WorksSection() {
  return (
    <section id="works" className="works-section">
      <div className="works-stage" id="worksStage">
        {/* Sticky Header HUD */}
        <div className="works-hud">
          <div className="hud-badge">
            <span className="hud-dot" />
            <span>SELECTED WORKS — 2024 / 2026</span>
          </div>
          <div className="hud-counter" id="worksCounter">
            <span className="counter-current">01</span>
            <span className="counter-sep">/</span>
            <span className="counter-total">04</span>
          </div>
          <div className="hud-waveform" aria-hidden="true">
            <span className="wave-bar" style={{ animationDelay: '0.1s' }} />
            <span className="wave-bar" style={{ animationDelay: '0.3s' }} />
            <span className="wave-bar" style={{ animationDelay: '0.15s' }} />
            <span className="wave-bar" style={{ animationDelay: '0.4s' }} />
            <span className="wave-bar" style={{ animationDelay: '0.2s' }} />
          </div>
        </div>

        {/* 3D Curved Film Carousel Track */}
        <div className="works-carousel-track" id="worksTrack">
          {PROJECTS.map((proj, idx) => (
            <article
              key={proj.id}
              className={`works-card ${idx === 0 ? 'active' : ''}`}
              data-project-idx={idx}
              id={`workCard-${idx}`}
            >
              <div className="works-card-inner">
                {/* Visual Media Poster */}
                <div
                  className="card-media"
                  style={{ backgroundImage: `url(${proj.image})` }}
                >
                  <div className="card-media-overlay" />
                  <div className="card-aspect-badge">{proj.aspect}</div>
                  <div className="card-play-pill">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                      <path d="M8 5v14l11-7z" />
                    </svg>
                    <span>View Production</span>
                  </div>
                </div>

                {/* Info Panel */}
                <div className="card-content">
                  <div className="card-meta">
                    <span className="card-num">{proj.num}</span>
                    <span className="card-client">{proj.client}</span>
                    <span className="card-year">{proj.year}</span>
                  </div>
                  <h3 className="card-title">{proj.title}</h3>
                  <p className="card-subtitle">{proj.subtitle}</p>
                  <p className="card-synopsis">{proj.synopsis}</p>
                  <div className="card-tags">
                    {proj.tags.map((tag) => (
                      <span key={tag} className="tag-pill">
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </article>
          ))}
        </div>

        {/* Progress Bar Track */}
        <div className="works-progress-bar">
          <div className="progress-fill" id="worksProgressFill" />
        </div>
      </div>
    </section>
  );
}
