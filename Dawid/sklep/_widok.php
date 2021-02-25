<!doctype html>
<html lang="pl">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
	<style type = "text/css">
		#text
		{
			width: 50%;
		}
	</style>
    <title>Sklep</title>
  </head>
  <body>

	<h1>Sklep</h1>	
	<form action="index.php" method="POST">
		<div class="form-group">
			<?php foreach((array)$errors as $error): ?>
				<?=$error;?>
			<?php endforeach;?>	
			
			<input type="text" name="nazwa" placeholder="nazwa" class="text" value="<?=((isset($_POST['nazwa']))?$_POST['nazwa']:'');?>" >
			<input type="text" name="ilosc" placeholder="ilosc" class="text" value="<?=((isset($_POST['ilosc']))?$_POST['ilosc']:'');?>" >
			<input type="text" name="cena" placeholder="cena" class="text" value="<?=((isset($_POST['cena']))?$_POST['cena']:'');?>" >
			<?php if(isset($_GET['edit'])):?><input type="hidden" name="edit" value="<?=$_GET['edit'];?>"/><?php endif; ?>
			
			<input  type="submit"></input>	
			<?php
				echo '<a href = "_wylogowanie.php" > Wyloguj się</a>'
			?>
		  </div>  
		  
		</div>
		
	</form>

<table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>	 
      <th scope="col">Nazwa</th>
      <th scope="col">Ilość</th>
      <th scope="col">Cena</th>
      <th scope="col">Opcje</th>
    </tr>
  </thead>
  <tbody>
    
	<?php
	
	$a = scandir($baza);
	$i = 0;
	foreach((array)$a as $nazwaPliku)
	{
		if(strlen($nazwaPliku)>3)
		{
			$zapis = explode("|", file_get_contents($baza.$nazwaPliku));
			$i++;
			echo '<tr>
				  <th scope="row">'.$i.'</th>
				  <td>'.$zapis[0].'</td>
				  <td>'. $zapis[1].'</td>
				  <td>'. $zapis[2].'</td>
				  <td><a href="?delete='.$nazwaPliku.'" class="btn btn-danger">Usuń pozycje</a> 
					  <a href= "?edit='.$nazwaPliku.'" class = "btn btn-warning">Edytuj</a></td>
				</tr>';
						//echo '<td>'.file_get_contents($baza.$nazwaPliku).'</td>';			
		}
	}
		?>
		
		
  </tbody>
</table>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
  </body>
</html>