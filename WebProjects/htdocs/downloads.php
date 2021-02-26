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
      1 <a class="download" href="FirstPack.jar">Download My First Plugin </a>
      <br>
      2 <a class="download" href="changes.php">Suggest Changes Here</a>
      <br>
      3 <a class="download" href="TextToMorse.zip">Download Morse Code converter</a>
      <br>
      4 <a class="download" href="app-release.apk">Download Morse Code converter Android App</a>
      <br>
      5. <a class="download" href="Cisco Packet Tracer 6.2 for Windows Student Version (no tutorials)(1).exe">Download Cisco</a>
  </body>
</html>

