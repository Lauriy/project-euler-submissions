<?php

	error_reporting(-1);
	
	$ruutudesumma = 0;
	$summa = 0;
	
	for($i = 1; $i < 101; $i++)
	{
		$ruutudesumma += pow($i, 2);
		$summa += $i;
	}
	
	$summaruut = pow($summa, 2);
	$vahe = $summaruut - $ruutudesumma;
	
	echo "<p>Ruutude summa on: $ruutudesumma</p>";
	echo "<p>Summa ruut on: $summaruut</p>";
	echo "<p>Nende vahe: $vahe</p>";
	
?>