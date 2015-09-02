$(document).ready(function(){
    //this listens for keyboard input and begins a search when the user stops typing
    $(function(){
        var timer;
        $('#search_form').on('keyup', function(){
            if($('#id_first_name').val() != '' || $('#id_last_name').val()) {
                timer && clearTimeout(timer);
                timer = setTimeout(create_post, 300);
            }
        });
    });


    function create_post(){
        //This is required for csrf token to work correctly
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
            url  : "/create_post/",
            type : "POST",
            data : {
                //PROBABLY HAVE TO CLEAN THESE VALUES BEFORE PASSING THEM IN
                first_name : $('#id_first_name').val(),
                last_name : $('#id_last_name').val(),
                department : $('#id_department').val()
            },

            success : function(json) {
                var result_array = parse_results(json);

                $('#results').empty();
                $('#results').prepend("<tr><th>Name</th><th>Phone</th><th>Email</th><th>Title</th>" +
                    "<th>Department</th></tr>");

                for(var i = 0; i < result_array.length; i++){
                    var object = result_array[i];
                    var result_object = object['1'];
                    var tel_number = parse_phone_number(result_object);

                    $('#results').append("<tr><td>" + result_object['givenName'] + " " + result_object['sn'] +
                        "</td><td>" + tel_number + "</td><td>" + result_object['mail'] + "</td><td>" +
                        result_object['title'] + "</td><td>" + result_object['department'] + "</td></tr>");
                }
            },

            error : function(xhr, errmsg){
                /*$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "
                    + errmsg + " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom*/
                $('#results').html("<div class='alert-box alert radius' data-alert>No listing based on the paramters you've entered.  "
                    + errmsg + " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
                // provide a bit more info about the error to the console
            }
        });
    }

    //All this does is split the json object into separate objects and stores them in an array to be
        // accessed one at a time
    function parse_results(json) {

        var get_results = [];
        for(var i = 0; i < json.results.length; i++) {
            get_results[i] = json.results[i];
        }
        return get_results;
    }

    //This checks for a default CNM number, and if so, formats appends the correct extension. If it's not default, the 7 digit
        // number is reformatted for readability.
    function parse_phone_number(result_obj){
        var tel_number;
        if(result_obj['otherTelephone']) {
            tel_number = result_obj['otherTelephone'].toString();
            if(tel_number == '5052244000'){
                tel_number = "(505) 224-4000 x. " + result_obj['telephoneNumber'];
            }
            else{
                var last_four = tel_number.substr(6, 10);
                tel_number = "(505) 224-" + last_four;
            }
        }
        else{
            tel_number = 'n/a';
        }
        return tel_number;
    }
});
