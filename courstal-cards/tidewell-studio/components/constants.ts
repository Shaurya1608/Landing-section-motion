export const ASSETS = {
  // Studio Editorial Visuals
  card0: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=900&q=85', // Warm amber editorial portrait
  card1: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=85', // Modern warm architecture & lighting
  card2: 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=900&q=85', // Warm cinematic lighting
  card3: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=900&q=85', // Minimalist warm interior studio
  card4: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=900&q=85', // Warm classical sculpture & oil
  card5: 'https://images.unsplash.com/photo-1518895949257-7621c3c786d7?auto=format&fit=crop&w=900&q=85', // Golden hour fashion motion
  card6: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=900&q=85', // Warm studio cinema setup
  card7: 'https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=900&q=85', // Vintage film camera
  card8: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=900&q=85', // Warm studio direction
  card9: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=900&q=85', // Warm fluid glass art
  card10: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=900&q=85', // Golden sunset architectural reflection
  card11: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=900&q=85', // Warm natural editorial light

  // Process chip
  process_chip: 'https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=300&q=85',

  // Sky / Viewport panel
  sky_plate: 'https://images.unsplash.com/photo-1495616811223-4d98c6e9c869?auto=format&fit=crop&w=2400&q=85', // Warm golden sunset sky
  sky_video: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261118_065029_a6ae2ebb-cd79-41fd-ae60-6b66fdda04ee.mp4',
  camera_1400: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261118_061547_10365665-40d3-4390-944f-7bcb10dc6d4a.png&w=1400&q=85',
  sticker_plane: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png&w=1200&q=85',
  sticker_sheet_700: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261118_061547_979f8673-f904-4102-90a0-6458bce33bc8.png&w=700&q=85'
};

export interface CardDef {
  image: string;
  pos: string;
  alt: string;
}

export const CARDS_DATA: CardDef[] = [
  { image: ASSETS.card0, pos: 'center', alt: 'Warm amber editorial portrait' },
  { image: ASSETS.card1, pos: 'center', alt: 'Modern warm architectural space' },
  { image: ASSETS.card2, pos: 'center', alt: 'Cinematic warm lighting' },
  { image: ASSETS.card3, pos: 'center', alt: 'Minimalist warm interior studio' },
  { image: ASSETS.card4, pos: 'center', alt: 'Sculptural fine art study' },
  { image: ASSETS.card5, pos: 'center', alt: 'Golden hour motion cinematography' },
  { image: ASSETS.card6, pos: 'center', alt: 'Film studio production lighting' },
  { image: ASSETS.card7, pos: 'center', alt: 'Analog medium format camera' },
  { image: ASSETS.card8, pos: 'center', alt: 'Creative studio direction' },
  { image: ASSETS.card9, pos: 'center', alt: 'Warm ambient fluid glasswork' },
  { image: ASSETS.card10, pos: 'center', alt: 'Golden architectural reflection' },
  { image: ASSETS.card11, pos: 'center', alt: 'Warm natural light portrait' }
];

export const CARD_RISES = [0.53, 0.67, 0.81, 0.95, 1.09, 1.23];
export const CARD_ORDER = [2, 3, 1, 4, 0, 5];

export const PLANE_POINTS = [
  [0.33, -3, 73],
  [0.45, 4, 71],
  [0.60, 13, 65],
  [0.70, 22, 55],
  [0.80, 31, 44],
  [0.87, 32.5, 47.5],
  [0.93, 26, 48],
  [1.00, 21.5, 45],
  [1.07, 22.5, 51.5],
  [1.15, 27, 52],
  [1.27, 45, 41]
];

export function easeInOutCubic(t: number): number {
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

export function easeGlide(t: number): number {
  return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
}

export function stepR(R: number, cw: number): number {
  return 2 * Math.asin((1.05 * cw) / (2 * R));
}
