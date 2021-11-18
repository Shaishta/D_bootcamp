let color = null;
let mousedown = false;

let body = document.getElementsByTagName("body")[0];
let color_blocks = document.querySelectorAll("#sidebar > *");
let fill_boxes = document.querySelectorAll("#box > *");
let clearAll_button = document.getElementById('button');

//put script inside the body not before body
clearAll_button.addEventListener ("click", function() {
    for (fill_box of fill_boxes){
        fill_box.style.backgroundColor = "white";
    }
});

body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})


for (color_block of color_blocks){
    color_block.addEventListener("click", function(event){
        color = event.target.style.backgroundColor;
    });
}

for (fill_box of fill_boxes){
    fill_box.addEventListener("mousedown", function(event){
        if (color != null) event.target.style.backgroundColor = color;
    });
    fill_box.addEventListener("mouseover", function(event){
        if (mousedown && color != null) event.target.style.backgroundColor = color;
    });
}
