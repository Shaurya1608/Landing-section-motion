import { Button } from "./ui/button"
import NavLinks from "./NavLinks"

export default function Navbar() {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 lg:px-16 py-5">
      <div className="text-foreground text-xl font-semibold tracking-tight">
        SENTINEL
      </div>

      <NavLinks />

      <Button
        variant="navCta"
        size="lg"
        className="hidden md:inline-flex rounded-lg uppercase text-xs tracking-widest px-6"
      >
        Get Quote
      </Button>
    </nav>
  )
}
