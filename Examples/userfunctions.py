import random

# 반환값: 보기문항들 (최소 4 개 이상), 정답문항번호, 정답

nChoices=4

def func1(choices=None, ans=None):
    from fractions import Fraction
    choicesBefore = []
    
    for j in range(15):
        fr1=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        fr2=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        tmp = (fr1, fr2, (fr1+fr2))
        if tmp[-1] not in [item[-1] for item in choicesBefore]: choicesBefore.append(tmp)

    choices=[]
    for _, _, fr in choicesBefore:
        choices.append(r'EQ% \frac {'+f'{fr.numerator}'+'} {'+f'{fr.denominator}'+'} %EQ')

    indx=random.choice(range(len(choices)))
    f1, f2, _=choicesBefore[indx]
    return choices, indx, fr'EQ% \frac {f1.numerator} {f1.denominator} + \frac {f2.numerator} {f2.denominator}%EQ'


def func1B(choices=None, ans=None):
    from fractions import Fraction
    choicesBefore = []
    for j in range(15):
        fr1=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        fr2=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        tmp = (fr1, fr2, (fr1+fr2))
        if tmp[-1] not in [item[-1] for item in choicesBefore]: choicesBefore.append(tmp)

    choices=[]
    for _, _, fr in choicesBefore:
        choices.append(r'EQ% \frac {'+f'{fr.numerator}'+'} {'+f'{fr.denominator}'+'} %EQ')

    indx=random.choice(range(len(choices)))
    f1, f2, _=choicesBefore[indx]
    return choices, indx, [300, [f1.numerator, f1.denominator, f2.numerator, f2.denominator]]


def func1C(choices=None, ans=None):
    from fractions import Fraction
    choicesBefore = []
    for j in range(15):
        fr1=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        fr2=Fraction(random.choice([1,2]), random.choice([4,5,6,7,8]))
        tmp = (fr1, fr2, (fr1+fr2))
        if tmp[-1] not in [item[-1] for item in choicesBefore]: choicesBefore.append(tmp)

    choices=[]
    for f1, f2, _ in choicesBefore:
        choices.append([100, [f1.numerator, f1.denominator,f2.numerator, f2.denominator]])

    indx=random.choice(range(len(choices)))
    _, _, fsum=choicesBefore[indx]
    return choices, indx, r'EQ% \frac {'+f'{fsum.numerator}'+'} {'+f'{fsum.denominator}'+'} %EQ'

if __name__ == '__main__':
##    for item in func1()[0]:
##        print(item)
    print(func1C())
