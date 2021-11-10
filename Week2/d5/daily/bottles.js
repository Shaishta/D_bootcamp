//the 99 beer song

function bSong() {  
 let bottles = prompt('Enter the number of bottles:');
 bottles = Number(bottles);
 let bottlesLeft;
  for (i = 99; i >= 1; i--) {
// if only 1 bottle is left
    if (i == 1) {
      bottles = "bottle";
        bottlesLeft = "No bottles of beer on the wall!";
    } 
//otherwise decrease the number of bottles    
    else {
      bottles = "bottles";
      bottlesLeft = i - 1 + " bottles of beer on the wall!";
    } 
    console.log(i+ " " + bottles + " of beer on the wall,");
    console.log(i+ " " + bottles + " of beer,");
    console.log("Take one down, pass it around,");
    console.log(bottlesLeft);
    } 
    
}
console.log(bSong());