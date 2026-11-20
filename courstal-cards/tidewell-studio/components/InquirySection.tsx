'use client';

import React, { useState } from 'react';

const SCOPES = [
  'Film Direction & Cinema',
  'World-Building & CGI',
  'Spatial Sound & Score',
  'Complete Brand System',
  'Special Exhibition Pass',
];

export default function InquirySection() {
  const [selectedScopes, setSelectedScopes] = useState<string[]>([
    'Film Direction & Cinema',
  ]);
  const [budgetIdx, setBudgetIdx] = useState<number>(1);
  const [submitted, setSubmitted] = useState<boolean>(false);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    timeline: 'Q2 / Q3 2026',
    brief: '',
  });

  const budgetTiers = [
    '$35,000 — $65,000 (Focused Production)',
    '$65,000 — $150,000 (Complete Film / Identity)',
    '$150,000+ (Global Campaign / Spatial Installation)',
  ];

  const toggleScope = (scope: string) => {
    if (selectedScopes.includes(scope)) {
      if (selectedScopes.length > 1) {
        setSelectedScopes(selectedScopes.filter((s) => s !== scope));
      }
    } else {
      setSelectedScopes([...selectedScopes, scope]);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({ name: '', email: '', timeline: 'Q2 / Q3 2026', brief: '' });
    }, 4000);
  };

  return (
    <section id="contact" className="inquiry-section">
      <div className="inquiry-stage">
        <div className="inquiry-card">
          <div className="inquiry-head">
            <div className="inquiry-badge">
              <span className="badge-spark" />
              <span>COMMISSION A PRODUCTION</span>
            </div>
            <h2 className="inquiry-title">
              Direct Your Next <span className="title-serif">Iconic Work</span>
            </h2>
            <p className="inquiry-subtitle">
              We accept a limited roster of 12 commissions annually to ensure relentless focus and uncompromised craft.
            </p>
          </div>

          <form onSubmit={handleSubmit} className="inquiry-form">
            {/* Scope Selection */}
            <div className="form-group">
              <label className="form-label">01 // SELECT PRODUCTION SCOPE</label>
              <div className="scope-chips">
                {SCOPES.map((scope) => {
                  const isSel = selectedScopes.includes(scope);
                  return (
                    <button
                      key={scope}
                      type="button"
                      className={`scope-pill ${isSel ? 'selected' : ''}`}
                      onClick={() => toggleScope(scope)}
                    >
                      <span className="pill-check">{isSel ? '✓' : '+'}</span>
                      <span>{scope}</span>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Budget Range Slider */}
            <div className="form-group">
              <div className="label-with-val">
                <label className="form-label">02 // ESTIMATED INVESTMENT TIER</label>
                <span className="budget-val">{budgetTiers[budgetIdx]}</span>
              </div>
              <input
                type="range"
                min="0"
                max="2"
                step="1"
                value={budgetIdx}
                onChange={(e) => setBudgetIdx(parseInt(e.target.value, 10))}
                className="budget-slider"
              />
              <div className="slider-ticks">
                <span>Core Film</span>
                <span>Full Production</span>
                <span>Global Campaign</span>
              </div>
            </div>

            {/* Input Details */}
            <div className="form-row-dual">
              <div className="form-field">
                <label className="field-label">NAME / ORGANIZATION</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Helena Vance / Aether Labs"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="text-input"
                />
              </div>
              <div className="form-field">
                <label className="field-label">DIRECT DISPATCH EMAIL</label>
                <input
                  type="email"
                  required
                  placeholder="helena@aetherlabs.com"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="text-input"
                />
              </div>
            </div>

            <div className="form-field">
              <label className="field-label">PROJECT BRIEF & ARTISTIC VISION</label>
              <textarea
                rows={3}
                required
                placeholder="Describe your narrative intent, target release date, and visual benchmarks..."
                value={formData.brief}
                onChange={(e) => setFormData({ ...formData, brief: e.target.value })}
                className="text-area"
              />
            </div>

            <div className="form-submit-row">
              <button
                type="submit"
                disabled={submitted}
                className={`dispatch-btn ${submitted ? 'sent' : ''}`}
              >
                <span>{submitted ? 'DISPATCH TRANSMITTED ✓' : 'TRANSMIT COMMISSION BRIEF →'}</span>
              </button>
              <div className="submit-note">
                Encrypted communication. Response within 24 business hours.
              </div>
            </div>
          </form>
        </div>

        {/* Studio Colophon & Footer */}
        <footer className="studio-colophon">
          <div className="colophon-top">
            <div className="colophon-brand">
              <span className="brand-dot" />
              <span className="brand-name">KROMA ATELIER</span>
              <span className="brand-tagline">PARIS • NEW YORK • TOKYO</span>
            </div>
            <button
              type="button"
              className="back-to-top"
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            >
              <span>RETURN TO APEX</span>
              <svg viewBox="0 0 16 16">
                <path d="M8 13V3M4 7l4-4 4 4" stroke="currentColor" strokeWidth="1.6" fill="none" />
              </svg>
            </button>
          </div>
          <div className="colophon-bottom">
            <span>© 2024–2026 KROMA MOTION ATELIER INC. ALL RIGHTS RESERVED.</span>
            <span>TYPESET IN INTER VARIABLE • DESIGNED FOR DIRECTORS & VISUAL PURISTS</span>
          </div>
        </footer>
      </div>
    </section>
  );
}
