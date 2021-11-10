//ask for the numbers

	let num1 = prompt('Enter a first number:')
	num1=Number(num1)
	console.log(num1);

//ask for the operator
	 let opr = prompt('Enter operator:(either +,-,*, or /)') ;
	 console.log(opr)
	
	let num2 = prompt('Enter a second number:');
	num2=Number(num2)
	console.log(num2);
	
	
//calculate the values
let number = ( num1,opr,num2) =>{
 	if (opr == "+"){
 		alert(num1 + num2);
 		let num3 =(num1 + num2)
 		return
 		console.log(num3);
 	}
 	else if (opr == "-"){
 		alert(num1 - num2);
 		let num3 = (num1 - num2);
 		return
 		console.log(num3);
 	}
 	else if (opr == "/"){
 		alert (num1 / num2);
 		let num4 = (num1 / num2);
 		return
 		console.log(num4);
 	}
 	else if (opr == "*"){
 		alert (num1*num2);
 		let num5 = (num1*num2);
 		return
 		console.log(num5);
 	}
 	else{
 	}
 }
 number(num1,opr,num2)
