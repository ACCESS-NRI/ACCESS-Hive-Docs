/* Same Swiper options as the live WordPress masthead (Swiper 8.0.7). */
document.addEventListener("DOMContentLoaded", function () {
  if (document.querySelector(".swiper-masthead-container") && window.Swiper) {
    new Swiper(".swiper-masthead-container", {
      slidesPerView: 1,
      autoplay: { delay: 6000, pauseOnMouseEnter: false },
      speed: 1000,
      loop: true,
      autoHeight: true,
      pagination: { el: ".my-swiper-pagination", clickable: true },
    });
  }
});
