import { lazy, Suspense } from "react"

const Spline = lazy(() => import("@splinetool/react-spline"))

export default function SplineBackground() {
  return (
    <>
      <div className="absolute inset-0">
        <Suspense fallback={<div className="absolute inset-0 bg-hero-bg" />}>
          <Spline
            scene="https://prod.spline.design/Slk6b8kz3LRlKiyk/scene.splinecode"
            className="w-full h-full"
          />
        </Suspense>
      </div>
      <div className="absolute inset-0 bg-black/30 z-[1] pointer-events-none" />
    </>
  )
}
