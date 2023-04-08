import random

def func2(choices=None, ans=None):
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

if __name__ == '__main__':
    print(func2())
