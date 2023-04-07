import hf4q

a=hf4q.scoreAnswerFiles('K0322c/K0322cWork.pickle', 'K0322c/K0322c_txt')
a.scoreThem()
a.saveResults()
