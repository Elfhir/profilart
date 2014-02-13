$(document).ready(function() {
    $(".wrapper-unique-theme").click( function() {
    var id = $(this).attr('id-template');
    var requestiduser = $(this).attr('requestiduser');
    var name = $(this).attr('name');
    $.ajax({  
            type: "POST",
            url: "/"+name+"/build/editTheme/"+id+"/",
            data: {id: id, requestiduser: requestiduser},
            success: function(data) {
                if (data == 3) $('#modalerror').modal();
                if (data == 2) $('#modalsuccess').modal();
            }
    });
    return false;
});

$(document).on($.modal.CLOSE, function(event, modal) {
    location.reload();
});

});