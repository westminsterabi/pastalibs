$(document).ready(function(){
  const URL = "http://localhost:8000/pasta_text"

  $.getJSON(URL, function(result){
    var JSONdata = result;
  });
});

//var JSONdata = '{"data":{"partofspeech": ["VERB", "ADV", "NOUN"], "text":"___ ran ___ through the ___"}}'; // example
var alldata = JSON.parse(JSONdata);
var textdata = alldata.blanked_text.data.text;

var para = document.createElement("p")
var node = document.createTextNode(textdata);
para.appendChild(node);
var element = document.getElementById("div1")
element.appendChild(para)
