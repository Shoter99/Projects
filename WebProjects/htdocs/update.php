<?php
    $msg = $_POST["comment"];
    $file = fopen("updates.txt","a") or die("Unable to open a file");
    fwrite($file,$msg);
    
    fclose($file);
    echo "<script>
alert('Thank you for your update!');
window.location.href='changes.php';
</script>";
    ?>