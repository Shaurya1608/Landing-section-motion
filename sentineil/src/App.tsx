import Navbar from "./components/Navbar"
import HeroSection from "./components/HeroSection"
import TrustedClients from "./components/TrustedClients"

export default function App() {
  return (
    <div className="bg-hero-bg min-h-screen">
      <Navbar />
      <HeroSection />
      <TrustedClients />
    </div>
  )
}
