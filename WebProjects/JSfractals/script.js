

function setup(){
    createCanvas(400,400);
}
var ang = (PI / 8);
function draw(){
 background(51);
 stroke(255);
 translate(200, height);
 branch(100,PI/8);
}

function branch(len,angle){
    line(0,0,0,-len);
    translate(0,-len);
    if (len >4){
        push()
        rotate(angle);
        branch(len*0.67,PI/8)   
        pop()
        push()
        rotate(-angle)
        branch(len*0.67,PI/8) 
        pop()  
    }
    rotate(angle)
}