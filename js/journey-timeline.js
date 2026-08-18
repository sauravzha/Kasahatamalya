/**
 * Journey Timeline 2.5D Experience
 */

const milestones = [
  {
    year: "2016",
    title: "The Beginning",
    description: "Where the journey started. A small seed planted in a rural landscape, focused on creating equitable education.",
    visual: "/assets/timeline/2016_beginning.png",
    yPos: 0
  },
  {
    year: "2017",
    title: "First Programmes",
    description: "Learning took flight. Children, educators, and communities coming together through initial learning activities and play.",
    visual: "/assets/timeline/2017_programmes.png",
    yPos: 200
  },
  {
    year: "2018",
    title: "Into Delhi",
    description: "Expanding our footprint. Bringing our vision to the urban environment of Delhi, connecting city and school.",
    visual: "/assets/timeline/2018_delhi.png",
    yPos: 400
  },
  {
    year: "2019",
    title: "Curriculum With the State",
    description: "Partnering for deeper impact. Opening new chapters with state-level curriculum integration.",
    visual: "/assets/timeline/2019_curriculum.png",
    yPos: 600
  },
  {
    year: "2020",
    title: "Pandemic & Radio",
    description: "Adaptation and resilience. Reaching children at home through radio waves and community networks.",
    visual: "/assets/timeline/2020_radio.png",
    yPos: 800
  },
  {
    year: "2021",
    title: "Institutional Footing",
    description: "Building strong foundations. Establishing solid partnerships and institutional stability.",
    visual: "/assets/timeline/2021_institution.png",
    yPos: 1000
  },
  {
    year: "2022",
    title: "Into Bihar",
    description: "Scaling across states. Expanding our model into Bihar, building new community connections.",
    visual: "/assets/timeline/2022_bihar.png",
    yPos: 1200
  },
  {
    year: "2023",
    title: "Recognised Globally",
    description: "Global acknowledgment of our grassroots work, bringing local impact to the world stage.",
    visual: "/assets/timeline/2023_global.png",
    yPos: 1400
  },
  {
    year: "2025",
    title: "Adopted by the System",
    description: "System-level transformation. Our models officially adopted by government bodies like the MCD.",
    visual: "/assets/timeline/2025_system.png",
    yPos: 1600
  },
  {
    year: "2026",
    title: "The Next Chapter",
    description: "The first decade taught us how to begin. The next will teach us how to deepen. The roots grow wider.",
    visual: "/assets/timeline/2026_future.png",
    yPos: 1800,
    isEnd: true
  }
];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("journey-timeline-container");
  if (!container) return;

  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1. Build Navigation
  const navHTML = `
    <div class="jt-nav">
      <div class="jt-nav-inner">
        ${milestones.map(m => `<a href="#jt-${m.year}" class="jt-nav-item" data-year="${m.year}">${m.year}</a>`).join('')}
      </div>
    </div>
  `;

  // 2. Build Milestones HTML
  let nodesHTML = '';
  milestones.forEach((m, index) => {
    nodesHTML += `
      <div class="jt-milestone ${m.isEnd ? 'jt-milestone-end' : ''}" id="jt-${m.year}" data-index="${index}">
        <div class="jt-content">
          <div class="jt-year">${m.year}</div>
          <h3 class="jt-milestone-title">${m.title}</h3>
          <p class="jt-milestone-desc">${m.description}</p>
        </div>
        
        <div class="jt-marker" id="jt-marker-${index}"></div>

        <div class="jt-visual">
          <div class="jt-visual-inner">
            <!-- We use empty divs with fallback background colors in case images are missing initially -->
            <img src="${m.visual}" alt="${m.title}" class="jt-scene-image" onerror="this.style.display='none'; this.parentElement.style.background='var(--jt-line)'; this.parentElement.style.borderRadius='50%';" loading="lazy">
          </div>
        </div>
      </div>
    `;
  });

  // 3. Inject HTML
  container.innerHTML = `
    ${navHTML}
    <div class="jt-svg-container">
      <svg width="100%" height="100%" preserveAspectRatio="none" id="jt-svg">
        <path class="jt-path-bg" id="jt-path-bg" />
        <path class="jt-path-active" id="jt-path-active" />
      </svg>
    </div>
    ${nodesHTML}
  `;

  // 4. Setup Scroll Logic and SVG Path
  const milestoneEls = document.querySelectorAll('.jt-milestone');
  const navItems = document.querySelectorAll('.jt-nav-item');
  const pathBg = document.getElementById('jt-path-bg');
  const pathActive = document.getElementById('jt-path-active');

  function drawPath() {
    if (window.innerWidth <= 900) {
      pathBg.setAttribute('d', '');
      pathActive.setAttribute('d', '');
      return;
    }

    let d = '';
    const containerRect = container.getBoundingClientRect();
    
    milestoneEls.forEach((el, index) => {
      const marker = document.getElementById(`jt-marker-${index}`);
      if (!marker) return;

      const rect = marker.getBoundingClientRect();
      // Calculate position relative to the container
      const x = rect.left + rect.width / 2 - containerRect.left;
      const y = rect.top + rect.height / 2 - containerRect.top + window.scrollY - (containerRect.top + window.scrollY - container.offsetTop); // adjust for relative positioning
      
      // Simple approximation for relative Y inside container
      const relativeY = el.offsetTop + (el.offsetHeight / 2);
      const relativeX = container.offsetWidth / 2; // markers are 50% left

      if (index === 0) {
        d += `M ${relativeX} ${relativeY} `;
      } else {
        // Create an organic bezier curve between points
        const prevEl = milestoneEls[index - 1];
        const prevY = prevEl.offsetTop + (prevEl.offsetHeight / 2);
        const cp1Y = prevY + (relativeY - prevY) / 2;
        const cp2Y = prevY + (relativeY - prevY) / 2;
        
        // Alternate curve bowing
        const bow = (index % 2 === 0) ? 150 : -150;
        
        d += `C ${relativeX + bow} ${cp1Y}, ${relativeX - bow} ${cp2Y}, ${relativeX} ${relativeY} `;
      }
    });

    pathBg.setAttribute('d', d);
    pathActive.setAttribute('d', d);

    // Setup dash array for drawing animation
    const length = pathBg.getTotalLength();
    if (length > 0) {
      pathActive.style.strokeDasharray = length;
      pathActive.style.strokeDashoffset = length;
    }
  }

  // Draw initially and on resize
  setTimeout(drawPath, 100);
  window.addEventListener('resize', () => {
    requestAnimationFrame(drawPath);
  });

  // 5. Scroll Interaction Observer
  let currentIndex = 0;

  const observerOptions = {
    root: null,
    rootMargin: '-30% 0px -40% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const index = parseInt(entry.target.getAttribute('data-index'));
        currentIndex = index;
        updateActiveState(index);
      }
    });
  }, observerOptions);

  milestoneEls.forEach(el => observer.observe(el));

  function updateActiveState(activeIndex) {
    milestoneEls.forEach((el, idx) => {
      if (idx === activeIndex) {
        el.classList.add('is-active');
        el.classList.remove('is-past');
      } else if (idx < activeIndex) {
        el.classList.remove('is-active');
        el.classList.add('is-past');
      } else {
        el.classList.remove('is-active', 'is-past');
      }
    });

    navItems.forEach((nav, idx) => {
      if (idx === activeIndex) {
        nav.classList.add('is-active');
      } else {
        nav.classList.remove('is-active');
      }
    });
  }

  // Handle path drawing on scroll
  if (!isReducedMotion) {
    window.addEventListener('scroll', () => {
      requestAnimationFrame(() => {
        if (window.innerWidth <= 900) return;
        
        const pathLength = pathBg.getTotalLength();
        if (pathLength === 0) return;

        // Calculate how far down the timeline we are
        const containerRect = container.getBoundingClientRect();
        const viewportCenter = window.innerHeight * 0.6;
        
        // Progress based on container bounds
        let progress = (viewportCenter - containerRect.top) / containerRect.height;
        progress = Math.max(0, Math.min(1, progress));
        
        // Offset is length - (length * progress)
        const offset = pathLength - (pathLength * progress);
        pathActive.style.strokeDashoffset = offset;
      });
    }, { passive: true });
  } else {
    // If reduced motion, just draw the whole path
    setTimeout(() => {
      const pathLength = pathBg.getTotalLength();
      pathActive.style.strokeDashoffset = 0;
    }, 500);
  }

  // Smooth scroll for nav items
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = item.getAttribute('href');
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        const offset = window.innerHeight * 0.3; // position target slightly below center
        const top = targetEl.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // Initial trigger
  updateActiveState(0);
});
