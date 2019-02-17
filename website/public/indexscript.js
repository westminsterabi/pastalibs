console.log("hi")

jQuery(document).ready(function() {
  jQuery('form#pg1form').bind('submit', function(event) {
    
    event.preventDefault();
    
    var data = $("#pg1form");
    console.log("test")
    data = data.serializeArray()
    var formData = {"pasta_text" : data}
    formData = JSON.stringify(formData)

    console.log(formData)

    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/pasta_text",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function(){
        console.log("done!")
        window.location.href = "pos.html"

    }).fail(function(){
        alert("Failed")
    });
  });
})

