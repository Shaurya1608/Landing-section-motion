'use client';

import React from 'react';

export default function Navbar() {
  return (
    <nav className="nav-bar" aria-label="Main navigation">
      <a href="#" className="nav-logo" aria-label="Solaria home">Solaria</a>
      
      <div className="nav-center">
        <a href="#flock" className="nav-link" data-draw-line>
          <span>About</span>
          <span className="underline-box"></span>
        </a>
        <a href="#drops" className="nav-link" data-draw-line>
          <span>Work</span>
          <span className="underline-box"></span>
        </a>
        <a href="#drops" className="nav-link" data-draw-line>
          <span>Services</span>
          <span className="underline-box"></span>
        </a>
      </div>

      <a href="#flock" className="nav-contact">
        <span className="nav-dot"></span>
        <span>Contact</span>
      </a>
    </nav>
  );
}
