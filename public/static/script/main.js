$(document).ready(function() {
    $(".form-select-language option").each(function(){
        var value = $(this).val().toUpperCase();
        $(this).html(value);
    });
    
    $("#datepicker, #datepicker2").datepicker({
        dateFormat: 'yy-mm-dd'
    });
});