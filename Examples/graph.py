graph='''var argsFromMain=null;
function init(prms) {argsFromMain=prms;}
//init();
if (argsFromMain == null) {argsFromMain=[200, [1, 1, -2], [-5, 5]];}
const height = argsFromMain[0];
cnvs.height = height;
cnvs.width=height;
const N=51;
const aj=argsFromMain[1], xlim=argsFromMain[2];
const dx=(xlim[1]-xlim[0])/(N-1);
yMin=Math.floor(aj[2]-aj[1]*aj[1]/4-1);
const ylim=[yMin, yMin+10];
const xPole=-aj[1]/2;
var x=[], y=[], v;
for (j=0; j<N; j++) {
  v=xlim[0]+j*dx;
  w=aj[0]*v**2 + aj[1]*v + aj[2];
  if (yMin<w && w<yMin+10) {
    x.push(v);
    y.push(w);
  }
}
function x2cnvs (x) {
  return bOrigX+pxl2x*(x-xlim[0]);
}
function y2cnvs (y) {
  return bOrigY+bL-pxl2x*(y-ylim[0]);
}
const bOrigX=0.5, bOrigY=0.5, bL=height, pxl2x=bL/(xlim[1]-xlim[0]);
ctx.beginPath();
ctx.fillStyle="#eee";
ctx.fillRect(bOrigX, bOrigY, bL, bL);
ctx.strokeStyle="#ccc";
for (let j=xlim[0]; j<=xlim[1]; j++) {
  px=x2cnvs(j);
  ctx.moveTo(px, bOrigY);
  ctx.lineTo(px, bOrigY+bL);
  ctx.stroke();
}
for (let j=Math.ceil(ylim[0]); j<=Math.floor(ylim[1]); j++) {
  py=y2cnvs(j);
  ctx.moveTo(bOrigX, py);
  ctx.lineTo(bOrigX+bL, py);
  ctx.stroke();
}
ctx.beginPath();
ctx.strokeStyle="blue";
py=y2cnvs(0);
ctx.moveTo(bOrigX, py);
ctx.lineTo(bOrigX+bL, py);
ctx.stroke();
ctx.beginPath();
ctx.strokeStyle="blue";
px=x2cnvs(0);
ctx.moveTo(px, bOrigY);
ctx.lineTo(px, bOrigY+bL);
ctx.stroke();
ctx.beginPath();
ctx.font="normal 14px Arial";
ctx.fillStyle="blue";
ctx.fillText("O", x2cnvs(0)-15,y2cnvs(0)+15);
ctx.fillText("x", bOrigX+bL-10,y2cnvs(0)-3);
ctx.fillText("y", x2cnvs(0)-12, bOrigY+13);
for (j=ylim[0]+1; j<ylim[1]; j++) {
  if (j%2 == 0) {
    if (j<0) {
      ctx.fillText(j.toString(), x2cnvs(0)-15,y2cnvs(j)+5);
    }
    else if (j>0) {
      ctx.fillText(j.toString(), x2cnvs(0)-10,y2cnvs(j)+5);
    }
  }
}
ctx.fillText("-4", x2cnvs(-4)-8,y2cnvs(0)+12);
ctx.fillText("-2", x2cnvs(-2)-8,y2cnvs(0)+12);
ctx.fillText("2", x2cnvs(2)-4,y2cnvs(0)+12);
ctx.fillText("4", x2cnvs(4)-4,y2cnvs(0)+12);
ctx.beginPath();
ctx.strokeStyle="black";
ctx.moveTo(x2cnvs(x[0]), y2cnvs(y[0]));
for (j=1; j<N; j++) {
  ctx.lineTo(x2cnvs(x[j]), y2cnvs(y[j]));
}
ctx.stroke();
ctx.beginPath();
for (j=0; j<N; j++) {
  ctx.beginPath();
  ctx.arc(x2cnvs(x[j]),y2cnvs(y[j]),2,0, 2*Math.PI);
  ctx.stroke();
}'''
