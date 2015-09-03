$.ajax({
    url  : "/create_post/",
    type : "POST",
    data : {
     "email": "john@gmail.com",
     "productId": "3c9e50736eb549a5bc951bc100b630a2",
     "firstName": "John",
     "lastName": "Doe",
     "receiveEmail": true,
     "checkoutAmount": 1000,
     "partnerInfo": {
         "partnerSiteId": "...",
         "partnerPermaItemUrl": "...",
         "partnerTransactionId": "..."
      }
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
        //
    }
});