var Button = function(prev, imag, scroll = false){
      this.scroll = scroll;
      if (this.scroll){
         this.si = createVector(width, height/2);
         this.pos = prev ? createVector(0, 0) : createVector(0, height/2);
      }else{
         this.si = createVector(width/2, height);
         this.pos = prev ? createVector(0, 0) : createVector(width/2, 0);
      }
      
      this.im = imag;
      
      if (this.scroll){
         this.name = prev ? "left" : "right";
      }else{
         this.name = prev? "up" : "down";
      }
}

Button.prototype.show = function(){
   stroke(255);
   strokeWeight(3);
   noFill();

   rect(this.pos.x, this.pos.y, this.pos.x + this.si.x, this.pos.y + this.si.y);
   
   
   // if(this.scroll){
   //    rect(this.pos.x, this.pos.y, this.pos.x + this.si.x, this.pos.y + this.si.y);
   // }else{
   //    rect(this.pos.x, this.pos.y, this.pos.x + this.si.x, this.pos.y + this.si.y);
   // }
   
   image(this.im, this.pos.x, this.pos.y, this.si.x, this.si.y);
}

Button.prototype.click = function(){
   stroke(255, 0, 255);
   strokeWeight(5);
   var message = "press: " + this.name;
   console.log(message);
}