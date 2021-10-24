//Exercise 1 : Divisible By Three
/*
let numbers = [123, 8409, 100053, 333333333, 7]
console.log(numbers)
for(let i = 0;i<numbers.length;i++){
	console.log(i)

if (i%3==0){
	console.log("True")
}

else{
	console.log("False")
}
}
*/

//Exercise 2 : Attendance
/*
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}
console.log(guestList);

let item = prompt('Enter your name:')

if(item in guestList ){
	console.log("Hi! " + " I'm " + item + " and I'm from " + guestList[item] +".")
}
else{
	console.log("I'm a guest.")
}*/

//Exercise 3 : Playing With Numbers
let age = [20,5,12,43,98,55];
let sum = 0;


for (let i = 0; i < age.length; i++) {
    sum += age[i];
}
console.log(sum);
let highest = age[0];
for (let i=0; i<=age,length;i++)
{
    if (highest<age[i]) {
         highest = age[i];
    }
}

console.log(highest);
