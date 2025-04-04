document.addEventListener('DOMContentLoaded', function() {
  const stickyNavbarContainer = document.getElementById('sticky-navbar-container');
  const header = document.getElementById('main-header');

  if (!stickyNavbarContainer) return;

  let lastScrollY = window.scrollY;
  const hideThreshold = 100;

  window.addEventListener('scroll', function() {
    const currentScrollY = window.scrollY;

    if (currentScrollY > lastScrollY && currentScrollY > hideThreshold) {
      stickyNavbarContainer.classList.add('navbar-hidden');
    } else if (currentScrollY < lastScrollY) {
      stickyNavbarContainer.classList.remove('navbar-hidden');
    }

    lastScrollY = Math.max(0, currentScrollY);
  });
});