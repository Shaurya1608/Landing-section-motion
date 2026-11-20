import { useState } from 'react'
import { motion } from 'framer-motion'
import { ArrowUpRight, X } from 'lucide-react'

const NAV_LINKS = ['Story', 'Expertise', 'Studios', 'Feedback']
const STATS = [
  { number: '300', label: 'CRAFTED\nBRANDS' },
  { number: '200', label: 'DIGITAL\nPRODUCTS' },
  { number: '100', label: 'VENTURES\nFUNDED' },
]
const HEADING_WORDS = ['Fearless', 'Vision', 'Delivered']

const fadeDown = {
  hidden: { opacity: 0, y: -20 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.1, duration: 0.5, ease: [0.22, 1, 0.36, 1] },
  }),
}

const fadeUp = {
  hidden: { opacity: 0, y: 32 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.12, duration: 0.6, ease: [0.22, 1, 0.36, 1] },
  }),
}

export default function HeroSection() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <div className="relative min-h-screen w-full font-inter font-semibold tracking-widest uppercase text-black overflow-hidden">
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute inset-0 w-full h-full object-cover"
      >
        <source
          src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260517_222138_3e3205be-3364-417b-a64a-bfe087acbec4.mp4"
          type="video/mp4"
        />
      </video>

      <div className="relative z-10 flex flex-col min-h-screen">
        <nav className="flex items-center justify-between px-5 sm:px-8 md:px-12 pt-5 md:pt-6">
          <motion.div
            custom={0}
            variants={fadeDown}
            initial="hidden"
            animate="visible"
            className="w-8 h-8 rounded-full border-2 border-accent flex items-center justify-center"
          >
            <div className="w-[10px] h-[10px] rounded-full bg-accent" />
          </motion.div>

          <div className="hidden md:flex items-center gap-8">
            {NAV_LINKS.map((link, i) => (
              <motion.a
                key={link}
                custom={i + 1}
                variants={fadeDown}
                initial="hidden"
                animate="visible"
                href="#"
                className="text-sm text-black no-underline"
              >
                {link}
              </motion.a>
            ))}
          </div>

          <motion.button
            custom={5}
            variants={fadeDown}
            initial="hidden"
            animate="visible"
            onClick={() => setMenuOpen(true)}
            className="w-9 h-9 rounded-full bg-black flex flex-col items-center justify-center gap-1 cursor-pointer"
            aria-label="Open menu"
          >
            <span className="w-4 h-0.5 bg-white block" />
            <span className="w-4 h-0.5 bg-white block" />
            <span className="w-4 h-0.5 bg-white block" />
          </motion.button>
        </nav>

        <div className="flex-1 flex items-center justify-end px-5 sm:px-8 md:px-12 py-8 md:py-0">
          <div className="flex items-center gap-5 sm:gap-8 md:gap-10">
            {STATS.map((stat, i) => (
              <motion.div
                key={stat.label}
                custom={i + 2}
                variants={fadeUp}
                initial="hidden"
                animate="visible"
                className="text-right"
              >
                <div style={{ fontSize: 'clamp(1.5rem, 5vw, 3.5rem)' }}>
                  <span className="text-accent" style={{ fontSize: '0.5em' }}>+</span>
                  <span className="text-black">{stat.number}</span>
                </div>
                <div className="text-[10px] sm:text-xs md:text-sm text-black whitespace-pre-line leading-tight">
                  {stat.label}
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        <div className="px-5 sm:px-8 md:px-12 pb-8 md:pb-12 flex flex-col gap-6 md:gap-12">
          <div className="flex items-center justify-between gap-4">
            <motion.p
              custom={5}
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              className="text-[10px] sm:text-xs md:text-sm text-black max-w-[130px] sm:max-w-[160px] md:max-w-xs"
            >
              Shaping Bold<br />Visions Into Power<br />For Your Tribe
            </motion.p>
            <motion.a
              custom={6}
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              href="#"
              className="text-accent text-base sm:text-xl md:text-2xl whitespace-nowrap no-underline flex items-center gap-1"
            >
              Work With Us
              <ArrowUpRight size={22} className="hidden sm:block" />
              <ArrowUpRight size={18} className="sm:hidden" />
            </motion.a>
          </div>

          <div className="flex items-end justify-between gap-3 sm:gap-4">
            <motion.div
              custom={7}
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              className="w-[120px] sm:w-[180px] md:w-[280px] shrink-0"
            >
              <p className="text-[9px] sm:text-xs md:text-sm text-black text-left md:text-right">
                Creative Studios Built Around Elevating Your Vision Into Striking Reality
              </p>
            </motion.div>
            <div
              className="text-right text-black"
              style={{ fontSize: 'clamp(2rem, 9vw, 9rem)', lineHeight: 0.88 }}
            >
              {HEADING_WORDS.map((word, i) => (
                <div key={word} className="overflow-hidden">
                  <motion.div
                    initial={{ y: '110%' }}
                    animate={{ y: 0 }}
                    transition={{
                      delay: 0.4 + i * 0.14,
                      duration: 0.7,
                      ease: [0.22, 1, 0.36, 1],
                    }}
                  >
                    {word}
                  </motion.div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {menuOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.3 }}
          className="fixed inset-0 z-50 bg-white flex flex-col px-5 sm:px-8 md:px-12 pt-5 md:pt-6 pb-8 md:pb-12"
        >
          <div className="flex items-center justify-between">
            <div className="w-8 h-8 rounded-full border-2 border-accent flex items-center justify-center">
              <div className="w-[10px] h-[10px] rounded-full bg-accent" />
            </div>
            <button
              onClick={() => setMenuOpen(false)}
              className="w-9 h-9 rounded-full bg-black flex items-center justify-center cursor-pointer"
              aria-label="Close menu"
            >
              <X size={18} color="white" />
            </button>
          </div>

          <div className="flex flex-col gap-8 mt-16">
            {NAV_LINKS.map((link) => (
              <a
                key={link}
                href="#"
                className="text-3xl font-semibold tracking-widest uppercase text-black no-underline"
              >
                {link}
              </a>
            ))}
          </div>

          <div className="mt-auto">
            <a
              href="#"
              className="text-accent text-xl font-semibold tracking-widest uppercase no-underline inline-flex items-center gap-2"
            >
              Work With Us
              <ArrowUpRight size={22} />
            </a>
          </div>
        </motion.div>
      )}
    </div>
  )
}
