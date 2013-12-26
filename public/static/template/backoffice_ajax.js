$(document).ready(function() {
    $("img.switch-visibility").click( function() {
            var name = $(this).attr('user');
            var isVisible = $(this).attr('isvisible');
            var element = $(this).attr('element');
            var selector = $(this)
            $.ajax({  
                    type: "POST",
                    url: "/"+name+"/build/switchvisible/",
                    data: {isVisible: isVisible, element: element},
                    success: function(data) {
                        if (isVisible == "True") {
                            selector.attr("isvisible", "False")
                            $(".switch-"+element).css("opacity", "0.5");
                        }else{
                            selector.attr("isvisible", "True")
                            $(".switch-"+element).css("opacity", "1");
                        }
                    }
            });
            return false;
        });
    
        $(document).on($.modal.CLOSE, function(event, modal) {
            location.reload();
        });
                      
        $("a.open-modal").click(function(event) {
            $(this).modal({
                fadeDuration: 200
            });
            return false;
        });
});