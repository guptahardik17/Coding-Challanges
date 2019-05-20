function main(input) {
    lines = input.split("\n");
    for(var i = 1; i <= parseInt(lines[0]); i++)
    {
        var len = lines[i].length;
        var temp = lines[i];
        var sum = 0;
        
        for(var j=len-1; j>=0;j=j-2){
            cal = parseInt(temp[j])*2;
            if(cal < 10){
                sum+= cal;
            }
            else{
                cal = cal.toString()
                sum += parseInt(cal[0])+parseInt(cal[1])
            }
        }
        for(j=len-2; j>=0;j=j-2){
            sum+=parseInt(temp[j])
        }
        sum = sum.toString();
        sum = sum[sum.length - 1]
        if (sum==0){
            process.stdout.write(sum.toString()+'\n');
        }
        else{
            process.stdout.write((10 - sum).toString()+'\n');
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
    main(stdin_input);
});