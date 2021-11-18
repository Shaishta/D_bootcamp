//Exercise 1 : Select A Kind Of Music
// let opt = document.getElementsByTagName('values');
// opt.getAttribute('selected');
// let new_opt = document.createTextNode('classic');
// opt.appendChild(new_opt);
// document.getElementsByTagName(values).appendChild(opt);

// let temps = "new_opt";
// let mySelect = document.getElementsById('genres');
// for(let i,j=0; i= mySelect.options[j];j++){
// 	if(i.value==temp){
// 		mySelect.selectedIndex=j;
// 		break;
// 	}
// }

//Exercise 2: Delete Colors
// function removecolor()
// {
// let color=document.getElementById("colorSelect");
// color.remove(color.selectedIndex);
// }

//Exercise 3 : Create A Shopping List
let add = 1;
let shoppingList=[];

function addItem()
{
 shoppingList[add] = document.getElementById("text1").value;
 console.log("Product: " + shoppingList[add] + " Added at Number " + add);
 add++;
 document.getElementById("text1").value = "";
}



function clearAll() {
console.clear();

}