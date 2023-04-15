import pickle, os, datetime

from ._common import round2MSF # scoreAnswerFiles.compare에서 사용.


class scoreAnswerFiles:

    def __init__(self, workPickle, path4files=None):
        self.ext='txt'
        self.path4files=path4files
        if workPickle and os.path.exists(workPickle):
            self.initWork(workPickle)
        else:
            print('We need the pickle fie')
            return

    def initWork(self, workPickle):
        self.work=pickle.load(open(workPickle,'rb'))
        self.WN=self.work.Name
        self.QGs=self.work.QGs
        self.Sheets=self.work.Sheets
        self.nProblems=len(self.QGs)

        if self.path4files and os.path.exists(self.path4files):
            try:
                self.getAnswersFromFiles()
            except Exception as err:
                print(err, '@ Ln25')
                return

            try:
                self.scoreThem()
            except Exception as err:
                print(err, '@ Ln31')
                return

            try:
                self.saveResults()
            except Exception as err:
                print(err, '@ Ln37')
                return
        else:
            print("we need the folder that students' answer text files are saved")
            return
                
            

    def getAnswersFromFiles(self):
        for r, v in enumerate(self.Sheets.values()):
            v['indexLB']=r # 필요함.
            v['file']='' # 답안지 파일 .pickle/.txt
            v['studAns']=[] # 정답은 v['Q&A'][1]에 있음.
            v['py']={} # 코드제출 python file 목록, 문제번호: (filename, func2bCalled object, 코드)
            v['msg']=''
            v['ox']=['X']*self.nProblems
            v['score']=0
            v['log']=[]

        self.getFiles() # just try to get the correct file names as ruled.
        self.readAnswers() # try to get the answer from the files


    def readAnswers(self):
        for sid, v in self.Sheets.items():
            if not v['file']: continue
            lines=self.txt2Answer(os.path.join(self.path4files,v['file'][0]))
            if isinstance(lines, str) and lines.startswith('readingError'):
                v['msg']=lines
                continue
            v['studAns']=lines

        for sid, v in self.Sheets.items():
            if not v['file']: continue
            if len(v['studAns'])<self.nProblems:
                v['studAns'].extend(['미제출']*(self.nProblems-len(v['Answer'])))
    


    def txt2Answer(self, txtPath):
        tenBytes=open(txtPath, 'rb').read(10)
        if b'\xff' in tenBytes:
            try:
                lines=open(txtPath, 'r', encoding='UTF-16-LE').readlines()
                lines=[line.split('\ufeff')[-1] if line.startswith('\ufeff') else line for line in lines]
            except:
                return 'readingError utf16LE'
        elif b'\xef' in tenBytes:
            try:
                lines=open(txtPath, 'r', encoding='UTF-8-SIG').readlines()
            except:
                return 'readingError utf8 bom'
        else:
            try:
                lines=open(txtPath, 'r', encoding='utf-8').readlines()
            except:
                try:
                    lines=open(txtPath, 'r', encoding='ansi').readlines()
                except:
                    return 'readingError UTF8/ANSI'

        answersFromTxt=['' for i in range(self.nProblems)]
        for line in lines:
            if not line.strip(): continue
            if '#' in line: continue
            if ':' not in line: continue
            hdr, *hdrValue=line.strip().split(':')
            hdr=hdr.strip()
            hdrValue=':'.join(hdrValue)
            if hdr.isnumeric() and int(hdr)<=self.nProblems and hdrValue:
                try:
                    answersFromTxt[int(hdr)-1]=eval(hdrValue)
                except SyntaxError: # 2023-04-14 added
                    answersFromTxt[int(hdr)-1]=hdrValue.strip() # 2023-04-14 added
                except Exception as err:
                    answersFromTxt[int(hdr)-1]=f'Error({err}) in ({hdrValue}) @ Ln90'

        return answersFromTxt


    def getFiles(self):
        fileList=[f for f in os.listdir(self.path4files) if 'Scores' not in f and f.endswith(self.ext)]
        mtime=[str(datetime.datetime.fromtimestamp(os.stat(self.path4files+f'/{f}').st_mtime))[5:] for f in fileList]
        sortingIndex=sorted(range(len(mtime)), key=mtime.__getitem__, reverse=True)

        for sid, v in self.Sheets.items():
            for j in sortingIndex:
                if sid in fileList[j] and self.WN in fileList[j]:
                    self.Sheets[sid]['file']=(fileList[j], mtime[j],
                                              os.stat(os.path.join(self.path4files,fileList[j])).st_size)
##                    if mtime[j]>late:
##                        self.Sheets[sid]['msg']='late(0)'
                    break

        for v in self.Sheets.values():
            if not v['file'] and not v['msg']:
                v['msg']='no submission(0)'

        
    def scoreThem(self):
        for sid, v in self.Sheets.items():
            if not v['file'] or v['msg']: continue
            for nChecked, (wv, ans0) in enumerate(zip(v['studAns'], v['Q&A'])):
                if isinstance(wv, str) and 'Error' in wv:
                    v['ox'][nChecked] = 'X'+wv
                    continue
                if wv is None:
                    v['ox'][nChecked] = 'Xanswer is None'
                    continue
                
                ans2match=ans0[1]
                if isinstance(ans2match, dict) and ('ret' in ans2match): # 코드제출
                    if isinstance(v['py'][nChecked][2], str):
                        v['ox'][nChecked] = self.compare(v['py'][nChecked][2], ans2match['ret'])
                    else:
                        try:
                            wv=evalPyCode(ans2match, v['py'][nChecked][2])
                        except Exception as err:
                            v['ox'][nChecked]='X'+f'Error({err})'
                            continue
                        v['ox'][nChecked] = self.compare(wv, ans2match['ret'])

                elif isinstance(ans2match, str) and ans2match.startswith('code:'):
                    if self.checkAnswerCode(wv, ans2match.split('code:')[-1]): # 반환값: T/F 2023-04-15 self.추
                        v['ox'][nChecked] = 'O'
                    else:
                        v['ox'][nChecked] = 'Xincorrect arb. value'

                else:
                    v['ox'][nChecked] = self.compare(wv, ans2match)

            v['score']=sum(10 if c[0]=='O' else 5 if c[0]=='5' else 3 if c[0]=='3' else 0 for c in v['ox'])


    def saveResults(self):
        QG=self.QGs
        sheets=self.Sheets
        path4files=self.path4files
        WN=self.WN
        CAR={q:[0,0] for q in range(len(QG))} # 질문지에 사용된 질문-군 목록
        log={}

        for sid,v in sheets.items():
            if not v['file']: continue
            for ox, q in zip(v['ox'], v['orders']):
                CAR[q][0] +=1
                if ox=='O': CAR[q][1] += 1
            if v['log']:
                log[sid]=v['log']

        YESCAR=False if any(not carV[0] for carV in CAR.values()) else True

        # 예전에 저장한 파일 이름 변경...    
        if os.path.exists(os.path.join(path4files,f'{WN}Scores.txt')):
            fileList=sorted([f for f in os.listdir(path4files) if 'Scores' in f], reverse=True)
            for f in fileList:
                if '_' in f:
                    front, rear=f.split('_')
                    rear, ext=rear.split('.')
                    newf=front+f'_{int(rear)+1:02d}.'+ext
                else:
                    front, ext=f.split('.')
                    newf=front+'_01.'+ext
                os.rename(os.path.join(path4files,f), os.path.join(path4files,newf))

        try:
            with open(path4files+'\\'+WN+'Scores.txt','w') as f:
                for sid, v in sheets.items():
                    if v['msg']:
                        f.write(sid+f'__{v["msg"]}\n')
                    else:
                        f.write(sid+f'__{v["ox"]}({v["score"]})\n')
                        for jj, ox in enumerate(v['ox']):
                            if ox == 'X':
                                f.write(f'\t{jj+1}: ({ox})\n')
                
                if log:
                    f.write('\n---Error messages---\n')
                    for k in sorted(log.keys()):
                        f.write(f'{k} -- {log[k]}\n')
 
                if CAR and YESCAR:
                    f.write('\n---질문별 정답율---\n')
                    for k in sorted(CAR.keys()):
                        if CAR[k][0]:
                            f.write(f'{k} -- {CAR[k]}, {round(CAR[k][1]*100/CAR[k][0],1)}\n')
                        else:
                            f.write(f'{k} -- {CAR[k]}\n')


        except PermissionError:
            return 'Error -- text file is open.\nPlease close the file and try again'
        except Exception as err:
            return f'Error({err}) in Saving scores.', CAR
        

        try:
            import csv
            with open(path4files+'\\'+WN+'Scores.csv','w', newline='') as f:
                csvwriter=csv.writer(f, delimiter=',')
                for sid, v in sheets.items():
                    if v['msg']:
                        csvwriter.writerow([sid,v['msg'],0])
                    else:
                        csvwriter.writerow([sid, ''.join([s[0] for s in v["ox"]]), v["score"]])
            
            return 'Saving the scores to csv file is OK', CAR
        except PermissionError:
            return 'Error -- csv file is open.\nPlease close the file and try again', CAR
        except Exception as err:
            return f'Error in Saving csv file\nwith {err}\n@ {item}'
            

    @staticmethod
    def compare(A, B): # self.scoreThem에서 사용
        '''A: 학생답, B: 정답'''
        if A is None:
            return 'XNo answer'
        elif type(A) == type(B):
            if A == B:
                return 'O'
            elif isinstance(B, float):
                if round2MSF(A) == round2MSF(B):
                    return 'O'
                else:
                    #print(round2MSF(A), round2MSF(B))
                    return 'Xrounding error'
            else:
                #print(f'학생답: ++{A}++', type(A)) # 2023-04-14 added
                #print(f'정답: ++{B}++', type(B)) # 2023-04-14 added
                return 'Xwrong Answer'
        else:
            return 'Xwrong type'


    @staticmethod
    def checkAnswerCode(StudentValue, ansCode):  # 2023-04-14 added incomplete
        try:
            tmp=eval(ansCode)
        except Exception:
            tmp=False
        return tmp

