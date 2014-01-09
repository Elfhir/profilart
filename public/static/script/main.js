$(document).ready(function() {
    $(".form-select-language option").each(function(){
        var value = $(this).val().toUpperCase();
        $(this).html(value);
    });
    
    $("#datepicker, #datepicker2").datepicker({
        dateFormat: 'yy-mm-dd'
    });
    
    $("input#id_in_focus_0").closest("ul").after('<div class="clear"></div>');
    
    /*$(".form-exhibition #id_mapLongitude").parent().hide();
    $(".form-exhibition #id_mapLatitude").parent().hide();
    $(".form-exhibition #id_adress").after("<p class='add-specific-address link-style'>> Ajouter un endroid bien précis</p>");
    $(".form-exhibition #id_mapLatitude").after("<p class='add-global-address link-style'>> J'ai une adresse !</p>");
    $(".add-specific-address").click(function(){
        $(".form-exhibition #id_mapLongitude").parent().show();
        $(".form-exhibition #id_mapLatitude").parent().show();
        $(".form-exhibition #id_adress").parent().hide(); 
    });
    $(".add-global-address").click(function(){
        $(".form-exhibition #id_mapLongitude").parent().hide();
        $(".form-exhibition #id_mapLatitude").parent().hide();
        $(".form-exhibition #id_adress").parent().show(); 
    });*/
});