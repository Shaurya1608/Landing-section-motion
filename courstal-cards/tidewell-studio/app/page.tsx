'use client';

import React, { useEffect, useRef } from 'react';
import SiteNav from '@/components/SiteNav';
import HeroHeader from '@/components/HeroHeader';
import PinnedStage from '@/components/PinnedStage';
import ManifestoSection from '@/components/ManifestoSection';
import WorksSection from '@/components/WorksSection';
import ServicesSection from '@/components/ServicesSection';
import AtelierSection from '@/components/AtelierSection';
import InquirySection from '@/components/InquirySection';
import {
  PLANE_POINTS,
  CARD_RISES,
  CARD_ORDER,
  easeInOutCubic,
  easeGlide,
  stepR,
} from '@/components/constants';

export default function Home() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let animId: number;
    let W = window.innerWidth;
    let H = window.innerHeight;
    let isMobile = W < 820 || W < H * 1.1;
    let cw = 218;

    const htmlEl = document.documentElement;
    const bodyEl = document.body;
    const storyEl = document.getElementById('story');
    const manifestoEl = document.getElementById('manifesto');
    const navLogo = document.getElementById('navLogo');
    const navLinks = document.querySelectorAll('.nav-link');
    const navCta = document.getElementById('navCta');
    const headlineInner = document.getElementById('headlineInner');
    const headlineWords = document.getElementById('headlineWords');
    const iconLayer = document.getElementById('iconLayer');
    const paperPlane = document.getElementById('paperPlane');
    const pixelIcons = document.querySelectorAll('.pixel-icon');
    const processBlock = document.getElementById('processBlock');
    const processHeadline = document.getElementById('processHeadline');
    const processSubline = document.getElementById('processSubline');
    const processBtn = document.getElementById('processBtn');
    const cardEls = document.querySelectorAll('.art-card') as NodeListOf<HTMLElement>;
    const skyPanel = document.getElementById('skyPanel');
    const skyPlate = document.getElementById('skyPlate');
    const skyVideo = document.getElementById('skyVideo') as HTMLVideoElement | null;
    const cameraWrap = document.getElementById('cameraWrap');
    const cameraInner = document.getElementById('cameraInner');
    const skyWordsTL = document.getElementById('skyWordsTL');
    const skyWordsBR = document.getElementById('skyWordsBR');
    const blackoutLayer = document.getElementById('blackoutLayer');
    const manifestoTrack = document.getElementById('manifestoTrack');
    const manifestoBadges = document.querySelectorAll('[data-reveal]') as NodeListOf<HTMLElement>;
    const worksEl = document.getElementById('works');
    const worksTrack = document.getElementById('worksTrack');
    const worksProgressFill = document.getElementById('worksProgressFill');
    const worksCounter = document.getElementById('worksCounter');
    const servicesEl = document.getElementById('services');
    const serviceItems = document.querySelectorAll('.service-item');
    const prismSvg = document.getElementById('prismSvg');
    const readoutTitle = document.getElementById('readoutTitle');
    const readoutTags = document.getElementById('readoutTags');
    const atelierEl = document.getElementById('atelier');
    const contactEl = document.getElementById('contact');

    if (!storyEl || !manifestoEl) return;

    // Build Hero Headline characters
    const targetText = 'Vision in Motion';
    if (headlineWords && headlineWords.children.length === 0) {
      for (let i = 0; i < targetText.length; i++) {
        const char = targetText[i];
        const span = document.createElement('span');
        span.className = 'headline-char' + (char === ' ' ? ' space' : '');
        span.textContent = char === ' ' ? '\u00A0' : char;
        headlineWords.appendChild(span);
      }
    }
    const charSpans = document.querySelectorAll('.headline-char') as NodeListOf<HTMLElement>;
    const manifestoChars = document.querySelectorAll('.manifesto-char') as NodeListOf<HTMLElement>;

    const processWords = document.querySelectorAll('.process-headline .word') as NodeListOf<HTMLElement>;
    const skyWords = document.querySelectorAll('.sky-word') as NodeListOf<HTMLElement>;

    function updateScale() {
      W = window.innerWidth;
      H = window.innerHeight;
      isMobile = W < 820 || W < H * 1.1;

      const n = isMobile
        ? Math.min(1, W / 560)
        : Math.min(Math.max(W / 1440, 0.62), 1.25);
      const u = Math.min(Math.max(W / 1440, 0.55), 1.15);
      const hfs = isMobile
        ? Math.min(W * 0.074, H * 0.055, 34)
        : Math.min(W * 0.074, H * 0.135);
      const ic = isMobile
        ? Math.min(hfs * 0.58, 20)
        : Math.min(W * 0.045, H * 0.082);
      const pfs = isMobile
        ? Math.min(W * 0.072, 38)
        : Math.min(Math.max(W * 0.033, 30), 48);
      const sfs = isMobile
        ? Math.min(W * 0.068, 36)
        : Math.min(Math.max(W * 0.033, 28), 48);
      const mfs = isMobile
        ? Math.min(W * 0.092, 44)
        : Math.min(Math.max(W * 0.05, 42), 72);
      const camw = isMobile
        ? Math.min(W * 0.44, 220)
        : Math.min(Math.max(W * 0.1875, 180), 270);
      cw = isMobile
        ? Math.min(Math.max(W * 0.38, 140), 200)
        : Math.min(Math.max(W * 0.151, 150), 218);

      const root = document.documentElement;
      root.style.setProperty('--n', n.toString());
      root.style.setProperty('--u', `${u}px`);
      root.style.setProperty('--hfs', `${hfs}px`);
      root.style.setProperty('--ic', `${ic}px`);
      root.style.setProperty('--pfs', `${pfs}px`);
      root.style.setProperty('--sfs', `${sfs}px`);
      root.style.setProperty('--mfs', `${mfs}px`);
      root.style.setProperty('--camw', `${camw}px`);
      root.style.setProperty('--cw', cw.toString());
      root.style.setProperty('--cw-px', `${cw}px`);
    }

    updateScale();
    window.addEventListener('resize', updateScale);

    // Smooth Scrolling state
    let sy = window.scrollY || window.pageYOffset || 0;
    let ty = sy;
    let lastWheelTime = 0;
    const hasFinePointer = window.matchMedia('(pointer: fine)').matches;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function onWheel(e: WheelEvent) {
      if (!hasFinePointer || prefersReducedMotion) return;
      lastWheelTime = performance.now();
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      ty = Math.max(0, Math.min(maxScroll, ty + e.deltaY));
    }
    window.addEventListener('wheel', onWheel, { passive: true });

    window.addEventListener('scroll', () => {
      if (!hasFinePointer || prefersReducedMotion || performance.now() - lastWheelTime > 250) {
        ty = window.scrollY || window.pageYOffset || 0;
      }
    });

    // Card Poses
    interface Pose {
      x: number;
      y: number;
      rot: number;
      scale: number;
      opacity: number;
    }

    const cardPoses: Pose[] = Array.from({ length: 12 }, () => ({
      x: W * 0.5,
      y: H * 1.5,
      rot: 8,
      scale: 1,
      opacity: 0,
    }));
    const cardTargets: Pose[] = Array.from({ length: 12 }, () => ({
      x: W * 0.5,
      y: H * 1.5,
      rot: 8,
      scale: 1,
      opacity: 0,
    }));

    function getFanPose(i: number): Pose {
      if (i > 5) return { x: W * 0.5, y: H * 1.4, rot: 0, scale: 1, opacity: 0 };
      if (!isMobile) {
        const R = (1250 * W) / 1440;
        const s = stepR(R, cw);
        const theta = (i - 2.5) * s;
        const cx = W * 0.55;
        const cy = H * 0.86 + R;
        return {
          x: cx + R * Math.sin(theta) - W * 0.02,
          y: cy - R * Math.cos(theta),
          rot: theta * (180 / Math.PI),
          scale: 1,
          opacity: 1,
        };
      } else {
        const R = W * 1.35;
        const s = stepR(R, cw);
        const theta = (i - 2.5) * s;
        const cx = W * 0.5;
        const cy = H * 0.86 + R;
        return {
          x: cx + R * Math.sin(theta),
          y: cy - R * Math.cos(theta) + cw * 0.2,
          rot: theta * (180 / Math.PI),
          scale: 1,
          opacity: 1,
        };
      }
    }

    function getScatterPose(i: number): Pose {
      if (i > 5) return { x: W * 0.5, y: H * 1.4, rot: 0, scale: 1, opacity: 0 };
      let p: [number, number, number];
      if (!isMobile) {
        const poses: [number, number, number][] = [
          [0.08, 0.46, -20],
          [0.2, 0.86, -12],
          [0.8, 0.84, 14],
          [0.38, 1.04, -8],
          [0.92, 0.42, 16],
          [0.62, 1.04, 9],
        ];
        p = poses[i];
      } else {
        const poses: [number, number, number][] = [
          [0.06, 0.6, -20],
          [0.45, 0.66, 12],
          [0.94, 0.6, 16],
          [0.22, 0.93, -14],
          [0.72, 0.96, 9],
          [0.5, 1.3, 0],
        ];
        p = poses[i];
      }
      let yFrac = p[1];
      if (H < 500 && yFrac < 0.1) yFrac += 0.08;
      return {
        x: p[0] * W,
        y: yFrac * H,
        rot: p[2],
        scale: 1,
        opacity: 1,
      };
    }

    function getPilePose(i: number): Pose {
      return {
        x: W * 0.5 + ((i % 3) - 1) * cw * 0.08,
        y: H * 0.62 + (((i * 7) % 5) - 2) * cw * 0.04,
        rot: (i % 2 === 0 ? 1 : -1) * (4 + i * 1.3),
        scale: 1,
        opacity: 1,
      };
    }

    function getWheelPose(i: number, rotVal: number): Pose {
      const R = !isMobile ? (900 * W) / 1440 : W * 1.2;
      const s = stepR(R, cw);
      const slot = ((((i + rotVal) % 12) + 12) % 12) - 5.5;
      const angle = slot * s;
      const cx = W * 0.5;
      const cy = !isMobile ? H * 0.82 + R : H * 0.76 + R;
      const deg = angle * (180 / Math.PI);
      const isVis = Math.abs(deg) < 62;
      return {
        x: cx + R * Math.sin(angle),
        y: cy - R * Math.cos(angle),
        rot: deg,
        scale: 1,
        opacity: isVis ? 1 : 0,
      };
    }

    function lerpPose(a: Pose, b: Pose, t: number): Pose {
      return {
        x: a.x + (b.x - a.x) * t,
        y: a.y + (b.y - a.y) * t,
        rot: a.rot + (b.rot - a.rot) * t,
        scale: a.scale + (b.scale - a.scale) * t,
        opacity: a.opacity + (b.opacity - a.opacity) * t,
      };
    }

    function getCatmullRom(tVal: number) {
      const pts = PLANE_POINTS;
      const dur = 1.27 - 0.33;
      const u = Math.max(0, Math.min(1, (tVal - 0.33) / dur));
      const nSegments = pts.length - 3;
      const segT = u * nSegments;
      const i = Math.min(Math.floor(segT), nSegments - 1);
      const s = segT - i;

      const p0 = pts[i];
      const p1 = pts[i + 1];
      const p2 = pts[i + 2];
      const p3 = pts[i + 3];

      const s2 = s * s;
      const s3 = s2 * s;

      const q = (v0: number, v1: number, v2: number, v3: number) =>
        0.5 *
        (2 * v1 +
          (-v0 + v2) * s +
          (2 * v0 - 5 * v1 + 4 * v2 - v3) * s2 +
          (-v0 + 3 * v1 - 3 * v2 + v3) * s3);

      const x = q(p0[1], p1[1], p2[1], p3[1]);
      const y = q(p0[2], p1[2], p2[2], p3[2]);

      const dq = (v0: number, v1: number, v2: number, v3: number) =>
        0.5 *
        (-v0 +
          v2 +
          2 * (2 * v0 - 5 * v1 + 4 * v2 - v3) * s +
          3 * (-v0 + 3 * v1 - 3 * v2 + v3) * s2);

      const dx = dq(p0[1], p1[1], p2[1], p3[1]);
      const dy = dq(p0[2], p1[2], p2[2], p3[2]);
      const angle = Math.atan2(dy, dx) * (180 / Math.PI);

      return { x, y, angle };
    }

    let startTime = 0;
    let lastTime = performance.now();
    let wheelCompleted = false;
    let cardsSettled = false;
    let skyGateAllowed = false;
    let skyDisplayProgress = 0;
    let processWordsRevealed = false;
    let skyWordsRevealed = false;
    let videoStarted = false;
    let curYawDeg = 0;
    let curCamScale = 0.75;
    let curZoomScale = 1;
    let curBobY = 0;

    function render(now: number) {
      if (!startTime) startTime = now;
      const dt = Math.min(34, now - lastTime);
      lastTime = now;
      const t = (now - startTime) / 1000;

      // Smooth scroll interpolation
      if (hasFinePointer && !prefersReducedMotion) {
        if (performance.now() - lastWheelTime > 250) {
          ty = window.scrollY || window.pageYOffset || 0;
        }
        const kScroll = 1 - Math.pow(1 - 0.06, dt / 16.67);
        sy += (ty - sy) * kScroll;
      } else {
        sy = window.scrollY || window.pageYOffset || 0;
      }

      const storyTop = storyEl?.offsetTop || 0;
      const storyHeight = (storyEl?.offsetHeight || 0) - H;
      const p = Math.max(0, Math.min(1, (sy - storyTop) / storyHeight));

      // 1. Headline Fade Calculation
      const navHeight =
        86 * (isMobile ? Math.min(1, W / 560) : Math.min(Math.max(W / 1440, 0.62), 1.25));
      const hfs = isMobile
        ? Math.min(W * 0.12, H * 0.09)
        : Math.min(W * 0.074, H * 0.135);
      const currentHeadlineTop = 0.41 * H - 0.5 * hfs - sy;
      const fadeStart = navHeight + 2.0 * hfs;
      const fadeEnd = navHeight + 0.6 * hfs;

      if (headlineInner) {
        if (currentHeadlineTop >= fadeStart) {
          headlineInner.style.opacity = '1';
        } else if (currentHeadlineTop <= fadeEnd) {
          headlineInner.style.opacity = '0';
        } else {
          const fadeFrac = (currentHeadlineTop - fadeEnd) / (fadeStart - fadeEnd);
          headlineInner.style.opacity = Math.max(0, Math.min(1, fadeFrac)).toString();
        }
      }

      // Load Sequence (0 - 6.5s)
      if (t < 6.5 && !prefersReducedMotion) {
        if (navLogo) {
          if (t >= 0.15 && t <= 0.35) {
            navLogo.style.opacity = Math.min(1, easeInOutCubic((t - 0.15) / 0.2)).toString();
          } else if (t > 0.35) {
            navLogo.style.opacity = '1';
          }
        }

        navLinks.forEach((link, idx) => {
          const el = link as HTMLElement;
          const st = 0.2 + idx * 0.03;
          const ed = 0.42 + idx * 0.03;
          if (t >= st && t <= ed) {
            const pVal = (t - st) / (ed - st);
            el.style.opacity = pVal.toString();
            el.style.transform = `translateY(${(1 - pVal) * 6}px)`;
          } else if (t > ed) {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0px)';
          }
        });

        if (navCta) {
          if (t >= 0.23 && t <= 0.42) {
            const pVal = (t - 0.23) / 0.19;
            const insetLeft = (1 - easeInOutCubic(pVal)) * 100;
            navCta.style.clipPath = `inset(0 0 0 ${insetLeft}% round calc(12px * var(--n)))`;
          } else if (t > 0.42) {
            navCta.style.clipPath = 'inset(0 0 0 0% round calc(12px * var(--n)))';
          }
        }

        if (pixelIcons[0]) {
          const rect = pixelIcons[0].getBoundingClientRect();
          PLANE_POINTS[PLANE_POINTS.length - 1][1] = ((rect.left + rect.width * 0.5) / W) * 100;
          PLANE_POINTS[PLANE_POINTS.length - 1][2] = ((rect.top + rect.height * 0.5) / H) * 100;
        }

        if (paperPlane) {
          if (t >= 0.33 && t <= 1.27) {
            paperPlane.style.opacity = '1';
            const pt = getCatmullRom(t);
            paperPlane.style.left = `${(pt.x * W) / 100}px`;
            paperPlane.style.top = `${(pt.y * H) / 100}px`;
            paperPlane.style.transform = `translate(-50%, -50%) rotate(${pt.angle}deg)`;
          } else if (t > 1.27 && t <= 1.33) {
            const pVal = (t - 1.27) / 0.06;
            const pt = getCatmullRom(1.27);
            paperPlane.style.left = `${(pt.x * W) / 100}px`;
            paperPlane.style.top = `${(pt.y * H) / 100}px`;
            paperPlane.style.opacity = (1 - pVal).toString();
            paperPlane.style.transform = `translate(-50%, -50%) rotate(${pt.angle}deg) scale(${1 - 0.4 * pVal})`;
          } else if (t > 1.33) {
            paperPlane.style.opacity = '0';
          }
        }

        if (pixelIcons[0] && t >= 1.27) {
          const el = pixelIcons[0] as HTMLElement;
          el.style.opacity = '1';
          el.style.transform = 'scale(1)';
        }

        for (let j = 1; j < 7; j++) {
          if (pixelIcons[j]) {
            const el = pixelIcons[j] as HTMLElement;
            const st = 1.27 + (0.03 + j * 0.07);
            if (t >= st && t <= st + 0.32) {
              const pVal = (t - st) / 0.32;
              const s = 1 + 1.15 * Math.pow(pVal - 1, 3) + (pVal - 1) * Math.pow(pVal - 1, 2);
              el.style.opacity = Math.min(1, pVal / 0.375).toString();
              el.style.transform = `scale(${Math.max(0, s)})`;
            } else if (t > st + 0.32) {
              el.style.opacity = '1';
              el.style.transform = 'scale(1)';
            }
          }
        }

        // Cards rise during intro
        CARD_ORDER.forEach((cIdx, orderIdx) => {
          const st = CARD_RISES[orderIdx];
          const endFan = getFanPose(cIdx);
          if (t < st) {
            cardTargets[cIdx] = { x: endFan.x, y: H + cw * 1.2, rot: 8, scale: 1, opacity: 0 };
            cardPoses[cIdx] = { ...cardTargets[cIdx] };
          } else if (t >= st && t <= st + 0.7) {
            const pVal = (t - st) / 0.7;
            const overshoot = (x: number) =>
              1 + 2.15 * Math.pow(x - 1, 3) + 1.15 * Math.pow(x - 1, 2);
            const op = Math.min(1, pVal * 2);
            const py = H + cw * 1.2 + (endFan.y - (H + cw * 1.2)) * overshoot(pVal);
            const pr = 8 + (endFan.rot - 8) * overshoot(pVal);
            cardTargets[cIdx] = { x: endFan.x, y: py, rot: pr, scale: 1, opacity: op };
            cardPoses[cIdx] = { ...cardTargets[cIdx] };
          }
        });

        // Icon to letter morph (1.9 -> ~5.2s)
        if (t >= 1.9) {
          const morphT = t - 1.9;
          const stepDur = 0.22;
          const stepIdx = Math.floor(morphT / stepDur);

          for (let i = 0; i < targetText.length; i++) {
            if (charSpans[i]) {
              if (i < stepIdx) {
                charSpans[i].style.opacity = '1';
                charSpans[i].style.clipPath = 'inset(0 0% 0 0)';
              } else if (i === stepIdx && stepIdx < targetText.length) {
                const stepFrac = (morphT % stepDur) / stepDur;
                if (stepFrac >= 0.32) {
                  const wipe = Math.min(1, (stepFrac - 0.32) / 0.58);
                  charSpans[i].style.opacity = '1';
                  charSpans[i].style.clipPath = `inset(0 ${(1 - wipe) * 100}% 0 0)`;
                } else {
                  charSpans[i].style.opacity = '0';
                  charSpans[i].style.clipPath = 'inset(0 100% 0 0)';
                }
              } else {
                charSpans[i].style.opacity = '0';
                charSpans[i].style.clipPath = 'inset(0 100% 0 0)';
              }
            }
          }

          const lettersLeft = Math.max(0, targetText.length - stepIdx);
          const iconsRemaining = Math.min(7, Math.ceil((7 * lettersLeft) / targetText.length));

          for (let k = 0; k < 7; k++) {
            if (pixelIcons[k]) {
              const el = pixelIcons[k] as HTMLElement;
              if (k < 7 - iconsRemaining) {
                el.style.display = 'none';
              } else if (k === 7 - iconsRemaining && stepIdx < targetText.length) {
                el.style.display = 'inline-flex';
                const stepFrac = (morphT % stepDur) / stepDur;
                if (stepFrac <= 0.45) {
                  const u = stepFrac / 0.45;
                  const syVal = 1 - (1 - 0.16) * u;
                  const sxVal = 1 + 0.25 * u;
                  const r = -28 * u;
                  el.style.transform = `scale(${sxVal}, ${syVal}) rotate(${r}deg)`;
                  el.style.filter = `brightness(${1 - u})`;
                  el.style.opacity = '1';
                } else {
                  const u = (stepFrac - 0.45) / 0.55;
                  const r = -28 - 62 * u;
                  el.style.transform = `scale(1.25, 0.16) rotate(${r}deg)`;
                  el.style.opacity = `${1 - u}`;
                }
              } else {
                el.style.display = 'inline-flex';
                el.style.opacity = '1';
                el.style.transform = 'scale(1) rotate(0deg)';
                el.style.filter = 'none';
              }
            }
          }
        }
      } else if (prefersReducedMotion) {
        if (navLogo) navLogo.style.opacity = '1';
        navLinks.forEach((l) => {
          (l as HTMLElement).style.opacity = '1';
          (l as HTMLElement).style.transform = 'none';
        });
        if (navCta) navCta.style.clipPath = 'none';
        charSpans.forEach((c) => {
          c.style.opacity = '1';
          c.style.clipPath = 'none';
        });
        if (iconLayer) iconLayer.style.display = 'none';
        if (paperPlane) paperPlane.style.display = 'none';
      }

      // 2. Cards Choreography driven by Scroll Progress p
      if (!(t < 1.56 && p < 0.004 && !prefersReducedMotion)) {
        if (p < 0.004) {
          for (let i = 0; i < 12; i++) cardTargets[i] = getFanPose(i);
        } else if (p >= 0.004 && p < 0.085) {
          const tVal = easeInOutCubic((p - 0.004) / 0.081);
          for (let i = 0; i < 12; i++)
            cardTargets[i] = lerpPose(getFanPose(i), getScatterPose(i), tVal);
        } else if (p >= 0.085 && p < 0.21) {
          for (let i = 0; i < 12; i++) cardTargets[i] = getScatterPose(i);
        } else if (p >= 0.21 && p < 0.31) {
          const tVal = easeInOutCubic((p - 0.21) / 0.1);
          for (let i = 0; i < 12; i++)
            cardTargets[i] = lerpPose(getScatterPose(i), getPilePose(i), tVal);
        } else if (p >= 0.31 && p < 0.41) {
          const tVal = easeGlide((p - 0.31) / 0.1);
          for (let i = 0; i < 12; i++)
            cardTargets[i] = lerpPose(getPilePose(i), getWheelPose(i, 0), tVal);
        } else if (p >= 0.41 && p < 0.56) {
          const wheelProg = (p - 0.41) / 0.15;
          const rotVal = -3 * easeInOutCubic(wheelProg);
          for (let i = 0; i < 12; i++) cardTargets[i] = getWheelPose(i, rotVal);
        } else if (p >= 0.56 && p < 0.66) {
          wheelCompleted = true;
          const q = (p - 0.56) / 0.10;
          const eq = easeInOutCubic(q);
          for (let i = 0; i < 12; i++) {
            const base = getWheelPose(i, -3);
            cardTargets[i] = {
              ...base,
              y: base.y + eq * (H * 0.32),
              scale: base.scale * (1 - 0.12 * eq),
              opacity: Math.max(0, base.opacity * (1 - eq)),
            };
          }
        } else {
          wheelCompleted = true;
          for (let i = 0; i < 12; i++) {
            const base = getWheelPose(i, -3);
            cardTargets[i] = { ...base, y: base.y + H * 0.32, opacity: 0 };
          }
        }
      }

      // Spring Inertia & Settlement
      cardsSettled = true;
      for (let i = 0; i < 12; i++) {
        const tgt = cardTargets[i];
        const cur = cardPoses[i];
        const w = 0.055 + (i % 4) * 0.008;
        const k =
          prefersReducedMotion || (t < 1.6 && sy < 10)
            ? 1
            : 1 - Math.pow(1 - w, dt / 16.67);

        cur.x += (tgt.x - cur.x) * k;
        cur.y += (tgt.y - cur.y) * k;
        cur.rot += (tgt.rot - cur.rot) * k;
        cur.scale += (tgt.scale - cur.scale) * k;
        cur.opacity += (tgt.opacity - cur.opacity) * k;

        if (Math.abs(tgt.x - cur.x) > 3 || Math.abs(tgt.rot - cur.rot) > 1) {
          cardsSettled = false;
        }

        const el = cardEls[i];
        if (el) {
          el.style.transform = `translate3d(${cur.x}px, ${cur.y}px, 0) rotate(${cur.rot}deg) scale(${cur.scale})`;
          el.style.opacity = cur.opacity.toString();
          el.style.display = cur.opacity < 0.01 ? 'none' : 'block';
        }
      }

      // 3. Process Block Reveal & Clean Fade-out before Sky Panel
      if (processBlock) {
        if (p >= 0.05 && p <= 0.075) {
          processBlock.style.visibility = 'visible';
          processBlock.style.opacity = ((p - 0.05) / 0.025).toString();
        } else if (p > 0.075 && p <= 0.53) {
          processBlock.style.visibility = 'visible';
          processBlock.style.opacity = '1';
          if (!processWordsRevealed) {
            processWordsRevealed = true;
            processWords.forEach((w, idx) => {
              setTimeout(() => {
                w.style.transition =
                  'opacity 0.55s cubic-bezier(0.2,0,0.2,1), transform 0.55s cubic-bezier(0.2,0,0.2,1), filter 0.55s cubic-bezier(0.2,0,0.2,1)';
                w.style.opacity = '1';
                w.style.transform = 'translateY(0)';
                w.style.filter = 'blur(0px)';
              }, idx * 110);
            });
            setTimeout(() => {
              if (processSubline) {
                processSubline.style.opacity = '1';
                processSubline.style.transform = 'translateY(0)';
              }
            }, 700);
            setTimeout(() => {
              if (processBtn) {
                processBtn.style.opacity = '1';
                processBtn.style.transform = 'translateY(0)';
              }
            }, 850);
          }
        } else if (p > 0.53 && p <= 0.59) {
          const fade = Math.max(0, 1 - (p - 0.53) / 0.06);
          processBlock.style.opacity = fade.toString();
          if (fade <= 0.01) processBlock.style.visibility = 'hidden';
        } else {
          processBlock.style.visibility = 'hidden';
          processBlock.style.opacity = '0';
          processWordsRevealed = false;
          processWords.forEach((w) => {
            w.style.opacity = '0';
            w.style.transform = 'translateY(0.35em)';
            w.style.filter = 'blur(6px)';
          });
          if (processSubline) {
            processSubline.style.opacity = '0';
            processSubline.style.transform = 'translateY(8px)';
          }
          if (processBtn) {
            processBtn.style.opacity = '0';
            processBtn.style.transform = 'translateY(8px)';
          }
        }
      }

      // 4. Smooth Sky Panel & Steadicam Camera (0.58 -> 0.74)
      const targetSkyProgress = Math.max(0, Math.min(1, (p - 0.58) / 0.15));
      const kSky = 1 - Math.pow(1 - 0.08, dt / 16.67);
      skyDisplayProgress += (targetSkyProgress - skyDisplayProgress) * kSky;

      if (skyPanel) {
        if (skyDisplayProgress > 0.005) {
          skyPanel.style.display = 'block';
          skyPanel.style.opacity = Math.min(1, skyDisplayProgress / 0.08).toString();

          const easedSky = easeInOutCubic(skyDisplayProgress);
          const topInset = !isMobile ? 38 * (1 - easedSky) : 40 * (1 - easedSky);
          const bottomInset = !isMobile ? 38 * (1 - easedSky) : 40 * (1 - easedSky);
          const leftInset = !isMobile ? 38 * (1 - easedSky) : 26 * (1 - easedSky);
          const rightInset = !isMobile ? 38 * (1 - easedSky) : 26 * (1 - easedSky);
          const rad = 16 * (1 - easedSky);

          skyPanel.style.clipPath = `inset(${topInset}% ${rightInset}% ${bottomInset}% ${leftInset}% round ${rad}px)`;

          const plateScale = 1.18 - 0.18 * easedSky;
          if (skyPlate) skyPlate.style.transform = `scale(${plateScale})`;
          if (skyVideo) skyVideo.style.transform = `scale(${plateScale})`;

          // Video playback handling
          if (skyVideo && !videoStarted) {
            videoStarted = true;
            skyVideo.playbackRate = 0.6;
            skyVideo.play().catch(() => {});
            setTimeout(() => {
              skyVideo.style.opacity = '0.78';
            }, 100);
          }

          // Camera Target Scale
          const tgtCamScale = 0.75 + 0.25 * easedSky;

          // Camera Bob & Yaw (Smooth continuous floating motion, no angle snaps)
          let tgtYawDeg = 0;
          let tgtBobY = 0;
          if (p >= 0.64 && p < 0.74) {
            const u = (p - 0.64) / 0.10;
            const eu = easeInOutCubic(u);
            tgtYawDeg = -8 * eu;
            tgtBobY = Math.sin(t * 1.5) * 6 * eu * (isMobile ? 0.75 : 1);
          } else if (p >= 0.74 && p <= 0.88) {
            const u = (p - 0.74) / 0.14;
            const eu = easeInOutCubic(u);
            tgtYawDeg = -8 + 16 * eu;
            tgtBobY = Math.sin(t * 1.5) * 6 * (isMobile ? 0.75 : 1);
          } else if (p > 0.88 && p <= 0.95) {
            const u = (p - 0.88) / 0.07;
            const eu = easeInOutCubic(u);
            tgtYawDeg = 8 * (1 - eu);
            tgtBobY = Math.sin(t * 1.5) * 6 * (1 - eu) * (isMobile ? 0.75 : 1);
          } else if (p > 0.95) {
            tgtYawDeg = 0;
            tgtBobY = 0;
          }

          // Camera Deep Zoom into Lens (0.88 -> 0.97)
          let tgtZoomScale = 1;
          let blackoutOp = 0;
          if (p >= 0.88 && p <= 0.97) {
            const rawQ = (p - 0.88) / 0.09;
            const gateMul = skyDisplayProgress >= 0.85 ? 1 : skyDisplayProgress / 0.85;
            const q = Math.pow(rawQ, 1.7) * gateMul;
            tgtZoomScale = 1 + q * q * 28;

            if (q >= 0.38) {
              blackoutOp = Math.min(1, (q - 0.38) / 0.45);
            }
          } else if (p > 0.97) {
            tgtZoomScale = 29;
            blackoutOp = 1;
          }

          // Smooth Camera Steadicam Interpolation
          const kCam = 1 - Math.pow(1 - 0.10, dt / 16.67);
          curYawDeg += (tgtYawDeg - curYawDeg) * kCam;
          curCamScale += (tgtCamScale - curCamScale) * kCam;
          curZoomScale += (tgtZoomScale - curZoomScale) * kCam;
          curBobY += (tgtBobY - curBobY) * kCam;

          if (cameraWrap) {
            cameraWrap.style.transform = `translate(-50%, -50%) translateY(${curBobY}px) scale(${curCamScale})`;
            cameraWrap.style.opacity = Math.min(1, skyDisplayProgress * 2.2).toString();
          }
          if (cameraInner) {
            cameraInner.style.transform = `rotateY(${curYawDeg}deg) scale(${curZoomScale})`;
          }
          if (blackoutLayer) {
            blackoutLayer.style.opacity = blackoutOp.toString();
          }

          // Sky Words Reveal
          if (skyDisplayProgress > 0.95 && !skyWordsRevealed) {
            skyWordsRevealed = true;
            const times = [0, 120, 240, 450, 570, 690, 810];
            skyWords.forEach((sw, sIdx) => {
              setTimeout(() => {
                sw.style.transition =
                  'opacity 0.6s cubic-bezier(0.2,0,0.2,1), transform 0.6s cubic-bezier(0.2,0,0.2,1), filter 0.6s cubic-bezier(0.2,0,0.2,1)';
                sw.style.opacity = '1';
                sw.style.transform = 'translateY(0)';
                sw.style.filter = 'blur(0px)';
              }, times[sIdx] || 0);
            });
          }
        } else {
          skyPanel.style.display = 'none';
          if (skyVideo && videoStarted) {
            skyVideo.pause();
            videoStarted = false;
            skyVideo.style.opacity = '0';
          }
          skyWordsRevealed = false;
          skyWords.forEach((sw) => {
            sw.style.opacity = '0';
            sw.style.transform = 'translateY(0.3em)';
            sw.style.filter = 'blur(6px)';
          });
        }
      }

      // 5. Dark Navigation Toggle
      if (p > 0.985 || sy >= (manifestoEl?.offsetTop || Infinity) - 100) {
        document.body.classList.add('dark-nav');
      } else {
        document.body.classList.remove('dark-nav');
      }

      // 6. Horizontal Manifesto Track Scroll (950vh)
      const manTop = manifestoEl?.offsetTop || 0;
      const manHeight = (manifestoEl?.offsetHeight || 0) - H;
      const mp = Math.max(0, Math.min(1, (sy - manTop) / manHeight));

      if (sy >= manTop - H * 0.2 && manifestoTrack) {
        const startX = !isMobile ? W * 0.06 : W * 0.08;
        const trackWidth = manifestoTrack.scrollWidth;
        const endX = -(trackWidth - W * 0.9);
        const curX = startX + (endX - startX) * mp;
        manifestoTrack.style.transform = `translate3d(${curX}px, -50%, 0)`;

        const revealThreshold = !isMobile ? W * 0.86 : W * 0.92;

        manifestoChars.forEach((charEl) => {
          if (!charEl.classList.contains('revealed')) {
            const r = charEl.getBoundingClientRect();
            if (r.left <= revealThreshold) {
              const charIdx = parseInt(charEl.getAttribute('data-char-idx') || '0', 10);
              setTimeout(() => {
                charEl.classList.add('revealed');
              }, charIdx * 35);
            }
          }
        });

        manifestoBadges.forEach((badgeEl) => {
          if (!badgeEl.classList.contains('revealed')) {
            const r = badgeEl.getBoundingClientRect();
            if (r.left <= revealThreshold) {
              setTimeout(() => {
                badgeEl.classList.add('revealed');
              }, 120);
            }
          }
        });
      }

      // 7. Chapter 4: Selected Works 3D Track (600vh)
      if (worksEl && worksTrack) {
        const worksTop = worksEl.offsetTop;
        const worksHeight = worksEl.offsetHeight - H;
        const wp = Math.max(0, Math.min(1, (sy - worksTop) / worksHeight));

        if (sy >= worksTop - H * 0.4 && sy <= worksTop + worksHeight + H * 0.4) {
          const trackWidth = worksTrack.scrollWidth;
          const maxShift = Math.max(0, trackWidth - W * 0.72);
          const curX = -(wp * maxShift);
          worksTrack.style.transform = `translate3d(${curX}px, 0, 0)`;

          if (worksProgressFill) {
            worksProgressFill.style.width = `${Math.min(100, Math.max(12, wp * 100))}%`;
          }

          const curProjectIdx = Math.min(3, Math.floor(wp * 4));
          if (worksCounter) {
            const numEl = worksCounter.querySelector('.counter-current');
            if (numEl) numEl.textContent = `0${curProjectIdx + 1}`;
          }

          const cards = worksTrack.querySelectorAll('.works-card');
          cards.forEach((card, idx) => {
            const dist = Math.abs(idx - curProjectIdx);
            const scale = Math.max(0.92, 1 - dist * 0.05);
            (card as HTMLElement).style.transform = `scale(${scale})`;
          });
        }
      }

      // 8. Chapter 5: Services & Apparatus Optical Prism (500vh)
      if (servicesEl) {
        const servTop = servicesEl.offsetTop;
        const servHeight = servicesEl.offsetHeight - H;
        const sp = Math.max(0, Math.min(1, (sy - servTop) / servHeight));

        if (sy >= servTop - H * 0.4 && sy <= servTop + servHeight + H * 0.4) {
          const activeIdx = Math.min(3, Math.floor(sp * 4));
          serviceItems.forEach((item, idx) => {
            if (idx === activeIdx) {
              item.classList.add('active');
            } else {
              item.classList.remove('active');
            }
          });

          if (prismSvg) {
            prismSvg.style.transform = `rotate(${sp * 360}deg)`;
          }

          const serviceSpecs = [
            { title: '01 // ARRI LARGE FORMAT CINEMATOGRAPHY', tags: ['35mm SENSOR', '4.6K RAW', 'EI 800 - 3200', 'T1.5 - T22'] },
            { title: '02 // REAL-TIME UNREAL ENGINE 5.4 WORLDS', tags: ['LUMEN GLOBAL ILLUM', 'NANITE 10B POLYGONS', 'RAYTRACED GLASS', '60FPS DCI'] },
            { title: '03 // MODULAR ANALOG SYNTHESIS & ATMOS', tags: ['EURORACK 16-VOICE', 'DOLBY ATMOS 7.1.4', 'CUSTOM TAPE FOLEY', '96kHz 24-BIT'] },
            { title: '04 // KINETIC BRAND & VARIABLE TYPOGRAPHY', tags: ['OPENTYPE VARIABLE', 'SYSTEM MOTION RULES', 'ANALOG FOIL PACKAGING', 'EDITORIAL PRINT'] },
          ];

          if (readoutTitle && serviceSpecs[activeIdx]) {
            readoutTitle.textContent = serviceSpecs[activeIdx].title;
          }
          if (readoutTags && serviceSpecs[activeIdx]) {
            readoutTags.innerHTML = serviceSpecs[activeIdx].tags
              .map((tag) => `<span class="spec-chip">${tag}</span>`)
              .join('');
          }
        }
      }

      animId = requestAnimationFrame(render);
    }

    animId = requestAnimationFrame(render);

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener('resize', updateScale);
      window.removeEventListener('wheel', onWheel);
    };
  }, []);

  const handleNavClick = (
    target: 'home' | 'process' | 'product' | 'manifesto' | 'works' | 'services' | 'atelier' | 'contact'
  ) => {
    const storyEl = document.getElementById('story');
    const manifestoEl = document.getElementById('manifesto');
    const worksEl = document.getElementById('works');
    const servicesEl = document.getElementById('services');
    const atelierEl = document.getElementById('atelier');
    const contactEl = document.getElementById('contact');

    const storyHeight = (storyEl?.offsetHeight || 0) - window.innerHeight;

    if (target === 'home') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (target === 'process') {
      window.scrollTo({ top: (storyEl?.offsetTop || 0) + storyHeight * 0.2, behavior: 'smooth' });
    } else if (target === 'product') {
      window.scrollTo({ top: (storyEl?.offsetTop || 0) + storyHeight * 0.74, behavior: 'smooth' });
    } else if (target === 'manifesto') {
      if (manifestoEl) window.scrollTo({ top: manifestoEl.offsetTop, behavior: 'smooth' });
    } else if (target === 'works') {
      if (worksEl) window.scrollTo({ top: worksEl.offsetTop, behavior: 'smooth' });
    } else if (target === 'services') {
      if (servicesEl) window.scrollTo({ top: servicesEl.offsetTop, behavior: 'smooth' });
    } else if (target === 'atelier') {
      if (atelierEl) window.scrollTo({ top: atelierEl.offsetTop, behavior: 'smooth' });
    } else if (target === 'contact') {
      if (contactEl) window.scrollTo({ top: contactEl.offsetTop, behavior: 'smooth' });
    }
  };

  return (
    <div ref={containerRef}>
      <SiteNav onNavClick={handleNavClick} />
      <section id="story">
        <HeroHeader />
        <PinnedStage />
      </section>
      <ManifestoSection />
      <WorksSection />
      <ServicesSection />
      <AtelierSection />
      <InquirySection />
    </div>
  );
}
