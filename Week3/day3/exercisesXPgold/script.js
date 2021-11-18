//Exercise 1 : Animation With The Alphabet
let root = document.getElementById('root');
let str = "abcdefghijklmnopqrstuvwxyz";
let left = 0;

for(var i = 0; i< str.length; i++){
   let div = document.createElement('div');
   div.classList.add('box');
   div.setAttribute('draggable','true');
   div.innerText = str[i];
   div.style.left= left +"px";
   left =left + 51;
   root.appendChild(div);
   div.addEventListener('dragend',function(e){
      let x = e.clientX;
      let y = e.clientY;
      div.style.left = x + 'px';
      div.style.top = y + 'px';
      console.log(x,y);
   })
}




//Exercise 2 : Animation With A Paragraph


// function dragStart(event) {
//             event.dataTransfer.setData("Text", event.target.id);
//          }
//          function draggingNow(event) {
//             document.getElementById("Text").style.fontFamily ="Impact,Charcoal,sans-serif";
//          }
//          function dropNow(event) {
//             event.preventDefault();

//          }
//          function drop(event) {
//             event.preventDefault();
//             var data = event.dataTransfer.getData("Text");
//             event.target.appendChild(document.getElementById(data));
            
//          }
//          document.getElementById("Text").style.fontFamily ="Impact,Charcoal,sans-serif";