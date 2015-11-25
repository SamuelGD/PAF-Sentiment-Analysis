<?php

try
{
    $bdd = new PDO('mysql:host=localhost;dbname=paf_chat;charset=utf8', 'server', 'tInIcO8762');
    
}
catch (Exception $e)
{
        die('Erreur : ' . $e->getMessage());
}



$message = $_GET['message'];

$user = $_GET['user'];

$score = $_GET['score'];

$message = $score.";".$message;

$bdd->exec('INSERT INTO message (message ,  users) VALUES ( "'.$message.'" , "'.$user.'")');



?>