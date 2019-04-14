<?php

function isInside($x, $y, $N){
    if ($x >= 1 and $x <= $N and $y >= 1 and $y <= $N){
        return(true);
    }
    return(false);
}
       
function minStepToReachTarget($knightpos, $targetpos, $N){
    $dx = array(2, 2, -2, -2, 1, 1, -1, -1);
    $dy = array(1, -1, 1, -1, 2, -2, 2, -2);
      
    $queue = array(); 
    $queue['x'] = $knightpos[0];
    $queue['y'] = $knightpos[1];
    $queue['dist'] = 0;
    
    $visited = array();
    for($i=0;$i<=$N;$i++)
    {
        for($j=0;$j<=$N;$j++)
        {
            $visited[$i][$j] = "False";
        }
    }
    
    $visited[$knightpos[0]][$knightpos[1]] = "True";
    
    print_r(count($queue));
    
    while(count($queue) > 0){
        $t = $queue;
        $queue = array();
        
        if($t['x'] == $targetpos[0] and $t['y'] == $targetpos[1]){
            return($t['dist']);
        }
              
        for($i=0;$i<8;$i++){
            $x = $t['x'] + $dx[$i];
            $y = $t['y'] + $dy[$i];
              
            if(isInside($x, $y, $N) and $visited[$x][$y]=="False"){
                $visited[$x][$y] = "True";
                $queue['x'] = $knightpos[0];
                $queue['y'] = $knightpos[1];
                $queue['dist'] = $t['dist']+1;
            }
        }
              
    }
          
} 

$N = 8;
$knightpos = [7, 3]; 
$targetpos = [3, 8];
print_r(minStepToReachTarget($knightpos, $targetpos, $N));

?>