<?php ini_set('session.gc_maxlifetime', 300); session_start(); if($_SESSION["logged"] == false){header("Location: login.php");echo "You are not allowed!";}?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Website 1.0 Download Center</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body> 
    
    <script src="script.js"></script>
    <br>
    <?php
	$t = date("H");
	if(($t <"12")and ($t > "6")){
    echo '<div id="welcome">Good Morning</div>';
  }
  elseif(($t > "12")and($t <"18")){
    echo '<div id="welcome">Good Afternoon</div>';
  }
  else{
    echo '<div id="welcome">Good Night</div>';
  }
    ?>
    <br>
    <br>

    <a href="index.php"><div id="welcome">Welcome to my Website 1.0 </div></a>
    <div id="menu">
      1 Soon here will be stream form cam.
      <br><br>
    <form action="logout.php" method="post">
      <input style="background-color: #3F9167; color: white;font-size:28px; " type="submit" name="logout" value="Log out">
    </form>
  </body>
</html>

