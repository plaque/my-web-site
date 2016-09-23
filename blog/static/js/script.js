$("document").ready(function(){

	var all_dates = $('.timeline li');

	function isElementInViewport(el) {
    	var rect = el.getBoundingClientRect();

	    return (
	      rect.top >= 0 &&
	      rect.left >= 0 &&
	      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
	      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
	    );
  	}

	function callbackFunc()
	{
		for (var i = 0; i < all_dates.length; i++)
		{
			if(isElementInViewport(all_dates[i]))
			{
				all_dates[i].classList.add("in-view");
			}
		}
	}

	$(window).bind('load', callbackFunc);
	$(window).bind('scroll', callbackFunc);

});