<?php

try
{
    $bdd = new PDO('mysql:host=localhost;dbname=paf_chat;charset=utf8', 'server', 'tInIcO8762');
    
}
catch (Exception $e)
{
        die('Erreur : ' . $e->getMessage());
}

$reponse = $bdd->query('SELECT * FROM message WHERE id IN ( SELECT MAX(id) FROM message )');

$donnees = $reponse->fetch();

$text = "";

if( strcmp( $donnees['users'] , "none") == 0 )
{

    echo "nothing";
    
}
else
{ 

    if( strcmp( $donnees['users'] , $_GET['user'] ) != 0 )
    {

    $id = $donnees['id'];

    $text = (string) $donnees['message'];

    $bdd->exec('DELETE FROM message WHERE id = "'.$id.'"');

    echo $donnees['id'].";".$text;

    }
   
}



?>