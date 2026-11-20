import React from 'react';
import { ChevronDown } from 'lucide-react';

export const Navbar: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-transparent px-6 py-4 flex items-center justify-between">
      {/* Left Section: Sunburst Icon */}
      <div className="flex items-center">
        <svg 
          width="24" 
          height="24" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="white" 
          strokeWidth="2" 
          strokeLinecap="round" 
          strokeLinejoin="round"
        >
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2" />
          <path d="M12 20v2" />
          <path d="m4.93 4.93 1.41 1.41" />
          <path d="m17.66 17.66 1.41 1.41" />
          <path d="M2 12h2" />
          <path d="M20 12h2" />
          <path d="m6.34 17.66-1.41 1.41" />
          <path d="m19.07 4.93-1.41 1.41" />
        </svg>
      </div>

      {/* Center Section: Links (Hidden on mobile) */}
      <div className="hidden md:flex items-center gap-8 font-sans text-sm font-medium text-white/80">
        <a href="#products" className="flex items-center gap-1 hover:text-white transition-colors">
          Products <ChevronDown size={14} className="mt-[2px]" />
        </a>
        <a href="#customer-stories" className="hover:text-white transition-colors">
          Customer Stories
        </a>
        <a href="#resources" className="hover:text-white transition-colors">
          Resources
        </a>
        <a href="#pricing" className="hover:text-white transition-colors">
          Pricing
        </a>
      </div>

      {/* Right Section: Actions */}
      <div className="flex items-center gap-6">
        <a 
          href="#demo" 
          className="hidden sm:block font-sans text-sm font-medium text-white/80 hover:text-white transition-colors"
        >
          Book A Demo
        </a>
        <button className="bg-white text-black font-sans font-semibold px-5 py-2.5 rounded-full text-sm hover:bg-gray-100 transition-colors">
          Get Started
        </button>
      </div>
    </nav>
  );
};
