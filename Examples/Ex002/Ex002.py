import html4quiz as h4q

QGs = []


Q=['What is the sum of the two fill areas of the color drawn below?<br>figure(addFractions)<br>init({%prms%});']
A='''data=[]
import userfunctions
choices, indx, ansValue = userfunctions.func2()
answer=[{'choices':choices, 'ans':choices[indx]}]
prms=ansValue'''

QGs.append([Q, A, ('Examples', 'Ex002'), 'choice'])

figures={'addFractions': h4q._common.getResource('addFractions')}

flagPreview = False
flagChoice = False
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
a = h4q.work('Ex002', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling, figures)
#h4q.mkHTMLs(a, figures)
#a.saveWork()
