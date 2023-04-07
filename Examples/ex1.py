import generateNscore as gNs

QGs = []
Q=['Submit the sum of the two integers {%vA%} and {%vB%}.',
   'Subtract {%vA%} from {%vB%} and submit your answer.']

A='''data=[]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer=[vA+vB, vB-vA]'''

QGs.append([Q, A, ('chap1', 'qg1'), 'short'])

flagSample = False
flagChoice = True
flagShuffling = False
figures = {}

a = gNs.work('checkups1', 'Testing', {'12345678': 'abc def'}, QGs, flagSample, flagChoice, flagShuffling)
gNs.mkHTMLs(a, figures)
