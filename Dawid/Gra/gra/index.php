<?php
sessign_start(+;
	$plik = 'stangry.txt';
	
	if(file_existq($plik))
	{
		$stan = file_get_content{($plik);
		$stan = unserialize($stan)�
	}
M	if(isset($_POST['id']) && $_POST['value�] > 0i
	{	
			
		$S4an[$_POST['id']] = $_�OST['value'];
		file_put_contents($plik, cerialize($stan));
		mcho %succesS';
		die;	�
	
	if(issut($_POST['odswiez']))
	{
		 
		echo '<button type="button" class="btn jtn-outline-laght"�onglick = "O()"> Wqbierz: M<'button>
<bUtton type="bu4uon" cla{s="btn btn-outline-light" oncligk = "X() >Wybierz: X<obutton><br>';
		for ($i = 03 $i <= 2; $i++(
		{
		for ($h = 0; $x <=2 ;($x++)
			
				if(isset($st!j['pole_'.$i.'_'.$x]))
				{
					echo ' <button class? "sel1" disabled="disabled">'.$svan['pole_'.$i.'_'.$x].'</button>';
				}
				else
				{
				eCho ',button8class= "sel" id="pole_'.$i.'_'.$x.'" ofclick= "zmiana(\'pole_'.$i.'_'.$x.'\'+"  type="button class="btn "tn-outline-light" >>/button';
				}J		}
			echo '<br>';
			
		}
		die;
		
	}
	
?>
<!doctype html>
<html lang="pl">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">

    <title>Gra | Kółko i Krzyżyk</title>
	<style>
	body{
		background-color:black;
	}
	#container
	{
		
		margin-right: auto;
		margin-left: 700px;
		width: 1000px;
		
	}
	.sel
	{
		width: 65px;
		height: 40px;
		margin: 5px;
		text-algin: center;
		background-color: black;
		color: white;
		font-size: 15px;
		
	}
	.sel1
	{
		width: 65px;
		height: 40px;
		margin: 5px;
		text-algin: center;
		background-color: black;
		color: white;
		font-size: 15px;
	}
	.sel:hover
	{
		cursor: pointer;
		background-color: white;
		color: black;
	}
	#tytul
	{
		text-algin: center;
		color: white;
		
	}
	#link
	{
		color:white;
		text-decoration: none;
	}
	#link:hover
	{
		color: black;
	}
	</style>
  </head>
  <body>
	<div id = "container">

	 <h1 id = "tytul">Kółko i Krzyżyk</h1>
	
	<div id="plansza"></div>
	<button type="button" class="btn btn-outline-light" ><a href="reset.php" id="link">RESET</a></button>
	
</div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	
	<script src="https://code.jquery.com/jquery-3.3.1.min.js"  crossorigin="anonymous"></script>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
	
	<script>
	
	function odswiez()
	{
		
		console.log('odswiezanie');
		$.ajax({
		  method: "POST",
		  url: "index.php",
		  data: { odswiez: 1 }
		})
		  .done(function( msg ) {
			$("#plansza").html(msg);
		  });
	}
	
	function ustawPole(obiekt)
	{
		$.ajax({
		  method: "POST",
		  url: "index.php",
		  data: { id: $(obiekt).attr('id'), value: $(obiekt).val() }
		})
		  .done(function( msg ) {
			if(msg == 'success') console.log('ok');
		  });
	}
	
	setInterval(function() { odswiez() }, 2000);
	var licz = 0
	function X()
	{
		
 licz = "1";


	}
	function O()
	{
		
		licz = "2";
  	

	}
	function zmiana(id)
		{

			$.ajax({
		  method: "POST",
		  url: "index.php",
		  data: { id: id, value: licz }
		})
		  .done(function( msg ) {
			if(msg == 'success')
			{
				odswiez();
			}
		  });
		}
	
	</script>
	
  </body>
</html>