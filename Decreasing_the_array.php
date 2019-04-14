<?php

fscanf(STDIN, "%d\n", $t);
for($i=0;$i<$t;$i++)
{
    fscanf(STDIN, "%d\n", $count);
    $values = array_map('intval', explode(' ', fgets(STDIN)));
    fscanf(STDIN, "%d\n", $counter);
    $initializers = array_map('intval', explode(' ', fgets(STDIN)));
    $limits = array_map('intval', explode(' ', fgets(STDIN)));
    
    
    for($j=0;$j<$counter;$j++)
    {
        $output = 0;
        if($initializers[$j]==1)
        {
            $temp = array_slice($values, 0, $limits[$j]);
            $minimum = min($temp);
            $output += $minimum;
            
            $temp = array_map(function($val) use ($minimum){ return $val-$minimum; }, $temp);
            
            $new_array = array_merge($temp, array_slice($values, $limits[$j]));
            $maximum = max($new_array);
            $output+= $maximum;
        }
        else if($initializers[$j]==-1)
        {
            $temp = array_slice($values, $count - $limits[$j]);
            $minimum = min($temp);
            $output += $minimum;
            
            $temp = array_map(function($val) use ($minimum){ return $val-$minimum; }, $temp);
            
            $new_array = array_merge(array_slice($values, 0 , $count - $limits[$j]),$temp);
            $maximum = max($new_array);
            $output+= $maximum;
        }
        print_r($output." ");
    }
}


?>