'use client';

import React from 'react';
import CropImage from './CropImage';

export default function HeroSection() {
  return (
    <section className="hero-section" data-cursor-cards>
      <video
        className="hero-video"
        muted
        loop
        playsInline
        preload="auto"
        aria-hidden="true"
        poster="https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261110_224241_f6feccd5-1c45-4d22-b369-f927916f9973.png&w=2048&q=85"
      >
        <source
          src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261110_231342_88260d66-aa30-4612-9157-d7f1b5a66d8c.mp4"
          type="video/mp4"
        />
      </video>

      {/* Cursor Card (behind text) */}
      <div className="hero-cursor-card" aria-hidden="true">
        <div className="media-layer">
          <CropImage crop="work2:1" className="on" />
          <CropImage crop="work1:0" />
          <CropImage crop="work2:3" />
          <CropImage crop="work1:1" />
          <CropImage crop="work2:2" />
          <CropImage crop="work1:2" />
          <CropImage crop="work2:0" />
          <CropImage crop="work1:3" />
        </div>
      </div>

      {/* Hero Content */}
      <div className="hero-content">
        <h1
          className="hero-headline"
          data-text-reveal="chars"
          data-font-weight-hover
          data-rest="700"
          data-near="200"
          data-radius="400"
        >
          STORIES THAT<br />
          GET{' '}
          <span
            className="alt-serif"
            data-font-weight-hover
            data-rest="300"
            data-near="800"
            data-radius="400"
          >
            SHARED
          </span>
        </h1>

        <a href="#drops" className="hero-link" data-draw-line="always">
          <span className="hero-link-text">See the reel</span>
          <span className="underline-box"></span>
          <span className="hero-arrow-box" aria-hidden="true">
            <span className="hero-arrow-inner">
              <svg viewBox="0 0 14 13">
                <path d="M12.94 5.7 9.95 8 6.9 10.37l.84 1.86V0h-2.55v12.23l.85-1.86L3 8 0 5.7V9.05l6.47 4.95 6.47-4.95z" />
              </svg>
              <svg viewBox="0 0 14 13" className="clone">
                <path d="M12.94 5.7 9.95 8 6.9 10.37l.84 1.86V0h-2.55v12.23l.85-1.86L3 8 0 5.7V9.05l6.47 4.95 6.47-4.95z" />
              </svg>
            </span>
          </span>
        </a>
      </div>

      {/* Client Marquee */}
      <div className="marquee-outer" aria-hidden="true">
        <div className="marquee-scroll-wrapper">
          <div className="marquee-track">
            <div className="marquee-collection">
              {/* 1. Asterisk */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#2563eb" strokeWidth="12" strokeLinecap="round">
                  <line x1="50" y1="15" x2="50" y2="85" />
                  <line x1="19.7" y1="32.5" x2="80.3" y2="67.5" />
                  <line x1="19.7" y1="67.5" x2="80.3" y2="32.5" />
                </svg>
              </div>
              {/* 2. Two capsule D shapes */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="#2563eb">
                  <path d="M18 25 h16 a25 25 0 0 1 0 50 h-16 z M54 25 h16 a25 25 0 0 1 0 50 h-16 z" />
                </svg>
              </div>
              {/* 3. Three wavy lines */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#2563eb" strokeWidth="8" strokeLinecap="round">
                  <path d="M15 32 Q 32.5 22 50 32 T 85 32" />
                  <path d="M15 50 Q 32.5 40 50 50 T 85 50" />
                  <path d="M15 68 Q 32.5 58 50 68 T 85 68" />
                </svg>
              </div>
              {/* 4. Four diamonds */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="#2563eb">
                  <polygon points="50,15 62,30 50,45 38,30" />
                  <polygon points="50,55 62,70 50,85 38,70" />
                  <polygon points="28,35 40,50 28,65 16,50" />
                  <polygon points="72,35 84,50 72,65 60,50" />
                </svg>
              </div>
              {/* 5. Half sun over 3 bars */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="#2563eb" stroke="#2563eb">
                  <path d="M25 45 A 25 25 0 0 1 75 45 Z" stroke="none" />
                  <line x1="25" y1="56" x2="75" y2="56" strokeWidth="6" strokeLinecap="round" />
                  <line x1="25" y1="68" x2="75" y2="68" strokeWidth="6" strokeLinecap="round" />
                  <line x1="25" y1="80" x2="75" y2="80" strokeWidth="6" strokeLinecap="round" />
                </svg>
              </div>
              {/* 6. Two arches */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#2563eb" strokeWidth="10" strokeLinecap="round">
                  <path d="M18 80 V 45 A 16 16 0 0 1 50 45 V 80" />
                  <path d="M50 80 V 45 A 16 16 0 0 1 82 45 V 80" />
                </svg>
              </div>
              {/* 7. Four-point sparkle */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="#2563eb">
                  <path d="M50 12 Q 50 50 12 50 Q 50 50 50 88 Q 50 50 88 50 Q 50 50 50 12 Z" />
                </svg>
              </div>
              {/* 8. Circle with cross */}
              <div className="marquee-item">
                <svg viewBox="0 0 100 100" fill="none" stroke="#2563eb" strokeWidth="8" strokeLinecap="round">
                  <circle cx="50" cy="50" r="35" />
                  <line x1="50" y1="25" x2="50" y2="75" />
                  <line x1="25" y1="50" x2="75" y2="50" />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
