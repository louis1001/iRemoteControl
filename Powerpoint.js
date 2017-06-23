var prevButton;
var nextButton;
var leftImage;
var rightImage;

var variables = ["key", "scroll"];

var variable = variables[0];

function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  leftImage = loadImage("data/left.jpeg");
  rightImage = loadImage("data/right.jpeg");
  prevButton = new Button(true, leftImage);
  nextButton = new Button(false, rightImage);
  
  console.log("Hello");
}

function draw() {
  background(0);
  prevButton.show();
  nextButton.show();
}

function http_send(vari, direction){
  var url_to_load = "http://"+window.location.hostname+":8000/?"+vari+"="+direction;
  print(url_to_load);
  httpGet(url_to_load);
}

function mousePressed() {
  if (mouseX < width / 2) {
    prevButton.click();
    http_send(variable, "left");
    //client.move(0)
  } else {
    nextButton.click();
    http_send(variable, "right");
    //client.move(1)
  }
}
