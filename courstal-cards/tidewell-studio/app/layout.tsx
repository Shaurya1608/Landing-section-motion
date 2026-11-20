import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Tidewell — Tides in Motion',
  description: 'Four-part coastal motion studio scroll story.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
