addFractions='''var argsFromMain=null;
function init(prms) {
  argsFromMain=prms;
}
//init();
if (argsFromMain == null) {
  argsFromMain=[200, [1, 2, 2, 3]];
}
var height = argsFromMain[0];
cnvs.height = height;
cnvs.width=2*height;
var radius = cnvs.height/4;
var cY = cnvs.height/2;
var cX = cnvs.width/2;
var radius = cY-20;
ctx.beginPath();
ctx.font="normal 60px Arial";
ctx.fillStyle="black";
ctx.fillText("+", cX-17, cY+20);
var angle = 2*Math.PI/argsFromMain[1][1];
for (let j=0; j<argsFromMain[1][1]; j++) {
  ctx.beginPath();
  ctx.moveTo(cX-radius-20, cY);
  ctx.strokeStyle="black";
  if (j<argsFromMain[1][0]) {
    ctx.fillStyle="#ed7";
  }
  else {
    ctx.fillStyle="white";
  }
  ctx.arc(cX-radius-20, cY, radius, j*angle, (j+1)*angle);
  ctx.lineTo(cX-radius-20, cY);  ctx.fill();  ctx.stroke();
}
angle = 2*Math.PI/argsFromMain[1][3];
for (let j=0; j<argsFromMain[1][3]; j++) {
  ctx.beginPath();
  ctx.moveTo(cX+radius+20, cY);
  ctx.strokeStyle="black";
  if (j<argsFromMain[1][2]) {
    ctx.fillStyle="#7ed";
  }
  else {
    ctx.fillStyle="white";
  }
  ctx.arc(cX+radius+20, cY, radius, j*angle, (j+1)*angle);
  ctx.lineTo(cX+radius+20, cY);
  ctx.fill();
  ctx.stroke();
}'''
