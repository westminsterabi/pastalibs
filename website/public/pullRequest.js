$(document).ready(function(){
  const URL = "http://localhost:8000/posts"

  $.getJSON(URL, function(result){
    console.log("Data: " + result);
  });
});
