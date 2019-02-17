var JSONdata = '{"data":{"partofspeech": ["VERB", "ADV", "NOUN"], "text":"I ran happily through the meadow"}}'; // example
var alldata = JSON.parse(JSONdata);
var posdata = alldata.data.partofspeech;

function createEntries(list, length, div_id) {
    var i;
    for(i=0; i<length; i++) {
        var para = document.createElement("p");
        var node = document.createTextNode(list[i]);
        para.appendChild(node);
        var element = document.getElementById(div_id);
        element.appendChild(para);
    }
}
var div_id = "div1";
createEntries(posdata, posdata.length, div_id);