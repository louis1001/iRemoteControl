b = undefined

var upButton;
var downButton;

function setup(){
  upImage = loadImage('data/up.jpeg');
  downImage = loadImage('data/down.jpeg');

  upButton = Button(true, upImage, true);
  upButton = Button(false, downImage, true);

}

function draw(){
  background(255);
  image()
  if(touches.length > 0){
    
  }else{
    
  }
}

function touchPressed(){

}

function http_send(vari, direction){
  var url_to_load = "http://"+window.location.hostname+":8000/?"+vari+"="+direction;
  print(url_to_load);
  httpGet(url_to_load);
}
