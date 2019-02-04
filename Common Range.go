package main

import (
    "bufio"
    "os"
    "fmt"
    "strings"
    "strconv"
)


func main() {
    var t, count int
    fmt.Scan(&t)
    // fmt.Println(t)
    
    for i := 0; i < int(t); i++ {
        
        fmt.Scan(&count)
        
        scanner := bufio.NewScanner(os.Stdin)
        
        scanner.Scan()
        temp_a := strings.Fields(scanner.Text())
        
        scanner.Scan()
        temp_p := strings.Fields(scanner.Text())
        
        scanner.Scan()
        temp_q := strings.Fields(scanner.Text())
        
        // a := make([]int, int(count))
        // p := make([]int, int(count))
        // q := make([]int, int(count))
        
        a := []int{}
        p := []int{}
        q := []int{}
        // var a,p,q []int
        
        // fmt.Println(temp_a,temp_p,temp_q)
        // fmt.Println(a,p,q)
        
        for j := 0; j < int(count); j++ {
            temp, _ := strconv.Atoi(temp_a[j])
            a = append(a,temp)
            
            temp, _ = strconv.Atoi(temp_p[j])
            p = append(p,temp)
            
            temp, _ = strconv.Atoi(temp_q[j])
            q = append(q,temp)
        }
        
        // fmt.Println(a,p,q)
            
        low := a[0]-q[0]
        high := a[0]+p[0]
        
        // fmt.Println(low,high)
        
        for j := 1; j < count; j++ {
            if a[j]-q[j]>low {
                low = a[j]-q[j]
            }
            if a[j]+p[j]<high {
                high = a[j]+p[j]
            }
        }
        
        fmt.Println(high-low+1)
        
        // fmt.Println(temp_a[0]+temp_p[0]+temp_q[0])
        
 
	}
}