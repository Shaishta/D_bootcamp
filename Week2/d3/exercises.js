/*let obj = {
	username:"Shaishta",
	password:"itiswhatitis12"
}
console.log(obj.username);
console.log(obj.password);

let database= []
database.push(obj);
console.log(database);


let obj1 = {
	name:"Shodna",
	timeline:"1271",
	nickname:"Shai"

}
let obj2 = {
	name:"Shodna",
	timeline:"1271",
	nickname:"Shai"

}
let obj3 = {
	name:"Shodna",
	timeline:"1271",
	nickname:"Shai"

}

let newsfeed=[];
newsfeed.push(obj1);
newsfeed.push(obj2);
newsfeed.push(obj3);
console.log(newsfeed);

//ex1
for(let i = 0;i<=15;i++){
	console.log(i)

if (i%2==0){
	console.log("0 is even")
}
else if(i%2==1){
console.log("1 is odd")}
else{
	console.log("2 is even")
}
}*/

//Exercise1
/*let colors = ["blue","red","green"] 
console.log(colors);

for (let i in colors) {
	console.log(i)
	  console.log(colors[i])
	  if (i==0){
	console.log("My #1 choice is blue")
}
else if(i==1){
	console.log("My #2 choice is red")
}
else {
	console.log("My #3 choice is green")
}
}*/

//Exercise 2 : List Of People
/*let people = ["Greg", "Mary", "Devon", "James"]
console.log(people);
people.shift();
console.log(people);
people.splice(2,1,"Jason");
console.log(people);
people.push("Shaishta");

for(let i=0; i<people.length; i++){
	if (people[i]=="Jason"){
		break;
	}
	console.log(people[i])
}

console.log(people)
console.log(people.slice(1,3))

console.log(people.indexOf("Mary"));
console.log(people.indexOf("Foo"))

let last = people[people.length -1]
console.log(last)*/

//Exercise 3 : Repeat The Question
/*
let result = prompt("Enter a number: ");
console.log(result)
let num = 10

do {
    result < num;
    num = parseInt(prompt('Enter a number: '));
} 
while(num >= 10){
	console.log(typeof 'result')

}
*/


//Exercise 4 : Building Management
/*
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor , building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[1],building.numberOfRoomsAndRent.dan[0] )

if (building.numberOfRoomsAndRent.sarah[1] + 
	building.numberOfRoomsAndRent.david[1] > 
	building.numberOfRoomsAndRent.dan[1]
	) {
	console.log('rent is increased to 1200')
}
else {
	console.log(building.numberOfRoomsAndRent.dan[1])
}
*/
//Exercise 5 : Family
/*let family={
	names:"Sophie",
	age:"20",
	names:"Anne",
	age:"49",
	names:"Danny",
	age:"49"
}


for (names in family){
		console.log(family.names) 	
}

for (age in family){
	console.log(family.age)
}
*/

//Exercise 6
/*let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

console.log("my  " + details.my + "  is  " + details.is + "  the  " + details.the)
*/

//Exercise 7 : Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

console.log(names.sort());

let short = names.toString();
let spl = short.split("");
console.log(spl);
spl.splice(1,6);
spl.splice(2,7);
spl.splice(3,4);
spl.splice(4,4);
spl.splice(5,6);
spl.splice(6,7);
console.log(spl);
short=spl.join("");
console.log(short);





