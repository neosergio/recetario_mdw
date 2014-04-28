var csrf = {
    getCookie : function(name){
        var cookieValue = null;

        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    csrfSafeMethod : function(method){
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    },

    sameOrigin : function(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;

        return(url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }
};

$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if(!csrf.csrfSafeMethod(settings.type) && csrf.sameOrigin(settings.url)){
            xhr.setRequestHeader('X-CSRFToken', csrf.getCookie('csrftoken'));
        }
    }
});