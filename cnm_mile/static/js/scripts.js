$(document).ready(function (){

	$("label").each(function( index ){
		console.log($(this).next().attr("id"));
		//$(this).attr("for", $(this).next().attr("name")) ;
		//console.log($(this).attr("for"));


		// Set the "for" attribute of the label to match the 
		// following input field id
		$(this).attr("for", $(this).next().attr("id")) ;

		// Set the input field's class to "form-control"
		$(this).next().addClass("form-control") ;

		
		if($(this).next().prop('tagName') == "INPUT"){

		}
		//console.log($(this).next().prop('tagName'));
	});

});