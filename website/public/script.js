var JSONdata = '{"data":{"partofspeech": ["VERB", "ADV", "NOUN"], "text":"I ran happily through the meadow"}}'; // example
var data = JSON.parse(JSONdata);


var verbs = ["running", "walking", "swimming"];
var nouns = ["runner", "walker", "swimmer"];
var adjs = ["running", "walking", "swimming"];
var advs = ["runningly", "walkingly", "swimmingly"];
var nums = ["one run", "one walk", "one swim"];

var i=0;

function createEntry(length, text, id) {
    for(i=0; i<length; i++) {
        var para = document.createElement("p");
        var node = document.createTextNode(text);
        para.appendChild(node);
        var element = document.getElementById(id);
        element.appendChild(para);
    }
}
createEntry(verbs.length, "VERB", "verb")
createEntry(nouns.length, "NOUN", "noun")
createEntry(adjs.length, "ADJECTIVE", "adj")
createEntry(advs.length, "ADVERB", "adv")
createEntry(nums.length, "NUMBER", "num")
