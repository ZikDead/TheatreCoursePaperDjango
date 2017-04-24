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
     var menu_clicked = false;
    $('.menu-item').click(function () {
      var menu_item_clicked = this;
      menu_clicked = true;
      if  ($('.hall-popup').css('display')==='block' && menu_clicked ){
        $('.hall-popup').animate({
          height: "toggle",
          }, 500);
          menu_clicked = false;
          return;
      }

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

                // When loading
                $.ajax({
                  url: '/load_performance',
                  type: 'POST',
                  data: {
                    id: performance_item_clicked.data('id-event'),
                  },
                  success: function (result) {

                    $('.places .inner-wrapper').html(result.html);

                    var responce_arr = [];
                    var current_number = 0;

                    if (result.json){
                      var parsed_json = JSON.parse(result.json);
                    }

                    var row = $('.places-row').first();
                    for (var i=0; i< $('.places-row').length; i++){

                      var places = row.find('.place');

                      var place = places.first();
                      for (var j=0; j<places.length; j++){

                        if (parsed_json) {
                            var json_place = parsed_json[current_number];

                        }
                        if (json_place){
                          place.removeClass(place.attr('class').split(' ')[1]);
                          place.addClass(json_place['status']);
                        }

                        place.data('number-place', (j+1).toString());
                        place.data('number-row', (i+1).toString());
                        place.data('current_number', (current_number+1).toString());
                        place.data('cost_of_ticket', result.cost.toString());

                        place.text((j+1).toString());

                        responce_arr.push({'row': (i+1).toString(),
                                           'place': (j+1).toString(),
                                           'status': place.attr('class').split(' ')[1],
                                            'current_number': place.data('current_number')});

                        if (responce_arr[current_number].status==='super'){
                          place.data('cost_of_ticket', (result.cost*1.5).toString());
                        }


                        place = place.next();
                        current_number = current_number + 1;
                      }
                      row = row.next()
                    }

                    // When loaded animation
                    $('.loader').animate({opacity: 0,}, 500);
                    $('.loaded').animate({opacity: 1,}, 500);

                    // Main 'logic'
                    $('.place').click(function(){
                      var status = $(this).attr('class').split(' ')[1];
                      if ( status !== 'choosed' && status!== 'busy'){
                          $(this).removeClass(status.toString());
                          $(this).data('status-was', status.toString());
                          $(this).addClass('choosed');
                          responce_arr[$(this).data('current_number')-1].status = 'busy';

                          var panel_id = $(this).data('current_number');
                          var panel_place = $(this).data('number-place');
                          var panel_row = $(this).data('number-row');
                          var cost = $(this).data('cost_of_ticket');
                          $('.panel').append('<div id="' + panel_id + '" class="ticket-item">Row <span>'+panel_row+
                              '</span>, place <span>'+panel_place+ '</span>, price <span>'+cost+'$</span> </div>');
                          if ($('button').text()==='Total'){
                            $('button').html(cost + '$');
                          }
                          else{
                            $('button').html((parseFloat($('button').text())+parseFloat(cost) + '$').toString());
                          }


                      }else {if (status === 'choosed'){
                        $(this).removeClass('choosed');
                        $(this).addClass($(this).data('status-was'));
                        responce_arr[$(this).data('current_number')-1].status = $(this).data('status-was');
                      }}
                    });

                    $('button').click(function(){
                      $.ajax({
                        url: '/save_performance',
                        type: 'POST',
                        data: {
                          'json': JSON.stringify(responce_arr),
                            'id': performance_item_clicked.data('id-event'),
                        },
                        success: function () {

                          if  ($('.hall-popup').css('display')==='block'){
                            $('.hall-popup').fadeOut(400, "linear")
                          }

                        }
                    })
                    })

                  }
                });
            });
          });
        }
      });
    });
  })();



});
