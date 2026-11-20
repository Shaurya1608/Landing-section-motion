'use client';

import React, { useEffect } from 'react';
import Navbar from '@/components/Navbar';
import LoadWipe from '@/components/LoadWipe';
import CursorLabel from '@/components/CursorLabel';
import HeroSection from '@/components/HeroSection';
import LatestDropsSection from '@/components/LatestDropsSection';
import MeetTheFlockSection from '@/components/MeetTheFlockSection';

export default function Home() {
  useEffect(() => {
    // 6.5 Underline stroke paths
    const UNDERLINE_PATHS = [
      'M5 20.9999C26.7762 16.2245 49.5532 11.5572 71.7979 14.6666C84.9553 16.5057 97.0392 21.8432 109.987 24.3888C116.413 25.6523 123.012 25.5143 129.042 22.6388C135.981 19.3303 142.586 15.1422 150.092 13.3333C156.799 11.7168 161.702 14.6225 167.887 16.8333C181.562 21.7212 194.975 22.6234 209.252 21.3888C224.678 20.0548 239.912 17.991 255.42 18.3055C272.027 18.6422 288.409 18.867 305 17.9999',
      'M5 24.2592C26.233 20.2879 47.7083 16.9968 69.135 13.8421C98.0469 9.5853 128.407 4.02322 158.059 5.14674C172.583 5.69708 187.686 8.66104 201.598 11.9696C207.232 13.3093 215.437 14.9471 220.137 18.3619C224.401 21.4596 220.737 25.6575 217.184 27.6168C208.309 32.5097 197.199 34.281 186.698 34.8486C183.159 35.0399 147.197 36.2657 155.105 26.5837C158.11 22.9053 162.993 20.6229 167.764 18.7924C178.386 14.7164 190.115 12.1115 201.624 10.3984C218.367 7.90626 235.528 7.06127 252.521 7.49276C258.455 7.64343 264.389 7.92791 270.295 8.41825C280.321 9.25056 296 10.8932 305 13.0242',
      'M5 29.5014C9.61174 24.4515 12.9521 17.9873 20.9532 17.5292C23.7742 17.3676 27.0987 17.7897 29.6575 19.0014C33.2644 20.7093 35.6481 24.0004 39.4178 25.5014C48.3911 29.0744 55.7503 25.7731 63.3048 21.0292C67.9902 18.0869 73.7668 16.1366 79.3721 17.8903C85.1682 19.7036 88.2173 26.2464 94.4121 27.2514C102.584 28.5771 107.023 25.5064 113.276 20.6125C119.927 15.4067 128.83 12.3333 137.249 15.0014C141.418 16.3225 143.116 18.7528 146.581 21.0014C149.621 22.9736 152.78 23.6197 156.284 24.2514C165.142 25.8479 172.315 17.5185 179.144 13.5014C184.459 10.3746 191.785 8.74853 195.868 14.5292C199.252 19.3205 205.597 22.9057 211.621 22.5014C215.553 22.2374 220.183 17.8356 222.979 15.5569C225.4 13.5845 227.457 11.1105 230.742 10.5292C232.718 10.1794 234.784 12.9691 236.164 14.0014C238.543 15.7801 240.717 18.4775 243.356 19.8903C249.488 23.1729 255.706 21.2551 261.079 18.0014C266.571 14.6754 270.439 11.5202 277.146 13.6125C280.725 14.7289 283.221 17.209 286.393 19.0014C292.321 22.3517 298.255 22.5014 305 22.5014',
      'M17.0039 32.6826C32.2307 32.8412 47.4552 32.8277 62.676 32.8118C67.3044 32.807 96.546 33.0555 104.728 32.0775C113.615 31.0152 104.516 28.3028 102.022 27.2826C89.9573 22.3465 77.3751 19.0254 65.0451 15.0552C57.8987 12.7542 37.2813 8.49399 44.2314 6.10216C50.9667 3.78422 64.2873 5.81914 70.4249 5.96641C105.866 6.81677 141.306 7.58809 176.75 8.59886C217.874 9.77162 258.906 11.0553 300 14.4892',
      'M4.99805 20.9998C65.6267 17.4649 126.268 13.845 187.208 12.8887C226.483 12.2723 265.751 13.2796 304.998 13.9998',
      'M5 29.8857C52.3147 26.9322 99.4329 21.6611 146.503 17.1765C151.753 16.6763 157.115 15.9505 162.415 15.6551C163.28 15.6069 165.074 15.4123 164.383 16.4275C161.704 20.3627 157.134 23.7551 153.95 27.4983C153.209 28.3702 148.194 33.4751 150.669 34.6605C153.638 36.0819 163.621 32.6063 165.039 32.2029C178.55 28.3608 191.49 23.5968 204.869 19.5404C231.903 11.3436 259.347 5.83254 288.793 5.12258C294.094 4.99476 299.722 4.82265 305 5.45025'
    ];

    let underlineVariantIdx = Math.floor(Math.random() * UNDERLINE_PATHS.length);

    function createUnderlineSvg(d: string) {
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('viewBox', '0 0 310 40');
      svg.setAttribute('preserveAspectRatio', 'none');
      svg.style.width = '100%';
      svg.style.height = '100%';
      svg.style.display = 'block';

      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', d);
      path.setAttribute('fill', 'none');
      path.setAttribute('stroke', 'currentColor');
      path.setAttribute('stroke-width', '10');
      path.setAttribute('stroke-linecap', 'round');
      svg.appendChild(path);
      return { svg, path };
    }

    // Motion query
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    let isReducedMotion = motionQuery.matches;

    // Failsafe reveal
    function revealEverythingFailsafe() {
      if (!document.documentElement.hasAttribute('data-page-ready')) {
        document.documentElement.setAttribute('data-page-ready', '');
        const overlay = document.querySelector('.load-wipe-overlay');
        if (overlay) overlay.setAttribute('data-transition-ready', '');
        document.querySelectorAll('[data-text-reveal], [data-scroll-reveal]').forEach((el: any) => {
          el.style.visibility = 'visible';
        });
      }
    }

    const failsafeTimeout = setTimeout(revealEverythingFailsafe, 4000);

    // Wait until GSAP is ready
    if (typeof (window as any).gsap === 'undefined') {
      revealEverythingFailsafe();
      return () => clearTimeout(failsafeTimeout);
    }

    const gsap = (window as any).gsap;
    const ScrollTrigger = (window as any).ScrollTrigger;
    const SplitText = (window as any).SplitText;
    const DrawSVGPlugin = (window as any).DrawSVGPlugin;
    const InertiaPlugin = (window as any).InertiaPlugin;
    const Lenis = (window as any).Lenis;

    if (ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
    if (SplitText) gsap.registerPlugin(SplitText);
    if (DrawSVGPlugin) gsap.registerPlugin(DrawSVGPlugin);
    if (InertiaPlugin) gsap.registerPlugin(InertiaPlugin);

    // Lenis Smooth Scroll
    let lenis: any = null;
    if (!isReducedMotion && typeof Lenis !== 'undefined') {
      lenis = new Lenis({ lerp: 0.165, wheelMultiplier: 1.25 });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time: number) => {
        lenis.raf(time * 1000);
      });
      gsap.ticker.lagSmoothing(0);
    }

    // In-page smooth navigation
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href === '#') return;
        const target = document.querySelector(href as string);
        if (target) {
          e.preventDefault();
          if (lenis && !isReducedMotion) {
            lenis.scrollTo(target, { duration: 1.4 });
          } else {
            target.scrollIntoView({ behavior: 'smooth' });
          }
        }
      });
    });

    // Draw Underlines on hover
    document.querySelectorAll('[data-draw-line]:not([data-draw-line="always"])').forEach((el: any) => {
      const box = el.querySelector('.underline-box');
      if (!box) return;

      let activePath: any = null;
      let activeSvg: any = null;
      let isDrawing = false;
      let pendingLeave = false;

      el.addEventListener('mouseenter', () => {
        if (isReducedMotion) return;
        pendingLeave = false;
        box.innerHTML = '';
        const d = UNDERLINE_PATHS[underlineVariantIdx % UNDERLINE_PATHS.length];
        underlineVariantIdx++;
        const { svg, path } = createUnderlineSvg(d);
        box.appendChild(svg);
        activePath = path;
        activeSvg = svg;
        isDrawing = true;

        gsap.fromTo(path, { drawSVG: '0%' }, {
          drawSVG: '100%',
          duration: 0.5,
          ease: 'power2.inOut',
          onComplete: () => {
            isDrawing = false;
            if (pendingLeave && activePath) {
              gsap.to(activePath, {
                drawSVG: '100% 100%',
                duration: 0.5,
                ease: 'power2.inOut',
                onComplete: () => {
                  if (activeSvg && activeSvg.parentNode) activeSvg.remove();
                  activeSvg = null;
                  activePath = null;
                }
              });
              pendingLeave = false;
            }
          }
        });
      });

      el.addEventListener('mouseleave', () => {
        if (isReducedMotion) return;
        if (isDrawing) {
          pendingLeave = true;
        } else if (activePath) {
          gsap.to(activePath, {
            drawSVG: '100% 100%',
            duration: 0.5,
            ease: 'power2.inOut',
            onComplete: () => {
              if (activeSvg && activeSvg.parentNode) activeSvg.remove();
              activeSvg = null;
              activePath = null;
            }
          });
        }
      });
    });

    // Always-on hero underline
    function drawHeroUnderline() {
      const heroLink = document.querySelector('[data-draw-line="always"]');
      if (!heroLink) return;
      const box = heroLink.querySelector('.underline-box');
      if (!box) return;
      box.innerHTML = '';
      const d = UNDERLINE_PATHS[underlineVariantIdx % UNDERLINE_PATHS.length];
      underlineVariantIdx++;
      const { svg, path } = createUnderlineSvg(d);
      box.appendChild(svg);
      if (isReducedMotion) {
        gsap.set(path, { drawSVG: '100%' });
      } else {
        gsap.fromTo(path, { drawSVG: '0%' }, {
          drawSVG: '100%',
          duration: 0.6,
          ease: 'power2.inOut'
        });
      }
    }

    // Font weight hover
    const isTouch = window.matchMedia('(hover: none), (pointer: coarse)').matches;
    let hoverChars: any[] = [];
    let pointerPageX = window.innerWidth / 2;
    let pointerPageY = window.innerHeight / 2;

    function setupFontWeightHover(targetEl: any, splitChars: any[]) {
      if (isTouch || isReducedMotion) return;

      splitChars.forEach((char) => {
        const host = char.closest('[data-font-weight-hover]') || targetEl;
        const rest = parseFloat(host.dataset.rest || 700);
        const near = parseFloat(host.dataset.near || 200);
        const radius = parseFloat(host.dataset.radius || 400);

        char.style.setProperty('--wght', rest);
        const isSerif = char.closest('.alt-serif') !== null;
        if (isSerif) {
          char.style.fontVariationSettings = `'wght' var(--wght, ${rest}), 'wdth' 87.5, 'opsz' 120`;
        } else {
          char.style.fontVariationSettings = `'wght' var(--wght, ${rest}), 'wdth' 72`;
        }

        hoverChars.push({
          el: char,
          rest,
          near,
          radius,
          current: rest,
          quickTo: gsap.quickTo(char, '--wght', { duration: 0.4, ease: 'power2.out' }),
          x: 0,
          y: 0
        });
      });
      updateCharCenters();
    }

    function updateCharCenters() {
      for (let i = 0; i < hoverChars.length; i++) {
        const c = hoverChars[i];
        const r = c.el.getBoundingClientRect();
        c.x = r.left + r.width / 2 + window.scrollX;
        c.y = r.top + r.height / 2 + window.scrollY;
      }
    }

    const onPointerMove = (e: PointerEvent) => {
      pointerPageX = e.pageX;
      pointerPageY = e.pageY;
    };

    window.addEventListener('pointermove', onPointerMove);
    window.addEventListener('resize', updateCharCenters);
    window.addEventListener('scroll', updateCharCenters, { passive: true });

    const fontTicker = () => {
      if (isReducedMotion || isTouch || hoverChars.length === 0) return;
      for (let i = 0; i < hoverChars.length; i++) {
        const c = hoverChars[i];
        const d = Math.hypot(pointerPageX - c.x, pointerPageY - c.y);
        const f = d >= c.radius ? 0 : 1 - d / c.radius;
        let target = c.rest + (c.near - c.rest) * f;
        const minVal = Math.min(c.rest, c.near);
        const maxVal = Math.max(c.rest, c.near);
        target = Math.max(minVal, Math.min(maxVal, target));
        if (Math.abs(target - c.current) >= 1) {
          c.current = target;
          c.quickTo(target);
        }
      }
    };
    gsap.ticker.add(fontTicker);

    // Text reveals
    function initTextReveals() {
      const heroH1 = document.querySelector('.hero-headline[data-text-reveal]');
      if (heroH1) {
        if (isReducedMotion) {
          (heroH1 as HTMLElement).style.visibility = 'visible';
          heroH1.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
        } else {
          const split = new SplitText(heroH1, {
            type: 'chars,words,lines',
            linesClass: 'line',
            charsClass: 'char',
            mask: 'lines',
            autoSplit: false
          });

          gsap.set(heroH1, { visibility: 'visible' });
          gsap.from(split.chars, {
            yPercent: 135,
            duration: 1,
            ease: 'expo.out',
            stagger: 0.0175,
            delay: 0.6,
            onComplete: () => {
              heroH1.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
              setupFontWeightHover(heroH1, split.chars);
            }
          });
        }
      }

      // Scroll reveal groups
      document.querySelectorAll('[data-scroll-reveal-group]').forEach((group) => {
        if (isReducedMotion) {
          group.querySelectorAll('[data-scroll-reveal]').forEach((el: any) => {
            el.style.visibility = 'visible';
            el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
          });
          return;
        }

        const elements = group.querySelectorAll('[data-scroll-reveal]');
        const tl = gsap.timeline({
          scrollTrigger: {
            trigger: group,
            start: 'top 85%',
            once: true
          }
        });

        elements.forEach((el: any, idx) => {
          const mode = el.getAttribute('data-scroll-reveal');
          const startTime = idx * 0.12;

          if (mode === 'chars') {
            const split = new SplitText(el, {
              type: 'chars,words,lines',
              linesClass: 'line',
              charsClass: 'char',
              mask: 'lines',
              autoSplit: false
            });

            tl.set(el, { visibility: 'visible' }, startTime);
            tl.from(split.chars, {
              yPercent: 135,
              duration: 1,
              ease: 'expo.out',
              stagger: 0.0175,
              onComplete: () => {
                el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
                if (el.hasAttribute('data-font-weight-hover')) {
                  setupFontWeightHover(el, split.chars);
                }
              }
            }, startTime);
          } else if (mode === 'lines') {
            const split = new SplitText(el, {
              type: 'lines,words',
              linesClass: 'line',
              mask: 'lines'
            });

            tl.set(el, { visibility: 'visible' }, startTime);
            tl.from(split.lines, {
              yPercent: 135,
              duration: 1,
              ease: 'expo.out',
              stagger: 0.07,
              onComplete: () => {
                el.dispatchEvent(new CustomEvent('reveal:done', { bubbles: true }));
              }
            }, startTime);
          }
        });
      });
    }

    // Hero Cursor Card
    function initHeroCursorCard() {
      if (isReducedMotion || isTouch || window.innerWidth <= 600) return;

      const hero = document.querySelector('.hero-section');
      const card = document.querySelector('.hero-cursor-card');
      if (!hero || !card) return;

      const mediaLayer = card.querySelector('.media-layer');
      const photos = card.querySelectorAll('.crop');

      const cardX = gsap.quickTo(card, 'x', { duration: 1, ease: 'power4' });
      const cardY = gsap.quickTo(card, 'y', { duration: 1, ease: 'power4' });
      const cardRot = gsap.quickTo(card, 'rotation', { duration: 1, ease: 'power4' });
      const mediaX = gsap.quickTo(mediaLayer, 'xPercent', { duration: 0.6, ease: 'power2' });
      const mediaY = gsap.quickTo(mediaLayer, 'yPercent', { duration: 0.7, ease: 'power2' });

      gsap.set(card, { autoAlpha: 0 });

      let firstMove = true;
      let lastX = 0, lastY = 0;
      let travel = 0;
      let photoIdx = 0;
      let timer: any = null;
      let isCardVisible = false;

      hero.addEventListener('mousemove', (e: any) => {
        if (e.target.closest('a, button')) {
          gsap.to(card, { autoAlpha: 0, duration: 0.25, ease: 'power2.out' });
          isCardVisible = false;
          return;
        }

        if (!isCardVisible) {
          gsap.to(card, { autoAlpha: 1, duration: 0.3 });
          isCardVisible = true;
        }

        const heroRect = hero.getBoundingClientRect();
        const targetX = e.clientX - window.innerWidth / 2;
        const targetY = e.clientY - window.innerHeight / 2 - heroRect.top;

        if (firstMove) {
          gsap.set(card, { x: targetX, y: targetY });
          cardX(targetX);
          cardY(targetY);
          lastX = targetX;
          lastY = targetY;
          firstMove = false;
          return;
        }

        const dx = (targetX - lastX) / 2;
        const dy = (targetY - lastY) / 2;
        const rot = (targetX - lastX) / 4;
        lastX = targetX;
        lastY = targetY;

        cardX(targetX);
        cardY(targetY);
        cardRot(rot);

        const driftX = -Math.max(-8, Math.min(8, dx));
        const driftY = -Math.max(-8, Math.min(8, dy));
        mediaX(driftX);
        mediaY(driftY);

        travel += Math.abs(dx) + Math.abs(dy);
        if (travel >= 300) {
          travel = 0;
          photoIdx = (photoIdx + 1) % photos.length;
          photos.forEach((p, i) => p.classList.toggle('on', i === photoIdx));
        }

        clearTimeout(timer);
        timer = setTimeout(() => {
          cardRot(0);
          mediaX(0);
          mediaY(0);
        }, 66);
      });

      hero.addEventListener('mouseleave', () => {
        firstMove = true;
        travel = 0;
        cardRot(0);
        mediaX(0);
        mediaY(0);
        gsap.to(card, { autoAlpha: 0, duration: 0.3 });
        isCardVisible = false;
      });
    }

    // Client marquee
    function initClientMarquee() {
      const marqueeOuter = document.querySelector('.marquee-outer');
      const scrollWrapper = document.querySelector('.marquee-scroll-wrapper');
      const track = document.querySelector('.marquee-track');
      const collection = document.querySelector('.marquee-collection');
      if (!marqueeOuter || !scrollWrapper || !track || !collection) return;

      const clone1 = collection.cloneNode(true);
      const clone2 = collection.cloneNode(true);
      track.appendChild(clone1);
      track.appendChild(clone2);

      if (isReducedMotion) return;

      const f = window.innerWidth <= 479 ? 0.25 : window.innerWidth <= 991 ? 0.5 : 1;
      const colWidth = (collection as HTMLElement).offsetWidth || (window.innerWidth * 1.5);
      const loopDuration = 30 * (colWidth / window.innerWidth) * f;

      const allCols = track.querySelectorAll('.marquee-collection');
      gsap.set(allCols, { xPercent: -100 });

      const marqueeTween = gsap.to(allCols, {
        xPercent: 0,
        repeat: -1,
        duration: loopDuration,
        ease: 'none'
      });
      marqueeTween.totalProgress(0.5);

      ScrollTrigger.create({
        trigger: marqueeOuter,
        start: 'top bottom',
        end: 'bottom top',
        onUpdate: (self: any) => {
          const dir = self.direction;
          marqueeTween.timeScale(dir === 1 ? 1 : -1);
        }
      });

      gsap.fromTo(scrollWrapper, { x: '10vw' }, {
        x: '-10vw',
        ease: 'none',
        scrollTrigger: {
          trigger: marqueeOuter,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 0
        }
      });
    }

    // "Latest drops" 3D stack
    function initDropsStack() {
      const dropsSection = document.querySelector('.section-drops');
      const pinElement = dropsSection?.querySelector('.drops-pin-element');
      const stackRoot = dropsSection?.querySelector('.drops-stack-root');
      const slides = dropsSection?.querySelectorAll('.drop-card');
      const badge = dropsSection?.querySelector('.drops-badge');

      if (!dropsSection || !pinElement || !stackRoot || !slides || slides.length === 0) return;

      const count = slides.length;
      const mm = gsap.matchMedia();

      mm.add('(min-width: 992px)', () => {
        slides.forEach((slide, b) => {
          gsap.set(slide, {
            z: -b * 120,
            y: -b * 40,
            zIndex: count - b,
            autoAlpha: 1
          });
        });

        const tl = gsap.timeline({ paused: true });

        for (let b = 0; b < count - 1; b++) {
          tl.to(slides[b], {
            y: '+=' + (window.innerHeight * 0.9),
            ease: 'power2.in',
            duration: 1
          }, b);

          tl.to(slides[b], {
            autoAlpha: 0,
            ease: 'none',
            duration: 0.25
          }, b + 0.7);

          for (let c = b + 1; c < count; c++) {
            const newC = c - (b + 1);
            tl.to(slides[c], {
              z: -newC * 120,
              y: -newC * 40,
              ease: 'none',
              duration: 1
            }, b);
          }
        }

        if (badge) {
          tl.to(badge, {
            rotation: 180,
            ease: 'none',
            duration: count - 1
          }, 0);
        }

        ScrollTrigger.create({
          trigger: dropsSection,
          start: 'top top',
          end: () => '+=' + (window.innerHeight * 1.2 * (count - 1)),
          pin: pinElement,
          pinSpacing: true,
          scrub: 0.3,
          refreshPriority: 1,
          invalidateOnRefresh: true,
          onUpdate: (self: any) => {
            tl.progress(self.progress);
          }
        });

        if (!isReducedMotion) {
          const tiltX = gsap.quickTo(stackRoot, 'rotationX', { duration: 0.6, ease: 'power3' });
          const tiltY = gsap.quickTo(stackRoot, 'rotationY', { duration: 0.6, ease: 'power3' });

          const onMouseMove = (e: any) => {
            const rect = pinElement.getBoundingClientRect();
            const rx = -((e.clientY - rect.top) / rect.height - 0.5) * 6;
            const ry = ((e.clientX - rect.left) / rect.width - 0.5) * 10;
            tiltX(rx);
            tiltY(ry);
          };

          const onMouseLeave = () => {
            tiltX(0);
            tiltY(0);
          };

          pinElement.addEventListener('mousemove', onMouseMove);
          pinElement.addEventListener('mouseleave', onMouseLeave);

          return () => {
            pinElement.removeEventListener('mousemove', onMouseMove);
            pinElement.removeEventListener('mouseleave', onMouseLeave);
          };
        }
      });
    }

    // Cursor label
    function initCursorLabel() {
      if (isTouch) return;

      const labelWrapper = document.querySelector('.cursor-label-wrapper');
      if (!labelWrapper) return;

      const textEls = labelWrapper.querySelectorAll('.cursor-label-text');
      const quickX = gsap.quickTo(labelWrapper, 'x', { duration: 0.4, ease: 'power3' });
      const quickY = gsap.quickTo(labelWrapper, 'y', { duration: 0.4, ease: 'power3' });

      let firstMove = true;
      let lastTarget: any = null;
      let pauseTimeout: any = null;

      function updateHover(clientX: number, clientY: number) {
        const hovered = document.elementFromPoint(clientX, clientY)?.closest('[data-cursor-marquee-text]');
        if (hovered && hovered !== lastTarget) {
          lastTarget = hovered;
          clearTimeout(pauseTimeout);
          const text = hovered.getAttribute('data-cursor-marquee-text') || 'View case →';
          textEls.forEach((el: any) => {
            el.textContent = text;
            el.style.setProperty('--dur', (text.length / 5) + 's');
          });
          labelWrapper.setAttribute('data-cursor-marquee-status', 'active');
        } else if (!hovered && lastTarget) {
          lastTarget = null;
          labelWrapper.setAttribute('data-cursor-marquee-status', 'inactive');
          pauseTimeout = setTimeout(() => {}, 400);
        }
      }

      window.addEventListener('pointermove', (e) => {
        if (firstMove) {
          gsap.set(labelWrapper, { x: e.clientX, y: e.clientY });
          quickX(e.clientX);
          quickY(e.clientY);
          firstMove = false;
        } else {
          quickX(e.clientX);
          quickY(e.clientY);
        }
        updateHover(e.clientX, e.clientY);
      });

      window.addEventListener('scroll', () => {
        if (!firstMove) {
          updateHover(pointerPageX - window.scrollX, pointerPageY - window.scrollY);
        }
      }, { passive: true });
    }

    // Team photo parallax
    function initTeamParallax() {
      const flock = document.querySelector('.section-flock');
      const cards = flock?.querySelectorAll('.team-photo-card');
      if (!flock || !cards) return;

      const mm = gsap.matchMedia();

      const createTriggers = (k: number) => {
        cards.forEach((card) => {
          const speed = parseFloat(card.getAttribute('data-speed') || '1');
          const dist = 320 * k * speed;
          gsap.fromTo(card, { y: dist }, {
            y: -dist,
            ease: 'none',
            scrollTrigger: {
              trigger: flock,
              start: 'clamp(top bottom)',
              end: 'clamp(bottom top)',
              scrub: true,
              invalidateOnRefresh: true,
              refreshPriority: -1
            }
          });
        });
      };

      mm.add('(min-width: 992px) and (prefers-reduced-motion: no-preference)', () => {
        createTriggers(1);
      });
      mm.add('(min-width: 480px) and (max-width: 991px) and (prefers-reduced-motion: no-preference)', () => {
        createTriggers(0.5);
      });
      mm.add('(max-width: 479px) and (prefers-reduced-motion: no-preference)', () => {
        createTriggers(0.3);
      });
    }

    // Momentum hover
    function initMomentumHover() {
      if (isTouch || isReducedMotion || typeof InertiaPlugin === 'undefined') return;

      const targets = document.querySelectorAll('[data-momentum-hover]');
      let prevX = 0, prevY = 0;
      let vx = 0, vy = 0;

      window.addEventListener('pointermove', (e) => {
        vx = e.clientX - prevX;
        vy = e.clientY - prevY;
        prevX = e.clientX;
        prevY = e.clientY;
      });

      gsap.ticker.add(() => {
        vx *= 0.8;
        vy *= 0.8;
      });

      targets.forEach((target) => {
        target.addEventListener('mouseenter', (e: any) => {
          const rect = target.getBoundingClientRect();
          const F = e.clientX - rect.left - rect.width / 2;
          const R = e.clientY - rect.top - rect.height / 2;
          const hyp = Math.hypot(F, R) || 1;
          const torque = (F * vy - R * vx) / hyp;

          const clampVal = (val: number, max: number) => Math.max(-max, Math.min(max, val));

          gsap.to(target, {
            inertia: {
              x: { velocity: clampVal(vx * 30, 1080), end: 0 },
              y: { velocity: clampVal(vy * 30, 1080), end: 0 },
              rotation: { velocity: clampVal(torque * 20, 60), end: 0 },
              resistance: 200
            }
          });
        });
      });
    }

    // Theme Switch
    function initThemeSwitch() {
      document.querySelectorAll('[data-page-theme]').forEach((el) => {
        const theme = el.getAttribute('data-page-theme');
        ScrollTrigger.create({
          trigger: el,
          start: 'top 55%',
          end: 'bottom 45%',
          refreshPriority: -1,
          onEnter: () => document.documentElement.setAttribute('data-theme', theme as string),
          onEnterBack: () => document.documentElement.setAttribute('data-theme', theme as string),
          onLeave: () => document.documentElement.removeAttribute('data-theme'),
          onLeaveBack: () => document.documentElement.removeAttribute('data-theme')
        });
      });
    }

    function initPage() {
      initTextReveals();
      initHeroCursorCard();
      initClientMarquee();
      initDropsStack();
      initCursorLabel();
      initTeamParallax();
      initMomentumHover();
      initThemeSwitch();
    }

    // 6.2 Load Sequence Timeline
    function startLoadSequence() {
      document.documentElement.setAttribute('data-page-ready', '');
      const overlay = document.querySelector('.load-wipe-overlay');
      const wipePath = document.querySelector('.load-wipe-path');

      if (isReducedMotion) {
        if (overlay) overlay.setAttribute('data-transition-ready', '');
        const main = document.querySelector('main');
        if (main) gsap.set(main, { autoAlpha: 1 });
        initPage();
        drawHeroUnderline();
        return;
      }

      const main = document.querySelector('main');
      const tl = gsap.timeline();

      tl.set(main, { autoAlpha: 0 }, 0);
      tl.set(wipePath, { drawSVG: '0% 100%', strokeWidth: '30%' }, 0);

      tl.addLabel('reveal', 0.4);
      tl.set(main, { autoAlpha: 1 }, 'reveal');
      tl.call(() => {
        initPage();
      }, null, 'reveal');

      tl.to(wipePath, {
        drawSVG: '100% 100%',
        strokeWidth: '5%',
        duration: 1.25,
        ease: 'power1.inOut',
        onComplete: () => {
          if (overlay) overlay.setAttribute('data-transition-ready', '');
        }
      }, 'reveal');

      tl.call(() => {
        drawHeroUnderline();
      }, null, 1.7);
    }

    const fontsPromise = document.fonts ? document.fonts.ready : Promise.resolve();
    const timeoutPromise = new Promise((resolve) => setTimeout(resolve, 1500));

    Promise.race([fontsPromise, timeoutPromise]).then(() => {
      startLoadSequence();
    }).catch(() => {
      startLoadSequence();
    });

    return () => {
      clearTimeout(failsafeTimeout);
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('resize', updateCharCenters);
      window.removeEventListener('scroll', updateCharCenters);
      gsap.ticker.remove(fontTicker);
    };
  }, []);

  return (
    <>
      <LoadWipe />
      <CursorLabel />
      <Navbar />
      <main>
        <HeroSection />
        <LatestDropsSection />
        <MeetTheFlockSection />
      </main>
    </>
  );
}
