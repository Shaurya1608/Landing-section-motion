'use client';

import React from 'react';
import { ASSETS } from './constants';

function ManifestoWord({ word, isGrey = false }: { word: string; isGrey?: boolean }) {
  return (
    <span className="manifesto-word">
      {word.split('').map((char, i) => (
        <span
          key={i}
          className={`manifesto-char ${isGrey ? 'grey' : ''}`}
          data-char-idx={i}
        >
          {char}
        </span>
      ))}
    </span>
  );
}

export default function ManifestoSection() {
  return (
    <section id="manifesto">
      <div className="manifesto-stage">
        <div className="manifesto-track" id="manifestoTrack">
          {/* 1. Intro block */}
          <div className="intro-block" data-reveal="track">
            <span
              className="small-badge"
              style={{
                top: '-0.95em',
                left: '0',
                backgroundColor: 'var(--peach)',
                ['--rest-rot' as any]: '-6deg',
              }}
              data-reveal="badge"
            >
              creative studio
            </span>
            <span
              className="small-badge"
              style={{
                top: '-1.1em',
                left: '3.4em',
                backgroundColor: 'var(--sand)',
                ['--rest-rot' as any]: '-4deg',
              }}
              data-reveal="badge"
            >
              est. twenty twenty-four
            </span>

            <div className="intro-row">
              <ManifestoWord word="Directing" isGrey />
              &nbsp;
              <ManifestoWord word="cinema" />
            </div>
            <div className="intro-row">
              <ManifestoWord word="that" />
              &nbsp;
              <ManifestoWord word="shapes" />
              &nbsp;
              <ManifestoWord word="culture." isGrey />
            </div>

            <span
              className="small-badge"
              style={{
                bottom: '-1em',
                left: '0.6em',
                backgroundColor: 'var(--ice)',
                ['--rest-rot' as any]: '4deg',
              }}
              data-reveal="badge"
            >
              global atelier
            </span>
          </div>

          {/* 2. Conch / Prism */}
          <span
            className="trinket-obj trinket-conch"
            style={{
              backgroundImage: `url(${ASSETS.sticker_sheet_700})`,
              ['--rest-rot' as any]: '-12deg',
            }}
            data-reveal="trinket"
          />

          {/* 3. Crafting */}
          <ManifestoWord word="Crafting" isGrey />

          {/* 4. Vertical badge stack */}
          <div className="vertical-badge-stack">
            <div className="badge-with-dot">
              <span
                className="badge-label"
                style={{
                  backgroundColor: 'var(--peach)',
                  ['--rest-rot' as any]: '-8deg',
                }}
                data-reveal="badge"
              >
                visual
              </span>
              <span className="badge-dot" />
            </div>
            <span
              className="badge-label"
              style={{
                backgroundColor: 'var(--lavender)',
                fontSize: '0.32em',
                ['--rest-rot' as any]: '6deg',
              }}
              data-reveal="badge"
            >
              and immersive
            </span>
          </div>

          {/* 5. cinematic worlds. */}
          <ManifestoWord word="cinematic" isGrey />
          <ManifestoWord word="worlds." />

          {/* 6. Sparkle & Pearl */}
          <span className="sparkle-icon" data-reveal="sparkle">
            <svg viewBox="0 0 20 20">
              <path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z" />
            </svg>
          </span>
          <span
            className="trinket-obj trinket-pearl"
            style={{
              backgroundImage: `url(${ASSETS.sticker_sheet_700})`,
              ['--rest-rot' as any]: '0deg',
            }}
            data-reveal="trinket"
          />

          {/* 7. The studio – is a */}
          <ManifestoWord word="The" />
          <ManifestoWord word="studio" />
          <ManifestoWord word="–" isGrey />
          <ManifestoWord word="is" isGrey />
          <ManifestoWord word="a" isGrey />

          {/* 8. Badge creative, Conch, Pearl, Sparkle, Badge collective */}
          <span
            className="badge-label"
            style={{
              backgroundColor: 'var(--peach)',
              ['--rest-rot' as any]: '-8deg',
            }}
            data-reveal="badge"
          >
            creative
          </span>
          <span
            className="trinket-obj trinket-conch"
            style={{
              backgroundImage: `url(${ASSETS.sticker_sheet_700})`,
              width: '1.05em',
              height: '1.05em',
              ['--rest-rot' as any]: '10deg',
            }}
            data-reveal="trinket"
          />
          <span
            className="trinket-obj trinket-pearl"
            style={{
              backgroundImage: `url(${ASSETS.sticker_sheet_700})`,
              width: '0.5em',
              height: '0.5em',
              ['--rest-rot' as any]: '0deg',
            }}
            data-reveal="trinket"
          />
          <span className="sparkle-icon" data-reveal="sparkle">
            <svg viewBox="0 0 20 20">
              <path d="M10 0c.8 5.6 3.6 8.6 10 10-6.4 1.4-9.2 4.4-10 10-.8-5.6-3.6-8.6-10-10 6.4-1.4 9.2-4.4 10-10z" />
            </svg>
          </span>
          <span
            className="badge-label"
            style={{
              backgroundColor: 'var(--lavender)',
              ['--rest-rot' as any]: '3deg',
            }}
            data-reveal="badge"
          >
            collective
          </span>

          {/* 9. and a, visionary, capsule */}
          <ManifestoWord word="and" isGrey />
          <ManifestoWord word="a" isGrey />
          <span
            className="badge-label"
            style={{
              backgroundColor: 'var(--sand)',
              ['--rest-rot' as any]: '-10deg',
            }}
            data-reveal="badge"
          >
            visionary
          </span>
          <span
            className="trinket-obj trinket-capsule"
            style={{
              backgroundImage: `url(${ASSETS.sticker_sheet_700})`,
              ['--rest-rot' as any]: '-8deg',
            }}
            data-reveal="trinket"
          />

          {/* 10. atelier that brings brands... */}
          <ManifestoWord word="space" />
          <ManifestoWord word="that" />
          <ManifestoWord word="brings" />
          <ManifestoWord word="brands," />
          <ManifestoWord word="artists," />
          <ManifestoWord word="and" isGrey />
          <ManifestoWord word="stories" />
          <ManifestoWord word="to" isGrey />
          <ManifestoWord word="life" isGrey />
          <ManifestoWord word="through" isGrey />
          <ManifestoWord word="film," />
          <ManifestoWord word="design," />
          <ManifestoWord word="and" isGrey />
          <ManifestoWord word="technology." />

          {/* 11. Spacer */}
          <span style={{ display: 'inline-block', width: '30vw', flexShrink: 0 }} />
        </div>
      </div>
    </section>
  );
}
