//declare
let libButton = document.getElementById('lib-button');

let libIt = function(){
	let storyDiv = document.getElementById('story');
	storyDiv.innerHTML = randomPhrase()
};

let randomPhrase = function () {
		let l1 =Math.Floor((Math.random() / (.10) + 1));
		let userNoun = document.getElementById("noun").value;
		let userAdjective = document.getElementById("adjective").value;
		let userName = document.getElementById("person").value;
		let userVerb = document.getElementById("verb").value;
		let userPlace = document.getElementById("place").value;

		let sentence

		if(l1<4){
			sentence = "Today, I found " + userName + " playing in a " + userPlace + " ."
		}
		else if(l1>=4 && l1 <7){
			sentence = "So, on a " + userAdjective + " day, " + userName + " and this " + userNoun + "came at my place."
		}
		else{
			sentence = "Since then, we " + userVerb + " together."
		}
		return sentence

}

libButton.addEventlistener('click', libIt);

	
