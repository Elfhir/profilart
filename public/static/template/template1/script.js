$(document).ready(function() {
    $('.bxslider').bxSlider({
        mode: 'fade',
        infiniteLoop: true,
        speed: 1000
    });
    
    $(".template1 .bxslider .wrapper-last-work img").each(function(){
        height = $(this).attr("height");
        newHeight = parseInt(-height/5.2);
        $(this).css("top", newHeight+"px");
    });
});