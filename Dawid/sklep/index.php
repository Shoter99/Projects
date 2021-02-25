<?php

session_start();
	
	if ( isset($_POST['password']) && $_POST['password'] == 123){	
		$_SESSION['logowanie'] = 1;
	}
	elseif ( isset($_POST['password'])) {
		echo '<div > Nie poprawne hasło</div> ';
	}	

	if(isset($_SESSION['logowanie']) && $_SESSION['logowanie'] == 1)
	{
		include '_kontroler.php';
		include '_widok.php';
		
	}
	else
	{
		include '_logowanie.php';
	}
