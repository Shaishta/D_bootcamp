let sentence= "The movie is not that bad, I like it."
let wordNot = sentence.indexOf("not");{
	console.log(wordNot)
}

let wordBad = sentence.indexOf("bad");{
	console.log(wordBad)
}

let arr = sentence.split("");
if (wordNot<wordBad && wordNot !wordNot= -1 && !wordBad = -1){
	arr.splice(wordNot, wordBad-wordNot +3, "good")
}
else  {
	arr.join()
}