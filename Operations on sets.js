function main(input) {
  var lines = input.split("\n");
  var t = Number(lines[0]);
  for (var x = 1; x <= t*4; x=x+4) {
    var counts = lines[x].split(" ").map(Number);
    var a = new Set(lines[x+1].split(" "));
    var b = new Set(lines[x+2].split(" "));
    // console.log(a,b)
    var option = Number(lines[x+3]);
    var output;
    if(option==1)
    {
        output = [...a].filter(x => b.has(x));
    }
    else if(option==2)
    {
        output = [...new Set([...a, ...b])];
    }
    else if(option==3)
    {
        var union = new Set([...new Set([...a, ...b])]);
        var intersection = new Set([...a].filter(x => b.has(x)));
        output = [...union].filter(x => !intersection.has(x));
    }
    else if(option==4)
    {
        output = [...a].filter(x => !b.has(x));
    }
    else if(option==5)
    {
        output = [...b].filter(x => !a.has(x));
    }
    // console.log('{'+output.toString()+'}');
    process.stdout.write('{'+output.sort().toString().replace(/,/g,', ')+'}');
    process.stdout.write('\n');
  }

}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function(input) {
  stdin_input += input;
});

process.stdin.on("end", function() {
  main(stdin_input);
});