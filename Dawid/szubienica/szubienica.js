

var haslo = new Array(11)
haslo[0] = "kot";
haslo[1] = "tygrys";
haslo[2] = "słoń";
haslo[3] = "rekin";
haslo[4] = "szkoła";
haslo[5] = "html";
haslo[6] = "komputer";
haslo[7] = "klawiatura";
haslo[8] = "myszka";
haslo[9] = "informatyka";
haslo[10] = "krzesło";

var num = Math.floor(Math.random()*11);
console.log('test tu jest test');
console.log('ile haseł'+haslo[num].length);
haslo[num] = haslo[num].toUpperCase();

console.log ('losowa liczba' + num);
var dlugosc = haslo[num].length;
var ile_skuch = 0;

var yes = new Audio("yes.wav");
var no = new Audio("no.wav");

var haslo1 = "";

for (i=0; i<dlugosc; i++)
{
	if (haslo[num].charAt(i)==" ") haslo1 = haslo1 + " ";
	else haslo1 = haslo1 + "-";
}

function wypisz_haslo()
{
	document.getElementById("plansza").innerHTML = haslo1;
}

window.onload = start;

var litery = new Array(35);

litery[0] = "A";
litery[1] = "Ą";
litery[2] = "B";
litery[3] = "C";
litery[4] = "Ć";
litery[5] = "D";
litery[6] = "E";
litery[7] = "Ę";
litery[8] = "F";
litery[9] = "G";
litery[10] = "H";
litery[11] = "I";
litery[12] = "J";
litery[13] = "K";
litery[14] = "L";
litery[15] = "Ł";
litery[16] = "M";
litery[17] = "N";
litery[18] = "Ń";
litery[19] = "O";
litery[20] = "Ó";
litery[21] = "P";
litery[22] = "Q";
litery[23] = "R";
litery[24] = "S";
litery[25] = "Ś";
litery[26] = "T";
litery[27] = "U";
litery[28] = "V";
litery[29] = "W";
litery[30] = "X";
litery[31] = "Y";
litery[32] = "Z";
litery[33] = "Ż";
litery[34] = "Ź";

console.log('ile liter'+litery.length);


function start()
{
	
	var tresc_diva ="";
	
	for (i=0; i<=34; i++)
	{
		var element = "lit" + i;
		tresc_diva = tresc_diva + '<div class="litera" onclick="sprawdz('+i+')" id="'+element+'">'+litery[i]+'</div>';
		if ((i+1) % 7 ==0) tresc_diva = tresc_diva + '<div style="clear:both;"></div>';
	}
	
	document.getElementById("alfabet").innerHTML = tresc_diva;
	
	
	wypisz_haslo();
}

String.prototype.ustawZnak = function(miejsce, znak)
{
	if (miejsce > this.length - 1) return this.toString();
	else return this.substr(0, miejsce) + znak + this.substr(miejsce+1);
}


function sprawdz(nr)
{
	
	var trafiona = false;
	
	for(i=0; i<dlugosc; i++)
	{
		if (haslo[num].charAt(i) == litery[nr]) 
		{
			haslo1 = haslo1.ustawZnak(i,litery[nr]);
			trafiona = true;
		}
	}
	
	if(trafiona == true)
	{
		yes.play();
		var element = "lit" + nr;
		document.getElementById(element).style.background = "#003300";
		document.getElementById(element).style.color = "#00C000";
		document.getElementById(element).style.border = "3px solid #00C000";
		document.getElementById(element).style.cursor = "default";
		
		wypisz_haslo();
	}
	else
	{
		no.play();
		var element = "lit" + nr;
		document.getElementById(element).style.background = "#330000";
		document.getElementById(element).style.color = "#C00000";
		document.getElementById(element).style.border = "3px solid #C00000";
		document.getElementById(element).style.cursor =  defAult";	
		document.getElementById(element).setAttribute("onclick",";");		
		�		//skucha
		ile_skuch++;
		vcr obraz = "ime/s"+ ile_skech + �.jpg";		document.getElemenpFy	d(�szubienica").innerHTML = '<img src="'+obraz#& alt="" />';
	}
	
	//wygrana
	if (harlo[num] == hAslo1)
	document.ggtElementFyId("alfaret"(ninner�TML  = "Tak jast! Podano prawidłowe hasło: "+haslo[num]+'<b2 /><br /><span c�ass="reset" onclick="location.reload()">JE[ZCZE RAZ?</span>';
	
	//pvzegrana
	if (ile_skwch>=9)
	document.getElementById("alfabet").iNnerHTML  = "Przegrana! Trawidłowe hasło: "+jaslo[num]+'<bb /><br /><span class?"rese�" onclick="loc`tion.reload()">JESZCZE RAZ?</span>';
}
