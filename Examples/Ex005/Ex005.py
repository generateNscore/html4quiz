import html4quiz_B as h4q


QGs = []

figures={'playWithNumbers': h4q._common.getResource('playWithNumbers')}


Q=['Find the integer in the box marked with an "X" that completes the division expression below.figure(playWithNumbers)init({%prms2%});']


A='''data=[]
vA=random.choice(range(2,20))
vB=random.choice(range(1,10))
op='÷'
vA *= vB
vAns=int(vA/vB)
vStr=list(f'{vA}{op}{vB}={vAns}')
x=random.choice([item for item in enumerate(vStr) if item[1].isnumeric()])
vStr[x[0]]='x'
answer=[{'choices': None, 'ans':int(x[1]), 'fn':'variation0_int'}]
prms2=[[50, 800], [len(vStr),1], vStr, 'null']'''

QGs.append([Q, A, ('Ex005', 'qg1'), 'short'])

Q=['Move the numbers and arithmetic signs shown below to complete the resulting equation with no spaces between them. Leading and trailing spaces are allowed. When finished, click the "Submit" button. figure(playWithNumbers)init({%prms1%});']


A='''data=[]
vA=random.choice(range(2,20))
vB=random.choice(range(1,10))
op='÷'
vA *= vB
vAns=int(vA/vB)
#answer=[f'{vA}{op}{vB}={vAns}']
#vStr=list(answer[0])
answer=["code:eval(StudentValue.replace('÷','/').replace('=', '=='))"]
vStr=list(f'{vA}{op}{vB}={vAns}')
columnsN=len(vStr)+4
random.shuffle(vStr)

prms1=[[50, 1400], [columnsN, 1], vStr, 'shuffle']'''

QGs.append([Q, A, ('Ex005', 'qg2'), 'short'])

flagPreview = False
flagChoice = True
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}

h4q.work('Ex005', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling, figures)


