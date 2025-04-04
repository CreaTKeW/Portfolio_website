document.addEventListener('DOMContentLoaded', function() {
  const stickyNavbarContainer = document.getElementById('sticky-navbar-container');
  if (!stickyNavbarContainer) return;

  let lastScrollY = window.scrollY;
  const hideThreshold = 100;

  window.addEventListener('scroll', function() {
    const currentScrollY = window.scrollY;
    let isScrollingUp = currentScrollY < lastScrollY;
    let isScrollingDown = currentScrollY > lastScrollY;

    if (isScrollingDown && currentScrollY > hideThreshold) {
      stickyNavbarContainer.classList.add('navbar-hidden');
    } else if (isScrollingUp || currentScrollY <= hideThreshold ) {
      stickyNavbarContainer.classList.remove('navbar-hidden');
    }

    if (currentScrollY > hideThreshold && !stickyNavbarContainer.classList.contains('navbar-hidden')) {
       stickyNavbarContainer.classList.add('navbar-scrolled-visible');
    } else {
       stickyNavbarContainer.classList.remove('navbar-scrolled-visible');
    }


    lastScrollY = Math.max(0, currentScrollY);
  });
});

window.addEventListener('load', function() {
  console.log("Window loaded, scrolling to top.");
  window.scrollTo(0, 0);
});