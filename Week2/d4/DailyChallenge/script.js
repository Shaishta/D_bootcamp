let str = 'Hello,world,in,a,frame';

//get the largest length of the word in an array

function getLength(arr){
	let len =0;

//Hello World in a frame	
	for (let i = 0; i<arr.length; i++){
		if (arr[i].length>len){
			len =arr[i].length;
		}
	}
	return len;
}
//calculate the spaces after a word
function calcSpaces(words, len) {
	return len-words.length;
}


function wrapWords(param){

//split words into array
	let words = param.split(", ");

//get the largest word
	let largest_len = getLength(words);

//print the first line
	console.log('*'.repeat(largest_len+4))
	for(let i=0;i<words.length;i++){

	let spaces = calcSPaces(words[i],largest_len);

		console.log("* " + words[i] +" ".repeat(spaces) + " *")
	}

//print the last line
	console.log('*'.repeat(largest_len+4))
}
wrapWords()