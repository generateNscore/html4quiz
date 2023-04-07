import random

# 반환값: 보기문항들 (최소 4 개 이상), 정답문항번호, 정답

nChoices=4


def func2(prm):
    rights=[]
    for _ in range(10):
        vA=random.choice(range(50,99))
        vB=random.choice(range(10,50))
        rights.append(f'{vA}+{vB}={vA+vB}')

    wrongs=[]
    for s in rights:
        eq, ans= s.split('=')
        a, b = eq.split('+')
        wrongs.append(f"{eq}={eval(ans)+1}" if random.choice([0,1]) else f"{eq}={eval(ans)-1}")
        
##    entries, indx, ans = RightWrong(rights, wrongs, prm)
##    return entries, indx, ans
    return RightWrong(rights, wrongs, prm)


def RightWrong(entries4Right=[], entries4Wrong=[], f='옳은'):
    if f in ('옳은', 'correct'):
        correctAns=random.choice(entries4Right)
        entries=entries4Wrong.copy()
        indx=entries4Right.index(correctAns)
        if len(entries)>indx: entries.pop(indx)
    else:
        correctAns=random.choice(entries4Wrong)
        entries=entries4Right.copy()
        indx=entries4Wrong.index(correctAns)
        if len(entries)>indx: entries.pop()

    entries.append(correctAns)

    return entries, entries.index(correctAns), correctAns



if __name__ == '__main__':
    print(func2('correct'))
