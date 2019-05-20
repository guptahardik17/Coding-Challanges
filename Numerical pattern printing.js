function innerPattern(n){
    var size = 2 * n - 1; 
    var front = 0; 
    var back = size - 1;
    var a = new Array(size).fill(null).map(()=>new Array(size).fill(null));
    while (n !== 0)  
    { 
        for (var i = front; i <= back; i++) { 
            for (var j = front; j <= back; j++) { 
                if (i == front || i == back || 
                    j == front || j == back) 
                a[i][j] = n; 
            } 
        } 
        ++front; 
        --back; 
        --n; 
    }
    for (i = 0; i < size; i++) { 
        console.log(a[i].join(" "));
        console.log('\n'); 
    }
}

function main(input) {
    lines = input.split("\n");
    for(var i = 1; i <= parseInt(lines[0]); i++)
    {
        innerPattern(parseInt(lines[i]));
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