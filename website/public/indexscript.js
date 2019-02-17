jQuery(document).on('ready', function() {
  jQuery('form#add-new-task').bind('submit', function(event) {
    
    event.preventDefault();
    
    var formData = JSON.stringify($("myForm").serializeArray());
    
    $.ajax({
      type: "POST", 
      url: "http://localhost:8000/pasta_text",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    });
  });
}

