<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Website 1.0 Download Center</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body onload="Clock()">
    <br>
    <div id="welcome" id="clock"></div>
    <br>
    <br>
    <a href="index.php"><div class="welcome">Welcome to my Website 1.0 </div></a>
    <div id="responde">
        <h2 style="color:moccasin;text-align:center;">Leave your updates here</h2>
        <form action="update.php" method="post">
            <textarea  name="comment" id="comment" rows="10" tabindex="4" required="required" style="width:100%; height:100%;" ></textarea><br><br>
            <input id="submited" name="submit" type="submit" value="Submit"  />
        </form>
    </div>
    <div class="content">
      <h1 style="color: white;text-align:center;">Things to do</h1>
      <?php
        $read = fopen("updates.txt","r") or die("cannot open a file");
        $count = 1;
        while(!feof($read)){
          echo $count.". ".fgets($read)."<br>";
          $count+=1;
        }
        fclose($read);
      ?>
    </div>
    <div class="content">
      <h1 style="color: white;text-align:center;">Things done</h1>
      <?php
        $read = fopen("done.txt","r") or die("cannot open a file");
        $count = 1;
        while(!feof($read)){
          echo $count.". ".fgets($read)."<br>";
          $count+=1;
        }
        fclose($read);
      ?>
    </div>
    <script type="javascript" href="scripts.js"/>
</body>
</html>

