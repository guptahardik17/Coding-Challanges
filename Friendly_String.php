<?php
fscanf(STDIN, "%d\n", $t);
for ($i=0;$i<$t;$i++)
{
    fscanf(STDIN, "%d\n", $count);
    $values = array();
    $output = 0;
    
    for ($j=0;$j<$count;$j++)
    {
        fscanf(STDIN, "%s\n", $temp);
        
        $stringParts = str_split($temp);
        sort($stringParts);
        
        $values[] = implode('', $stringParts);
    }
    
    for ($x=0;$x<$count;$x++)
    {
        for ($y=$x;$y<$count;$y++)
        {
            $result = "";
            
            if(strlen($values[$x])==2*strlen($values[$y]))
            {
                for($z = 0; $z < strlen($values[$x]); $z +=2 )
                {
                    $result .= $values[$x][$z];
                }
                if($result==$values[$y])
                {
                    $output+=1;
                    break;
                }
            }
            else if(strlen($values[$y])==2*strlen($values[$x]))
            {
                for($z = 0; $z < strlen($values[$y]); $z +=2 )
                {
                    $result .= $values[$y][$z];
                }
                if($result==$values[$x])
                {
                    $output+=1;
                    break;
                }
            }
        }
    }
    
    print_r($output."\n");
}

?>