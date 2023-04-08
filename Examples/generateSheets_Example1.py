import htmlfilesforquiz as hf4q

clock='''var argsFromMain=null;function init(prms) {argsFromMain=prms;}//init();
if (argsFromMain == null) {argsFromMain=[300, 10, 10];}const width= argsFromMain[0];cnvs.width=width;cnvs.height=width;ctx.clearRect(0,0, cnvs.width, cnvs.height);var radius = width/2;ctx.translate(radius, radius);radius = radius * 0.90;
function drawFace(ctx, radius) {  ctx.beginPath();  ctx.arc(0, 0, radius, 0, 2*Math.PI);  ctx.fillStyle = "white";  ctx.fill();  ctx.strokeStyle = "black";  ctx.stroke();}function drawNumbers(ctx, radius) {  var ang;  var num;  ctx.font = radius*0.15 + "px arial";  ctx.textBaseline="middle";  ctx.fillStyle = "black";  ctx.textAlign="center";  for(num = 1; num < 13; num++){    ang = num * Math.PI / 6;    ctx.rotate(ang);    ctx.translate(0, -radius*0.85);    ctx.rotate(-ang);    ctx.fillText(num.toString(), 0, 0);    ctx.rotate(ang);    ctx.translate(0, radius*0.85);    ctx.rotate(-ang);  }}
function drawHand(ctx, pos, length, width) {    ctx.beginPath();    ctx.lineWidth = width;    ctx.lineCap = "round";    ctx.moveTo(0, 0);    ctx.rotate(pos);    ctx.lineTo(0,-length);    ctx.stroke();    ctx.rotate(-pos);}
drawFace(ctx, radius);drawNumbers(ctx, radius);var hour=argsFromMain[1];var minute=argsFromMain[2];hour=hour%12;hour=hour*Math.PI/6 + minute*Math.PI/(6*60);drawHand(ctx, hour, radius*0.5, radius*0.04);minute=(minute*Math.PI/30);drawHand(ctx, minute, radius*0.8, radius*0.02);'''

graph='''var argsFromMain=null;function init(prms) {argsFromMain=prms;}//init();
if (argsFromMain == null) {argsFromMain=[[1, 1, -2], [-5, 5]];}const height = 200;cnvs.height = height;cnvs.width=height;const N=51;const aj=argsFromMain[0], xlim=argsFromMain[1];const dx=(xlim[1]-xlim[0])/(N-1);yMin=Math.floor(aj[2]-aj[1]*aj[1]/4-1);const ylim=[yMin, yMin+10];const xPole=-aj[1]/2;var x=[], y=[], v;for (j=0; j<N; j++) {  v=xlim[0]+j*dx; w=aj[0]*v**2 + aj[1]*v + aj[2];  if (yMin<w && w<yMin+10) {x.push(v); y.push(w);}}function x2cnvs(x) {return bOrigX+pxl2x*(x-xlim[0]);}function y2cnvs(y) {return bOrigY+bL-pxl2x*(y-ylim[0]);}const bOrigX=0.5, bOrigY=0.5, bL=height, pxl2x=bL/(xlim[1]-xlim[0]);ctx.beginPath();ctx.fillStyle="#eee";ctx.fillRect(bOrigX, bOrigY, bL, bL);ctx.strokeStyle="#ccc";for (let j=xlim[0]; j<=xlim[1]; j++) { px=x2cnvs(j); ctx.moveTo(px, bOrigY); ctx.lineTo(px, bOrigY+bL);ctx.stroke();}for (let j=Math.ceil(ylim[0]); j<=Math.floor(ylim[1]); j++) { py=y2cnvs(j); ctx.moveTo(bOrigX, py); ctx.lineTo(bOrigX+bL, py);ctx.stroke();}ctx.beginPath();ctx.strokeStyle="blue"; py=y2cnvs(0); ctx.moveTo(bOrigX, py); ctx.lineTo(bOrigX+bL, py); ctx.stroke();ctx.beginPath();ctx.strokeStyle="blue"; px=x2cnvs(0); ctx.moveTo(px, bOrigY); ctx.lineTo(px, bOrigY+bL); ctx.stroke();ctx.beginPath();ctx.font="normal 14px Arial";ctx.fillStyle="blue";ctx.fillText("O", x2cnvs(0)-15,y2cnvs(0)+15);ctx.fillText("x", bOrigX+bL-10,y2cnvs(0)-3);ctx.fillText("y", x2cnvs(0)-12, bOrigY+13);for (j=ylim[0]+1; j<ylim[1]; j++) {  if (j%2 == 0) {     if (j<0) {ctx.fillText(j.toString(), x2cnvs(0)-15,y2cnvs(j)+5);}     else if (j>0) {ctx.fillText(j.toString(), x2cnvs(0)-10,y2cnvs(j)+5);}  }}ctx.fillText("-4", x2cnvs(-4)-8,y2cnvs(0)+12);ctx.fillText("-2", x2cnvs(-2)-8,y2cnvs(0)+12);ctx.fillText("2", x2cnvs(2)-4,y2cnvs(0)+12);ctx.fillText("4", x2cnvs(4)-4,y2cnvs(0)+12);ctx.beginPath();ctx.strokeStyle="black";ctx.moveTo(x2cnvs(x[0]), y2cnvs(y[0]));for (j=1; j<N; j++) {ctx.lineTo(x2cnvs(x[j]), y2cnvs(y[j]));}ctx.stroke();ctx.beginPath();for (j=0; j<N; j++) {ctx.beginPath();  ctx.arc(x2cnvs(x[j]),y2cnvs(y[j]),2,0, 2*Math.PI);  ctx.stroke();}'''

addFractions='''var argsFromMain=null;function init(prms) {argsFromMain=prms;}//init();
if (argsFromMain == null) {argsFromMain=[200, [1, 2, 2, 3]];}
var height = argsFromMain[0];cnvs.height = height;cnvs.width=2*height; var radius = cnvs.height/4;var cY = cnvs.height/2;var cX = cnvs.width/2;var radius = cY-20;
ctx.beginPath();ctx.font="normal 60px Arial";ctx.fillStyle="black";ctx.fillText("+", cX-17, cY+20);
var angle = 2*Math.PI/argsFromMain[1][1];for (let j=0; j<argsFromMain[1][1]; j++) {  ctx.beginPath();  ctx.moveTo(cX-radius-20, cY);  ctx.strokeStyle="black";  if (j<argsFromMain[1][0]) {ctx.fillStyle="#ed7";}  else {ctx.fillStyle="white";}  ctx.arc(cX-radius-20, cY, radius, j*angle, (j+1)*angle);  ctx.lineTo(cX-radius-20, cY);  ctx.fill();  ctx.stroke();}
angle = 2*Math.PI/argsFromMain[1][3];for (let j=0; j<argsFromMain[1][3]; j++) {  ctx.beginPath();  ctx.moveTo(cX+radius+20, cY);  ctx.strokeStyle="black";  if (j<argsFromMain[1][2]) {ctx.fillStyle="#7ed";}  else {ctx.fillStyle="white";}  ctx.arc(cX+radius+20, cY, radius, j*angle, (j+1)*angle);  ctx.lineTo(cX+radius+20, cY);  ctx.fill();  ctx.stroke();}
'''

figures={'clock':clock, 'graph': graph, 'addFractions':addFractions}


QGs=[]
Q=['Submit the acceleration, in unit of m/s², of an object of {%vM%} kg when the force of {%vF%} N is acted upon.',
   'Sumbit the force in unit of N to give an object of {%vM%} kg acceleration of {%round(vF/vM,3)%} m/s².']
A='''data=[]
vM=random.randint(1,10)
vF=random.randint(10,30)
answer=[vF/vM, vM*round(vF/vM,3)]'''

QGs.append([Q, A, ('chap3', 'short0'), 'short'])

Q=['Submit the sum of the two integers {%vA%} and {%vB%}.',
   'Submit the product of the two integers {%vA%} and {%vB%}.',
   'Subtract {%vA%} from {%vB%} and submit your answer.']

A='''data=[]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer=[vA+vB, vA*vB, vB-vA]'''

QGs.append([Q, A, ('chap3', 'short1'), 'short'])

Q=['Submit the sum of the two integers {%vA%} and {%vB%}.',
   'Submit the product of the two integers {%vA%} and {%vB%}.',
   'Subtract {%vA%} from {%vB%} and submit your answer.']

A='''data=[]
from userfunctions11 import func1
vA, vB = func1()
answer=[vA+vB, vA*vB, vB-vA]'''

QGs.append([Q, A, ('chap3', 'udf_short'), 'short'])

Q=['Submit the sum of the two integers {%vA%} and {%vB%}.']

A='''data=[]
choices=[(random.randint(10,30), random.randint(10,30)) for _ in range(10)]
choice=random.choice(range(len(choices)))
ans=choices[choice]
vA, vB=ans
answer=[{'choices': [a+b for a, b in choices], 'ans': sum(ans)}]'''

QGs.append([Q, A, ('chap3', 'choices'), 'short'])

Q=['Submit the sum of the two integers {%vA%} and {%vB%}.', 'Submit the sum of the two integers {%vA%} and {%vB%}.']

A='''data=[]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer=[{'choices':None, 'ans':vA+vB, 'fn': 'variation0_int'}, vA+vB]'''

QGs.append([Q, A, ('chap3', 'variation0_int'), 'short'])

Q=['Submit the sum of the two integers {%vA%} and {%vB%}.']

A='''data=[]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer=[{'choices':None, 'ans':vA+vB, 'fn': 'variation0_int_5Add'}]'''

QGs.append([Q, A, ('chap3', 'variation0_int_5Add'), 'short'])

Q=['What time is the clock shown below?figure(clock)']

A='''data=[]
answers = [f'{random.choice(range(1,12))}:{random.choice(range(5,60,5))}' for _ in range(10)]
answers.append('10:10')
ans = '10:10'
answer=[{'choices':answers, 'ans':ans}]'''

QGs.append([Q, A, ('chap3', 'clock0'), 'short'])


Q=['What time is the clock shown below?figure(clock)init({%prms%});']

A='''data=[]
answers = [f'{random.choice(range(1,12))}:{random.choice(range(5,60,5))}' for _ in range(random.choice(range(5,10)))]
ans=random.choice(answers)
answer=[{'choices':answers, 'ans':ans}]
vH, vM=[int(s) for s in ans.split(':')]
prms=[300, vH, vM]'''

QGs.append([Q, A, ('chap3', 'clock1'), 'short'])


Q=['What clock shows the time of  {%ans%}?figure(clock)', 'What time is the clock shown below?figure(clock)init({%prms2%});','Subtract {%vA%} from {%vB%} and submit your answer.']

A='''data=[]
times = [f'{random.choice(range(1,12))}:{random.choice(range(5,60,5))}' for _ in range(10)]
indx=random.choice(range(len(times)))
ans=times[indx]
prms=[f'[200, {int(choice.split(":")[0])}, {int(choice.split(":")[1])}]' for choice in times]
answer=[{'choices':prms, 'ans':prms[indx], 'cols':prms}]

answers = [f'{random.choice(range(1,12))}:{random.choice(range(5,60,5))}' for _ in range(random.choice(range(5,10)))]
ans2=random.choice(answers)
answer.append({'choices':answers, 'ans':ans2})
vH, vM=[int(s) for s in ans2.split(':')]
prms2=[300, vH, vM]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer.append(vB-vA)'''

QGs.append([Q, A, ('chap3', 'clock2'), 'short'])


Q=['What is the correct function shown on right?<br>figure(graph)<br>init({%prms%});']

A='''data=[]
choices=[]
for _ in range(6):
  b=random.choice([-4, -3,-2,-1, 0, 1, 2, 3, 4])
  c=random.choice([-4, -3,-2,-1, 0, 1, 2, 3, 4])
  choices.append([[1, b, c], [-5,5]])

indx=random.choice(range(len(choices)))
ansValue=choices[indx]
eqs=[]
term1=lambda v: '+ x' if v==1 else '- x' if v==-1 else f'+ {v}x' if v>0 else f'- {-v}x' if v<0 else ''
term2=lambda v: f'+ {v}' if v>0 else f'- {-v}' if v<0 else ''
eqs = []
for aj, _ in choices: eqs.append(f'EQ% x^2 {term1(aj[1])} {term2(aj[2])} %EQ')

answer=[{'choices':eqs, 'ans':eqs[indx]}]
prms=choices[indx]'''

QGs.append([Q, A, ('chap3', 'eq_graph1'), 'short'])


Q=['What is the correct function of {%eq%}?figure(graph)']

A='''data=[]
choices=[]
for _ in range(10):
  b=random.choice([-4, -3,-2,-1, 0, 1, 2, 3, 4])
  c=random.choice([-4, -3,-2,-1, 0, 1, 2, 3, 4])
  choices.append([[1, b, c], [-5,5]])

indx=random.choice(range(len(choices)))

term1=lambda v: '+ x' if v==1 else '- x' if v==-1 else f'+ {v}x' if v>0 else f'- {-v}x' if v<0 else ''
term2=lambda v: f'+ {v}' if v>0 else f'- {-v}' if v<0 else ''
eq=f'EQ% x^2 {term1(choices[indx][0][1])} {term2(choices[indx][0][2])} %EQ'

#cnvss = []
#xtra = []
#for j, choice in enumerate(choices):
#  cnvss.append(f'<div id="cnvs{j}"></div>')
#  xtra.append(f'graphF("cnvs{j}", {choice});')
#answer=[{'choices':cnvss, 'ans':cnvss[indx], 'cols':xtra}]
answer=[{'choices':choices, 'ans':choices[indx], 'cols':choices}]'''

QGs.append([Q, A, ('chap3', 'eq_graph2'), 'short'])


Q=['''The code below is for calculating the sum of odd integers between 5 and {%vN-1%}. Find the value associated with the variable f, after execution.
<div style="display: flex; justify-content: center; padding: 5px 10px; line-height: 1.1em">
<pre class="preBody">
<font color="#ff7700">for</font> f <font color="#ff7700">in</font> <font color="#900090">range</font>(5, {%vN%}):<br>
  <font color="#ff7700">if</font> f%2:<br>
    f += f
</pre></div>''', '''The code below is for calculating the sum of even integers between 5 and {%vN-1%}. Find the value associated with the variable f, after execution.
<div style="display: flex; justify-content: center; padding: 5px 10px; line-height: 1.1em">
<pre class="preBody">
<font color="#ff7700">for</font> f <font color="#ff7700">in</font> <font color="#900090">range</font>(5, {%vN%}):<br>
  <font color="#ff7700">if not</font> f%2:<br>
    f += f
</pre></div>''']

A='''data = []
vN=random.choice(range(1000,5000))
for f in range(5, vN):
  if f%2:
    f += f
answer=[f]
for f1 in range(5, vN):
  if not f1%2:
    f1 += f1
answer.append(f1)'''

QGs.append([Q, A, ('chap13', 'python'), 'python'])

Q=['Select the {%vA%} one. ',
   'Select the {%vA%} one. ']

A='''data=[]
vA=random.choice(['correct', 'incorrect'])
import userfunctions2
choices, indx, ansValue = userfunctions2.func2(vA)
answer=[{'choices':choices, 'ans':choices[indx]}, {'choices':choices, 'ans':choices[indx]}]'''

QGs.append([Q, A, ('chap10', 'udf_RightWrong'), 'short'])


Q=['What is the sum of {%ansValue%}?']
A='''data=[]
import userfunctions
choices, indx, ansValue = userfunctions.func1()
answer=[{'choices':choices, 'ans':choices[indx]}]'''

QGs.append([Q, A, ('chap10', 'udf_fraction0'), 'short'])

Q=['What is the sum of the two fill areas of the color drawn below?<br>figure(addFractions)<br>init({%prms%});']
A='''data=[]
import userfunctions
choices, indx, ansValue = userfunctions.func1B()
answer=[{'choices':choices, 'ans':choices[indx]}]
prms=ansValue'''

QGs.append([Q, A, ('chap10', 'udf_fraction_shapes1'), 'choice'])


Q=['Which choice equals to {%ansValue%}?figure(addFractions)']

A='''data=[]
import userfunctions
choices, indx, ansValue = userfunctions.func1C()
prms=ansValue
answer=[{'choices':choices, 'ans':choices[indx], 'cols':choices}]'''

QGs.append([Q, A, ('chap10', 'udf_fraction_shapes2'), 'short'])






name='examples'
heading='Testing'
STDs={'12345678': 'oooo'}

iMultipleChoices=False

a=hf4q.work(name, heading, STDs, QGs, True, iMultipleChoices, False)
hf4q.mkHTMLs(a, figures)
