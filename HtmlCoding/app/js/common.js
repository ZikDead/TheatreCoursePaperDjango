$(function() {


  // Slider of schedule
  $('.menu').slick({

  infinite: false,
  centerPadding: '0px',
  slidesToShow: 4,
  prevArrow: $('.left-pagination'),
  nextArrow: $('.right-pagination'),
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerPadding: '40px',
        slidesToShow: 2
      }
    }
  ]
});


});
