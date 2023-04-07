clock='''var argsFromMain=null;
function init(prms) {
  argsFromMain=prms;
}
//init();
if (argsFromMain == null) {
  argsFromMain=[300, 10, 10];
}
const width= argsFromMain[0];
cnvs.width=width;
cnvs.height=width;
ctx.clearRect(0,0, cnvs.width, cnvs.height);
var radius = width/2;ctx.translate(radius, radius);
radius = radius * 0.90;
function drawFace (ctx, radius) {
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2*Math.PI);
  ctx.fillStyle = "white";
  ctx.fill();
  ctx.strokeStyle = "black";
  ctx.stroke();
}
function drawNumbers (ctx, radius) {
  var ang;
  var num;
  ctx.font = radius*0.15 + "px arial";
  ctx.textBaseline="middle";
  ctx.fillStyle = "black";
  ctx.textAlign="center";
  for (let num = 1; num < 13; num++) {
    ang = num * Math.PI / 6;
    ctx.rotate(ang);
    ctx.translate(0, -radius*0.85);
    ctx.rotate(-ang);
    ctx.fillText(num.toString(), 0, 0);
    ctx.rotate(ang);
    ctx.translate(0, radius*0.85);
    ctx.rotate(-ang);
  }
}
function drawHand (ctx, pos, length, width) {
  ctx.beginPath();
  ctx.lineWidth = width;
  ctx.lineCap = "round";
  ctx.moveTo (0, 0);
  ctx.rotate(pos);
  ctx.lineTo(0,-length);
  ctx.stroke();
  ctx.rotate(-pos);
}
drawFace (ctx, radius);
drawNumbers (ctx, radius);
var hour=argsFromMain[1];
var minute=argsFromMain[2];
hour=hour%12;
hour=hour*Math.PI/6 + minute*Math.PI/(6*60);
drawHand (ctx, hour, radius*0.5, radius*0.04);
minute=(minute*Math.PI/30);
drawHand (ctx, minute, radius*0.8, radius*0.02);'''
