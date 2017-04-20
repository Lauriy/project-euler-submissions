<?php

	error_reporting(-1);
	
	$fibonaccinumbrid = array();
	$fibonaccinumbrid[0] = 0;
	$fibonaccinumbrid[1] = 1;
	$loendur = 2;
	$edasi = true;
	$summa = 0;
	
	while($edasi)
	{
		$j2rgmine = $fibonaccinumbrid[$loendur - 1] + $fibonaccinumbrid[$loendur - 2];
		if($j2rgmine < 4000000)
		{
			$fibonaccinumbrid[$loendur] = $j2rgmine;
			$loendur++;
			if($j2rgmine % 2 == 0)
			{
				$summa += $j2rgmine;
			}
		}
		else
		{
			$edasi = false;
		}
	}
	
	echo $summa;
?>