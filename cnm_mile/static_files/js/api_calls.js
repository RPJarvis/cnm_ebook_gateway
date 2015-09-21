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
                console.log(json);
                console.log(json[1]);

                $('#messages').prepend("<tr><th>Name</th><th>Phone</th><th>Email</th><th>Title</th>" +
                "<th>Department</th></tr>");
                $('#messages').append(json);
            }
        });
    }
/*
inkling partner key: Partner Key: p-529864ffd7394252a900c4e2a4ba76a1
  To inkling
         {
     "email": "john@gmail.com",
     "productId": "3c9e50736eb549a5bc951bc100b630a2",
     "firstName": "John",
     "lastName": "Doe",
     "receiveEmail": true,
     "checkoutAmount": 1000,
     "partnerInfo": {
         "partnerSiteId": "...",
         "partnerPermaItemUrl": "...",
         "partnerTransactionId": "...",
     }
 }*/
    $('#user_form').on('submit', function(event){
        event.preventDefault();
        console.log('can is ee this?');
        passToInkling();
    });

});

function displayInklingResult(json){

}