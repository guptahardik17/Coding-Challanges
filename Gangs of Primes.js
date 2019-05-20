function checkPrime(number){
    for(let i = 2, s = Math.sqrt(number); i <= s; i++)
        if(number % i === 0) return false; 
    return number > 1;
}

function primeGangs(grid) {

    function checkNeighbour(grid, x, y, visited) {
      if(x < 0 || x > grid.length - 1 || y < 0 || y > grid[x].length - 1) {
        return;
      }
      if(visited[x][y] === true) {
        return;
      }
      visited[x][y] = true;
      if(grid[x][y] === '0') {
        return;
      }
      checkNeighbour(grid, x - 1, y, visited);
      checkNeighbour(grid, x + 1, y, visited);
      checkNeighbour(grid, x, y - 1, visited);
      checkNeighbour(grid, x, y + 1, visited);
    }
    
      let visited = [];
      for(let i = 0; i < grid.length; i++) {
        visited[i] = [];
      }
      let count = 0;
      for(let x = 0; x < grid.length; x++) {
        for(let y = 0; y < grid[x].length; y++) {
          if(!visited[x][y] && grid[x][y] === '1') {
            count++;
            checkNeighbour(grid, x, y, visited);
          }
          visited[x][y] = true;
        }
      }
    return count;
}

function main(input) {
    lines = input.split("\n");
    counter = 1;
    for(var x = 1; x <= parseInt(lines[0]); x++)
    {
        var size = lines[counter].split(" ");
        counter+=1;
        var a = [];
        for(var y=0; y<size[0];y++){
            a.push(lines[counter].split(" "));
            counter+=1;
        }
        
        for(var i=0; i<size[0]; i++){
            for(var j=0; j<size[1]; j++){
                if(checkPrime(a[i][j])){
                    a[i][j] = '1';
                }
                else{
                    a[i][j] = '0';
                }
            }
        }
        console.log(primeGangs(a))
        // process.stdout.write(calculate.toString()+"\n");
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