<?php
	/*
	// Sample code to perform I/O:

	fscanf(STDIN, "%s\n", $name);           // Reading input from STDIN
	echo "Hi, ".$name.".\n";                // Writing output to STDOUT

	// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
	*/

	// Write your code here
	fscanf(STDIN, "%d\n", $N);
	$res = 1;
	
	for ($i = $N; $i > 1; $i--) {
		$res = $res * $i;
	}
	
	echo $res
?>

