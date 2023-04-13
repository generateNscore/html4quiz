import htmlfilesforquiz as hf4q

QGs = []

figures={'division': hf4q._common.getFigure('division')}

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
