import htmlfilesforquiz as hf4q

QGs = []

division='''var argsFromMain=null;function init(prms) {argsFromMain=prms;}//init();
if (argsFromMain == null) {argsFromMain=[[50,1000], ['x', '8', '÷', '3', '=', '6']];}cnvs.height = argsFromMain[0][0];cnvs.width = argsFromMain[0][1];
function drawRect(xo, yo) { ctx.beginPath(); ctx.strokeStyle="#888"; ctx.rect(xo, yo, rectA, rectA); ctx.stroke(); ctx.closePath();}
const word=argsFromMain[1], rectA=40, xo=50.5, yo=0.5, digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x'];
for (let i=0; i<word.length; i++) {
  if (digits.includes(word[i])) { ctx.beginPath(); ctx.strokeStyle="#888"; ctx.rect(xo+i*(rectA+5), yo, rectA, rectA); ctx.stroke();}
  if (word[i] != 'x') { ctx.beginPath(); ctx.fillStyle="red"; ctx.textAlign="center"; ctx.font="normal 40px Palatino Linotype"; ctx.fillText(word[i], xo+i*(rectA+5)+rectA/2, yo+rectA-6); }
}'''

figures={'division': division}

QGs=[]

Q=['Find the integer in the blank that completes the division expression below.figure(division)init({%prms%});',
   'Find the integer in the blank that completes the division expression below.figure(division)init({%prms%});']

A='''data=[]
vA=random.choice(range(2,20))
vB=random.choice(range(1,10))
op='÷'
vA *= vB
vAns=int(vA/vB)
vStr=list(f'{vA}{op}{vB}={vAns}')
x=random.choice([item for item in enumerate(vStr) if item[1].isnumeric()])
vStr[x[0]]='x'
exps=[str(f) for f in range(10)]
answer=[x[1], {'choices':exps, 'ans':x[1]}]
prms=[[50, 800], vStr]'''

QGs.append([Q, A, ('Examples', 'Ex003'), 'choice'])

flagPreview = False
flagChoice = False
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = hf4q.work('Ex003', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling)
hf4q.mkHTMLs(a, figures)
a.saveWork()
