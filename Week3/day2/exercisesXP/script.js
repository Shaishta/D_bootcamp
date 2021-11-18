//console.log('hello')
// Part 1
// let h1 = document.getElementsByTagName('h1')
// console.log(h1[0])

// // Part 2
// let paras = document.getElementsByTagName('p')
// let para_len = paras.length
// paras[para_len - 1].remove();

// // Part 3
// let h2 = document.querySelector('h2')
// console.log(h2);
// h2.addEventListener("click", function(event){
//     h2.style.backgroundColor = 'Red';
// });

// // Part 4
// let h3 = document.querySelector('h3')
// console.log(h3);
// h3.addEventListener("click", function(event){
//     h3.style.display = 'None';
// })

// // Part 5
// function bold_para(){
//     console.log("Turn all paragraph bold");
//     let paras = document.getElementsByTagName('p');
//     console.log(paras);

//     for (let p of paras){
//         p.style.fontWeight = 'bold';
//     }
// }
// // part 6
// let tit1 = document.querySelector('h1');
// tit1.addEventListener("click", function(event){
//     h1.style.fontSize = Math.floor(Math.random() * 101);
// })
// //part 7

//form ex2
// let form = document.forms.my;
// //or let form = document.forms[0];
// console.log(form);
// console.log(form.elements);

// let fname = document.getElementById('fname');
// let lname = document.getElementById('lname');
// console.log(fname,lname);
 
// // console.log (frm.elements.fname)
// // console.log (frm.elements.lname)




// form.addEventListener("submit",function(e){
//     e.preventDefault();
//     let fname_value = document.getElementById('fname').value;
//     let lname_value = document.getElementById('lname').value;
//     console.log(fname_value.trim().length)

// })

//   function a(){
//      if (fname_value.trim().length > 0){
//         alert('Submit!')

//     }
//     else{
//         alert('Please enter a valid input!')
//     }
//     return false
//  }





//exercise3
// function getBoldItems(){
//     let boldItems = document.querySelectorAll("#paragraph strong");
//     return boldItems;
// }

// //make the variable global
// let boldItemFromParagraph = getBoldItems();

// function highlight(){
//     for (let i = 0; i < boldItemFromParagraph.length ; i++){
//         boldItemFromParagraph[i].classList.toggle("changeColor")
//     }
// }

// // highlight and returnNormal do the same things. So we can delete one of them


// // function returnNormal(){
// //  for (let i = 0; i < boldItemFromParagraph.length ; i++){
// //      boldItemFromParagraph[i].classList.toggle("changeColor")
// //  }
// // }


// let p = document.querySelector("#paragraph");
// p.addEventListener("mouseover", highlight)
// // we change the callback function from returnNormal to highlight
// p.addEventListener("mouseout", highlight)

//Exercice 3 : Volume Of A Sphere
function volume_sphere()
 {
  let volume;
  let radius = document.getElementById('radius').value;
  radius = Math.abs(radius);
  volume = (4/3) * Math.PI * Math.pow(radius, 3);
  volume = volume.toFixed(4);
  document.getElementById('volume').value = volume;
  return false;
 } 
window.onload = document.getElementById('MyForm').onsubmit = volume_sphere;
    

