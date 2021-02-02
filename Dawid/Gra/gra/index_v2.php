<?php

	$plik = 'stangry.txt';
	
	if(file_exists($plik))
	{
		$stan = file_get_contents($plik);
		$stan = unserialize($stan);
	}

	if(isset($_POST['id']) && $_POST['value'] > 0)
	{	
		$stan[$_POST['id']] = $_POST['value'];
		file_put_contents($plik, serialize($stan));
		echo 'success';
		die;
	}
	
	if(isset($_POST['odswiez']))
	{
		for ($i = 0; $i <= 2; $i++)
		{
			for ($x = 0; $x <=2 ; $x++)
			{
				if(isset($stan['pole_'.$i.'_'.$x]))
				{
					echo '<select class="sel" disabled="disabled"><option>'.$stan['pole_'.$i.'_'.$x].'</option></select>';
				}
				else
				{
					echo '<select onclick="ustawPole(this);" class="sel" id="pole_'.$i.'_'.$x.'">
						<option value="0"></option>
						<option value="1">X</option>
						<option value="2">O</option>
						</select>';
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

    <title>Hello, world!</title>
	<style>
	body{
		background-color:black;
	}
	#container
	{
		
		margin-right: auto;
		margin-left: auto;
		width: 1000px;
		
	}
	.sel
	{
		width: 80px;
		height: 40px;
		margin: 5px;
		text-algin: center;
		background-color: black;
		color: white;
		
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
	</style>
  </head>
  <body>
	<div id = "container">
	
	<div id="plansza"></div>
	
</div>

    <!-- JavaScript -->
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
		  url: "index_v2.php",
		  data: { odswiez: 1 }
		})
		  .done(function( msg ) {
			$("#plansza").html(msg);
		  });
	}
	
	function ustawPole(obiekt)
	{
		// // // // // // // // // // // // // // // // // $.ajax({
		  method: "POST",
		  url: "index.php",
		  data: { id: $(obiekt).attr('id'), value: $(obiekt).val() }
		})
		  .done(function( msg ) {
			if(msg == 'success') console.log('ok');
		  });
	}
	
	setInterval(function() { odswiez() }, 2000);
		
	
	
</script>
	
  </body>
|/html>