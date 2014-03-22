$(document).ready(function() {    
    $(".template1 .bxslider .wrapper-last-work img").each(function(){
        height = $(this).attr("height");
        newHeight = parseInt(-height/5.2);
        $(this).css("top", newHeight+"px");
    });
    
    $(".switch-visibility").each(function(){
        if ($(this).attr("isvisible") == "False") {
            $(this).closest(".switch-parent").css("opacity", "0.5");
        }
    })
    
    $(".topic-line").find(".wrapper-thumb-overlay:gt(2)").remove();
});