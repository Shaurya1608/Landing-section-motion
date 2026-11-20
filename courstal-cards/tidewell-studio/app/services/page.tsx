'use client';

import React from 'react';
import SiteNav from '@/components/SiteNav';
import { SERVICES } from '@/components/ServicesSection';
import Link from 'next/link';

export default function ServicesPage() {
  return (
    <main className="dedicated-page">
      <SiteNav />

      <section className="dedicated-hero">
        <div className="page-container">
          <div className="dedicated-tag">
            <span className="tag-dot" />
            <span>DISCIPLINES & PRODUCTION PIPELINE</span>
          </div>
          <h1 className="dedicated-title">
            Crafting Sensation Across <span className="title-serif">Four Mediums</span>
          </h1>
          <p className="dedicated-desc">
            KROMA operates as a full-service creative direction and physical production atelier. We handle projects from blank sheet conceptual treatments through to final DCP color mastering and spatial Atmos delivery.
          </p>
        </div>
      </section>

      {/* Services Deep Dive */}
      <section className="services-deep-section">
        <div className="page-container">
          <div className="deep-services-stack">
            {SERVICES.map((srv) => (
              <div key={srv.num} className="deep-service-card">
                <div className="deep-card-header">
                  <span className="deep-num">{srv.num}</span>
                  <div className="deep-titles">
                    <h2 className="deep-title">{srv.title}</h2>
                    <p className="deep-headline">{srv.headline}</p>
                  </div>
                  <div className="deep-spec-badge">{srv.lensSpec}</div>
                </div>

                <p className="deep-desc">{srv.description}</p>

                <div className="deep-columns-grid">
                  <div className="deep-col">
                    <h3 className="col-heading">PRODUCTION PIPELINE</h3>
                    <ul className="spec-list">
                      {srv.pipeline.map((step) => (
                        <li key={step} className="spec-item">
                          <span className="step-arrow">→</span>
                          <span>{step}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="deep-col">
                    <h3 className="col-heading">CORE DELIVERABLES</h3>
                    <ul className="spec-list">
                      {srv.deliverables.map((item) => (
                        <li key={item} className="spec-item">
                          <span className="step-check">✓</span>
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="cta-banner">
            <div className="banner-text">
              <h3>Have a multi-disciplinary vision?</h3>
              <p>We combine direction, CGI simulation, and bespoke analog score into cohesive packages.</p>
            </div>
            <Link href="/#contact" className="banner-btn">
              Direct an Inquiry →
            </Link>
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
