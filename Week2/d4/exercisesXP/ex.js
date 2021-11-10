//ex1
/*
function myAge(myAge){
	let mumage = myAge*2;
	let dadage = mumage*1.2;
	let arr = [mumage,dadage]
	
	return arr
	
}
let result = myAge(20);
console.log("My mum is "+ result[0]+, "and my dad is " + result[1])
*/


//exercises

//Exercise 1 : Information
//Part I
/*
function infoAboutMe(){
	let name = shaishta;
	let age = "20";
	let hobby = music;

	console.log("My name is "+ name + "I'm "+ age +"I love "+ hobby +".")
}

*/

//Part II
/*
function infoAboutperson(personName, personAge, personFavoriteColor){

		console.log("You name is " + personName  + "you are " + personAge +" years old" + "your favorite color is "+ personFavoriteColor " . ")
	}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")
*/

//Part III
/*
function infoAboutperson(personName, personAge, personFavoriteColor, personHobbies){
		
		let arr = [personName, personAge, personFavoriteColor, personHobbies]
		console.log("You name is " + personName  + "you are " + personAge +" years old" + "your favorite color is "+ personFavoriteColor + " . ")
		for(let i= 0; i< personHobbies.length; i++){
			console.log(personHobbies);
		}

	}

infoAboutperson("David", 45, "blue", ["tennis", "painting"])
infoAboutperson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])
*/

//Exercise 2 : Keyless Car
/*
let age = prompt('Please enter your age:');
console.log(age);
age = Number(age)

function checkDriverAge(){

	if (age === 18) {
alert('"Congratulations on your first year of driving. Enjoy the ride!')
	console.log("after condition");

}
 else if (age>18) {
 	
alert('"Powering On. Enjoy the ride!" ');

 }

 else {
 	alert('"Sorry, you are too young to drive this car. Powering off"');
	}

}

checkDriverAge()

*/
//Exercise 3: Odd Or Even
/*
let num1 = prompt ("Please enter a number ");
console.log(num1);

num1 = Number(num1)

function checkNumber(){
	
	for (i=0;i<=100;i++){
		console.log[i];
	}
	if(num1 % 2 == 0) {
    console.log("The number" + num1 + "is even.");
}


	else {
    console.log("The number" + num1 + "is odd.");
}

	
}

checkNumber()
*/

//Exercise 4 : Tips
/*
let bill = prompt("Enter the amount of the bill:")
console.log("$" + bill);
bill=Number(bill);


function tipAmount(value){
	
	if(value<50){
		console.log(value*0.2)
		return (value*0.2)
	}
	else if(value>=50 && value<=200){
		console.log(value*0.15)
		return value*0.15
	}
	else if(value>200){
		return(value*0.1)
		}	
}
let tip = tipAmount(bill)

let finalBill = tip+bill
console.log(finalBill)
*/


//Exercise 5 : Find The Numbers Divisible By 23

/*
function isDivisible(){
	let arr =[]
	for(let i=0;i<500;i++){
		//console.log[i];

		if(i%23==0){
			arr.push(i)
		}
		
	}
	console.log(arr)
	let sum=0
	for(let j=0;j<arr.length;j++){
		//sum=sum+arr[j]
		sum+=arr[j]

	}
	console.log(sum)
}

isDivisible()
*/

//Exercise 6 : Amazon Shopping
/*
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
let item = prompt('Enter an item:')
	console.log(item)


function checkBasket(){
	if(item in amazonBasket){
		console.log(amazonBasket[item]+" is available")
	}
	else{
		console.log("This is not available.")
	}
}
checkBasket()
*/

//Exercise 7 : Shopping List
/*
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana","orange", "apple"]

let total = 0;

function in_stock(item) {
	return stock[item] > 0
}

function buy(item){
	total += prices[item];
	stock[item] -= 1;
}
for (item of list){
	if in_stock(item) {
	buy(item)
	}
}
*/

//Exercise 8 : What’s In My Wallet ?
// let change = [0.25,0.1,0.05,0.01];


// function changeEnough(item_price,arr_pocket_amount) {
// 	let total = 0;
// 	for (var i = 0; i < arr_pocket_amount.length; i++) {
// 		total += (arr_pocket_amount[i]*change[i]); 
// 	}
// 	if(total>=item_price){
// 		return true
// 	}
// 		return false
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]));
// //.......................................................
// //Exercise 8 : What’s In My Wallet ?
// let change = {
// 	quarters = 0.25,
// 	dimes =  0.10,
// 	nickel =  0.05,
// 	penny =  0.01
// }
// function changeEnough(item_price,arr_pocket_amount) {
// 	let total = 0;
	
// 		total += change.quarters*arr_pocket_amount[0]; 
// 		total += change.dimes*arr_pocket_amount[1]; 
// 		total += change.nickel*arr_pocket_amount[2]; 
// 		total += change.penny*arr_pocket_amount[3]; 
	
// 	if(total>=item_price){
// 		return true
// 	}
// 		return false
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]));



//ex9 Vacations Costs
// function hotelCost(){

// }








