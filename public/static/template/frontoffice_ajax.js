$(document).ready(function() {
    $("a.addfollow").click( function() {
        var name = $(this).attr('username');
        var iduser = $(this).attr('iduser');
        var requestiduser = $(this).attr('requestiduser');
        $.ajax({  
                type: "POST",
                url: "/"+name+"/social/addfollow/",
                data: {iduser: iduser, requestiduser: requestiduser},
                success: function(data) {
                    if (data == 0) $('#modalfollowerror').modal();
                    if (data == 3) $('#modalfollowanonymous').modal();
                    if (data == 1) $('#modalfollowsuccess').modal();
                }
        });
        return false;
    });
    
    $(document).on($.modal.CLOSE, function(event, modal) {
        location.reload();
    });
});