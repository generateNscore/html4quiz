import random

from ._common import round2MSF
#from _common import round2MSF

# 위 import의 common 앞의 .(dot)은 반드시 필요하다.
# 본 코드를 수정하면, .(dot)을 삭제하고 실행한다.
# 그러나, 오류가 없음을 확인하면 반드시 .(dot)을 되돌린 후 저장한다.

# 보기문항은 반드시 정답란에서 정한다.
# 보기문항은 string object으로 생성되며 이름은 choices으로 한다.
# 즉, 이름이 choices인 변수가 존재하면,  선택형 질문이 된다.


def generateChoices(ans, nChoices: int=4): # generateEm.work.makeSheets()에서 사용
    '''
ans: either a number or a dictionary object
    when it is a number, either integer or floating number,
        choices and correct choice are generated randomly.

    when it is a dictionary object,
        a key of "choices" must be present with/without a value.
        the value of "ans" key should the correct answer value, not the index of it among the choices provided.

        if the value of "choices" key is None,
        choices and correct choice are generated randomly with the specified method, given by the value for "fn" key.

        ** a list of methods available can be found by running the code below in Shell screen **

            gNs.makeChoices.fns

        if the key of "cols" is present,
            it indicates a special layout; each choice is a figure.
            this case used multiple canvases in HTML page and a lot of extra coding in HTML, CSS, and Javascript is involved.
            ...
            this case requires more attention in future


To test this function, try the code below in Shell screen.

    gNs.makeChoices.generateChoices(ans)

'''

    columnsN=None
    if isinstance(ans, dict) and 'choices' in ans:
        if 'cols' in ans and ans['cols']: columnsN=ans['cols']

        if ans['choices'] and isinstance(ans['choices'], (list, tuple)):
            try:
                choices=ans['choices'] # 이 경우, 정답, ans, 은 항상 들어있음.
                ans=ans['ans']
            except Exception as err:
                return f'<font color="#dd0000"><bold>Error</bold></font>::  {err}', 0, 0
        elif 'fn' in ans:
            if ans['fn'] in fns:
                fn=eval(ans['fn'])
                ans=round2MSF(ans['ans'])
                choices=fn(str(ans))
            else:
                return '<font color="#dd0000"><bold>Error</bold></font>::  ??????', 0, 0
        else:
            return f'<font color="#dd0000"><bold>Error</bold></font>::  {err}', 0, 0
    else:
        if ans: # 정수 또는 실수인 일반적인 경우
            ans=round2MSF(ans)
            if isinstance(ans, int):
                if random.randint(0, 1):
                    choices=variation0_int(str(ans))
                else:
                    tmp=random.randint(0,3)
                    if tmp==2:
                        choices=variation0_int_5Add(str(ans)) if random.randint(0,1) else variation0_int(str(ans))
                    elif tmp==1:
                        choices=variation0_int_3Add(str(ans)) if random.randint(0,1) else variation0_int(str(ans))
                    else:
                        if ans > 50:
                            choices=variation0_int_2Add(str(ans)) if random.randint(0,1) else variation0_int(str(ans))
                        else:
                            if random.randint(0,3):
                                choices=variation0_int_2Add(str(ans)) if random.randint(0,1) else variation0_int(str(ans))
                            else:
                                choices=variation0_int_2(str(ans)) if random.randint(0,1) else variation0_int(str(ans))
            else:
                if random.randint(0,5):
                    choices=variation0(str(ans))
                else:
                    choices=variation2(str(ans))
        else:
            ans=0
            choices=variation0_int(str(ans))

    choices.remove(ans)
    random.shuffle(choices)
    if not random.choice(range(8)):
        if len(choices)<nChoices:
            print(len(choices), nChoices, ans, choices, '답 없음 ...')
            nChoices=len(choices)
        answers=random.sample(choices, nChoices)
        return _ChoicesWithRadiobuttons(answers, columnsN), nChoices+1, ans, answers # 4th 추가
    else:
        if len(choices)<nChoices-1:
            print(len(choices), nChoices-1, ans, choices, '답 ...')
            nChoices = len(choices)+1
        answers=random.sample(choices, nChoices-1)
        answers.append(ans)
        random.shuffle(answers)
        return _ChoicesWithRadiobuttons(answers, columnsN), answers.index(ans)+1, ans, answers # 4th 추가


def _ChoicesWithNumbers(answers):
    choices = '<br>'
    for j, choice in enumerate(answers):
        choices += '<br>'+chr(9312+j)+f' {choice}'

    choices += '<br>'+chr(9312+j)+' None of the above'
    choices += '<br>'+chr(9313+j)+' All of the above'
    return choices


##def _ChoicesWithRadiobuttons(answers):
##    choices = '<br> '
##    for j, choice in enumerate(answers):
##        charInCircle=chr(9312+j)
##        choices += f'<br><input type="radio" style="height:20px; width:20px; vertical-align: middle; border-radius: 50%; bckground: white;" id="{charInCircle}" name="QqNUM" onclick="handleClick(this);" value="{j}"><label for="{charInCircle}"> {choice}</label>'
##
##    charInCircle=chr(9312+j)
##    choices += f'<br><input type="radio" style="height:20px; width:20px; vertical-align: middle; border-radius: 50%; bckground: white;" id="{charInCircle}" name="QqNUM" onclick="handleClick(this);" value="{j+1}"><label for="{charInCircle}"> None of the above</label>'
##    charInCircle=chr(9313+j)
##    choices += f'<br><input type="radio" style="height:20px; width:20px; vertical-align: middle; border-radius: 50%; bckground: white;" id="{charInCircle}" name="QqNUM" onclick="handleClick(this);" value="{j+2}"><label for="{charInCircle}"> All of the above</label>'
##    return choices


def _ChoicesWithRadiobuttons(answers, columns):
    if columns:
        choices = '<div> '
        for j, choice in enumerate(answers+['None of the above', 'All of the above']):
            if 'above' in choice:
                choices += f'<div style="float: left"><label class="radiocontainer"> {choice}<input type="radio" name="QqNUM" onclick="handleClick(this);" value="{j}"><span class="checkmark"></span></label></div>'
            else:
                choices += f'<div style="float: left"><label class="radiocontainer"> <div id="cnvs{j}"></div><input type="radio" name="QqNUM" onclick="handleClick(this);" value="{j}"><span class="checkmark"></span></label></div>'

        return choices+'</div>'

    else:        
        choices = '<div> <div style="float: left">'
        for j, choice in enumerate(answers+['None of the above', 'All of the above']):
            choices += f'<label class="radiocontainer"> {choice}<input type="radio" name="QqNUM" onclick="handleClick(this);" value="{j}"><span class="checkmark"></span></label>'

        return choices+'</div></div>'

    
def variation0_int_5Add(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=answer[1:] # 음수기호가 제거된 답

    for i4NZ, c in enumerate(ans[::-1]):
        if int(c):
            break
    if i4NZ:
        ans=ans[:-i4NZ]

    zeros='0'*i4NZ

    value = int(ans)
    if value<30:
        tmp = [f'{value+5*j}{zeros}' for j in range(-3,7) if len(f'{value+5*j}')<=3]
    else:
        tmp = [f'{value+5*j}{zeros}' for j in range(-4,6) if len(f'{value+5*j}')<=3]
     
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]

   
##def variation0_int_5(answer: str):
##    # 음수여부
##    ans=answer
##    negative=False
##    if answer.startswith('-'):
##        negative=True
##        ans=answer[1:] # 음수기호가 제거된 답
##
##    for i4NZ, c in enumerate(ans[::-1]):
##        if int(c):
##            break
##    if i4NZ:
##        ans=ans[:-i4NZ]
##
##    zeros='0'*i4NZ
##
##    # 약수 5의 갯수
##    value = int(ans)
##    nYaksoo=0
##    while not value%5:
##        value //= 5
##        nYaksoo += 1
##
##    tmp = [f'{value*5**j}{zeros}' for j in range(10) if len(f'{value*5**j}')<=3]
##     
##    # 음수 복원
##    if negative: tmp=['-'+item for item in tmp if item]
##
##    return [eval(f) for f in tmp]
##
##
##def variation0_int_3(answer: str):
##    # 음수여부
##    ans=answer
##    negative=False
##    if answer.startswith('-'):
##        negative=True
##        ans=answer[1:] # 음수기호가 제거된 답
##
##    for i4NZ, c in enumerate(ans[::-1]):
##        if int(c):
##            break
##    if i4NZ:
##        ans=ans[:-i4NZ]
##
##    zeros='0'*i4NZ
##
##    # 약수 3의 갯수
##    value = int(ans)
##    nYaksoo=0
##    while not value%3:
##        value //= 3
##        nYaksoo += 1
##
##    tmp = [f'{value*3**j}{zeros}' for j in range(10) if len(f'{value*3**j}')<=3]
##     
##    # 음수 복원
##    if negative: tmp=['-'+item for item in tmp if item]
##
##    return [eval(f) for f in tmp]
##
def variation0_int_3Add(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=answer[1:] # 음수기호가 제거된 답

    for i4NZ, c in enumerate(ans[::-1]):
        if int(c):
            break
    if i4NZ:
        ans=ans[:-i4NZ]

    zeros='0'*i4NZ

    value = int(ans)
    if value<20:
        tmp = [f'{value+3*j}{zeros}' for j in range(-3,7) if len(f'{value+3*j}')<=3]
    else:
        tmp = [f'{value+3*j}{zeros}' for j in range(-4,6) if len(f'{value+3*j}')<=3]
     
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]


def variation0_int_2Add(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=answer[1:] # 음수기호가 제거된 답

    for i4NZ, c in enumerate(ans[::-1]):
        if int(c):
            break
    if i4NZ:
        ans=ans[:-i4NZ]

    zeros='0'*i4NZ

    value = int(ans)
    if value<20:
        tmp = [f'{value+2*j}{zeros}' for j in range(-3,7) if len(f'{value+2*j}')<=3]
    else:
        tmp = [f'{value+2*j}{zeros}' for j in range(-4,6) if len(f'{value+2*j}')<=3]
     
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]


def variation0_int_2(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=answer[1:] # 음수기호가 제거된 답

    for i4NZ, c in enumerate(ans[::-1]):
        if int(c):
            break
    if i4NZ:
        ans=ans[:-i4NZ]

    zeros='0'*i4NZ

    # 약수 2의 갯수
    value = int(ans)
    nYaksoo=0
    while not value%2:
        value //= 2
        nYaksoo += 1

    tmp = [f'{value*2**j}{zeros}' for j in range(10) if len(f'{value*2**j}')<=3]
     
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]



def variation0_int(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=answer[1:] # 음수기호가 제거된 답
    
    if len(ans)==1:
        tmp = [str(j) for j in range(10)]
    elif len(ans) == 2:
        if random.randint(0,1):
            tmp = [ans[0]+str(j) for j in range(10)]
        else:
            tmp = [str(j)+ans[1] for j in range(1, 10)]
    else:
        whichone = random.randint(0, 2)
        if  whichone == 0:
            # 유효숫자들 중 첫 번째숫자를 1부터 9까지 변화시킨 목록 생성
            tmp=[f'{i}'+ans[1:] for i in range(1, 10)] # 2022.07.16 추가...
        elif whichone == 1:
            # 유효숫자들 중 2 번째를 0부터 9까지 변화시킨 목록 생성
            tmp=[ans[:1]+f'{i}'+ans[2:] for i in range(10)]
        else:
            # 유효숫자들 중 3 번째를 0부터 9까지 변화시킨 목록 생성
            tmp=[ans[:2]+f'{i}'+ans[3:] for i in range(10)]
 
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]


def variation0(answer: str):
    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=ans[1:] # 음수기호가 제거된 답

    # 소수점여부
    iDot=None
    if '.' in ans:
        iDot=ans.index('.')
        ans=''.join(ans.split('.')) #소수점이 제거된 답

    # i: 0이 아닌 숫자 index
    for i4NZ, c in enumerate(ans):
        if int(c): break
    
    if len(ans)==1:
        tmp=[ans[:i4NZ]+f'{i}'+ans[i4NZ+1:] for i in range(10)]
    else:
        if random.randint(0,1):
            # 유효숫자들 중 첫 번째숫자를 0부터 9까지 변화시킨 목록 생성
            tmp=[ans[:i4NZ]+f'{i}'+ans[i4NZ+1:] for i in range(10)] # 2022.07.16 추가...
        else:
            # 유효숫자들 중 2 번째를 0부터 9까지 변화시킨 목록 생성
            tmp=[ans[:i4NZ+1]+f'{i}'+ans[i4NZ+2:] for i in range(10)]

    # 소수점 복원
    if iDot: tmp=[item[:iDot]+'.'+item[iDot:] for item in tmp]
    # 음수 복원
    if negative: tmp=['-'+item for item in tmp if item]

    return [eval(f) for f in tmp]



def variation2(answer: str):

    # 음수여부
    ans=answer
    negative=False
    if answer.startswith('-'):
        negative=True
        ans=ans[1:] # 음수기호가 제거된 답

    # 소수점여부
    iDot=len(ans)
    if '.' in ans:
        iDot=ans.index('.')
        ans=''.join(ans.split('.')) #소수점이 제거된 답

    ans='0'*3+ans+'0'*3 # 2022.07.16 수정..

    a=[(ans[:i]+'.'+ans[i:]).strip('0') for i in range(1, len(ans))]
    a=['0'+item if item.startswith('.') else item for item in a]
    ans=[item[:-1] if item.endswith('.') else item for item in a]
    if negative: ans=['-'+item for item in ans if item] # 음수 복원

    return [eval(f) for f in ans]


fns=[k for k in globals().keys() if k.startswith('v')]
if __name__ == '__main__':
    for j in range(10000):
        #generateChoices(random.choice(range(10000))/10)
        generateChoices(random.choice(range(10000)))
