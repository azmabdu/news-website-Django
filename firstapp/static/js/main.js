jQuery(function($) {'use strict',

		$('#payModal').on('shown.bs.modal', function () {
			$('#payModal').focus()
		});
	
	
	
	
	//goto top
	$('.gototop').click(function(event) {
		event.preventDefault();
		$('html, body').animate({
			scrollTop: $("body").offset().top
		}, 500);
	});	

	 $('.go_to').click( function(){ // ловим клик по ссылке с классом go_to
	var scroll_el = $(this).attr('href'); // возьмем содержимое атрибута href, должен быть селектором, т.е. например начинаться с # или .
        if ($(scroll_el).length != 0) { // проверим существование элемента чтобы избежать ошибки
	    $('html, body').animate({ scrollTop: ($(scroll_el).offset().top)-122 }, 500); // анимируем скроолинг к элементу scroll_el
        }
	    return false; // выключаем стандартное действие
    });
										
	$(".btn_mnu").click(function() {
		$(this).toggleClass("active");
		$("div#openSearch").removeClass("active");
		$( "div.lmenu_box" ).removeClass( "open" );
	});
	$("#openSearch").click(function() {
		$(this).toggleClass("active");
		$("div#openSearch").toggleClass("active");
		$( "div.lmenu_box" ).removeClass( "open" );
		$( "button.btn_mnu" ).removeClass( "active" );
		
		$("div.navbar-collapse").removeClass("in");
		$('html, body').animate({
			scrollTop: $("body").offset().top
		}, 500);
	});
                    
     $("button.search_btn").click(function() {
		$(this).toggleClass("active");
		$("form.search_btn_box").toggleClass("active");
		$("button.search_btn_close").toggleClass("active");
		
	});  
	$("button.search_btn_close").click(function() {
		$("form.search_btn_box").toggleClass("active");
		$("button.search_btn").toggleClass("active");
	});
                    
    $('body').scrollspy({
        target: '.navbar',
        offset: 51
    })

    // Closes the Responsive Menu on Menu Item Click
    
    $( "button.collapsed" ).click(function() {
        $( "div.navbar-header" ).toggleClass( "open" );
    });
		$("button.lmenu" ).click(function() {
        $( "div.lmenu_box" ).toggleClass( "open" );
        $("button.lmenu" ).toggleClass( "open" );
				$("div#openSearch").removeClass("active");
				$("div.navbar-collapse").removeClass("in");
			  $( "button.btn_mnu" ).removeClass( "active" );
    });
    
    // Offset for Main Navigation
    $('nav.navbar').affix({
        offset: {
            top: 20
        }
    });
                    
});