document.addEventListener('DOMContentLoaded', () => {
  // Check for reduced motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── NAVBAR ──
  initNavbar();

  // ── SCROLL REVEALS ──
  if (!prefersReducedMotion) {
    initScrollReveals();
  } else {
    // Show all elements immediately
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
      el.classList.add('visible');
    });
  }

  // ── ANIMATED COUNTERS ──
  initCounters();

  // ── 3D CARD TILT ──
  if (!prefersReducedMotion) {
    initCardTilt();
  }

  // ── SMOOTH SCROLL ──
  initSmoothScroll();

  // ── HERO WORD ANIMATION ──
  if (!prefersReducedMotion) {
    initHeroAnimation();
  }

  // ── PARALLAX DOODLES ──
  if (!prefersReducedMotion) {
    initParallaxDoodles();
  }

  // ── MAGNETIC BUTTONS ──
  if (!prefersReducedMotion) {
    initMagneticButtons();
  }

  // ── SVG DRAW ON SCROLL ──
  if (!prefersReducedMotion) {
    initSvgDrawOnScroll();
  }

  // ── VALUE CARD WIGGLE ──
  if (!prefersReducedMotion) {
    initValueCardWiggle();
  }

  // ── CUSTOM CURSOR ──
  if (!prefersReducedMotion && window.matchMedia('(hover: hover)').matches) {
    initCustomCursor();
  }

  // ── HOVER IMAGE REVEAL ──
  if (!prefersReducedMotion && window.matchMedia('(hover: hover)').matches) {
    initHoverReveal();
  }
});


/* ── Navbar Scroll & Mobile Menu ── */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.querySelector('.navbar__hamburger');
  const mobileMenu = document.querySelector('.navbar__mobile-menu');

  // Scroll effect
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
  }, { passive: true });

  // Mobile menu toggle
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
    });

    // Close mobile menu on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }

  // Close mobile menu on escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu?.classList.contains('active')) {
      hamburger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}


/* ── Scroll-Triggered Reveals ── */
function initScrollReveals() {
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  
  if (!revealElements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        const parent = entry.target.closest('[data-stagger]');
        if (parent) {
          const siblings = parent.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
          const siblingIndex = Array.from(siblings).indexOf(entry.target);
          entry.target.style.transitionDelay = `${siblingIndex * 0.08}s`;
        }
        
        entry.target.classList.add('visible');
      } else {
        entry.target.classList.remove('visible');
        entry.target.style.transitionDelay = '0s';
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => observer.observe(el));
}


/* ── Animated Counters ── */
function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
        animateCounter(entry.target);
        entry.target.classList.add('counted');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.5
  });

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-count'));
  const suffix = el.getAttribute('data-suffix') || '';
  const duration = 1500; // ms
  const startTime = performance.now();

  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easedProgress = easeOutQuart(progress);
    const currentValue = Math.floor(easedProgress * target);

    el.textContent = formatNumber(currentValue) + suffix;

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      el.textContent = formatNumber(target) + suffix;
      // Trigger sparkle animation
      const sparkle = el.closest('.stat-card')?.querySelector('.stat-card__sparkle');
      if (sparkle) {
        sparkle.style.opacity = '1';
        sparkle.classList.add('anim-sparkle');
      }
    }
  }

  requestAnimationFrame(update);
}

function formatNumber(num) {
  if (num >= 1000) {
    return num.toLocaleString('en-IN');
  }
  return num.toString();
}


/* ── 3D Card Tilt (enhanced with inner Z-axis parallax) ── */
function initCardTilt() {
  const cards = document.querySelectorAll('[data-tilt]');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = (y - centerY) / centerY * -8;
      const rotateY = (x - centerX) / centerX * 8;
      
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px) scale(1.02)`;

      // Inner element parallax — lift icons/titles forward in Z
      const icon = card.querySelector('.program-card__icon');
      const title = card.querySelector('.program-card__name');
      if (icon) {
        const moveX = (x - centerX) / centerX * 5;
        const moveY = (y - centerY) / centerY * 5;
        icon.style.transform = `translateZ(30px) translate(${moveX}px, ${moveY}px) scale(1.1)`;
      }
      if (title) {
        const moveX = (x - centerX) / centerX * 3;
        const moveY = (y - centerY) / centerY * 3;
        title.style.transform = `translateZ(15px) translate(${moveX}px, ${moveY}px)`;
      }
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
      card.style.transition = 'transform 0.5s ease-out';

      const icon = card.querySelector('.program-card__icon');
      const title = card.querySelector('.program-card__name');
      if (icon) {
        icon.style.transform = 'translateZ(0) translate(0, 0) scale(1)';
        icon.style.transition = 'transform 0.5s ease-out';
      }
      if (title) {
        title.style.transform = 'translateZ(0) translate(0, 0)';
        title.style.transition = 'transform 0.5s ease-out';
      }
    });

    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 0.1s ease-out';
      const icon = card.querySelector('.program-card__icon');
      const title = card.querySelector('.program-card__name');
      if (icon) icon.style.transition = 'transform 0.1s ease-out';
      if (title) title.style.transition = 'transform 0.1s ease-out';
    });
  });
}


/* ── Smooth Scroll ── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (targetId === '#') return;
      
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const navbarHeight = document.querySelector('.navbar')?.offsetHeight || 0;
        const targetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}


/* ── Hero Word Animation ── */
function initHeroAnimation() {
  const heroTitle = document.querySelector('.hero__title');
  if (!heroTitle || heroTitle.dataset.animated) return;

  heroTitle.dataset.animated = 'true';
  const words = heroTitle.querySelectorAll('.word');
  
  words.forEach((word, index) => {
    word.style.opacity = '0';
    word.style.transform = 'translateY(20px)';
    word.style.transition = `all 0.6s cubic-bezier(0.16, 1, 0.3, 1) ${0.3 + index * 0.06}s`;
    
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        word.style.opacity = '1';
        word.style.transform = 'translateY(0)';
      });
    });
  });
}


/* ── Timeline Scroll Draw ── */
function initTimelineDraw() {
  const timelinePath = document.querySelector('.timeline__path');
  if (!timelinePath) return;

  const pathLength = timelinePath.getTotalLength();
  timelinePath.style.strokeDasharray = pathLength;
  timelinePath.style.strokeDashoffset = pathLength;

  window.addEventListener('scroll', () => {
    const timelineSection = timelinePath.closest('.timeline');
    if (!timelineSection) return;

    const rect = timelineSection.getBoundingClientRect();
    const scrollPercent = Math.max(0, Math.min(1, 
      (window.innerHeight - rect.top) / (rect.height + window.innerHeight)
    ));

    timelinePath.style.strokeDashoffset = pathLength * (1 - scrollPercent);
  }, { passive: true });
}


/* ── Parallax Doodles ── */
function initParallaxDoodles() {
  const doodles = document.querySelectorAll('[data-parallax-speed]');
  if (!doodles.length) return;

  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollY = window.pageYOffset;

        doodles.forEach(doodle => {
          const speed = parseFloat(doodle.getAttribute('data-parallax-speed')) || 0.3;
          const rect = doodle.closest('section')?.getBoundingClientRect();
          if (!rect) return;

          // Only apply parallax when section is in view
          if (rect.top < window.innerHeight && rect.bottom > 0) {
            const offset = scrollY * speed;
            const rotateAmount = Math.sin(scrollY * 0.002) * 5 * speed;
            doodle.style.transform = `translateY(${-offset % 60}px) rotate(${rotateAmount}deg)`;
          }
        });

        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}


/* ── Magnetic Buttons ── */
function initMagneticButtons() {
  const buttons = document.querySelectorAll('.btn--primary, .btn--donate, .btn--secondary');

  buttons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;

      btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px) scale(1.05)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0, 0) scale(1)';
      btn.style.transition = 'transform 0.4s var(--ease-spring)';
    });

    btn.addEventListener('mouseenter', () => {
      btn.style.transition = 'transform 0.15s ease-out';
    });
  });
}


/* ── SVG Draw On Scroll ── */
function initSvgDrawOnScroll() {
  const drawElements = document.querySelectorAll('.doodle-circle-draw, .doodle-squiggle-draw');
  if (!drawElements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.5
  });

  drawElements.forEach(el => observer.observe(el));
}


/* ── Value Card Wiggle on Hover ── */
function initValueCardWiggle() {
  const valueCards = document.querySelectorAll('.value-card-3d');

  valueCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const icon = card.querySelector('h3');
      if (icon) {
        icon.classList.add('anim-wiggle');
        icon.addEventListener('animationend', () => {
          icon.classList.remove('anim-wiggle');
        }, { once: true });
      }
    });
  });
}


/* ── Button Squish Effect ── */
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.btn');
  if (btn) {
    btn.classList.add('anim-squish');
    btn.addEventListener('animationend', () => {
      btn.classList.remove('anim-squish');
    }, { once: true });
  }
});


/* ── Custom Smart Cursor ── */
function initCustomCursor() {
  const cursor = document.getElementById('cursor');
  if (!cursor) return;

  const dot = cursor.querySelector('.cursor__dot');
  const ring = cursor.querySelector('.cursor__ring');
  const label = cursor.querySelector('.cursor__label');

  let mouseX = 0, mouseY = 0;
  let cursorX = 0, cursorY = 0;
  let ringX = 0, ringY = 0;

  document.body.classList.add('custom-cursor-active');

  // Track mouse position
  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  // Smooth follow with lag
  function updateCursor() {
    // Dot follows closely
    cursorX += (mouseX - cursorX) * 0.25;
    cursorY += (mouseY - cursorY) * 0.25;
    
    // Ring follows with more lag
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;

    dot.parentElement.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
    ring.style.transform = `translate(${ringX - cursorX}px, ${ringY - cursorY}px)`;

    requestAnimationFrame(updateCursor);
  }
  updateCursor();

  // Interactive elements config: [selector, label]
  const interactiveElements = [
    ['.btn', 'Click'],
    ['.program-card', 'Explore'],
    ['.navbar__link', 'Go'],
    ['.navbar__dropdown-item', 'Go'],
    ['a[href]', ''],
    ['.value-card-3d', 'View'],
    ['.team-card', 'Meet'],
    ['img', 'View'],
  ];

  // Hover detection
  document.addEventListener('mouseover', (e) => {
    for (const [selector, text] of interactiveElements) {
      const match = e.target.closest(selector);
      if (match) {
        cursor.classList.add('cursor--hover');
        if (text && label) label.textContent = text;
        return;
      }
    }
  });

  document.addEventListener('mouseout', (e) => {
    for (const [selector] of interactiveElements) {
      if (e.target.closest(selector)) {
        cursor.classList.remove('cursor--hover');
        if (label) label.textContent = '';
        return;
      }
    }
  });

  // Click effect
  document.addEventListener('mousedown', () => {
    cursor.classList.add('cursor--click');
  });
  document.addEventListener('mouseup', () => {
    cursor.classList.remove('cursor--click');
  });

  // Hide when mouse leaves window
  document.addEventListener('mouseleave', () => {
    cursor.style.opacity = '0';
  });
  document.addEventListener('mouseenter', () => {
    cursor.style.opacity = '1';
  });
}


/* ── Hover Image Reveal (on Program Cards) ── */
function initHoverReveal() {
  const reveal = document.getElementById('hover-reveal');
  if (!reveal) return;

  const revealImg = reveal.querySelector('.hover-reveal__img');

  // Map program card names to images
  const imageMap = {
    'school excellence program': '/assets/photos/pic1.jpg',
    'teacher support program': '/assets/photos/pic2.jpg',
    'fale fale shiksha muhim': '/assets/photos/pic1.jpg',
    'learning festivals internship': '/assets/photos/pic2.jpg',
    'star parents': '/assets/photos/pic1.jpg',
  };

  let isRevealing = false;
  let targetX = 0, targetY = 0;
  let currentX = 0, currentY = 0;

  function animateReveal() {
    if (!isRevealing) return;

    currentX += (targetX - currentX) * 0.1;
    currentY += (targetY - currentY) * 0.1;

    reveal.style.left = `${currentX + 20}px`;
    reveal.style.top = `${currentY - 90}px`;

    requestAnimationFrame(animateReveal);
  }

  const programCards = document.querySelectorAll('.program-card');

  programCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const nameEl = card.querySelector('.program-card__name');
      if (!nameEl) return;

      const name = nameEl.textContent.trim().toLowerCase();
      const imgSrc = imageMap[name];
      if (!imgSrc) return;

      revealImg.src = imgSrc;
      reveal.classList.add('active');
      isRevealing = true;
      animateReveal();
    });

    card.addEventListener('mousemove', (e) => {
      targetX = e.clientX;
      targetY = e.clientY;
    });

    card.addEventListener('mouseleave', () => {
      reveal.classList.remove('active');
      isRevealing = false;
    });
  });
}

