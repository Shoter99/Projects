<?php
    $name = $_POST['name'];
    $lastname = $_POST['lastname'];
    $email = $_POST['email'];
    $text = $_POST['content'];
    if($lastname == "" or $lastname == 0){
        $message = "Imię $name,\nEmail $email,\n\nWiadomość $text"
    }
    else{
        $message = "Imię $name,\nNazwisko $lastname,\nEmail $email,\nWiadomość $text"
    }
    
    mail("dawidr2003@gmail.com", "FORM", $message);
    echo "<script>
alert('Dziękuję za wiadomość');
window.location.href='index.html';
</script>";
    
    ?>