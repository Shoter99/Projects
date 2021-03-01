function TimeToText(i){
	var text;
	if((i<6) && (i>19)){
		text = "Good Night";
	}else if((i>6)&&(i<12)){
		text = "Good Morning";
	}else{
		text = "Good Afternoon";
	}
	return text;
}
function myFunction() {
	  var d = new Date();
	  var x = document.getElementById("demo");
	  var h = d.getHours();
	  x.innerHTML = TimeToText(h);
}

