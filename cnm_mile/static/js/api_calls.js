$(document).ready(function(){
    $('#loading_image').bind('ajaxStart', function(){
        $(this).show();
    }).bind('ajaxStop', function(){
        $(this).hide();
    });
    function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
    function passToTouchnet(){
        //open in new window UPAY_SITE_ID=1
        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url : "/pass_to_touchnet/", //django url
            type : "POST",
            data : {
                first_name : $('#id_first_name').val(),
                last_name : $('#id_last_name').val(),
                cnm_email : $('#id_cnm_email').val()

            }
            //TODO: success and error
        })
    }


 function passToInkling(){
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
                return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/pass_to_inkling/", //django url
            type: "POST",
            data: {
                first_name: $('#id_first_name').val(),
                last_name: $('#id_last_name').val(),
                cnm_email: $('#id_cnm_email').val()
            },
            //TODO: success and error


            success: function (json) {
                result_obj = JSON.parse(json);
                console.log(result_obj);
                console.log(result_obj['status']);
                console.log(result_obj['result']);
                $('#loading_image').hide();

                $('#messages').prepend("<h1>Results here:</1>");
                $('#messages').append(json);

                //{"info": {},
                // "status": {"statusMsg": "Schema validation failed.",
                // "statusDetails": {"resource": "Purchase", "error": "Value u'' for field 'firstName' cannot be blank"},
                // "statusCode": "SchemaValidationError"}, "result": {}}
            }
        });
    }
    $('#user_form').on('submit', function(event){
        event.preventDefault();
        $('#user_form').hide();
        $('#loading_image').show();
        console.log('can is ee this?');
        passToInkling();
    });

});