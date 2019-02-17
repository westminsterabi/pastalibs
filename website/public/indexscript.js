console.log("hi")

jQuery(document).ready(function() {
  jQuery('form#pg1form').bind('submit', function(event) {
    
    event.preventDefault();
    
    var data = $("#pg1form");
    console.log("test")
    data = data.serializeArray()
    var formData = {"pasta_text" : data}
    formData = JSON.stringify(formData)

    console.log(formData)

    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/pasta_text",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function(result){
        console.log("done!")
        // page 2
        window.location.href = "pos.html"
        var JSONdata = result
        var alldata = JSON.parse(JSONdata);
        var posdata = alldata.blanked_text.data.parts_of_speech;
        createEntries(posdata, posdata.length, "div1")

        // page 3
        // var alldata = JSON.parse(JSONdata);
        // var textdata = alldata.blanked_text.data.text;

        // var para = document.createElement("p")
        // var node = document.createTextNode(textdata);
        // para.appendChild(node);
        // var element = document.getElementById("div1")
        // element.appendChild(para)

    }).fail(function(){
        alert("Failed")
    });
  });
})

