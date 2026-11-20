import { useEffect } from 'react';
import { HeroSection } from './components/HeroSection';
import { MarqueeSection } from './components/MarqueeSection';
import { AboutSection } from './components/AboutSection';
import { ServicesSection } from './components/ServicesSection';
import { ProjectsSection } from './components/ProjectsSection';

function App() {
  // Smooth scroll for anchor links
  useEffect(() => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const href = anchor.getAttribute('href');
        if (href) {
          const target = document.querySelector(href);
          if (target) {
            target.scrollIntoView({
              behavior: 'smooth'
            });
          }
        }
      });
    });
  }, []);

  return (
    <div className="main-wrapper font-sans text-white bg-[#0C0C0C]">
      <HeroSection />
      <MarqueeSection />
      <AboutSection />
      <ServicesSection />
      <ProjectsSection />
      
      {/* Simple Footer */}
      <footer id="contact" className="bg-[#0C0C0C] py-10 text-center border-t border-[#D7E2EA]/10 relative z-20">
        <p className="text-[#D7E2EA]/50 text-sm font-light uppercase tracking-widest">
          © {new Date().getFullYear()} Jack. All rights reserved.
        </p>
      </footer>
    </div>
  );
}

export default App;
