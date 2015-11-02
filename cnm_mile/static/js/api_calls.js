$(document).ready(function(){
    function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
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

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
                $('#messages').append("Bulk provisioning in progress.");
            }
        });

        $.ajax({
            url: "/admin/do_bulk_upload/" ,
            type: "POST",
            data: {
                data: $('#id_csv_field').val(),
                book_choice: $('#id_book_choice').val()
            },
            success: function(json){
                console.log('success');
                $('#messages').empty().append('Results:');
                $('#messages').append(json);
                var result_length = json.length;
                for(i = 0; i < result_length; i++){
                    $('#messages').append(String('<li>' + json[i]['first_name'] + ' ' + json[i]['last_name'] +
                        ' ' + json[i]['user'] + ' ' + json[i]['details'] + '</a>'));
                }
            },
            error: function(data){
                $('#messages').empty().append('fail');
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

        var UPAY_SITE_ID = 1;//go get it
        var base_url = "https:\/\/test.secure.touchnet.net:8443/C20016test_upay/web/index.jsp";
        var final_url = base_url + '?UPAY_SITE_ID=' + UPAY_SITE_ID;
        var form = document.createElement("form");
        form.setAttribute("method", "post");
        form.setAttribute("action", final_url);

        // setting form target to a window named 'formresult'
        form.setAttribute("target", "formresult");

        var hiddenField = document.createElement("input");

        document.body.appendChild(form);

        // creating the 'formresult' window with custom features prior to submitting the form
        window.open('', 'formresult', 'scrollbars=no,menubar=no,height=600,width=800,resizable=yes,toolbar=no,status=no');

        form.submit();


        //var UPAY_SITE_ID = 0;
        //console.log(UPAY_SITE_ID);
        //jQuery.post('https://test.secure.touchnet.net:8443/C20016test_upay/web/index.jsp', UPAY_SITE_ID);
    });

});