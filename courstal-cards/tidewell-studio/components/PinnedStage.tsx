'use client';

import React from 'react';
import { ASSETS, CARDS_DATA } from './constants';

export default function PinnedStage() {
  return (
    <div className="pinned-stage" id="pinnedStage">
      {/* PROCESS BLOCK */}
      <div className="process-block" id="processBlock">
        <h2 className="process-headline" id="processHeadline">
          <span className="line line1">
            <span className="word bold">From</span> <span className="word">concept</span>{' '}
            <span
              className="process-chip"
              aria-hidden="true"
              style={{ backgroundImage: `url(${ASSETS.process_chip})` }}
            />{' '}
            <span className="word bold">to</span> <span className="word">screen</span>
          </span>
          <br />
          <span className="line line2">
            <span className="word">crafted</span> <span className="word bold">through</span>{' '}
            <span className="word">pure</span> <span className="word">direction</span>
          </span>
        </h2>
        <p className="process-subline" id="processSubline">
          Partnering with visionary brands to direct iconic films, identities, and visual culture.
        </p>
        <div className="process-btn-wrap">
          <button className="process-btn" id="processBtn" type="button">
            <span>Explore Portfolio</span>
            <svg viewBox="0 0 16 16">
              <path
                d="M3 8h10M9 4l4 4-4 4"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>

      {/* CARDS LAYER (12 cards) */}
      <div className="cards-layer" id="cardsLayer">
        {CARDS_DATA.map((card, idx) => (
          <div
            key={idx}
            className="art-card"
            data-card={idx}
            style={{
              backgroundImage: `url(${card.image})`,
              backgroundPosition: card.pos,
            }}
          />
        ))}
      </div>

      {/* SKY / VIEWPORT SHOWCASE PANEL */}
      <div className="sky-panel" id="skyPanel">
        <div
          className="sky-plate"
          id="skyPlate"
          style={{ backgroundImage: `url(${ASSETS.sky_plate})` }}
        />
        <video
          className="sky-video"
          id="skyVideo"
          src={ASSETS.sky_video}
          muted
          loop
          playsInline
          preload="auto"
        />
        <div className="camera-wrap" id="cameraWrap">
          <div className="camera-inner" id="cameraInner">
            <div
              className="camera-sprite"
              id="cameraSprite"
              style={{ backgroundImage: `url(${ASSETS.camera_1400})` }}
            />
          </div>
        </div>

        <div className="sky-words-tl" id="skyWordsTL">
          <span className="sky-word grey">Not</span> <span className="sky-word grey">just</span>{' '}
          <span className="sky-word">frames</span>
        </div>
        <div className="sky-words-br" id="skyWordsBR">
          <span className="sky-word grey">Real</span> <span className="sky-word">stories</span>{' '}
          <span className="sky-word grey">that</span> <span className="sky-word">move</span>
        </div>
      </div>

      {/* BLACKOUT LAYER */}
      <div className="blackout-layer" id="blackoutLayer" />
    </div>
  );
}
