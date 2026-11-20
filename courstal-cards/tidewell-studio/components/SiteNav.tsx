'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

interface SiteNavProps {
  onNavClick?: (target: 'home' | 'process' | 'product' | 'manifesto' | 'works' | 'services' | 'atelier' | 'contact') => void;
}

export default function SiteNav({ onNavClick }: SiteNavProps) {
  const pathname = usePathname();
  const isHome = pathname === '/';

  const handleLink = (e: React.MouseEvent, target: 'home' | 'process' | 'product' | 'manifesto' | 'works' | 'services' | 'atelier' | 'contact') => {
    if (isHome && onNavClick) {
      e.preventDefault();
      onNavClick(target);
    }
  };

  return (
    <header className="site-nav" role="banner">
      <Link
        href="/"
        className="nav-logo"
        id="navLogo"
        aria-label="KROMA Studio home"
        onClick={(e) => handleLink(e, 'home')}
      >
        <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="18" cy="18" r="16" stroke="currentColor" strokeWidth="2" />
          <circle cx="18" cy="18" r="7" fill="currentColor" />
          <path d="M18 2V8M18 28V34M2 18H8M28 18H34" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        </svg>
        <span>KROMA</span>
      </Link>

      <nav className="nav-links" aria-label="Main navigation">
        <Link
          href="/"
          className={`nav-link ${isHome ? 'active' : ''}`}
          onClick={(e) => handleLink(e, 'home')}
        >
          Home
        </Link>
        <Link
          href="/#works"
          className="nav-link"
          onClick={(e) => handleLink(e, 'works')}
        >
          Works
        </Link>
        <Link
          href="/#services"
          className="nav-link"
          onClick={(e) => handleLink(e, 'services')}
        >
          Services
        </Link>
        <Link
          href="/#atelier"
          className="nav-link"
          onClick={(e) => handleLink(e, 'atelier')}
        >
          Atelier
        </Link>
        <Link
          href="/#manifesto"
          className="nav-link"
          onClick={(e) => handleLink(e, 'manifesto')}
        >
          Manifesto
        </Link>
      </nav>

      <button
        className="nav-cta"
        id="navCta"
        type="button"
        aria-label="Book Studio"
        onClick={(e) => handleLink(e as any, 'contact')}
      >
        <span>Book Studio</span>
        <svg viewBox="0 0 16 16">
          <path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </button>
    </header>
  );
}
