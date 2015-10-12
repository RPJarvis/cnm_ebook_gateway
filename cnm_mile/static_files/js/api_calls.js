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

    function passToInkling(){

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
                cnm_email: $('#id_cnm_email').val(),
                book_choice: $('#id_book_choice').val()
            },
            //TODO:error


            success: function(json){
                console.log(json);
                console.log(json['firstNameErrors'][0]);
                $('#messages').prepend("<tr><th>Name</th><th>Phone</th><th>Email</th><th>Title</th>" +
                "<th>Department</th></tr>");
                $('#messages').append(json);
            }
        });
    }

    function bulkUpload(){
        var csrftoken = getCookie('csrftoken');
        console.log('bulk upload function called');
        console.log(csrftoken);

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/admin/do_bulk_upload/" ,
            type: "POST",
            data: {
                first_name: $('#id_first_name').val(),
                last_name: $('#id_last_name').val(),
                cnm_email: $('#id_cnm_email').val()
            },

        });

    }

    $('#user_form').on('submit', function(event){
        event.preventDefault();
        console.log('can is ee this?');
        passToInkling();
    });

    $('#bulk_upload_btn').on('submit', function(event){
        event.preventDefault();
        console.log('bulk button clicked');
        bulkUpload();
    });
});

