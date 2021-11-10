


function playTheGame(){
	let answer = confirm('Do you want to play a game:');
	console.log(answer)
		if (answer === false){
			 alert("No problem, Goodbye.")
		}
		else{
			//let num = prompt('Enter a number from 0 to 10:');
			//console.log(num);
			 //num=Number(num);
			 let randomNumber = Math.floor(Math.random()*10);

			 let chances = 1;
			 while(chances<=3){
			 	let userNumber = prompt('Enter a number from 0 to 10: [chances ' + chances +']')
			 	userNumber=Number(userNumber)
			 	
			 		let good = chooseNum( userNumber, randomNumber);
			 		if (good){
			 			let game= test(userNumber,randomNumber)
			 			if (game){
			 				if (chance=== 3){
			 					alert('You are out of chances')
			 					break;
			 				}
			 				
			 			}
			 			else{
			 				chances++
			 			}
			 			console.log(userNumber, randomNumber)
			 			chances++//=chances+1
			 		}
			 }
		}
		alert('Game Over!!')

}

playTheGame()

function chooseNum(num, randomNumber) {
	if(num>=0 && num<=10){
		return true
		}
				
	else if (num<0 && num>10){
				alert('“Sorry it’s not a good number, Goodbye”.');
				return false
			}	
	else{
				alert("Sorry Not a number, Goodbye")
				return false
			}		
	
}
			 
				
function test(userNumber,computerNumber,chances){
	if(userNumber===computerNumber){
		alert("WINNER")
		return true
	}

	else if(userNumber>computerNumber){
		console.log(chances)
		prompt("Your number is bigger then the computer’s, guess again" );
		return false
		
	}

	else if(userNumber<computerNumber){
		console.log(chances)
		prompt("Your number is smaller then the computer’s, guess again")
		return false
	}

}



