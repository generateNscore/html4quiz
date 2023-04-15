import random, re, os, pickle, copy, webbrowser
from .makeChoices import generateChoices



class work():
    def __init__(self, name: str ='Preview', heading: str='Example', STDs: dict={'12345678': '홍 길동(abc def)'},
                 QGs: list=[], flagPreview: bool=True, flagChoice: bool=False, flagShuffling: bool=False,
                 resources: dict={}):
        self.Name=name
        self.Heading=heading
        self.STDs=STDs
        self.QGs=QGs
        self.Flag4Preview = flagPreview
        self.Flag4Choice = flagChoice
        self.Flag4Shuffling = flagShuffling
        #self.Flag4Answer = True
        self.Sheets={}
        self.resources = resources
        
        if self.QGs and self.STDs:
            self.initializeWork()
            self.makeSheets()
            self.mkHTMLs()
            if not self.Flag4Preview:
                print(f'Question sheets in HTML files and answer files are saved in the "{self.Name}" folder')
                self.saveWork()
            
        
    def initializeWork(self):
        if not self.QGs or not self.STDs: return
        self.Sheets.clear()

        # check STDs
        if not isinstance(self.STDs, dict):
            print('STDs is not a proper dictionary.')
            return

        for k, v in self.STDs.items():
            if not k or not v:
                print('One of keys and values is not a proper value')
                return

            if not isinstance(k, str) or not isinstance(v, str):
                print('One of keys and values is not a string')
                return
                
        if self.Flag4Preview:
            for j, qg in enumerate(self.QGs):
                indices=list(range(len(qg[0])))
                self.Sheets[j]={'orders':indices,
                                  'seed':random.sample(range(10001,100000), len(qg[0]))}

        else:
            if '12345678' in self.STDs and self.STDs['12345678'] == '홍 길동(abc def)':
                print('STDs is not ready for question sheets')
                return
            
            indices=list(range(len(self.QGs)))
            for std in self.STDs.keys():
                self.Sheets[std]={'orders':indices.copy(),
                                  'seed':random.sample(range(10001,100000), len(self.QGs))}

            if self.Flag4Shuffling:
                for v in self.Sheets.values():
                    random.shuffle(v['orders'])


    def makeSheets(self):
        if not self.QGs or not self.STDs: return
        
        if self.Flag4Preview:
            for std, v in self.Sheets.items():
                tmp=[]
                for seed, j in zip(v['seed'], v['orders']):
                    out=self.getQA(self.QGs[std], j, seed, self.resources) #<--- 아래와 차이, 2023.04-15 추가
                    origAnswer=copy.deepcopy(out[1])
                    if out[0] is None:
                        print(std, out, self.QGs[cat][name].Name, '????---Try again!')
                        self.Sheets.clear()
                        return

                    if self.QGs[std][-1] == 'python':
                        tmp.append(out)
                    elif isinstance(out[1], (int, float)) and self.Flag4Choice:
                        xtra, ansChoice, ans, choicesUsed = generateChoices(out[1])
                        out = (out[0]+xtra, int(ansChoice), out[-1], (origAnswer, choicesUsed))
                        tmp.append(out)
                    elif isinstance(out[1], dict) and 'choices' in out[1]:
                        xtra, ansChoice, ans, choicesUsed = generateChoices(out[1])
                        out = (out[0]+xtra, int(ansChoice), out[-1], (origAnswer, choicesUsed))
                        tmp.append(out)
                    else:
                        tmp.append(out)

                v['Q&A'] = tmp
                
        else:
            for std, v in self.Sheets.items():
                tmp=[]
                for seed, j in zip(v['seed'], v['orders']):
                    out=self.getQA(self.QGs[j], -1, seed, self.resources) #<--- 위와 차이, 2023.04-15 추가
                    origAnswer=copy.deepcopy(out[1])
                    if out[0] is None:
                        print(std, out, self.QGs[cat][name].Name, '????---Try again!')
                        self.Sheets.clear()
                        return

                    if self.QGs[j][-1] == 'python':
                        tmp.append(out)
                    elif isinstance(out[1], (int, float)) and self.Flag4Choice:
                        xtra, ansChoice, ans, choicesUsed = generateChoices(out[1])
                        out = (out[0]+xtra, int(ansChoice), out[-1], (origAnswer, choicesUsed))
                        tmp.append(out)
                    elif isinstance(out[1], dict) and 'choices' in out[1]: # and isinstance(out[1]['ans'], (int, float)):
                        xtra, ansChoice, ans, choicesUsed = generateChoices(out[1])
                        out = (out[0]+xtra, int(ansChoice), out[-1], (origAnswer, choicesUsed))
                        tmp.append(out)
                    else:
                        tmp.append(out)

                v['Q&A'] = tmp


    def getAnswers(self):
        return {std:[item[1] for item in v['Q&A']] for std,v in self.Sheets.items()}


    def saveWork(self):
        if self.Flag4Preview:
            print("'Preview' flag is True, ignoring calls to saveWork(). Change the Flag4Preview to False and try again")
            return
        
        if not os.path.exists(os.path.join('.', f'{self.Name}')):
            os.mkdir(os.path.join('.', f'{self.Name}'))

        # save work to a pickle file - to be used to score student's answer files
        pickle.dump(self, open(os.path.join('.',f'{self.Name}',f'{self.Name}Work.pickle'),'wb'),
                               protocol=pickle.HIGHEST_PROTOCOL)

        # save all answers to a text file - to provide to students after scoring is done
        with open(os.path.join('.',f'{self.Name}',f'{self.Name}Answers.txt'), mode='w', encoding='utf-8') as f:
            f.write(f'{self.Heading} Answers {self.Name}\n')
            for SID, ans in self.getAnswers().items():
                f.write('SID: '+SID+'\n')
                for j, item in enumerate(ans):
                    f.write(f'\t{j+1}: {item}\n')


    @staticmethod
    def getQA(QG, indxJ: int =-1, seed: int =None, resources: dict=None):
        if seed:
            random.seed(seed)

        Q, strA, _, qType = QG

        if indxJ<0:
            indxJ=random.choice(range(len(Q)))

        try:
            exec(strA)
        except Exception as err:
            return f'<font color="#dd0000"><bold>Error</bold></font>::exec(A)...{err}', None, None, None

        try:
            dataA=eval('data')
        except Exception as err:
            return f'<font color="#dd0000"><bold>Error</bold></font>::eval(data)....{err}', None, None, None
        
        try:
            answers=eval('answer')
        except Exception as err:
            return f'<font color="#dd0000"><bold>Error</bold></font>::eval(answer)....{err}', None, None, None

        if not answers:
            return f'<font color="#dd0000"><bold>Error</bold></font>::empty answer. Add answer.', None, None, None

        if len(answers)<len(Q):
            return f'<font color="#dd0000"><bold>Error</bold></font>::insufficent answers. Add answer.', None, None, None

        strQ=Q[indxJ]

        if '<!--' in strQ:
            indx=strQ.index('<!--')
            print(indx)
            strQ = strQ[:indx]

        if '{%' in strQ and '%}' in strQ:
            for string in re.findall(r"\{%(.*?)\%}", strQ):
                try:
                    strQ=strQ.replace('{%'+string+'%}', str(eval(string)))
                except Exception as err:
                    return f'<font color="#dd0000"><bold>Error</bold></font>::질문 #{indxJ+1}에 들어있는 변수-{string}....{err}', None, None, None

        if dataA:
            if strQ.rstrip().endswith('</pre>'):
                strQ += '<p><b>DATA:</b><br>'+'<br>'.join(f'{v}' for v in dataA)+'</p>'
            else:
                strQ += '<p><b>DATA:</b><br>'+'<br>'.join(f'{v}' for v in dataA)+'</p>'

        return strQ, answers[indxJ], indxJ, qType


    def mkHTMLs(self):
        if not self.Sheets: return 'No work is given.'

        HTMLfiles={}
        for std, v in self.Sheets.items():
            qna=v['Q&A']
            list4HTML=[(j, item[0].split('%HTML%')[-1]) for j, item in enumerate(qna) if '%HTML%' in item[0]]
            list4HTMLindices=[j for j, item in list4HTML]

            if list4HTML: # 단순한 설명 html 내용이 있는 경우
                func='<script type="application/javascript">\n'
                for j, item in enumerate(qna):
                    if j in list4HTMLindices: # 단순한 설명 html인 경우
                        func +=templateF.replace('qNUM', f'{j}').replace('TEXT', '')
                    else: # 질문인 경우
                        func += self.mkHtmlFuncDisplayQ(j, item[0], None, self.resources)
                        
            else: # 예전과 동일
                func='<script type="application/javascript">\n'
                for j, item in enumerate(qna):
                    if isinstance(item[-1], (tuple, list)) and len(item[-1])>1 and isinstance(item[-1][0], dict) and 'cols' in item[-1][0]:
                        func += self.mkHtmlFuncDisplayQ(j, item[0], item[-1], self.resources) # 2023-04-03 보기문항이 그림들인 경우
                    else:
                        func += self.mkHtmlFuncDisplayQ(j, item[0], None, self.resources) # 예전과 동일
                
            func += templateEnd.replace('QMAX', f'{len(qna)-1}')

            if self.Flag4Preview:
                table=templateTable+''.join([f'\n{jj+1}: {qna[jj][1]}' for jj in range(len(qna))])
                table=table.replace('NAME', f'{std}') #<---
            else:
                table=templateTable+''.join([f'\n{jj+1}: ' for jj in range(len(qna))])
                table=table.replace('NAME', self.STDs[std])
            
            table += '</textarea></td></tr></tbody></table>'

            if self.Flag4Preview:
                file = templateHEAD.replace('TITLE', f'{self.Heading} {self.Name}{std} {std}') + table
            else:
                file = templateHEAD.replace('TITLE', f'{self.Heading} {self.Name}{std} {self.STDs[std]}') + table

            file = file.replace('ONCONTEXTMENU', '<body style="word-break:keep-all; display: block; font-family: malgun;  font-size: 18px;">')

            for jj in range(len(qna)):
                file += f'<input type="button" onclick="javascript:display_Q{jj}();" class= "btn" value="Q-{jj+1}"  />\n'

            file += templateBodyR.replace('FILENAME', f'{self.Name}{std}')

            if list4HTML:
                for j, txt in list4HTML:
                    file += f'<div id="HTML{j}" style="word-break:keep-all; padding: 0px 20px 10px 20px; background-color: #f2f6fc; border: 1px solid #999; display: block; font-family: malgun;  font-size: 18px;line-height: 1.5em; display=none;">'
                    file += txt
                    file += '</div>'
            
            if 'line_arrow' in func:
                func = line_arrow +func


            if self.Flag4Preview:
                file += JS4TABLEwithRadiobuttons.replace('FILENAME', f'{self.Name}{std}').replace('NAME', f'{std}')
            else:
                file += JS4TABLEwithRadiobuttons.replace('FILENAME', f'{self.Name}{std}').replace('NAME', self.STDs[std])
            
            HTMLfiles[std]=file+func

        if not os.path.exists(os.path.join('.', f'{self.Name}')):
            os.mkdir(os.path.join('.', f'{self.Name}'))
        if not os.path.exists(os.path.join('.', f'{self.Name}', f'{self.Name}')):
            os.mkdir(os.path.join('.', f'{self.Name}', f'{self.Name}'))

        for k, v in HTMLfiles.items():
            open(os.path.join('.',f'{self.Name}',f'{self.Name}',f'{self.Name}_{k}.html'),
                 mode='w', encoding='utf-8').write(v)

        # index.html
        if self.Flag4Preview:
            file = templateBodyF.replace('TITLE', f'{self.Heading} {self.Name}') + '\n<table><tbody>'
            for k in self.Sheets.keys():
                file += f'\n<tr><td><a href="./{self.Name}_{k}.html">{k}--{self.QGs[k][2]}</a></td></tr>'
            file +='</tbody></table></html>'
            open(os.path.join('.',f'{self.Name}',f'{self.Name}','index.html'), mode='w', encoding='utf-8').write(file)
            if k:
                webbrowser.open(os.path.join('.',f'{self.Name}',f'{self.Name}','index.html'))
            else:
                webbrowser.open(os.path.join('.',f'{self.Name}',f'{self.Name}',f'{self.Name}_{k}.html'))
        else:
            file = templateBodyF.replace('TITLE', f'{self.Heading} {self.Name}') + '\n<table><tbody>'
            for k, Sname in self.STDs.items():
                file += f'\n<tr><td><a href="./{self.Name}_{k}.html">{k}--{Sname}</a></td></tr>'
            file +='</tbody></table></html>'
            open(os.path.join('.',f'{self.Name}',f'{self.Name}','index.html'), mode='w', encoding='utf-8').write(file)


    @staticmethod
    def mkHtmlFuncDisplayQ(qJ, txt, xtra=None, resources=None): # 2023-04-03 correctAnswer --> xtra
        if '<!--' in txt: # 2023-03-21 추가
            indx=txt.index('<!--')
            txt = txt[:indx]
        
        txt=txt.strip().replace('\n', '')  # '\n' 없애야 하는 이유는 FIG% %FIG 을 사용하기 위해...그리고 ... 많음.

        str2bUsed=''
        if 'init(' in txt:
            init=txt.split('init(')[-1].split(';')[0]
            str2bUsed=f'init({init};'
            txt = txt.replace(str2bUsed,'')

        figObjts=[]
##        if 'FIG%' in txt: # 직접 변경 가능
##            for item in re.findall(figPattern, txt):
##                itemStripped=item.strip()
##                if itemStripped:
##                    figObjts.append(itemStripped)
##                    txt=txt.replace(f'FIG%{item}%FIG', '')
##
        if 'figure(' in txt: # 한 번 만든 것.. 직접 변경 불가능..
            for item in re.findall(figurePattern, txt):
                figureKey=item.strip()
                if figureKey and figureKey in resources:
                    figObjts.append(resources[figureKey])
                    txt=txt.replace(f'figure({item})','')
                else:
                    txt=txt.replace(f'figure({item})',f'figure({item}):Error of not finding it')        

        txt=txt.replace("'", "&#39;") # 2022.08.07 둘다 사용하지 않는 것으로...

        if 'chr(9)' in txt:
            txt=txt.replace('chr(9)','&nbsp;&nbsp;&nbsp;&nbsp;')

        if 'EQ%' in txt:
            for item in re.findall(eqPattern, txt):
                txt=txt.replace(f'EQ%{item}%EQ',
                                r'<img src="http://latex.codecogs.com/png.latex?\dpi{130}'+ f' {item}"/>')
            txt=txt.replace('\\', '\\\\')

        if str2bUsed:
            for j, obj in enumerate(figObjts):
                if '//init();' in obj:
                    figObjts[j] = obj.replace('//init();', str2bUsed)

        txt = f'<p><font color=red><strong>{qJ+1}.</strong></font> '+txt
        #indx = txt.find('<form')
        indx = txt.find('<div> ')  # 반드시 makeChoices._ChoicesWithRadiobuttons() 와 맞춰야 함....
        if indx == -1:
            txt += '</p>'
        else:
            txt = txt[:indx]+'</p>'+txt[indx:]


    ##    out=templateF.replace('TEXT', f'<p><font color=red><strong>{qJ+1}.</strong></font> '+txt).replace('qNUM', f'{qJ}')
        out=templateF.replace('TEXT', txt).replace('qNUM', f'{qJ}')

        if figObjts:
            if xtra:
                figureKey += 'F'
                jsCode=f'function {figureKey}'+cnvs2nd+figObjts[0]+'}'
                jsCode=jsCode.replace('//init();', 'init(prms);')

                more = [f'{figureKey}("cnvs{j}", {item});' for j, item in enumerate(xtra[1])]
                out=out.replace('JS_CODE', 'cnvs.height=0;\n'+jsCode+''.join(more))
                    
            else:
                out=out.replace('JS_CODE', 'cnvs.height=300;\n'+'\n'.join(figObjts))
        else:
            out=out.replace('JS_CODE', 'cnvs.height=0;')

        for item in re.findall('<br><br>*<br>', out):
            out=out.replace(item, '')

        return out

            


eqPattern='EQ%(.*?)%EQ'
figPattern='FIG%(.*?)%FIG'
figurePattern='figure\((.*?)\)'

cnvs2nd='''(cnvsName, prms) {
var cnvs = document.createElement("canvas");
div = document.getElementById(cnvsName);
div.appendChild(cnvs);
var ctx = cnvs.getContext("2d");
'''

# 단순한 html page 용 template
templateHEAD='''<!DOCTYPE html>
<html>
<head>
<title>TITLE</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style>
.prePrompt {float: left; margin: 20px   0px 20px 10px; padding: 10px   5px 10px   5px; background: #efc; font-family: bold Courier New; font-size: 14px; line-height: 0.5 em; width: 30px;              text-align: left; border: 1px solid powderblue; border-right: none; color: #700;}
.preBody     {float: left; margin: 20px 10px 20px   0px; padding: 10px 10px 10px 10px; background: #efc; font-family: bold Courier New; font-size: 14px; line-height: 0.5 em; width: text-content; text-align: left; border: 1px solid powderblue; }
.preChoice  {float: left; margin: 0px 10px 20px 10px; padding: 10px; background: #fff; font-family: bold Courier New; font-size: 14px; line-height: 0.5 em; width: text-content; text-align: left; border: 1px solid powderblue; }
.btn             {align-items: center; appearance: none; background-color: #eef; border-radius: 24px; border-style: none; box-shadow: rgba(0, 0, 0, .2) 0 3px 5px -1px,rgba(0, 0, 0, .14) 0 6px 10px 0,rgba(0, 0, 0, .12) 0 1px 18px 0; box-sizing: border-box; color: #3c40e3; cursor: pointer; display: inline-flex; fill: currentcolor; font-family: "Google Sans",Roboto,Arial,sans-serif; font-size: 16px; font-weight: 500; height: 48px; justify-content: center; letter-spacing: .25px; line-height: normal; max-width: 100%; overflow: visible; padding: 2px 24px; margin: 5px; position: relative; text-align: center; text-transform: none; transition: box-shadow 280ms cubic-bezier(.4, 0, .2, 1),opacity 15ms linear 30ms,transform 270ms cubic-bezier(0, 0, .2, 1) 0ms; user-select: none; -webkit-user-select: none; touch-action: manipulation; width: auto; will-change: transform,opacity; z-index: 0;}
.btn2           {align-items: center; background-clip: padding-box; background-color: #fa6400; border: 1px solid transparent; border-radius: .25rem; box-shadow: rgba(0, 0, 0, 0.2) 0 1px 3px 0; box-sizing: border-box; color: #fff; cursor: pointer; display: inline-flex; font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif; font-size: 20px; font-weight: 600; justify-content: center; line-height: 1.25; margin: 0px 10px 2px 5px; min-height: 3rem; padding: calc(.875rem - 1px) calc(1.5rem - 1px); position: relative; text-decoration: none; transition: all 250ms; user-select: none; -webkit-user-select: none; touch-action: manipulation; vertical-align: baseline; width: auto;}

.radiocontainer {background-color:#e8e8f8; display: block; position: relative; padding:10px 20px 10px 50px; margin: 0px 5px 2px 0px; cursor: pointer; font-size: 18px; -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; word-wrap: break-word; min-width: 200px;}
.radiocontainer input {  position: absolute;  opacity: 0;  cursor: pointer;}
.checkmark {  position: absolute;  top: 15px;  left: 15px;  height: 19px;  width: 19px;  background-color: #fff;  border-radius: 50%;}
.checkedlabel {  background-color:#ddd;}
.radiocontainer:hover input ~ .checkmark {}
.radiocontainer:hover {  background-color: #ddd;}
.radiocontainer input:checked ~ .checkmark {  background-color: #12693F;}
.checkmark:after {  content: "";  position: absolute;  display: none;}
.radiocontainer input:checked ~ .checkmark:after {  display: block;}
.radiocontainer .checkmark:after {top: 6px; left: 6px; width: 7px; height: 7px; border-radius: 50%; background: white;}
</style>
</head>
ONCONTEXTMENU
<center><h4>TITLE</h4></center>'''

templateBodyF='''<!DOCTYPE html>
<html>
<head>
<title>TITLE</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<body oncontextmenu="return false">
<center><h4>TITLE</h4></center>'''

templateBodyR='''<hr> <div id="Qs" style="word-break:keep-all; display: block; font-family: malgun; font-size: 18px; margin: 0px 10px 0px 10px; padding: 0px 5px 0px 5px;"></div>
<canvas id="canvas" width="800" height="0"></canvas>
'''

templateF='''function display_QqNUM() {
document.getElementById("Qs").innerHTML='TEXT';
Qnumber = qNUM;
setCheckedRadio(qNUM);

var cnvs = document.getElementById("canvas");
var ctx = cnvs.getContext("2d");
ctx.clearRect(0,0, cnvs.width, cnvs.height);
JS_CODE
}
'''

templateEnd='''
document.onkeydown = function (e) {
  if (e.altKey && e.keyCode == 39) {
    Qnumber += 1;
    if (Qnumber>Qmax) {Qnumber = 0};
    eval("display_Q"+Qnumber+"()");}
  else if (e.altKey && e.keyCode == 37) {
    Qnumber -= 1;
    if (Qnumber<0) {Qnumber = Qmax};
    eval("display_Q"+Qnumber+"()");}
}
var Qnumber = 0;
var Qmax = QMAX;
var answers = [];
for (let j=0; j<=Qmax; j++) {answers.push(null);}

display_Q0();</script>\n</body>\n</html>
'''

templateTable='''<ul style="font-size: 14px">
<li>객관식 질문의 답은 정수로 답하시오. For multiple-choice questions, answer with an integer.</li>
<li>단답형 질문의 숫자 답은, 가장 중요한 3개의 숫자로 반올림하시오. For numerical answer to short questions, round to the three most significant digits.</li>
<li>요청에 따라 숫자를 문자열로 제출해는 경우, 양쪽에 따옴표를 붙이시오. If you are asked to submit a number as a string, put quotes around it.</li></ul>
<table>
<tbody>
<tr>
<td ><button onclick="saveTextAsFile()" class="btn2">Save<br>Answers<br>to File</button></td>
<td><textarea id="inputTextToSave" cols="155" rows="5" style="font-family: malgun;  font-size: 16px; padding: 5px  0px  5px  20px; ">
나, NAME은(는) 위 내용을 읽고 아래 답을 직접 작성했음을 확인합니다. I, NAME, confirm that I read the notes above and wrote the answer myself below.
--------------------------------------------------------------------------------------------------------------------'''


JS4TABLEwithRadiobuttons='''<script type="text/javascript">
function saveTextAsFile() {
  var textToSave = document.getElementById("inputTextToSave").value;
  var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
  var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
  var fileNameToSaveAs = "FILENAME.txt"

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  downloadLink.href = textToSaveAsURL;
  downloadLink.onclick = destroyClickedElement;
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);
  downloadLink.click();
}

function addAnswers2Textarea() {
  const textarea = document.getElementById("inputTextToSave");
  var text = textarea.value;
  const searchTerm = "--------------------------------------------------------------------------------------------------------------------";
  const indexOfFirst = text.indexOf(searchTerm);
  var newText = text.slice(0, indexOfFirst+searchTerm.length);
  for (let q=0; q<=Qmax; q++) {
    if (answers[q] == null) {newText += String.fromCharCode(13)+(q+1).toString()+": ";}
    else {newText += String.fromCharCode(13)+(q+1).toString()+": "+answers[q].toString();}
  }
  textarea.value = newText;
}

function handleClick(myRadio) {
  answers[parseInt(myRadio.name.slice(1))]=parseInt(myRadio.value)+1;
  addAnswers2Textarea();
}

function setCheckedRadio(q) {
  var radios = document.getElementsByName('Q'+q.toString());
  //for (let j=0; j<radios.length; j++) {radios[j].removeAttribute("checked");}
  if (radios.length > 0 && answers[q] != null) {radios[answers[q]-1].setAttribute("checked", true);}
}

function destroyClickedElement(event) {
    document.body.removeChild(event.target);
}
</script>
'''


line_arrow='''<script type="application/javascript">
function line_arrow(context, fromx, fromy, tox, toy, color, end) {
  var headlen = 7;
  var dx = tox - fromx;
  var dy = toy - fromy;
  var angle = Math.atan2(dy, dx);
  context.beginPath();
  context.strokeStyle = color;
  if (end == "last") {
    context.moveTo(fromx, fromy);
    context.lineTo(tox, toy);
    context.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
    context.moveTo(tox, toy);
    context.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
  }
  else if (end=="both") {
    context.moveTo(fromx, fromy);
    context.lineTo(tox, toy);
    context.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
    context.moveTo(tox, toy);
    context.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
    context.moveTo(fromx, fromy);
    context.lineTo(fromx + headlen * Math.cos(angle + Math.PI / 6), fromy + headlen * Math.sin(angle + Math.PI / 6));
    context.moveTo(fromx, fromy);
    context.lineTo(fromx + headlen * Math.cos(angle - Math.PI / 6), fromy + headlen * Math.sin(angle - Math.PI / 6));
  }
  else if (end == "first"){
    context.moveTo(tox, toy);
    context.lineTo(fromx, fromy);
    context.lineTo(fromx + headlen * Math.cos(angle + Math.PI / 6), fromy + headlen * Math.sin(angle + Math.PI / 6));
    context.moveTo(fromx, fromy);
    context.lineTo(fromx + headlen * Math.cos(angle - Math.PI / 6), fromy + headlen * Math.sin(angle - Math.PI / 6));
  }
  context.stroke();
}
</script>
'''
