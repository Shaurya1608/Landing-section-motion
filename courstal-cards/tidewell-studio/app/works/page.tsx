'use client';

import React, { useState } from 'react';
import SiteNav from '@/components/SiteNav';
import { PROJECTS } from '@/components/WorksSection';
import Link from 'next/link';

const ALL_PROJECTS = [
  ...PROJECTS,
  {
    id: 'chronos',
    num: '05',
    title: 'CHRONOS: Kinetic Horizon',
    subtitle: 'Experimental High-Speed Camera R&D',
    client: 'Chronos Optics / Tokyo',
    year: '2024',
    aspect: '2.40:1 Cinemascope',
    tags: ['Phantom Flex4K', '1000fps', 'Fluid Dynamics'],
    image: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=1400&q=85&fit=crop',
    synopsis: 'Super-slow-motion droplets of volcanic ink colliding in a micro-gravity chamber, captured at 1000fps on vintage Cooke glass.',
  },
  {
    id: 'meridian',
    num: '06',
    title: 'MERIDIAN: Sound of Monoliths',
    subtitle: 'Spatial Acoustic Installation & Identity',
    client: 'Guggenheim Museum / Bilbao',
    year: '2024',
    aspect: '16:9 DCI 4K',
    tags: ['Spatial Audio', 'Exhibition Design', 'Analog Score'],
    image: 'https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?w=1400&q=85&fit=crop',
    synopsis: 'Twelve tuned acoustic bronze plates suspended in resonant gallery spaces, vibrating in harmony with atmospheric barometric shifts.',
  },
];

const FILTERS = ['All', 'Direction', 'CGI & Worlds', 'Spatial Audio', 'Identity'];

export default function WorksPage() {
  const [activeFilter, setActiveFilter] = useState('All');
  const [activeModalProject, setActiveModalProject] = useState<typeof ALL_PROJECTS[0] | null>(null);

  const filtered = ALL_PROJECTS.filter((p) => {
    if (activeFilter === 'All') return true;
    if (activeFilter === 'Direction') return p.tags.some((t) => t.includes('Direction') || t.includes('Film'));
    if (activeFilter === 'CGI & Worlds') return p.tags.some((t) => t.includes('CGI') || t.includes('Unreal') || t.includes('Fluid'));
    if (activeFilter === 'Spatial Audio') return p.tags.some((t) => t.includes('Audio') || t.includes('Sound') || t.includes('Score'));
    if (activeFilter === 'Identity') return p.tags.some((t) => t.includes('Identity') || t.includes('Creative'));
    return true;
  });

  return (
    <main className="dedicated-page">
      <SiteNav />

      <section className="dedicated-hero">
        <div className="page-container">
          <div className="dedicated-tag">
            <span className="tag-dot" />
            <span>ARCHIVE OF MOTION & DIRECTION // 2024–2026</span>
          </div>
          <h1 className="dedicated-title">
            Selected Works & <span className="title-serif">Cinematic Productions</span>
          </h1>
          <p className="dedicated-desc">
            Explore our body of directed films, spatial simulations, and bespoke brand artifacts. Every production is built on large-format optics, physical choreography, and custom sound architecture.
          </p>

          {/* Filter Bar */}
          <div className="filter-bar">
            {FILTERS.map((f) => (
              <button
                key={f}
                type="button"
                className={`filter-btn ${activeFilter === f ? 'active' : ''}`}
                onClick={() => setActiveFilter(f)}
              >
                {f}
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Projects Grid */}
      <section className="projects-grid-section">
        <div className="page-container">
          <div className="archive-grid">
            {filtered.map((proj) => (
              <article
                key={proj.id}
                className="archive-card"
                onClick={() => setActiveModalProject(proj)}
              >
                <div
                  className="archive-card-image"
                  style={{ backgroundImage: `url(${proj.image})` }}
                >
                  <div className="archive-card-aspect">{proj.aspect}</div>
                  <div className="archive-hover-prompt">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                      <path d="M8 5v14l11-7z" />
                    </svg>
                    <span>View Case</span>
                  </div>
                </div>

                <div className="archive-card-info">
                  <div className="archive-meta">
                    <span className="archive-num">{proj.num}</span>
                    <span className="archive-client">{proj.client}</span>
                    <span className="archive-year">{proj.year}</span>
                  </div>
                  <h2 className="archive-title">{proj.title}</h2>
                  <p className="archive-subtitle">{proj.subtitle}</p>
                  <div className="archive-tags">
                    {proj.tags.map((t) => (
                      <span key={t} className="archive-tag-pill">
                        {t}
                      </span>
                    ))}
                  </div>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Project Detail Drawer Modal */}
      {activeModalProject && (
        <div className="project-modal-backdrop" onClick={() => setActiveModalProject(null)}>
          <div className="project-modal-card" onClick={(e) => e.stopPropagation()}>
            <button
              type="button"
              className="modal-close-btn"
              onClick={() => setActiveModalProject(null)}
              aria-label="Close modal"
            >
              ✕
            </button>
            <div
              className="modal-image"
              style={{ backgroundImage: `url(${activeModalProject.image})` }}
            >
              <div className="modal-aspect">{activeModalProject.aspect}</div>
            </div>
            <div className="modal-body">
              <div className="modal-meta">
                <span className="modal-num">{activeModalProject.num}</span>
                <span className="modal-client">{activeModalProject.client}</span>
                <span className="modal-year">{activeModalProject.year}</span>
              </div>
              <h2 className="modal-title">{activeModalProject.title}</h2>
              <p className="modal-subtitle">{activeModalProject.subtitle}</p>
              <p className="modal-synopsis">{activeModalProject.synopsis}</p>
              <div className="modal-tags">
                {activeModalProject.tags.map((t) => (
                  <span key={t} className="tag-pill">
                    {t}
                  </span>
                ))}
              </div>
              <div className="modal-actions">
                <Link href="/#contact" className="modal-cta-btn">
                  Commission Similar Project →
                </Link>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
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
