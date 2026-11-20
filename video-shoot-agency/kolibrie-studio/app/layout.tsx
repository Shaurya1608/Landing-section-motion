import type { Metadata } from 'next';
import Script from 'next/script';
import './globals.css';

export const metadata: Metadata = {
  title: 'Solaria Studio',
  description: 'Solaria: a small studio for scroll-stopping reels, films and motion.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <Script src="/libs/gsap.min.js" strategy="beforeInteractive" />
        <Script src="/libs/ScrollTrigger.min.js" strategy="beforeInteractive" />
        <Script src="/libs/SplitText.min.js" strategy="beforeInteractive" />
        <Script src="/libs/DrawSVGPlugin.min.js" strategy="beforeInteractive" />
        <Script src="/libs/InertiaPlugin.min.js" strategy="beforeInteractive" />
        <Script src="/libs/lenis.min.js" strategy="beforeInteractive" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
