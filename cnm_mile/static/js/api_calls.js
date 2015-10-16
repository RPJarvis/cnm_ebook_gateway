$(document).ready(function(){
    function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
    function passToTouchnet(){
        //open in new window UPAY_SITE_ID=1
        var first_name = $('#id_first_name').val();
        var last_name = $('#id_last_name').val();
        var cnm_email = $('#id_cnm_email').val();

        //HOW DO I GET UPDAY SITE ID?? AJAX for just that??
/*
        var base_url = "https://secure.touchnet.com:8443/C20016test_upay/ext_site_test.jsp";
        var u_pay_id = "";
        var url = base_url + "?UPAY_SITE_ID=" + u_pay_id + "&BILL_NAME=" + first_name + " " +
            last_name + "&BILL_EMAIL_ADDRESS=" + cnm_email;

        var short_url = base_url + "?UPAY_SITE_ID=" + "1";
        window.open(short_url);*/
        //window.open(base_url);
        //https://secure.touchnet.com:8443/C20016test_upay/ext_site_test.jsp?UPAY_SITE_ID=1?BILL_NAME=ryanjarvis?BILL_EMAIL_ADDRESS=rjarvis1@cnm.edu
        var UPAY_SITE_ID = 1;
        jQuery.post('https://test.secure.touchnet.net:8443/C20016test_upay/ext_site_test.jsp', UPAY_SITE_ID);

        /*$.ajax({
            url: "https://secure.touchnet.com:8443/C20016test_upay/ext_site_test.jsp?UPAY_SITE_ID=1", //django url
            type: "POST",
            data: {
                first_name: first_name,
                last_name: last_name,
                cnm_email: cnm_email
                //book_choice: $('#id_book_choice').val()
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
        });*/
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
        var csrftoken = getCookie('csrftoken');
        console.log('bulk upload function called');

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
                data: $('#id_csv_field').val()
            },
            success: function(){
                console.log('success');
            },
            error: function(data){
                console.log('fail');
                console.log(data);
            }
        });
    }

    //INKLING
/*    $('#user_form').on('submit', function(event){
        event.preventDefault();
        $('#user_form').hide();
        $('#loading_image').show();
        console.log('can is ee this?');
        passToInkling();
        //call url from here?
    });*/


    //TOUCHNET
    $('#user_form').on('submit', function(event){
        event.preventDefault();
        $('#user_form').hide();
        $('#loading_image').show();
        console.log('can i see this?');
        passToTouchnet();
        //call url from here?
    });


    $('#bulk_upload_btn').on('click', function(event){
        event.preventDefault();
        console.log('bulk button clicked');
        bulkUpload();
    });
    $('#touchnet_post_btn').on('click', function(event){
        event.preventDefault();

        var UPAY_SITE_ID = 1;
        console.log(UPAY_SITE_ID);
        window.open("https://test.secure.touchnet.net:8443/C20016test_upay/ext_site_test.jsp?UPAY_SITE_ID=1");
    });

});