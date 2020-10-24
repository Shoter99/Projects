void setup(){
  size(1360,720);
}
void draw(){
   background(255);
   drawCircle(width/2,height/2,800);
}
      



void drawCircle(float x, float y, float radius){
  color(255,0,0);
  ellipse(x,y,radius,radius);
  stroke(0);
  noFill();
  
  if(radius > 8){
    
    drawCircle(x + radius/2,y,radius/2);
    drawCircle(x - radius/2,y,radius/2);
    drawCircle(x,y + radius/2,radius/2);
    drawCircle(x,y - radius/2,radius/2);
  }}
