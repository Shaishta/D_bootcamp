//Exercise 1:
//1.
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);

//2. 
fruits.sort();
  console.log(fruits);

//3.
 fruits.push("Kiwi");
console.log(fruits); 

//4.
fruits.splice(0, 1);
console.log(fruits);
//use index instead of 0 
//let indexofapple = fruits.indexof["Apples"];
//console.log(fruits);

//5.
fruits.reverse();
console.log(fruits)

//Exercise 2:
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);

/*let white = moreFruits[0];
console.log(white);

let light = moreFruits[1][0];
console.log(light);

let purple = moreFruits [1][2];
console.log(purple);

let Orange = moreFruits [1][1][0];
console.log(Orange);
console.log("Oranges");*/