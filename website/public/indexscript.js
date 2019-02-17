
var formData = JSON.stringify($("myForm").serializeArray());

$.ajax({
  type: "POST",
  url: "http://localhost:8000/pasta_text",
  data: formData,
  dataType: "json",
  contentType : "application/json"
});

