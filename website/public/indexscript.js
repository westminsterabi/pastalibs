console.log("hi")

jQuery(document).ready(function() {
  jQuery('form#pg1form').bind('submit', function(event) {
    
    event.preventDefault();
    
    var formData = JSON.stringify($("myForm").serializeArray());
    console.log("test")
    console.log(formData)
    
    $.ajax({
      type: "POST",
      url: "http://localhost:8000/pasta_text",
      data: formData,
      dataType: "jsonp",
      contentType : "application/json"
    });
  });
})

