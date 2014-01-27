$(document).ready(function() {
    var valFont = $("select#id_font option:selected").val();
    $(".fontpicker-example").attr("style", "font-family:"+valFont);
        
    $(".fontpicker-example").insertAfter("#id_font");
    $("select#id_font").change(function() {
        var valFont = $("select#id_font option:selected").val();
        $(".general-template").attr("style", "font-family:"+valFont);
    });
});