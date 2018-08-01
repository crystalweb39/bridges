$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});


window.requestAnimFrame = (function() {
    return window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.oRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    function(
    /* function */
    callback,
    /* DOMElement */
    element) {
        window.setTimeout(callback, 1000 / 60);
    };
})();

var CL = (typeof CL === 'undefined') ? {classes:{}} : console.log('global namespace CL in use')

CL.classes.scrollController = function(){
	var headerheight = $('header').height()
	var $win = $(window)
	
	
	var $why = $('#why')
	var $services = $('#services')
	var $team = $('#team')
	var $contact = $('#contact')
	
	var currentScroll = $win.scrollTop();
    var newScroll = currentScroll;
		
	
	var sections = [$why,$services,$team,$contact]
	
	var $nav = $('header nav ul li')
	
    $(window).resize(function(){
        windowResize();

    }); 
    
    var _this = this;

    
    this.deviceDetect = function(){
		var isiPad = navigator.userAgent.match(/iPad/i) != null;
		var isMobile = navigator.userAgent.toLowerCase().match(/iphone|ipod|blackberry|android|palm|windows\s+ce/i) != null;;
		if (isMobile || isiPad){
			mobileState()
			navClick()
			
			imageSlider(true)
			

		}else{
			navClick()
			
			
			imageSlider(false)
		}
    }
    
    
	var imageSlider = function(mobile){
		if(mobile){
			$('#slides.slider').slidesjs({
		        width: 868,
		        height: 454,
		        pagination: {
			      active: false,

			    },
			    navigation:{
			    	active:false,
			    }
		      });			
		}else{
		
			$('#slides.slider').slidesjs({
		        width: 868,
		        height: 454,
		        pagination: {
			      active: false,

			    },
			    navigation:{
			    	active:false,
			    },
			    play:{
			    	auto:true,
			    	pauseOnHover: true,
			    	effect: "slide",
			    	interval: 5000,
			    }
		      });
		      
		     }
	}
    
	var scrollLoop = function(){
		newScroll = $win.scrollTop();
		
        if (newScroll != currentScroll){
        	scrollDirection = newScroll > currentScroll ? 1 : -1;
            currentScroll = newScroll;          
            
            
        }
		
		requestAnimFrame(scrollLoop);
	}
    
	
	var mobileState = function(){
		$nav.each(function(i){
			$(this).addClass('nohover')
		})
	}
	
	var windowResize = function(){
		
		headerheight = $('header').height()
		
		for(i=0;i<sections.length;i++){
			
			
			infodata = {
				$el: sections[i],
				position: sections[i].offset().top - headerheight
				
			}
			
			sections[i].data('info',infodata)
		}
		
		
		
		
		
		
		
	}
	
	var navClick = function(){
		$nav.each(function(i){
			$(this).data('index', i)
			
			$('a',this).bind('click touchstart',function(e){
				e.preventDefault()
				scrollTo(sections[i].data('info').position)
				

			})
			
		})
	}



	
	
	var removeState = function(){
		$nav.find('span').removeClass('active')
		$nav.find('a').removeClass('active')
	}
	
	var scrollTo = function(position, callback){
		removeState()
        var animationDuration = calculateAnimateDuration($win.scrollTop(), position);
        $('html,body').stop().animate({'scrollTop' : position+'px'},animationDuration, 'swing');  
        setTimeout(function(){
        	var joinh = $('#footer').height()
        	$('#footer').height(joinh+10)
        	setTimeout(function(){
        		$('#footer').height(joinh)
        	},10)
            if (typeof callback == 'function') callback();
        },animationDuration);
		
	}
	
    var calculateAnimateDuration = function(currentPos, targetPos) {
        var distanceToGo = Math.abs(currentPos - targetPos);
        return Math.min(3500, distanceToGo);            
    };
	
	
	this.goTo = function(section){
		p = section.data('info').position
		scrollTo(p)		
	}
	
	this.directTo = function(section){
		p = section.data('info').position
		$(window).scrollTop(p)
	}
	
	
	
	
	$(window).trigger('resize')
	
}


$(window).load(function(){
	CL.scrollController = new CL.classes.scrollController()
	
	CL.scrollController.deviceDetect()
})
