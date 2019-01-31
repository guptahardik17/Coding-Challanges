<?php

fscanf(STDIN, "%d\n", $count);
$values = array_map('intval', explode(' ', fgets(STDIN)));

function gcd( $a, $b) 
{ 
    if ($a == 0) 
        return $b; 
    return gcd($b % $a, $a); 
} 
  
function findGCD($arr, $n) 
{ 
    $result = $arr[0]; 
    for ($i = 1; $i < $n; $i++) 
        $result = gcd($arr[$i], $result); 
   
    return $result; 
} 

echo (findGCD($values, $count)); 

?>
