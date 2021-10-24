//Exercise 1
let me = ["my","favorite","color","is","blue"];
console.log(me);
let m = me.join();
console.log(m);

//Exercise 2
let str1 = "mix";
let str3 = str1.slice(1); 
let str2 = "pod";
let str4 = str2.slice(1);
console.log(str3);
console.log(str4);
let rep = str1.replace(str3,str4);
let rep2 = str2.replace(str4,str3);
console.log(rep);
console.log(rep2);
let res = rep.concat( rep2);
console.log(res);

//Exercise 3
let num1 = prompt ("Please enter a number from 0 to 10");
console.log(num1);
let num2 = prompt ("Please enter a number from 10 to 30");
console.log(num2);
alert(Number(num1) + Number(num2));
let num3 = prompt ("Please enter a number from 0 to 10");
console.log(num3);
let num4 = prompt ("Please enter a number from 10 to 30");
console.log(num4);
alert(Number(num3) - Number(num4));
let num5 = prompt ("Please enter a number from 0 to 10");
console.log(num5);
let num6 = prompt ("Please enter a number from 10 to 30");
console.log(num6);
alert(Number(num5) / Number(num6));
let num7 = prompt ("Please enter a number from 0 to 10");
console.log(num7);
let num8 = prompt ("Please enter a number from 10 to 30");
console.log(num8);
alert(Number(num7) + Number(num8));

