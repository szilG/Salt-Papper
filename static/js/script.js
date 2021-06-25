


//Swiper - Credit to Vladimir Kharlampidi https://github.com/nolimits4web/Swiper/blob/master/demos/150-freemode.html
const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    loop: true,
    centeredSlides: true,
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      540: {
        slidesPerView: 1,
      },  
      541: {
        slidesPerView: 2,  
      },
      1024: {
        slidesPerView: 3,  
      },
      1200: {
        slidesPerView: 4,
      }
    }
  });
