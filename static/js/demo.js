/* un ejemplo con jquery */
$(function(){
    $('#menu a[href*="' + location.pathname.split("/")[1] + '"][class!="noactivo"]').addClass('activo');
});