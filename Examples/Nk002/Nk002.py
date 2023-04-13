import html4quiz as h4q

QGs = []

figures={'add2Vectors': h4q._common.getFigure('add2Vectors')}

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



flagPreview = False
flagChoice = True
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = h4q.work('Nk002', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling)
h4q.mkHTMLs(a, figures)
a.saveWork()
