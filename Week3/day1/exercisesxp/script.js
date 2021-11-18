//Exercise 1 : Change The Navbar
// //changing navbar to social..
// let div = document.getElementById('navBar');
// console.log(div.setAttribute('Id','socialNetworkNavigation'));

// //new li
// let list = document.createElement('li');
// console.log(list);

// //textnode
// let newText = document.createTextNode('Logout');
// console.log(newText);

// //append
// list.appendChild(newText);
// document.getElementById('socialNetworkNavigation').appendChild(list);

//--------------------------------------------------------------------------------

//Exercise 2 : Users
// let div = document.getElementById('container');
// console.log(div);
// let list =document.getElementsByTagName('ul');
// console.log(list)
// console.log(list[0].lastElementChild.innerHTML="Richard");

// list[0].firstElementChild.innerHTML="Shaishta";
// list[1].firstElementChild.innerHTML="Shaishta";
// //list[1].removeChild(list[1].childNodes[1]);
// console.log(list[1].removeChild(list[1].childNodes[3]))

//--------------------------------------------------------------------------------

//Exercise 3 : Users And Style
// “light blue” background color and some padding to the <div>.
let div = document.getElementById('div')
div.style.backgroundColor = 'lightblue';
div.style.padding = "10px 20px 10px 20px";

//Do not display the first name (John) in the list.
let list = document.getElementsByTagName('ul');
list[0].removeChild(list[0].firstElementChild);

//Add a border to the second name (Pete)
let pete = list[0].firstElementChild;
console.log(pete);
pete.style.border = "thick solid #CE93D8";

//Change the font size of the whole body
let body = document.body;
body.style.fontSize = 'x-large';