const navLinks = [
  "Services",
  "About Us",
  "Projects",
  "Team",
  "Contacts",
]

export default function NavLinks() {
  return (
    <div className="hidden md:flex gap-8">
      {navLinks.map((link) => (
        <a
          key={link}
          href={`#${link.toLowerCase().replace(/\s+/g, "-")}`}
          className="text-sm text-muted-foreground hover:text-foreground transition-colors uppercase tracking-widest"
        >
          {link}
        </a>
      ))}
    </div>
  )
}
