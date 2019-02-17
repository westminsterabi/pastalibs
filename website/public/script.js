var JSONdata = '{"data":{"partofspeech": ["VERB", "ADV", "NOUN"], "text":"I ran happily through the meadow"}}'; // example
var alldata = JSON.parse(JSONdata);
var posdata = alldata.data.partofspeech;
var num_verbs = 0;
var num_nouns = 0;
var num_adjs = 0;
var num_advs = 0;
var num_nums = 0;

var i;
for(i=0; i<posdata.length; i++) {
    pos = posdata[i];
    if(pos.localeCompare("VERB") == 0) {
        num_verbs++;
    } else if(pos.localeCompare("NOUN") == 0) {
        num_nouns++;
    } else if(pos.localeCompare("ADJ") == 0) {
        num_adjs++;
    } else if(pos.localeCompare("ADV") == 0) {
        num_advs++;
    } else if(pos.localeCompare("NUM") == 0) {
        num_nums++;
    }
}

function createEntry(length, text, id) {
    var i=0;
    for(i=0; i<length; i++) {
        var para = document.createElement("p");
        var node = document.createTextNode(text);
        para.appendChild(node);
        var element = document.getElementById(id);
        element.appendChild(para);
    }
}
createEntry(num_verbs, "VERB", "verb");
createEntry(num_nouns, "NOUN", "noun");
createEntry(num_adjs, "ADJECTIVE", "adj");
createEntry(num_advs, "ADVERB", "adv");
createEntry(num_nums, "NUMBER", "num");
