$(document).ready(function(){
    var ajaxDBResponseData = 'bogus';
    var purchaseHistoryStatus = false;
    //this is the main workflow that calls the other functions. functino definitions below.
    $('#main_submit').on('click', function(event){
        event.preventDefault();
        var error = '';
        //checkFields();
        $('#errors').empty();

        var fieldsValid = false;
        var userEmail = $('#id_cnm_email').val();
        var lettersOnlyFirst = /^[a-zA-Z]+(-[a-zA-Z]+)*$/.test($('#id_first_name').val());
        console.log('letters only first check' + lettersOnlyFirst);
        if(lettersOnlyFirst == false){
            error += ' First Name - Letters only, please.';
            console.log(error);
        }
        var lettersOnlyLast = /^[a-zA-Z]+(-[a-zA-Z]+)*$/.test($('#id_last_name').val());
        console.log('letters only last check' + lettersOnlyLast);
        if(lettersOnlyLast == false){
            error += ' Last Name - Letters only, please.';
            console.log(error);
        }
        var edu_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.+-]+\.edu$/.test(userEmail);
        console.log('regex check' + edu_email);
        if(edu_email == false){
            error += ' You must use a \".edu\" email address to purchase a book.';
        }
        var book = document.getElementById('id_book_choice');
        try {
            var title = book.options[book.selectedIndex].text;
        }
        catch(err){
            error += ' Please select a book.'
        }
        console.log(error);
        if (title != '' &&  lettersOnlyFirst &&  lettersOnlyLast && edu_email){
            fieldsValid = true;
        } else {
            error += ' ';
        }
        if(fieldsValid){
            checkPurchaseHistory(userEmail, title);
            console.log(purchaseHistoryStatus + 'from before check');
            if(purchaseHistoryStatus == false){
                getPrice(title); //MIGHT BE WACKY
                var price = ajaxDBResponseData['price'];
                console.log(price);
                var site_id = ajaxDBResponseData['site_id'];
                dispatch(title, price, site_id);
            } else {
                error += 'According to our records, you have already purchased this book. If you believe this to be incorrect, ' +
                'please call the Cashier\'s Office at (505) 224-3471.';
                $('#errors').append(error);
            }
        } else {
            $('#errors').append(error);
        }
    });

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
            url: "/pass_to_inkling/",
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

    //Bulk upload in the admin backend
    $('#bulk_upload_btn').on('click', function(event){
        event.preventDefault();
        console.log('bulk button clicked');
        bulkUpload();
    });

    //1
    function dispatch(title, price, site_id){
        if(price > 0){
            passToTouchnet(price, site_id);
            //passToInkling(); inkling has to be handled in callback view from touchnet
        }
        else{
            passToInkling();
        }
    }

    //2
    function passToTouchnet(price, site_id){
 //       For Credit Card payments, use the below numbers  with any valid future expiration date (eg. 1208)
//MC: 5454545454545454
//AmEx: 343434343434343
//DI:  6011666666666666

        //WITH FORM IN POPUP
        console.log('pass to touchnet');
        var user_first = $('#id_first_name').val();
        var user_last = $('#id_last_name').val();
        var full_name = '&BILL_NAME=' + user_first + ' ' + user_last;
        var user_email = '&BILL_EMAIL_ADDRESS=' + $('#id_cnm_email').val();
        var ammount = '&AMT=' + price;
        var base_url = "https:\/\/test.secure.touchnet.net:8443/C20016test_upay/web/index.jsp";
        var final_url = base_url + '?UPAY_SITE_ID=' + site_id + full_name + ammount + user_email;
        console.log(final_url);
        var form = document.createElement("form");
        form.setAttribute("method", "post");
        form.setAttribute("action", final_url);

        // setting form target to a window named 'formresult'
        form.setAttribute("target", "formresult");

        var hiddenField = document.createElement("input");

        document.body.appendChild(form);

        // creating the 'formresult' window with custom features prior to submitting the form
        window.open('', 'formresult', 'scrollbars=no,menubar=no,height=600,width=800,resizable=yes,toolbar=no,status=no');
        //############ TRY LOCATION HERE???

        form.submit();

        //SAME WINDOW
        //var base_url = "https:\/\/test.secure.touchnet.net:8443/C20016test_upay/web/index.jsp";
        //var final_url = base_url + '?UPAY_SITE_ID=' + site_id;
        //$.post(final_url);
    }




    function getPrice(title){
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                $('#main_submit').hide();
                $('#messages').append('Opening Touchnet');
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            async: false,
            url: '/get_price/',
            method: 'post',
            data: {
                'title': title
            },
            success: function(response){
                ajaxDBResponseData = response;
            },
            error: function(){
                console.log('ajax error');
            }
        });
    }

    function checkPurchaseHistory(email, title){
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
            async: false,
            url: /check_purchase_history/,
            method: 'post',
            data: {
                'email': email,
                'title': title
            },
            success: function(json){
                console.log('victory');
                purchaseHistoryStatus = json['purchased'];
                console.log(purchaseHistoryStatus + 'from success');
            },
            error: function(json){
                console.log('failsauce');
                console.log(json);
            }
        });
    }
});