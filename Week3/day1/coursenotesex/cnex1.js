./*For each of the questions, find 2 WAYS of accessing :

1. The div DOM node?

2. The ul DOM node?

3. The second li (with Pete)?*/

//ex.1
// //by id
// let div_users = document.getElementById('users');
// console.log(div_users);
// //by TagName
// let div_node = document.getElementsByTagName('div')
// console.log(div_node[0]);
// //ex 2
// let list = document.getElementsByTagName('ul');
// console.log(list[0]);

// //ex3

// let lastelem = document.getElementsByTagName('li')
// console.log(lastelem[1]);

// For each of the questions, find 2 WAYS to access :

// 1. The div node
// let first_div = document.getElementById('container');
// console.log(first_div);

// // 2. The ul nodes, and render all of it's children one by one
// let elements = document.querySelectorAll('ul,li');
// for (let elem of elements){
// 	console.log(elem.innerHTML);
// }

// // 3. The first li of each ul
// let first = document.querySelectorAll('ul,li:first-child')
// console.log(first[1].innerHTML)
// let last = document.querySelectorAll('.li_2');
// console.log(last[0].innerText)
//-------------------------------------------------------------------------------------
// Write variables to get the value of the attributes of the specified link :

// href
// hreflang
// rel
// target
// type
//ANS:

// let newLink = document.getElementById("dI");
// console.log(newLink.getAttribute('href'));
// console.log(newLink.getAttribute('hreflang'));
// console.log(newLink.getAttribute('rel'));
// console.log(newLink.getAttribute('target'));
// console.log(newLink.getAttribute('type'))

//-------------------------------------------------------------------------------------

//Modify the style of the paragraph text (such as fontSize, fontFamily, color, etc. )through javascript code.
let div = document.getElementById("text");
div.style.color= 'purple';
div.style.backgroundColor = 'pink';
div.style.fontFamily = 'Arial';
div.style.fontSize = 'x-large';
div.style.textAlign = 'center'




