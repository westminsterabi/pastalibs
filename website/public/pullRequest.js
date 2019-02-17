$(document).ready(function(){
  const URL = "http://localhost:4000/posts"

  $.getJSON(URL, function(result){
    console.log("Data: " + result);
  });
});
