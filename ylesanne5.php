<?php
	
	error_reporting(-1);
	$edasi = true;
	$number = 20;
	
	while($edasi == true)
	{
		//echo "<p>Number on $number</p>";
		for($i = 20; $i > 0; $i--)
		{
			if($number % $i == 0)
			{
				//echo "<p>Jagub $i-ga<p>";
				if($i == 1)
				{
					$edasi = false;
				}
			}
			else
			{
				break;
			}
		}	
		$number += 20;
	}
	$number -= 20;
	echo "<p>Number, mis jagub 1-20ga on $number</p>";
	
?>