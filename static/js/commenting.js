$("#commentform").on("submit", function(event){
    event.preventDefault()

    var commentform = {
      username: null,
      comment: null,
    }
  
    //For each of the form input fields
    $(this).find("input, textarea").each(function(){

      
      if ($(this).prop("name") == "username") {
        commentform.username = $(this).val();
      }
  
      if ($(this).prop("name") == "comment") {
        commentform.comment = $(this).val();
      }
    })
  
    //Now, we turn the completed object into a JSON object for use with ajax call to the server
    var JSONFormData = JSON.stringify(commentform)
  
    console.log("Testing database");

    console.log(JSONFormData);

    // To clear the data that the user has put into the form
    event.preventDefault();
    document.getElementById("commentform").reset();

    // This is the code for the ajax call to the server to get the comments
    $.ajax({
      type: "POST",
      url: "/commented",
      contentType: "application/json; charset=utf-8",
      data: {
          JSONFormData: JSONFormData
      }
    })
  })
