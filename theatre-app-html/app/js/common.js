$(function() {

  // Slider of schedule
  (function() {
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
  })();

  // Log in animation
  (function () {
    $('#log-in').click(function () {
        $(this).blur();
        $('.log-in').animate({
        height: "toggle"
        }, 500);
    })
  })();


  // Load performances
  (function () {

    $('.menu-item').click(function () {
      var menu_item_clicked = this;

      // Setup of Ajax to Django
      var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
      function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      }
      $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
          }
      });

      $.ajax({
        url: '/load_performances',
        type: 'POST',
        data: {
          date: $(menu_item_clicked).find('.date').text(),
        },
        success: function (result) {
          $('.performances').find('.row').html(result);

          $('div.performance-item').click(function () {

            var performance_item_clicked = $(this);

            //Animation  of loading
            $('.hall-popup').blur();
            // Restore defauls
            $('.loader').css('opacity', '1');
            $('.loaded').css('opacity', '0');
            $('.hall-popup').animate({
                height: "toggle",
            }, 500, function () {

                // When loaded
                $.ajax({
                  url: '/load_performance',
                  type: 'POST',
                  data: {
                    id: performance_item_clicked.data('id-event'),
                  },
                  success: function (result) {

                    $('.loader').animate({opacity: 0,}, 500);
                    $('.loaded').animate({opacity: 1,}, 500);




                  }

                });

            });

          });


        }



      });

    });

  })();


});
