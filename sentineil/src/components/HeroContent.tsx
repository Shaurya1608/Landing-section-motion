import CtaButtons from "./CtaButtons"

export default function HeroContent() {
  return (
    <div className="relative z-10 pointer-events-none w-full max-w-lg mx-auto px-6">
      <h1
        className="text-[clamp(1.5rem,3.5vw,2.75rem)] font-semibold leading-[1.2] tracking-[-0.02em] text-foreground mb-4 opacity-0 animate-fade-up"
        style={{ animationDelay: "0.2s" }}
      >
        We Build Brands{" "}
        <span className="text-primary font-bold">People Remember.</span>
      </h1>

      <p
        className="text-muted-foreground text-[clamp(0.8rem,1.1vw,0.9rem)] font-light leading-[1.7] mb-7 opacity-0 animate-fade-up"
        style={{ animationDelay: "0.4s" }}
      >
        Trenvity is a creative digital marketing agency focused on cinematic
        content, branding, reels, social media strategy, Meta Ads, and Google
        Ads for modern businesses.
      </p>

      <div
        className="opacity-0 animate-fade-up"
        style={{ animationDelay: "0.6s" }}
      >
        <CtaButtons />
      </div>
    </div>
  )
}
