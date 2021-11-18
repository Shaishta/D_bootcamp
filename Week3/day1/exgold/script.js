// //gold exercises
// let allBooks = [
// 	{
// 		title:"The Great Gatsby",
// 		author: "F.Scott Fitzgerald", 
// 		img:"https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781471173936/the-great-gatsby-9781471173936_hr.jpg",
// 		alreadyRead:true
// 	}, 
// 	{
// 		title:"The Alchemist ",
// 		author:"Paulo Coelho",
// 		img:"http://3.bp.blogspot.com/-L_vNcreT79M/UVl-cUrlFoI/AAAAAAAADFM/nRDtusQKQt8/s1600/The-Alchemist-Paulo-Coelho.jpg",
// 		alreadyRead:false
// 	}
// ]

// //table
// let tb1 =document.createElement('table');
// 	tb1.style.width = '100%';
// 	tb1.setAttribute('id','tableid');
// 		document.getElementsByTagName('body')[0].appendChild(tb1);

// //call function
// allBooks.forEach(booklist);

// //functions

// function booklist(arg,i){
// 	let details1 = allBooks[i]["title"] + "written by" + allBooks[i]["author"];
// 	let details2 = allBooks[i]["alreadyRead"];
// 	let cover = allBooks[i]["img"];

// 	let tr1 = document.createElement("tr");
// 	let th1 = document.createElement("th");
// 		th1.innerText = "Book";
// 	let th2 = document.createElement("th");
// 		th2.innerText = "Details";

// 		document.getElementById("tableid").appendChild(tr1);
// 		document.getElementById("tableid").lastChild.appendChild(th1);
// 		document.getElementById("tableid").lastChild.appendChild(th2);

// let tr2 = document.createElement("tr");
// let td1 = document.createElement("td");
// 	td1.setAttribute("rowspan",2);

// let img = document.createElement("img");
// 	img.setAttribute("src",cover);
// 	img.setAttribute("style","width:100px");
// 	td1.appendChild(img);

// let td2 = document.createElement("td");
// 	td2.innerText = details1;

// 	document.getElementById("tableid").appendChild(tr2);
// 	document.getElementById("tableid").lastChild.appendChild(td1);
// 	document.getElementById("tableid").lastChild.appendChild(td2);

// let tr3 = document.createElement("tr");
// let td3 = document.createElement("td");
// 	td3.innerText = details2;

// 	if(details2){
// 		td3.setAttribute("style","color:red","font-weight:bold")
// 		td3.innerText="DONE"
// 	}
// 	else{
// 		td3.innerText="pending"
// 	};

// 	document.getElementById("tableid").appendChild(tr3);
// 	document.getElementById("tableid").lastChild.appendChild(td3);
// }	

//Exercise 2 : Red Table
let table = document.body.firstElementChild;

	for (let i = 0; i < table.rows.length; i++) {
	let row = table.rows[i];
	row.cells[i].style.backgroundColor = 'red';
	}