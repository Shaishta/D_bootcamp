//Exercise 1 : Move The Box
/*
function setTime_out(){
  setTimeout(function(){
   console.log('heloo')
  },3000);
}
let id;
function setInter_val(){
  id = setInterval(function(){
    console.log('hiii')
  },2000)
}

function clearInter_val(){
  clearInterval(id)
}

function myMove() {
  let pos = 0;
  let elem = document.getElementById('animate');
  let id = setInterval(function(){
      if(pos === 350){
        clearInterval(id)
      }
      else {
        elem.style.left = pos + 'px';
               pos++;
      }
  },5)
}
*/

//Exercise 2: Drag & Drop
const fill = document.querySelector('.fill');
const empties = document.querySelectorAll('.empty');

// Fill listeners
fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);

// Loop through empty boxes and add listeners
for (const empty of empties) {
  empty.addEventListener('dragover', dragOver);
  empty.addEventListener('dragenter', dragEnter);
  empty.addEventListener('dragleave', dragLeave);
  empty.addEventListener('drop', dragDrop);
}

// Drag Functions

function dragStart() {
  this.className += ' hold';
  setTimeout(() => (this.className = 'invisible'), 0);
}

function dragEnd() {
  this.className = 'fill';
}

function dragOver(e) {
  e.preventDefault();
}

function dragEnter(e) {
  e.preventDefault();
  this.className += ' hovered';
}

function dragLeave() {
  this.className = 'empty';
}

function dragDrop() {
  this.className = 'empty';
  this.append(fill);
}
