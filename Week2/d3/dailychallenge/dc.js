 //Daily Challenge: Stars
//simple loop

 for(var i=1; i<=6; i++){
       console.log("* ".repeat(i));
    }

//nested loop
let n = 6;
let string = "";
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);    