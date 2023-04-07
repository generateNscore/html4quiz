import random

# 반환값: 보기문항들 (최소 4 개 이상), 정답문항번호, 정답

nChoices=4

def func1(choices=None, ans=None):
    vA=random.randint(10,30)
    vB=random.randint(10,30)

    return vA, vB



if __name__ == '__main__':
    print(func1())
