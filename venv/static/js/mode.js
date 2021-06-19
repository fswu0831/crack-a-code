
function clickBtn1(){
    var t1 = document.getElementById("t1");
	var t2 = document.getElementById("t2");
    var input_box = document.getElementsByClassName("input_box");
    var t1_class = t1.classList;
    var t2_class = t2.classList;

    if (!t1_class.contains("chosen")){
        t1.classList.add("chosen");
    }
    if (t2_class.contains("chosen")){
        t2.classList.remove("chosen");
    }
    if(input_box[0].name!="code"){
        input_box[0].name="code";
    }

}

function clickBtn2(){
    var t1 = document.getElementById("t1");
	var t2 = document.getElementById("t2");
    var input_box = document.getElementsByClassName("input_box")
    var t1_class = t1.classList;
    var t2_class = t2.classList;

    if (t1_class.contains("chosen")){
        t1.classList.remove("chosen");
    }
    if (!t2_class.contains("chosen")){
        t2.classList.add("chosen");
    }
    if(input_box[0].name!="plain"){
        input_box[0].name="plain";
    }

}