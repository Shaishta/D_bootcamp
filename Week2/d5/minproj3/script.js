/*
//welcome
alert('Welcome to Hangman');
//user1
let word = prompt('User 1, Please enter your word:')
//

 for (var i = 0; i < word.length; i++) {
 word[i] = "*";
 }
 var remainingLetters = word.length;
 // The game loop
 while (remainingLetters > 0) {
 // Show the player their progress
 alert(answerArray.join(" "));
 // Get a guess from the player
let guess = prompt("Guess a letter, or click Cancel to stop playing.");

 if (guess === null) {
 // Exit the game loop
 break;
 } 
 else if (guess.length !== 1) {
 alert("Please enter a single letter.");
 } 
 else {
 // Update the game state with the guess
 for (let j = 0; j < word.length; j++) {
 if (word[j] === guess) {
 answerArray[j] = guess;
 remainingLetters--;
 }
 }
 }

 // The end of the game loop
 }
 // Show the answer and congratulate the player
 alert(answerArray.join(" "));
 alert("Good job! The answer was " + word);
 */

 // step 1
 // get user hidden word


//check 
//shold be a minimum of 8letters


 //step 2
 //get user2 Letter


 //step 3
 // 10guesses for user 2


//to check 
//prevent the choice of the same letter


function hangmanGame(){
    let word_to_guess = "";
do{
    word_to_guess = prompt('Please enter a word to guess - min 8 letters')
    console.log(word_to_guess)
    }
   //create an array 
while(word_to_guess.length < 8)

    let word_arr = word_to_guess.split('');
    let word_hidden = "*".repeat(word_to_guess.length).split('');

    console.log(word_hidden.join(''));

let guesses = 0;

while (guesses < 10){
    let letter = prompt('Please guess a letter:');
//check if letter exists

    for(var i = 0; i<word_arr.length;i++){

            if(word_arr[i]===letter){
                word_hidden[i] = letter;
            }
        } 
        console.log(word_hidden.join('')); 
        if(!word_hidden.includes('*')){
            console.log('You won');
            return//(to go out either we put break)

        } 
        else if (word_hidden.includes(letter));
        console.log('already there.')    
        
        guesses++;
    }
        if(guesses>=10){
            console.log('you lose');
        }

}
hangmanGame()
 //if letter is included in the  hidden array 
