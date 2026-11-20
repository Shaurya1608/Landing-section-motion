'use client';

import React from 'react';
import CropImage from './CropImage';

export default function MeetTheFlockSection() {
  return (
    <section className="section-flock" id="flock" data-page-theme="dark">
      {/* Sticky Title */}
      <div className="sticky-title-wrap">
        <div className="sticky-title-content" data-scroll-reveal-group>
          {/* Stamp Sticker */}
          <div className="stamp-sticker" data-momentum-hover>
            <svg viewBox="0 0 228 136" style={{ width: '100%', height: 'auto', display: 'block' }}>
              <ellipse cx="114" cy="68" rx="104" ry="58" fill="#f0f5fa" stroke="#2563eb" strokeWidth="10" />
              <text x="114" y="78" textAnchor="middle" fontFamily="'Yellowtail', cursive" fontSize="54" fill="#2563eb" transform="rotate(-8 114 68)">
                Solaria
              </text>
            </svg>
          </div>

          <p className="eyebrow-m" data-scroll-reveal="lines">The people behind the frames</p>
          <h2
            className="team-headline"
            data-scroll-reveal="chars"
            data-font-weight-hover
            data-rest="700"
            data-near="200"
            data-radius="400"
          >
            <span
              className="alt-serif"
              data-font-weight-hover
              data-rest="300"
              data-near="800"
              data-radius="400"
            >
              MEET{' '}
            </span>
            THE{' '}
            <span
              className="alt-serif"
              data-font-weight-hover
              data-rest="300"
              data-near="800"
              data-radius="400"
            >
              FLOCK
            </span>
          </h2>
          <p className="paragraph" data-scroll-reveal="lines">
            Twelve makers, one group chat. We shoot, cut and animate before the espresso goes cold.
          </p>
        </div>
      </div>

      {/* Photo Layer */}
      <div className="photo-layer">
        {/* Left 1: Noor */}
        <div
          className="team-photo-card"
          data-index="0"
          data-speed="1"
          data-momentum-hover
          style={{ left: '2.5vw', top: '3%', width: '14rem', transform: 'rotate(-4deg)' }}
        >
          <CropImage crop="team1:0" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(-7deg)' }}>Noor</span>
        </div>
        {/* Left 2: ON SET */}
        <div
          className="team-photo-card"
          data-index="1"
          data-speed="0.6"
          data-momentum-hover
          style={{ left: '21vw', top: '19%', width: '11rem', transform: 'rotate(3deg)' }}
        >
          <CropImage crop="bts:0" />
          <span className="caption-tag">ON SET</span>
        </div>
        {/* Left 3: Sem */}
        <div
          className="team-photo-card"
          data-index="2"
          data-speed="1.3"
          data-momentum-hover
          style={{ left: '3vw', top: '33%', width: '13rem', transform: 'rotate(5deg)' }}
        >
          <CropImage crop="team1:1" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(4deg)' }}>Sem</span>
        </div>
        {/* Left 4: Mila */}
        <div
          className="team-photo-card"
          data-index="3"
          data-speed="0.8"
          data-momentum-hover
          style={{ left: '23vw', top: '49%', width: '13.5rem', transform: 'rotate(-3deg)' }}
        >
          <CropImage crop="team2:3" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(-5deg)' }}>Mila</span>
        </div>
        {/* Left 5: DINNER, IN 9:16 */}
        <div
          className="team-photo-card"
          data-index="4"
          data-speed="1.15"
          data-momentum-hover
          style={{ left: '2vw', top: '64%', width: '11.5rem', transform: 'rotate(-6deg)' }}
        >
          <CropImage crop="bts:2" />
          <span className="caption-tag">DINNER, IN 9:16</span>
        </div>
        {/* Left 6: Daan */}
        <div
          className="team-photo-card"
          data-index="5"
          data-speed="0.7"
          data-momentum-hover
          style={{ left: '20vw', top: '79%', width: '14rem', transform: 'rotate(4deg)' }}
        >
          <CropImage crop="team1:2" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(6deg)' }}>Daan</span>
        </div>

        {/* Right 1: Lotte */}
        <div
          className="team-photo-card"
          data-index="6"
          data-speed="0.75"
          data-momentum-hover
          style={{ right: '3vw', top: '2%', width: '13.5rem', transform: 'rotate(4deg)' }}
        >
          <CropImage crop="team2:0" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(5deg)' }}>Lotte</span>
        </div>
        {/* Right 2: TAKE ONE */}
        <div
          className="team-photo-card"
          data-index="7"
          data-speed="1.25"
          data-momentum-hover
          style={{ right: '22vw', top: '17%', width: '11rem', transform: 'rotate(-5deg)' }}
        >
          <CropImage crop="bts:1" />
          <span className="caption-tag">TAKE ONE</span>
        </div>
        {/* Right 3: Jules */}
        <div
          className="team-photo-card"
          data-index="8"
          data-speed="0.9"
          data-momentum-hover
          style={{ right: '2.5vw', top: '32%', width: '14rem', transform: 'rotate(-3deg)' }}
        >
          <CropImage crop="team2:1" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(-6deg)' }}>Jules</span>
        </div>
        {/* Right 4: Yara */}
        <div
          className="team-photo-card"
          data-index="9"
          data-speed="1.4"
          data-momentum-hover
          style={{ right: '23vw', top: '48%', width: '13rem', transform: 'rotate(5deg)' }}
        >
          <CropImage crop="team1:3" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(4deg)' }}>Yara</span>
        </div>
        {/* Right 5: GOLDEN HOUR */}
        <div
          className="team-photo-card"
          data-index="10"
          data-speed="0.65"
          data-momentum-hover
          style={{ right: '3vw', top: '63%', width: '11.5rem', transform: 'rotate(6deg)' }}
        >
          <CropImage crop="bts:3" />
          <span className="caption-tag">GOLDEN HOUR</span>
        </div>
        {/* Right 6: Kenji */}
        <div
          className="team-photo-card"
          data-index="11"
          data-speed="1.05"
          data-momentum-hover
          style={{ right: '20vw', top: '78%', width: '14rem', transform: 'rotate(-4deg)' }}
        >
          <CropImage crop="team2:2" />
          <span className="name-sticker" style={{ transform: 'translateX(-50%) rotate(-4deg)' }}>Kenji</span>
        </div>
      </div>
    </section>
  );
}
