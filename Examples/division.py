division='''var argsFromMain=null;
function init(prms) {
  argsFromMain=prms;
}
//init();
if (argsFromMain == null) {
  argsFromMain=[[50,1000], ['x', '8', '÷', '3', '=', '6']];
}
cnvs.height = argsFromMain[0][0];
cnvs.width = argsFromMain[0][1];
function drawRect(xo, yo) {
  ctx.beginPath();
  ctx.strokeStyle="#888";
  ctx.rect(xo, yo, rectA, rectA);
  ctx.stroke(); ctx.closePath();
}
const word=argsFromMain[1], rectA=40, xo=50.5, yo=0.5, digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x'];
for (let i=0; i<word.length; i++) {
  if (digits.includes(word[i])) {
    ctx.beginPath();
    ctx.strokeStyle="#888";
    ctx.rect(xo+i*(rectA+5), yo, rectA, rectA);
    ctx.stroke();
  }
  if (word[i] != 'x') {
    ctx.beginPath();
    ctx.fillStyle="red";
    ctx.textAlign="center";
    ctx.font="normal 40px Palatino Linotype";
    ctx.fillText(word[i], xo+i*(rectA+5)+rectA/2, yo+rectA-6);
  }
}'''
