//Exercise 1 : Is_Blank
/*
let isBlank = prompt('Enter something:');

if(isBlank == ""){
 console.log("isBlank('')");
 
}
else{
  console.log("isBlank('abc')");
  
}
*/

//Exercise 2 : Abbrev_name
/*
abbrev_name = function (str1) {
    let split_names = str1.trim().split(" ");
    if (split_names.length > 1) {
        return (split_names[0] + " " + split_names[1].charAt(0) + ".");
    }
    return split_names[0];
};
console.log(abbrev_name("Shaishta Pandea"));
*/

//Exercise 3 : SwapCase
/*
let str = prompt('Enter a phrase:');
let UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let LOWER = 'abcdefghijklmnopqrstuvwxyz';
let result = [];
  
  for(let x=0; x<str.length; x++)
  {
    if(UPPER.indexOf(str[x]) !== -1)
    {
      result.push(str[x].toLowerCase());
    }
    else if(LOWER.indexOf(str[x]) !== -1)
    {
      result.push(str[x].toUpperCase());
    }
    else 
    {
      result.push(str[x]);
    }
  }
console.log(result.join(''));
*/

//Exercise 4 : Omnipresent Value
/*
let arr = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];
function isOmnipresent(arr, val) {
    for (let i = 0; i < arr.length; i++) {
        if (!arr[i].includes(val)) {
            return false
        }
    }
    return true;
}
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) )
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)) 
console.log(isOmnipresent([[5], [5], [5], [6, 5]], 5))
console.log(isOmnipresent([[5], [5], [5], [6, 5]], 6)) 
*/