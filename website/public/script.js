$(document).ready(function(){
  const URL = "http://127.0.0.1:8000"

  $.getJSON(URL, function(result){
    var JSONdata = result;
  });
});


//var JSONdata = '{"data":{"partofspeech": ["VERB", "ADV", "NOUN"], "text":"I ran happily through the meadow"}}'; // example
var alldata = JSON.parse(JSONdata);
var posdata = alldata.blanked_text.data.parts_of_speech;

function createEntries(list, length, div_id) {
    var i;
    for(i=0; i<length; i++) {
        var mylabel = document.createElement("label");
        mylabel.setAttribute("for",list[i]);
        mylabel.setAttribute("class","wordtypelabs");

        var node = document.createTextNode(list[i]);
        mylabel.appendChild(node);

        var myinput = document.createElement("input")
        myinput.setAttribute("type","text");
        myinput.setAttribute("name", list[i]);
        myinput.setAttribute("class","wordinputs");

        var element = document.getElementById(div_id);

        element.appendChild(mylabel);
        $(mylabel).after(myinput);

        element.appendChild(document.createElement("br"))
    }
}

$(document).ready(function(){
    $(".homebutton").click(function(){
        $(".homebutton").css("background-color","blue")
    });
  });

var div_id = "div1";
createEntries(posdata, posdata.length, div_id);
