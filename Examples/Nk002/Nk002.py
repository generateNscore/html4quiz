import htmlfilesforquiz as hf4q

QGs = []

add2Vectors='''var argsFromMain=null;
function init(prms) {argsFromMain=prms;}
//init();
//if (argsFromMain == null) {argsFromMain=[[300, 1400], [[2, 0], [0, 3]]];}
//if (argsFromMain == null) {argsFromMain=[[20, 20], [[2, 0], [0, 3]], 'off'];}
if (argsFromMain == null) {argsFromMain=[[20, 20], [[2, 0, -2,-1], [0, 3, 1, 3]], 'off'];}
//[cnvs.height, cnvs.width]=argsFromMain[0];
//cnvs.width=window.innerWidth-50; cnvs.height=window.innerHeight-380;
const rA = argsFromMain[0][0], jB=argsFromMain[0][1];
var pxX, pxY, bbox, dragging=false, vec2drag=null, point=null;

const hafA=rA/2, yo=20.5, yB=yo+jB*rA, jC=jB/2, cY=yo+rA*jC, hafPI=Math.PI/2;
cnvs.height = yB+10, cnvs.width = yB+220;
const ch=cnvs.height, cw=cnvs.width;
const btn=argsFromMain[2];
var SubmitBtn=null;

if (btn == 'on') {SubmitBtn={x: yB+100, y:40, w:140, h:50, color:"#d7d"};}

function randInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

const colors={0:"red", 1:"green", 2:"blue", 3:"#ff0", 4: "#f0f", 5:"#0ff"};
const vectors = new Array();
for (let j=0; j<argsFromMain[1].length; j++) {
  const vec = argsFromMain[1][j];
  if (vec.length == 2) {vectors.push({x: vec[0]*rA, y: vec[1]*rA, xo: randInt(-3,4)*rA, yo: randInt(-3,4)*rA, c: colors[j], points: null});}
  else {vectors.push({x: vec[0]*rA, y: vec[1]*rA, xo: vec[2]*rA, yo: vec[3]*rA, c: colors[j], points: null});}
}

for (let j=0; j<vectors.length; j++) {
  var points=[], ratio, xVo=vectors[j].xo+cY, yVo=cY-vectors[j].yo;

  if (Math.abs(vectors[j].x) > Math.abs(vectors[j].y)) {
    ratio = vectors[j].y/vectors[j].x;
    if (vectors[j].x > 0) {
      for (let x=0; x<=vectors[j].x; x++) {points.push([xVo+x, yVo+x*ratio]);}
    }
    else {
      for (let x=0; x>=vectors[j].x; x--) {points.push([xVo+x, yVo+x*ratio]);}
    }
    points.push('x');
  }
  else {
    ratio = vectors[j].x/vectors[j].y;
    if (vectors[j].y > 0) {
      for (let y=0; y<=vectors[j].y; y++) {points.push([xVo+y*ratio, yVo-y]);}
    }
    else {
      for (let y=0; y>=vectors[j].y; y--) {points.push([xVo+y*ratio, yVo-y]);}
    }
    points.push('y');
  }
  vectors[j].points=points;
}

//console.log(vectors);
var y, angle, length, canvasImage;

function drawBackground() {
  ctx.fillStyle="black"; ctx.font = "12px Arial";  ctx.textAlign="center";
  for (j=0; j<=jB; j++) {
    y = yo+j*rA;
    if ((j-jC)%5 == 0) {
      ctx.beginPath();
      ctx.strokeStyle="#aaa";
      ctx.fillText(Math.floor((j-jC)/5)*5, y, cY+13);
      ctx.fillText(Math.floor((jC-j)/5)*5, cY-10, y+5);
    }
    else {ctx.strokeStyle="#ddd";}
    ctx.beginPath(); ctx.moveTo(y, yo); ctx.lineTo(y, yB); ctx.stroke(); // vertical;
    ctx.beginPath(); ctx.moveTo(yo, y); ctx.lineTo(yB, y); ctx.stroke(); //horizontal;
  }

  if (SubmitBtn != null) {
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

function Submit() {
  var ans="to be determined....";
  answers[Qnumber]=ans;
  addAnswers2Textarea();
}



function isPointOnLine(points, x,y) {
  const xORy = points.slice(-1);
  if (xORy == 'x') {
    for (let j=0; j<points.length-1; j++) {
      if (points[j][0] == x) {
         if (points[j][1]-1 <= y && y <= points[j][1]+1) {
            return true;
         }
      }
    }
  }
  else {
    for (let j=0; j<points.length-1; j++) {
      if (points[j][1] == y) {
         if (points[j][0]-1 <= x && x <= points[j][0]+1) {
            return true;
         }
      }
    }
  }
  return false;
}

function onmouseup(e) {
  if (dragging) {
    const dx=vectors[vec2drag].xo+cY-vectors[vec2drag].points[0][0], dy=cY-vectors[vec2drag].yo-vectors[vec2drag].points[0][1];

    var newPoints = new Array();
    for (let j=0; j<vectors[vec2drag].points.length-1; j++) {
      newPoints.push( [vectors[vec2drag].points[j][0]+dx, vectors[vec2drag].points[j][1]+dy]);
    }
    newPoints.push(vectors[vec2drag].points.slice(-1));

    vectors[vec2drag].points=newPoints;
    vectors[vec2drag].c = vec2drag ? "blue" : "red";
    dragging=false;
    vec2drag=null;
    point = null;
    drawAll();
  }
}

function onmousedown(e) {
  e.preventDefault();
  bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (SubmitBtn != null && SubmitBtn.x-SubmitBtn.w/2<=pxX && pxX <= SubmitBtn.x+SubmitBtn.w/2 && SubmitBtn.y-SubmitBtn.h/2<=pxY && pxY <= SubmitBtn.y+SubmitBtn.h/2) {Submit();}


  for (let j=0; j<vectors.length; j++) {
    const isItON = isPointOnLine(vectors[j].points, Math.round(pxX)+0.5, Math.round(pxY)+0.5);
    if (isItON) {
       dragging=true;
       vec2drag=j;
       vectors[j].c="black";
       point = [Math.round(pxX)+0.5, Math.round(pxY)+0.5];
       drawAll();
       break;
    }
  }
}


function onmousemove(e) {
  e.preventDefault();
  bbox = cnvs.getBoundingClientRect();
  pxX=e.clientX-bbox.left*(cw/bbox.width);
  pxY=e.clientY-bbox.top*(ch/bbox.height);

  if (dragging) {
    vectors[vec2drag].xo += (Math.round(pxX)+0.5-point[0]);
    vectors[vec2drag].yo += -(Math.round(pxY)+0.5-point[1]);
    point = [Math.round(pxX)+0.5, Math.round(pxY)+0.5];
    drawAll();
  }
  else {
    for (let j=0; j<vectors.length; j++) {
      const isItON = isPointOnLine(vectors[j].points, Math.round(pxX)+0.5, Math.round(pxY)+0.5);
      if (isItON) {
        vectors[j].c="black";
        drawAll();
        break;
      }
      else {
        vectors[j].c=colors[j];
        drawAll();
      }
    }
  }
}



function drawVector(angle, length) {
  ctx.beginPath(); ctx.moveTo(0, 0); ctx.rotate(angle); ctx.lineTo(0, -length); ctx.lineTo(-3, 6-length); ctx.lineTo(0, -length); ctx.lineTo(3, 6-length); ctx.stroke(); ctx.rotate(-angle);
}

function drawAll() {
  ctx.putImageData(canvasImage,0,0);
/*
  if (vectors[0].xo-0.1 <= vectors[1].xo && vectors[1].xo <= vectors[0].xo+0.1 && vectors[0].yo-0.1 <= vectors[1].yo && vectors[1].yo <= vectors[0].yo+0.1) {
    vectors[vec2drag].c = vec2drag ? "blue" : "red";
    vec2drag=null;
    point = null;
    dragging=false;
    vectors[0].xo=0, vectors[0].yo=0, vectors[1].xo=0, vectors[1].yo=0;
  }
*/

  ctx.lineWidth=2;
  for (let j=0; j<vectors.length; j++) {
    ctx.beginPath();
    ctx.translate(vectors[j].xo+cY, cY-vectors[j].yo);
    ctx.strokeStyle=vectors[j].c;
    angle=hafPI-Math.atan2(vectors[j].y, vectors[j].x);
    length=Math.sqrt(vectors[j].x**2 + vectors[j].y**2);
    ctx.moveTo(0, 0); ctx.rotate(angle); ctx.lineTo(0, -length); ctx.lineTo(-3, 6-length); ctx.lineTo(0, -length); ctx.lineTo(3, 6-length); ctx.stroke(); ctx.rotate(-angle);
    ctx.translate(-vectors[j].xo-cY, vectors[j].yo-cY);
  }
  ctx.lineWidth=1;

}

cnvs.addEventListener('mouseup', onmouseup);
cnvs.addEventListener('mousedown', onmousedown);
cnvs.addEventListener('mousemove', onmousemove);

drawAll();'''

figures={'add2Vectors': add2Vectors}

QGs=[]

Q=['Find the x component of the sum of 2 vectors shown in red and in green below. figure(add2Vectors)init({%prms%});']

A='''data=[]
vectors = [[random.choice(range(-5,6)), random.choice(range(-5,6)),random.choice(range(-3,4)), random.choice(range(-3,4))] for _ in range(2)]
answer=[  sum(vec[0] for vec in vectors) ]
prms=[[20, 20], vectors, 'off']'''

QGs.append([Q, A, ('Examples', 'Nk002-1'), 'short'])

Q=['Find the y component of the sum of 2 vectors shown in red and in green below. figure(add2Vectors)init({%prms%});']

A='''data=[]
vectors = [[random.choice(range(-5,6)), random.choice(range(-5,6)),random.choice(range(-3,4)), random.choice(range(-3,4))] for _ in range(2)]
answer=[  sum(vec[1] for vec in vectors) ]
prms=[[20, 20], vectors, 'off']'''

QGs.append([Q, A, ('Examples', 'Nk002-2'), 'short'])



flagPreview = True
flagChoice = False
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = hf4q.work('Nk002', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling)
hf4q.mkHTMLs(a, figures)
a.saveWork()
