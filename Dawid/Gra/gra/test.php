<?php
	
	// otwarcie sesji
	session_start();

	// plik ze stanem gry
	$plik = 'stangry.txt';
	
	// jezeli plik istnieje to wczytanie danych
	if(file_exists($plik))
	{
		$stan = file_get_contents($plik);
		$stan = unserialize($stan);
	}

	if (isset($_POST['UstawGracza']))
	{
		$_SESSION['gracz'] = $_POST['UstawGracza'];
		$stan[$_POST['UstawGracza']] = $_POST['UstawGracza'];
		file_put_contents($plik, serialize($stan));
		echo 'success';
		die;
	}
			
	if(isset($_POST['id']) && isset($_SESSION['gracz']))
	{
		print_r($_POST);
		print_r($_SESSION['gracz']);
		die;
	}
		
	
	
	if(isset($_POST['odswiez']))
	{
		if (isset($_SESSION['gracz']))
		{	
			echo '<br>';
		}
		else
		{
			echo '<button type="button" class="btn btn-outline-light" onclick="UstawGracza(1)"> Wybierz: O</button>
			<button type="button" class="btn btn-outline-light" onclick="UstawGracza(2)">Wybierz: X</button><br>';
		}
		
		for ($i = 0; $i <= 2; $i++)
		{
			for ($x = 0; $x <=2 ; $x++)
			{
				if(isset($stan['pole_'.$i.'_'.$x]))
				{
					echo ' <button class= "sel1" disabled="disabled">'.$stan['pole_'.$i.'_'.$x].'</button>';
				}
				else
				{
					echo '<button class= "sel" id="pole_'.$i.'_'.$x.'" onclick= "zmiana(\'pole_'.$i.'_'.$x.'\')"  type="button" class="btn btn-outline-light" ></button>';
				}
			}
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
	#n{
		color: white;
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
		  url: "test.php",
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
		  url: "test.php",
		  data: { id: $(obiekt).attr('id'), value: $(obiekt).val() }
		})
		  .done(function( msg ) {
			if(msg == 'success') console.log('ok');
		  });
	}
	
	setInterval(function() { odswiez() }, 2000);
	var licz = 0;
	
	
	
	function UstawGracza(id)
	{
		$.ajax({
		  method: "POST",
		  url: "test.php",
		  data: {UstawGracza : id }
		})
		  .done(function( msg ) {
			if(msg == 'success') console.log('GraczUstawiony');
		  });
		
	}
		 
	
	function zmiana(id)
	{

			$.ajax({
		  method: "POST",
		  url: "test.php",
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