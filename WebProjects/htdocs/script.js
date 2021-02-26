function HoursToText(i){
    if((i > 5 ) && (i<12)){
        i = "Good Morning";
    }
    else if(i<17){
        i = "Good Afternoon";
    }
    else{
        i = "Good Night";
    }
    return i;
}

function Clock(){
    var d = new Date();
    var doc = document.getElementById("clock");
    var h = HoursToText(d.getHours());
    doc.innerHTML = h;
}