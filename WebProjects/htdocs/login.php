<?php
ini_set('session.gc_maxlifetime', 300);
session_start();
$login = $_POST["login"];
$pass = $_POST["pass"];

if(($login == "test123") and ($pass == "test123")){
    header("Location: cam.php");
    $_SESSION["logged"] = true;
    $_SESSION["failed_login"] = false;
    unset($_SESSION["failed_login"]);
}
else{
    $_SESSION["failed_login"] = '<span style="color:Tomato">Your password or login is incorrect!</span>';
    header("Location: index.php");

}
    ?>
