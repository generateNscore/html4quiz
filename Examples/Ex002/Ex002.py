import htmlfilesforquiz as hf4q

QGs = []

addFractions='''var argsFromMain=null;function init(prms) {argsFromMain=prms;}//init();
if (argsFromMain == null) {argsFromMain=[200, [1, 2, 2, 3]];}
var height = argsFromMain[0];cnvs.height = height;cnvs.width=2*height; var radius = cnvs.height/4;var cY = cnvs.height/2;var cX = cnvs.width/2;var radius = cY-20;
ctx.beginPath();ctx.font="normal 60px Arial";ctx.fillStyle="black";ctx.fillText("+", cX-17, cY+20);
var angle = 2*Math.PI/argsFromMain[1][1];for (let j=0; j<argsFromMain[1][1]; j++) {  ctx.beginPath();  ctx.moveTo(cX-radius-20, cY);  ctx.strokeStyle="black";  if (j<argsFromMain[1][0]) {ctx.fillStyle="#ed7";}  else {ctx.fillStyle="white";}  ctx.arc(cX-radius-20, cY, radius, j*angle, (j+1)*angle);  ctx.lineTo(cX-radius-20, cY);  ctx.fill();  ctx.stroke();}
angle = 2*Math.PI/argsFromMain[1][3];for (let j=0; j<argsFromMain[1][3]; j++) {  ctx.beginPath();  ctx.moveTo(cX+radius+20, cY);  ctx.strokeStyle="black";  if (j<argsFromMain[1][2]) {ctx.fillStyle="#7ed";}  else {ctx.fillStyle="white";}  ctx.arc(cX+radius+20, cY, radius, j*angle, (j+1)*angle);  ctx.lineTo(cX+radius+20, cY);  ctx.fill();  ctx.stroke();}'''

Q=['What is the sum of the two fill areas of the color drawn below?<br>figure(addFractions)<br>init({%prms%});']
A='''data=[]
import userfunctions
choices, indx, ansValue = userfunctions.func2()
answer=[{'choices':choices, 'ans':choices[indx]}]
prms=ansValue'''

QGs.append([Q, A, ('Examples', 'Ex002'), 'choice'])

figures={'addFractions': addFractions}

flagPreview = False
flagChoice = False
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = hf4q.work('Ex002', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling)
hf4q.mkHTMLs(a, figures)
a.saveWork()
