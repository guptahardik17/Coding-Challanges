function main(input) {
    process.stdout.write(input);
    lines = input.split("\n");
    for(var i = 1; i <= parseInt(lines[0]); i++)
    {
        var calculate = parseInt(lines[i])*2+1;
        process.stdout.write(calculate.toString()+"\n");
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