import html4quiz as h4q

QGs = []
Q=['Submit the sum of the two integers {%vA%} and {%vB%}.',
   'Subtract {%vA%} from {%vB%} and submit your answer.']

A='''data=[]
vA=random.randint(10,30)
vB=random.randint(10,30)
answer=[vA+vB, vB-vA]'''

QGs.append([Q, A, ('chap1', 'qg1'), 'short'])

flagPreview = True
flagChoice = False
flagShuffling = False
figures = {}

a = h4q.work('checkups1', 'Testing', {'12345678': 'abc def'}, QGs, flagPreview, flagChoice, flagShuffling)
h4q.mkHTMLs(a, figures)
