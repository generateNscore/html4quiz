import html4quiz as h4q

resources={'playWithNumbers': h4q._common.getResource('playWithNumbers')}
resources['WordWizardVocabList6-8']=h4q._common.getResource('WordWizardVocabList6-8')

QGs = []

Q=['Find the word that means the following (Vocabulary source: <a href="https://fefonline.org/coe/WordWizardVocabList6-8.pdf">WordWizardVocabList6-8</a>):<p><font color="#00f">"{%wordmeaning%}"</font></p>']

A='''global typeInQ, wordL
data=[]
words=resources['WordWizardVocabList6-8']
types={'n': [4, 5, 6, 7, 8, 9, 10], 'adj':[5, 6, 7, 8, 9, 10], 'v':[6, 7, 8, 9, 10]}
typeInQ=random.choice(list(types.keys()))
wordL=random.choice(types[typeInQ])
wordChoices=random.sample([w for w,v in words.items() if v[0] == typeInQ and len(w)==wordL], 5)
word = random.choice(wordChoices)
wordmeaning=words[word][1]
answer=[{'choices': wordChoices, 'ans': word}]'''

QGs.append([Q, A, ('Examples', 'Nk001-1'), 'short'])


Q=['Move the alphabet shown below to complete a word that means the following. When finished, click the "Submit" button. (Vocabulary source: <a href="https://fefonline.org/coe/WordWizardVocabList6-8.pdf">WordWizardVocabList6-8</a>):<p><font color="#00f">"{%wordmeaning%}"</font></p>figure(playWithNumbers)init({%prms%});']

A='''global typeInQ, wordL
data=[]
words=resources['WordWizardVocabList6-8']
types={'n': [4, 5, 6, 7, 8, 9, 10], 'adj':[5, 6, 7, 8, 9, 10], 'v':[6, 7, 8, 9, 10]}
typeInQ=random.choice(list(types.keys()))
wordL=random.choice(types[typeInQ])
word=random.choice([w for w,v in words.items() if v[0] == typeInQ and len(w)==wordL])
wordmeaning=words[word][1]
answer=[word]
vStr=list(answer[0])
random.shuffle(vStr)
columnsN=len(vStr)+3
prms=[[50, 1400], [columnsN, 1], vStr, 'shuffle']'''

QGs.append([Q, A, ('Examples', 'Nk001-2'), 'short'])

Q=['Find the correct meaning for the word <font color="#00f">"{%word[0]%}"</font>. (Vocabulary source: <a href="https://fefonline.org/coe/WordWizardVocabList6-8.pdf">WordWizardVocabList6-8</a>)']

A='''global typeInQ, wordL
data=[]
words=resources['WordWizardVocabList6-8']
wordChoices=random.sample([(w, v[1]) for w,v in words.items() if 10<=len(v[1])<=30], 5)
word = random.choice(wordChoices)

answer=[{'choices': [v[1] for v in wordChoices], 'ans': word[1]}]'''

QGs.append([Q, A, ('Examples', 'Nk001-3'), 'short'])


flagPreview = False
flagChoice = True
flagShuffling = True

STDs={'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
h4q.work('Nk003', 'Example', STDs, QGs, flagPreview, flagChoice, flagShuffling, resources)
