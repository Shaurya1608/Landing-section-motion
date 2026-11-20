export default function CtaButtons() {
  return (
    <div className="flex flex-wrap gap-3 font-semibold">
      <button
        type="button"
        className="pointer-events-auto bg-primary text-primary-foreground px-6 py-3 md:px-8 md:py-4 text-sm rounded-sm cursor-pointer hover:brightness-110 transition-all active:scale-[0.97]"
      >
        View Portfolio
      </button>
      <button
        type="button"
        className="pointer-events-auto bg-white text-background px-6 py-3 md:px-8 md:py-4 text-sm rounded-sm cursor-pointer hover:brightness-90 transition-all active:scale-[0.97]"
      >
        Let&rsquo;s Work Together
      </button>
    </div>
  )
}
