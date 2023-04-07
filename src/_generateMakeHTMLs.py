import re, os, math, webbrowser


def mkHTMLs(work, figures=None):
    if not work.Sheets: return 'No work is given.'

    HTMLfiles={}
    for std, v in work.Sheets.items():
        qna=v['Q&A']
        list4HTML=[(j, item[0].split('%HTML%')[-1]) for j, item in enumerate(qna) if '%HTML%' in item[0]]
        list4HTMLindices=[j for j, item in list4HTML]

        if list4HTML: # 단순한 설명 html 내용이 있는 경우
            func='<script type="application/javascript">\n'
            for j, item in enumerate(qna):
                if j in list4HTMLindices: # 단순한 설명 html인 경우
                    func +=templateF.replace('qNUM', f'{j}').replace('TEXT', '')
                else: # 질문인 경우
                    func += mkHtmlFuncDisplayQ(j, item[0], None, figures)
                    
        else: # 예전과 동일
            func='<script type="application/javascript">\n'
            for j, item in enumerate(qna):
                #func += mkHtmlFuncDisplayQ(j, item[0], None, figures)
                if isinstance(item[-1], (tuple, list)) and len(item[-1])>1 and isinstance(item[-1][0], dict) and 'cols' in item[-1][0]:
                    func += mkHtmlFuncDisplayQ(j, item[0], item[-1], figures) # 2023-04-03 보기문항이 그림들인 경우
                else:
                    func += mkHtmlFuncDisplayQ(j, item[0], None, figures) # 예전과 동일
            
        func += templateEnd.replace('QMAX', f'{len(qna)-1}')

        gitHubFolder=r'D:/GitHub/Jict2004'
        if gitHubFolder in func:
            for i in range(func.count(gitHubFolder)):
                func=func.replace(gitHubFolder, 'https://pvlaboratory.github.io/Jict2004')

        if work.Flag4Sample:
            table=templateTable+''.join([f'\n{jj+1}: {qna[jj][1]}' for jj in range(len(qna))])
            table=table.replace('NAME', f'{std}') #<---
        else:
            table=templateTable+''.join([f'\n{jj+1}: ' for jj in range(len(qna))])
            table=table.replace('NAME', work.STDs[std])
        
        table += '</textarea></td></tr></tbody></table>'

        if work.Flag4Sample:
            file = templateHEAD.replace('TITLE', f'{work.Heading} {work.Name}{std} {std}') + table
        else:
            file = templateHEAD.replace('TITLE', f'{work.Heading} {work.Name}{std} {work.STDs[std]}') + table

        file = file.replace('ONCONTEXTMENU', '<body style="word-break:keep-all; display: block; font-family: malgun;  font-size: 18px;">')

        for jj in range(len(qna)):
            file += f'<input type="button" onclick="javascript:display_Q{jj}();" class= "btn" value="Q-{jj+1}"  />\n'

        file += templateBodyR.replace('FILENAME', f'{work.Name}{std}')

        if list4HTML:
            for j, txt in list4HTML:
                file += f'<div id="HTML{j}" style="word-break:keep-all; padding: 0px 20px 10px 20px; background-color: #f2f6fc; border: 1px solid #999; display: block; font-family: malgun;  font-size: 18px;line-height: 1.5em; display=none;">'
                file += txt
                file += '</div>'
        
        if 'line_arrow' in func:
            func = line_arrow +func


        if work.Flag4Sample:
            file += JS4TABLEwithRadiobuttons.replace('FILENAME', f'{work.Name}{std}').replace('NAME', f'{std}')
        else:
            file += JS4TABLEwithRadiobuttons.replace('FILENAME', f'{work.Name}{std}').replace('NAME', work.STDs[std])
        
        HTMLfiles[std]=file+func

    if not os.path.exists(os.path.join('.', f'{work.Name}')):
        os.mkdir(os.path.join('.', f'{work.Name}'))
    if not os.path.exists(os.path.join('.', f'{work.Name}', f'{work.Name}')):
        os.mkdir(os.path.join('.', f'{work.Name}', f'{work.Name}'))

    for k, v in HTMLfiles.items():
        open(os.path.join('.',f'{work.Name}',f'{work.Name}',f'{work.Name}{k}.html'),
             mode='w', encoding='utf-8').write(v)

    # index.html
    if work.Flag4Sample:
        file = templateBodyF.replace('TITLE', f'{work.Heading} {work.Name}') + '\n<table><tbody>'
        for k in work.Sheets.keys():
            file += f'\n<tr><td><a href="./{work.Name}{k}.html">{k}--{work.QGs[k][2]}</a></td></tr>'
        file +='</tbody></table></html>'
        open(os.path.join('.',f'{work.Name}',f'{work.Name}','index.html'), mode='w', encoding='utf-8').write(file)
        if k:
            webbrowser.open(os.path.join('.',f'{work.Name}',f'{work.Name}','index.html'))
        else:
            webbrowser.open(os.path.join('.',f'{work.Name}',f'{work.Name}',f'{work.Name}{k}.html'))
    else:
        file = templateBodyF.replace('TITLE', f'{work.Heading} {work.Name}') + '\n<table><tbody>'
        for k, Sname in work.STDs.items():
            file += f'\n<tr><td><a href="./{work.Name}{k}.html">{k}--{Sname}</a></td></tr>'
        file +='</tbody></table></html>'
        open(os.path.join('.',f'{work.Name}',f'{work.Name}','index.html'), mode='w', encoding='utf-8').write(file)





def mkHtmlFuncDisplayQ(qJ, txt, xtra=None, figures=None): # 2023-04-03 correctAnswer --> xtra
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
    if 'FIG%' in txt: # 직접 변경 가능
        for item in re.findall(figPattern, txt):
            itemStripped=item.strip()
            if itemStripped:
                figObjts.append(itemStripped)
                txt=txt.replace(f'FIG%{item}%FIG', '')

    if 'figure(' in txt: # 한 번 만든 것.. 직접 변경 불가능..
        for item in re.findall(figurePattern, txt):
            figureKey=item.strip()
            if figureKey and figureKey in figures:
                figObjts.append(figures[figureKey])
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
    else {newText += String.fromCharCode(13)+(q+1).toString()+": "+(answers[q]+1).toString();}
  }
  textarea.value = newText;
}

function handleClick(myRadio) {
  answers[parseInt(myRadio.name.slice(1))]=parseInt(myRadio.value);
  addAnswers2Textarea();
}

function setCheckedRadio(q) {
  var radios = document.getElementsByName('Q'+q.toString());
  //for (let j=0; j<radios.length; j++) {radios[j].removeAttribute("checked");}
  if (radios.length > 0 && answers[q] != null) {radios[answers[q]].setAttribute("checked", true);}
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
