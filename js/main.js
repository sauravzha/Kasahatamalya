/* ============================================
   KSHAMTALAYA — Main JavaScript
   Interactions, counters, scroll animations
   ============================================ */

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
        // Stagger children within a parent
        const parent = entry.target.closest('[data-stagger]');
        if (parent) {
          const siblings = parent.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
          const siblingIndex = Array.from(siblings).indexOf(entry.target);
          entry.target.style.transitionDelay = `${siblingIndex * 0.08}s`;
        }
        
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
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


/* ── 3D Card Tilt ── */
function initCardTilt() {
  const cards = document.querySelectorAll('[data-tilt]');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = (y - centerY) / centerY * -6;
      const rotateY = (x - centerX) / centerX * 6;
      
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0)';
      card.style.transition = 'transform 0.5s ease-out';
    });

    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 0.1s ease-out';
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
