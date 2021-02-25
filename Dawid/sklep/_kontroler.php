<?php

	$baza = "baza/";
	$errors = array();

// dodawanie pozycjie

	if(!empty($_POST['nazwa']) && strlen($_POST['nazwa'])>3)
	{
		$dozapisu = strip_tags($_POST['nazwa'].'|'.$_POST['ilosc'].'|'.$_POST['cena']);
		
		if(isset($_POST['edit']))
		{
			$file = 'baza/'.$_POST['edit'];	
		}
		else
		{
			$file = 'baza/'.time().'.txt';			
		}
		
		file_put_contents($file, $dozapisu);
		header("location: ./");
	}
	elseif(isset($_POST['nazwa']))
	{
		$dozapisu = strip_tags($_POST['nazwa'].'|'.$_POST['ilosc'].'|'.$_POST['cena']);
		
		if(!empty($dozapisu) && strlen($dozapisu)<=3) $errors[] = 'Nazwa za krótka min. 3 znaki';
	}
	
// usuwanie pozycji
	 
	if(isset($_GET['delete']) && file_exists($baza.$_GET['delete'])&& strlen($_GET['delete']) == 14)
	{
		@unlink($baza.$_GET['delete']);		
		header("location: ./");		
	}
	
//  edytowanie pozycji 

	if(isset($_GET['edit']) && file_exists($baza.$_GET['edit'])&& strlen($_GET['edit']) == 14)
	{
		$zapis = explode("|", file_get_contents($baza.$_GET['edit']));
		$_POST['nazwa'] = $zapis[0];
		$_POST['ilosc'] = $zapis[1];
		$_POST['cena'] = $zapis[2];
	}