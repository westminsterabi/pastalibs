console.log("hi")

jQuery(document).ready(function() {
  jQuery('form#pg1form').bind('submit', function(event) {
    
    event.preventDefault();
    
    var formData = $("#pg1form");
    console.log("test")
    formData = JSON.stringify(formData.serializeArray())
    console.log(formData)

    $.ajax({
      type: "POST",
      url: "../http://127.0.0.1:8000/",
      data: formData,
      dataType: "jsonp",
      contentType : "application/json"
    }).done(function(){
        console.log("done!")
        window.location.href = "pos.html"
    }).fail(function(){
        alert("Failed")
    });
  });
})

