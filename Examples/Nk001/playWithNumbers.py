playWithNumbers='''var argsFromMain=null;
function init(prms) {argsFromMain=prms;}
//init();
if (argsFromMain == null) {argsFromMain=[[500, 1400], [10, 7], ['x', '8', '÷', '3', '=', '6'], 'shuffle'];}

[cnvs.height, cnvs.width]=argsFromMain[0];
var cw = cnvs.width, ch = cnvs.height, cells=[];
const cellW=50, [cols, rows]=argsFromMain[1];
cnvs.height=Math.max(10, rows)*50+40; ch=cnvs.height;
cnvs.height=(rows+1)*cellW; ch=cnvs.height;
cnvs.width=(cols+4)*cellW; cw=cnvs.width;
const yTop=20.5, xLeft=20.5;
const eqn = argsFromMain[2];
const shuffling = argsFromMain[3];
var pxX, pxY, bbox, dragging=false, clickedChar=null;

var clickedValue=null;
const SubmitBtn={x:(cols+2)*cellW, y:40, w:140, h:50, color:"#d7d"};

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

var arr = [], r4arr=[];
if (shuffling == 'shuffle') {
  var j=0, r;
  while(arr.length < eqn.length){
    r = getRandomInt(0, cols*rows);
    if (r4arr.indexOf(r) == -1) {
      arr.push({c: eqn[j], n: r, color:"#000"});
      r4arr.push(r);
      j += 1;
    }
  }
}
else {
  for (let j=0; j<eqn.length; j++) {
    arr.push({c: eqn[j], n:j});
  }
}

var canvasImage;

function drawBackground() {
  ctx.clearRect(0,0,cw,ch);

  ctx.strokeStyle = "#eee";
  var yBottom=yTop+rows*cellW, x, y;
  for (let j=0; j<cols+1; j++) {
    ctx.beginPath();
    x=xLeft+j*cellW;
    ctx.moveTo(x, yTop);
    ctx.lineTo(x, yBottom);
    ctx.stroke();
  }
  var xRight=xLeft+cols*cellW
  for (let j=0; j<rows+1; j++) {
    ctx.beginPath();
    y = yTop+j*cellW;
    ctx.moveTo(xLeft, y);
    ctx.lineTo(xRight, y);
    ctx.stroke();
  }

  if (shuffling == 'shuffle') {
    ctx.beginPath();
    ctx.shadowColor = "black";
    ctx.shadowOffsetX = 1;
    ctx.shadowOffsetY = 1;
    ctx.shadowBlur = 3;
    ctx.fillStyle=SubmitBtn.color;
    ctx.fillRect(SubmitBtn.x-SubmitBtn.w/2,SubmitBtn.y-SubmitBtn.h/2,SubmitBtn.w,SubmitBtn.h);
    ctx.shadowColor = "transparent";
    ctx.fillStyle="black"; ctx.font = "28px arial"; ctx.textAlign="center"; 
    ctx.fillText("Submit", SubmitBtn.x, SubmitBtn.y+10);
    ctx.closePath();
  }

  canvasImage=ctx.getImageData(0,0,cw,ch);
}

drawBackground();


function trim(x) {
  return x.replace(/^\s+|\s+$/gm, '');
}

function Submit() {
  var ans="";
  var flag;
  for (let n=0; n<cols*rows; n++) {
    flag=null;
    for (let j=0; j<arr.length; j++) {
      if (arr[j].n == n) {
        flag=j;
        break;
      }
    }
    if (flag == null) {ans += ' ';}
    else {ans += arr[flag].c;}
  }
  answers[Qnumber]=trim(ans);
  addAnswers2Textarea();
}

if (shuffling == 'shuffle') {
  cnvs.addEventListener('mouseup', onmouseup);
  cnvs.addEventListener('mousedown', onmousedown);
  cnvs.addEventListener('mousemove', onmousemove);
}

function onmousedown(e) {
  e.preventDefault();
  bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (SubmitBtn.x-SubmitBtn.w/2<=pxX && pxX <= SubmitBtn.x+SubmitBtn.w/2 && SubmitBtn.y-SubmitBtn.h/2<=pxY && pxY <= SubmitBtn.y+SubmitBtn.h/2) {Submit();}

  if (pxX>20 && pxX<cols*cellW && pxY>20 && pxY<rows*cellW) {
    clickedValue = getValue();
    for (let j=0; j<arr.length; j++) {
      if (arr[j].n == clickedValue) {
        dragging=true;
        clickedChar=j;
        arr[clickedChar].color="#f00";
        break;
      }
    }
  }
}

function onmouseup(e) {
  e.preventDefault();
  var bbox = cnvs.getBoundingClientRect();
  var pxX=e.clientX-bbox.left*(cw/bbox.width);
  var pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (dragging == true) {
    arr[clickedChar].color="#000";

    ctx.beginPath();
    ctx.font = "36px arial"; ctx.textAlign="center";
    var Rem, Quo;
    Rem = arr[clickedChar].n%cols; Quo = Math.floor((arr[clickedChar].n-Rem)/cols);
    ctx.fillStyle=arr[clickedChar].color;
    ctx.fillText(arr[clickedChar].c, Rem*cellW+45, Quo*cellW+60);

    clickedChar=null;
    dragging=false;
  }
}

function onmousemove(e) {
  e.preventDefault();
  var bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (dragging == true && pxX>20 && pxX<cols*cellW && pxY>20 && pxY<rows*cellW) {
    clickedValue = getValue();
    arr[clickedChar].n=clickedValue;
    drawAll();
  }
}

function getValue() {
  let col=Math.floor((pxX-20)/cellW);
  let row=Math.floor((pxY-20)/cellW);
  return col+row*cols;
}

function drawAll() {
  ctx.putImageData(canvasImage,0,0);

  ctx.beginPath();
  ctx.font = "36px arial"; ctx.textAlign="center";
  var Rem, Quo;
  for (let j=0; j<arr.length; j++) {
    Rem = arr[j].n%cols; Quo = Math.floor((arr[j].n-Rem)/cols);
    ctx.fillStyle=arr[j].color;
    ctx.fillText(arr[j].c, Rem*cellW+45, Quo*cellW+60);
  }
}

drawAll();
'''
