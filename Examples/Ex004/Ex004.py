import htmlfilesforquiz as hf4q

QGs = []

playWithNumbers='''var argsFromMain=null;
function init(prms) {argsFromMain=prms;}
//init();
if (argsFromMain == null) {argsFromMain=[[500, 1400], [10, 7], ['x', '8', '÷', '3', '=', '6']];}

[cnvs.height, cnvs.width]=argsFromMain[0];
var cw = cnvs.width, ch = cnvs.height, cells=[];
const cellW=50, [cols, rows]=argsFromMain[1];
cnvs.height=Math.max(10, rows)*50+40; ch=cnvs.height;
const yTop=20.5, xLeft=20.5;
const eqn = argsFromMain[2];
var pxX, pxY, bbox, dragging=false, clickedChar=null;

var clickedValue=null;
const SubmitBtn={x:(cols+2)*cellW, y:40, w:140, h:50, color:"#d7d"};

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

var arr = [], r4arr=[];
var j=0, r;
while(arr.length < eqn.length){
  r = getRandomInt(0, cols*rows);
  if (r4arr.indexOf(r) == -1) {
    arr.push({c: eqn[j], n: r});
    r4arr.push(r);
    j += 1;
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

cnvs.addEventListener('mouseup', onmouseup);
cnvs.addEventListener('mousedown', onmousedown);
cnvs.addEventListener('mousemove', onmousemove);

function onmousedown(e) {
  e.preventDefault();
  bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (SubmitBtn.x-SubmitBtn.w/2<=pxX && pxX <= SubmitBtn.x+SubmitBtn.w/2 && SubmitBtn.y-SubmitBtn.h/2<=pxY && pxY <= SubmitBtn.y+SubmitBtn.h/2) {Submit();}

  if (pxX>20 && pxX<cols*cellW && pxY>20 && pxY<rows*cellW) {
    clickedValue = getValue()-1;
    for (let j=0; j<arr.length; j++) {
      if (arr[j].n == clickedValue) {
        dragging=true;
        clickedChar=j;
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
    dragging=false;
  }
}

function onmousemove(e) {
  e.preventDefault();
  var bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (dragging == true && pxX>20 && pxX<cols*cellW && pxY>20 && pxY<rows*cellW) {
    clickedValue = getValue()-1;
    arr[clickedChar].n=clickedValue;
    drawAll();
  }
}

function getValue() {
  let col=Math.floor((pxX-20)/cellW);
  let row=Math.floor((pxY-20)/cellW);
  return col+row*cols+1;
}

function drawAll() {
  ctx.putImageData(canvasImage,0,0);

  ctx.beginPath();
  ctx.fillStyle="black"; ctx.font = "36px arial"; ctx.textAlign="center";
  var Rem, Quo;
  for (let j=0; j<arr.length; j++) {
    Rem = arr[j].n%cols; Quo = Math.floor((arr[j].n-Rem)/cols);
    ctx.fillText(arr[j].c, Rem*cellW+45, Quo*cellW+60);
  }
}

drawAll();
'''

figures={'playWithNumbers': playWithNumbers}

QGs=[]

Q=['Move the numbers and arithmetic signs shown below to complete the resulting equation with no spaces between them. Leading and trailing spaces are allowed. When finished, click the "Submit" button. figure(playWithNumbers)init({%prms1%});']

A='''data=[]
vA=random.choice(range(2,20))
vB=random.choice(range(1,10))
op='÷'
vA *= vB
vAns=int(vA/vB)
answer=[f'{vA}{op}{vB}={vAns}']
vStr=list(answer[0])
columnsN=len(vStr)+4
prms1=[[500, 1400], [columnsN, 1], vStr]'''

QGs.append([Q, A, ('Examples', 'Ex004'), 'short'])

flagPreview = False
flagChoice = False
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = hf4q.work('Ex004', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling)
hf4q.mkHTMLs(a, figures)
a.saveWork()
