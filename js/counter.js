document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".stat-card__number");
  
  const animateCounter = (counter) => {
    const target = +counter.getAttribute("data-count");
    const suffix = counter.getAttribute("data-suffix") || "";
    const duration = 2000; // 2 seconds
    const start = 0;
    let startTime = null;
    
    // Format number with commas
    const formatNumber = (num) => {
      return num.toLocaleString('en-IN');
    };

    const step = (currentTime) => {
      if (!startTime) startTime = currentTime;
      const progress = Math.min((currentTime - startTime) / duration, 1);
      
      // Easing function for smooth deceleration
      const easeOutQuad = progress * (2 - progress);
      const currentVal = Math.floor(easeOutQuad * target);
      
      counter.innerText = formatNumber(currentVal) + suffix;
      
      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        counter.innerText = formatNumber(target) + suffix;
      }
    };
    
    window.requestAnimationFrame(step);
  };
  
  // Use Intersection Observer to trigger animation when visible
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  
  counters.forEach(counter => observer.observe(counter));
});
