<?php ini_set('session.gc_maxlifetime', 300); session_start();if(isset($_SESSION["logged"]))if($_SESSION["logged"] == true) header("Location: cam.php");?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Website 1.0</title>
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
    <div id="welcome">Welcome to my Website 1.0 </div>
    <div id="menu">
      1.<a href="downloads.php"> Downloads</a>
      <br>
      <h2>Please log in to view rest of the page</h2>
      <form action="login.php" method="post">
        Enter your login: <input type="text" name="login"><br><br>
        Enter your password: <input type="password" name="pass"> <br>
        <input class="submited"; type="submit" value="Submit">
      </form>
      <?php
        if(isset($_SESSION["failed_login"])) echo $_SESSION["failed_login"];
        unset($_SESSION["failed_login"]);
        ?>
  </body>
</html>
