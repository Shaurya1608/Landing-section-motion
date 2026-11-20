'use client';

import React from 'react';
import { 
  ArrowUpRight, Sparkle, Figma, Framer, Palette, 
  PenTool, Layers, Type, Aperture, Chrome, 
  Camera, Brush, Box, Wand2 
} from 'lucide-react';

const row1Icons = [Figma, Framer, Palette, PenTool, Layers, Type, Aperture, Chrome];
const row2Icons = [Camera, Brush, Box, Wand2, Figma, Framer, Type, Layers];

const IconWrapper = ({ Icon }: { Icon: React.ComponentType<any> }) => {
  return (
    <div className="liquid-glass h-14 w-14 md:h-16 md:w-16 rounded-xl flex items-center justify-center flex-shrink-0 text-white">
      <Icon className="h-6 w-6 md:h-7 md:w-7" strokeWidth={1.5} />
    </div>
  );
};

export const FeaturesSection = () => {
  return (
    <section className="relative w-full min-h-screen lg:h-screen bg-[#0a0a0a] text-white font-sans antialiased overflow-hidden flex flex-col justify-between px-4 sm:px-6 md:px-10 lg:px-14 py-6 sm:py-8 md:py-10 select-none">
      {/* Embedded CSS for styling custom layout overlays and animation marquees */}
      <style dangerouslySetInnerHTML={{ __html: `
        .liquid-glass {
          background: rgba(255, 255, 255, 0.01);
          background-blend-mode: luminosity;
          backdrop-filter: blur(4px);
          box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
          position: relative;
          overflow: hidden;
        }
        .liquid-glass::before {
          content: '';
          position: absolute;
          inset: 0;
          border-radius: inherit;
          padding: 1.4px;
          background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%, rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%, rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%);
          -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
          -webkit-mask-composite: xor;
          mask-composite: exclude;
          pointer-events: none;
        }

        @keyframes marquee-left { 
          from { transform: translateX(0); } 
          to { transform: translateX(-50%); } 
        }
        @keyframes marquee-right { 
          from { transform: translateX(-50%); } 
          to { transform: translateX(0); } 
        }
        .animate-marquee-left { 
          animation: marquee-left 22s linear infinite; 
        }
        .animate-marquee-right { 
          animation: marquee-right 26s linear infinite; 
        }

        .noise-overlay {
          position: relative;
        }
        .noise-overlay::after {
          content: '';
          position: absolute;
          inset: 0;
          pointer-events: none;
          opacity: 0.55;
          mix-blend-mode: soft-light;
          background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix type='matrix' values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
          background-size: 240px 240px;
          border-radius: inherit;
        }
      ` }} />

      {/* Top Header Row - Centered Layout */}
      <div className="flex flex-col items-center text-center max-w-3xl mx-auto gap-4 mb-8 md:mb-10 w-full">
        <h1 className="text-[28px] sm:text-3xl md:text-4xl lg:text-[44px] leading-[1.15] font-normal tracking-tight text-white">
          Hi, I'm Max Reed!
        </h1>
        <p className="text-sm md:text-[15px] leading-[1.6] text-white/60 max-w-2xl">
          A London-based independent creator shaping sharp visual systems, web-ready products, and story-first campaigns. With a decade of craft behind me, I help ideas move with focus and intention.
        </p>
        <div className="mt-2">
          <button className="liquid-glass rounded-full px-5 sm:px-6 py-2.5 sm:py-3 text-sm font-medium text-white transition-all duration-300 hover:bg-white/5 active:scale-95">
            Let's Team Up Today
          </button>
        </div>
      </div>

      {/* Grid Layout Container */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5 flex-grow w-full items-stretch">
        
        {/* Column 1: Background Card */}
        <div className="rounded-2xl bg-black relative overflow-hidden p-6 flex flex-col justify-between min-h-[380px] lg:h-full border border-white/5">
          {/* Background Video */}
          <video 
            src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260507_150203_44a5bd32-516a-47ce-a077-8acbf9aa8991.mp4" 
            autoPlay 
            loop 
            muted 
            playsInline 
            className="absolute inset-0 object-cover w-full h-full opacity-60 pointer-events-none"
          ></video>

          {/* Top Label */}
          <div className="flex items-center justify-center gap-2 relative z-10 w-full">
            <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
            <span className="uppercase tracking-[0.22em] text-[11px] text-white/70 font-semibold">BACKGROUND</span>
            <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
          </div>

          {/* Bottom Career Timeline */}
          <div className="grid grid-cols-[auto_auto_1fr_auto] items-center gap-x-3 gap-y-4 relative z-10 w-full text-xs md:text-sm text-white/90">
            {/* Row 1 */}
            <span className="font-semibold text-white/60 tabular-nums">2023-Now</span>
            <Sparkle className="h-3 w-3 text-white/60" strokeWidth={1.5} />
            <span className="font-medium">Freelance Creative</span>
            <span className="text-white/60 text-right">Solo Studio</span>

            {/* Row 2 */}
            <span className="font-semibold text-white/60 tabular-nums">2020-2023</span>
            <Sparkle className="h-3 w-3 text-white/60" strokeWidth={1.5} />
            <span className="font-medium">Head of Brand Design</span>
            <span className="text-white/60 text-right">Rove Studio</span>

            {/* Row 3 */}
            <span className="font-semibold text-white/60 tabular-nums">2017-2020</span>
            <Sparkle className="h-3 w-3 text-white/60" strokeWidth={1.5} />
            <span className="font-medium">Visual Stylist</span>
            <span className="text-white/60 text-right">Ember Works</span>
          </div>
        </div>

        {/* Column 2: Client Voice + 10M+ Raised */}
        <div className="grid grid-rows-[auto_1fr] gap-4 md:gap-5 h-full">
          {/* Top: Client Voice Card */}
          <div className="rounded-2xl bg-[#324444] p-5 md:p-6 noise-overlay flex flex-col justify-between gap-4 border border-white/5 min-h-[180px] relative overflow-hidden">
            {/* Background Video playing behind the text */}
            <video 
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260507_153148_d7a3e1dd-e5d0-4ce6-8306-00d7522ecc44.mp4" 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="absolute inset-0 object-cover w-full h-full opacity-20 pointer-events-none mix-blend-overlay"
            ></video>

            {/* Top Label */}
            <div className="flex items-center gap-2 relative z-10">
              <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
              <span className="uppercase tracking-[0.22em] text-[11px] text-white/70 font-semibold">CLIENT VOICE</span>
              <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
            </div>

            {/* Content Quote */}
            <p className="text-[13px] sm:text-[13.5px] leading-[1.6] text-white/85 relative z-10">
              "Max reshaped our image with a degree of finesse and vision that surpassed what we'd hoped for. The process felt graceful, and the outcomes speak for themselves."
            </p>

            {/* Attribution */}
            <div className="text-xs sm:text-[13px] text-white/70 relative z-10">
              <strong className="text-white font-semibold">Elena Brooks</strong>, Creative Director — Halcyon
            </div>
          </div>

          {/* Bottom: 10M+ Raised Card */}
          <div className="rounded-2xl bg-black relative overflow-hidden p-6 flex flex-col justify-between items-center border border-white/5 min-h-[220px] lg:h-full">
            {/* Background Video */}
            <video 
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260507_154543_d5b83fc1-9cea-44f3-b5e8-8f325935211a.mp4" 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="absolute inset-0 object-cover w-full h-full opacity-60 pointer-events-none"
            ></video>

            {/* Empty space for top layout alignment */}
            <div></div>

            {/* Huge Number */}
            <h2 className="text-5xl sm:text-6xl md:text-7xl lg:text-[88px] font-light tracking-tight drop-shadow relative z-10 text-white my-auto">
              10M+
            </h2>

            {/* Caption */}
            <p className="text-white/85 text-sm font-medium relative z-10">
              Raised for startups
            </p>
          </div>
        </div>

        {/* Column 3: Daily Software + Reach Me */}
        <div className="grid grid-rows-[1fr_auto] gap-4 md:gap-5 h-full">
          {/* Top: Daily Software Card */}
          <div className="rounded-2xl bg-black relative overflow-hidden p-6 flex flex-col justify-between border border-white/5 min-h-[240px] lg:h-full">
            {/* Background Video */}
            <video 
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260507_153148_d7a3e1dd-e5d0-4ce6-8306-00d7522ecc44.mp4" 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="absolute inset-0 object-cover w-full h-full opacity-50 pointer-events-none"
            ></video>

            {/* Top Label */}
            <div className="flex items-center justify-center gap-2 relative z-10 w-full mb-6">
              <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
              <span className="uppercase tracking-[0.22em] text-[11px] text-white/70 font-semibold">DAILY SOFTWARE</span>
              <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
            </div>

            {/* Dual Scrolling Marquee Container */}
            <div className="w-full overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_8%,black_92%,transparent)] relative z-10 flex flex-col gap-3 my-auto">
              {/* Row 1 (scrolls left) */}
              <div className="overflow-hidden w-full">
                <div className="flex w-max gap-3 animate-marquee-left">
                  {row1Icons.map((Icon, idx) => <IconWrapper key={`r1-${idx}`} Icon={Icon} />)}
                  {row1Icons.map((Icon, idx) => <IconWrapper key={`r1-dup-${idx}`} Icon={Icon} />)}
                </div>
              </div>

              {/* Row 2 (scrolls right) */}
              <div className="overflow-hidden w-full">
                <div className="flex w-max gap-3 animate-marquee-right">
                  {row2Icons.map((Icon, idx) => <IconWrapper key={`r2-${idx}`} Icon={Icon} />)}
                  {row2Icons.map((Icon, idx) => <IconWrapper key={`r2-dup-${idx}`} Icon={Icon} />)}
                </div>
              </div>
            </div>

            {/* Empty element for bottom padding layout placeholder */}
            <div></div>
          </div>

          {/* Bottom: Reach Me Card */}
          <div className="rounded-2xl bg-[#324444] p-5 md:p-6 noise-overlay flex flex-col justify-between gap-4 border border-white/5 relative min-h-[150px] overflow-hidden">
            {/* Background Video playing behind the text */}
            <video 
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260507_150203_44a5bd32-516a-47ce-a077-8acbf9aa8991.mp4" 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="absolute inset-0 object-cover w-full h-full opacity-20 pointer-events-none mix-blend-overlay"
            ></video>

            {/* Top Row Label + Arrow Button */}
            <div className="flex items-center justify-between w-full relative z-10">
              <div className="flex items-center gap-2">
                <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
                <span className="uppercase tracking-[0.22em] text-[11px] text-white/70 font-semibold">REACH ME</span>
                <Sparkle className="h-3 w-3 text-white/70" strokeWidth={1.5} />
              </div>
              <a 
                href="mailto:hi@maxreed.com"
                className="h-9 w-9 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors duration-300"
                aria-label="Send email to Max Reed"
              >
                <ArrowUpRight className="h-4 w-4" strokeWidth={1.5} />
              </a>
            </div>

            {/* Bottom Contact Info */}
            <div className="flex flex-col gap-1 text-white relative z-10">
              <a 
                href="mailto:hi@maxreed.com" 
                className="text-lg md:text-xl font-semibold hover:text-white/80 transition-colors tracking-tight"
              >
                hi@maxreed.com
              </a>
              <span className="text-white/60 text-sm md:text-[15px] tabular-nums">
                +44 207 81 63
              </span>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
};

export default FeaturesSection;
