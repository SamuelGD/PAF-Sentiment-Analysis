<?php


$text = addslashes($_GET['text']);


if(isset($_GET['class']) && $_GET['class'] == 2)
	$class = 2;
else
	$class = 3;

$lowertext = strtolower($text);

$input = 'python handle_opinion.py "'.$lowertext.'" '.$class;

system($input, $output);


$opinion = (string) $output[0];

$opinion = (string) $opinion.";".stripslashes($text);

echo $opinion;

?>