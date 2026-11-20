const clients = [
  "Color Zebra",
  "FlatInRanchi",
  "NovaStudio",
  "PixelCraft",
  "BrandForge",
  "UrbanWave",
]

export default function TrustedClients() {
  return (
    <section className="w-full bg-hero-bg border-t border-border/40 py-16 md:py-24">
      <div className="max-w-6xl mx-auto px-6 md:px-10">
        <h2 className="text-center text-2xl md:text-3xl font-semibold tracking-tight text-foreground mb-12 opacity-0 animate-fade-up">
          Brands We&rsquo;ve Worked With
        </h2>

        <div className="flex flex-wrap justify-center gap-6 md:gap-10">
          {clients.map((name, i) => (
            <div
              key={name}
              className="w-40 h-20 md:w-48 md:h-24 flex items-center justify-center border border-border/30 rounded-lg bg-secondary/20 opacity-0 animate-fade-up"
              style={{ animationDelay: `${0.2 + i * 0.1}s` }}
            >
              <span className="text-muted-foreground/50 text-sm md:text-base font-medium tracking-wide uppercase">
                {name}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
