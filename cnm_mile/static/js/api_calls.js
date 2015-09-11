$(document).ready(function(){
    $('#loading_image').bind('ajaxStart', function(){
        $(this).show();
    }).bind('ajaxStop', function(){
        $(this).hide();
    });

    //check for ownsership

    //GET /products/3c9e50736eb549a5bc951bc100b630a2?email=john@gmail.com&access_token=<key>
    function checkOwnership(email) {
        //TODO: dint need access token, api key is fine
        var check_url = "/products/3c9e50736eb549a5bc951bc100b630a2?email=" + email + "&access_token=<key>";
        $.ajax({
            url: check_url,
            type: "GET",
            //log with django
            success: function () {
            },
            error: function () {
            }
        });
    }
    /*{
        "s9id": "3c9e50736eb549a5bc951bc100b630a2",
        "purchased": false,
        "subProductPurchased": false,
        "name": "Product Build: Campbell Biology",
    }

    */

    function passToTouchnet(){

        //open in new window UPAY_SITE_ID=1

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
});

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
