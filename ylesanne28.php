<?php

	error_reporting(-1);
	
	$summa = 0;
	$kylg = 1;
	
	while($kylg < 1002)
	{
		if($kylg == 1)
		{
			$summa += 1;
		}
		else
		{
			$a = pow($kylg, 2);
			$summa += ($a + ($a - ($kylg - 1)) + ($a - 2 * ($kylg - 1)) + ($a - 3 * ($kylg - 1)));
		}
		$kylg += 2;
	}
	
	echo $summa;
	
?>