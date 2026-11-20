import SplineBackground from "./SplineBackground"
import HeroContent from "./HeroContent"

export default function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-hero-bg overflow-hidden">
      <SplineBackground />
      <HeroContent />
    </section>
  )
}
