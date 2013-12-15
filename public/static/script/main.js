$(document).ready(function() {
    $(".form-select-language option").each(function(){
        var value = $(this).val().toUpperCase();
        $(this).html(value);
    });
    $("#datepicker").datepicker({
        dateFormat: 'yy-mm-dd'
    });
});