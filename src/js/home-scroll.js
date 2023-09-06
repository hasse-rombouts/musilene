window.addEventListener("scroll", () => {
  // get height of .banner
  const bannerHeight = document.querySelector(".banner").clientHeight;
  const checkpoint = 1 * bannerHeight;
  const currentScroll = window.pageYOffset;
  if (currentScroll <= checkpoint) {
    opacity = 1 - currentScroll / checkpoint;
  } else {
    opacity = 0;
  }
  document.querySelector(".banner").style.opacity = opacity;
});
