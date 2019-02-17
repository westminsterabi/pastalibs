$(document).ready(function(){
  const URL = "http://127.0.0.1:8000/pasta_text"

  $.getJSON(URL, function(result){
    console.log("Data: " + result);
  });
});
