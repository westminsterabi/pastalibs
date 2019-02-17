$(document).ready(function(){
  const URL = "http://localhost:8000/pasta_text"

  $.getJSON(URL, function(result){
    console.log("Data: " + result);
  });
});
