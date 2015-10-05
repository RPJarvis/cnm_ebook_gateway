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
                cnm_email: $('#id_cnm_email').val(),
                book_choice: $('#id_book_choice').val()
            },

            success: function(json){
                console.log(json);
                //TODO:conditional here to redisplay form on error??
                $('#loading_image').hide();
                if(json['status']['statusCode'] != "SchemaValidationError"){
                    $('#user_form').hide();
                    $('#messages').empty().prepend("<h1>Results here:</1>").append(json['display_dict']['user_details']);
                }
                else{
                    $('#user_form').show();
                    $('#messages').empty().prepend("<h1>Results here:</1>").append(json['display_dict']['user_details']);
                }
            },

            error: function(json){
                console.log('error');
                $('#loading_image').hide();
                $('#messages').append("this is an error message");
                $('#messages').append(json);
            }
        });
    }

    function bulkUpload(){
        console.log('bulkUpload function called');
        $.ajax({
            //does this have to call a view or can it call a function?? probably a view.
            url: "/bulk_upload/",
            type: "POST",
            data: {
                csv_file: $('#id_csv_file')
            },

            success: function(){
                console.log("bulkUpload success function");
            },

            error: function(){
                //redirect back??
                console.log("bulkUpload error called");
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

    $('#bulk_upload_btn').on('click', function(event){
        event.preventDefault();
        console.log('bulk button clicked');
        bulkUpload();
    });

});