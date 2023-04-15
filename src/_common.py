import math, random, re, json
from urllib.request import urlopen
import urllib

def getFigure(file: str):
    try:
        return json.loads(urlopen(f'https://generateNscore.github.io/html4quiz/JS/{file}.json').read())
    except urllib.error.HTTPError:
        return 'HTTP Error 404: Not Found'


def getResource(src: str):
    try:
        return json.loads(urlopen(f'https://generateNscore.github.io/html4quiz/res/{src}.json').read())
    except urllib.error.HTTPError:
        return 'HTTP Error 404: Not Found'


def round2MSF(a):
    if not a or (isinstance(a, int) and abs(a)<1000) : return a

    sfN=3
    signFlag=False
    if a<0: a=-a; signFlag=True
    n=int(math.log10(a))
    if a>1: n +=1
    b=round(a*10**(-n), sfN) # floating number 0.1<b<1
    if signFlag: b *= -1
    
    ans=eval(f'{round(b,3)}e{n}')
    if str(ans).endswith('.0') or str(ans).endswith('.00'): ans=int(ans)
    return ans


def getStudList(csvName: str='', header4SID: str='', header4Name: str=''):
    '''Usage: getStudList('csvName.csv', 'ID', 'Name')'''
    import csv
    if not csvName or not csvName.endswith('.csv') or not csvName.split('.csv')[0]:
        return 'Error: no csv file name'

    if not header4SID:
        return 'Error: no column header for student IDs'

    if not header4Name:
        return 'Error: no column header for student names'

    try:
        with open(csvName) as csvFile:
            csvData=[row for row in csv.reader(csvFile, delimiter=',')]
    except UnicodeDecodeError:
        with open(csvName, encoding='UTF-8') as csvFile:
            csvData=[row for row in csv.reader(csvFile, delimiter=',')]
    except Exception as err:
        return f'Error: reading error, contact me, {err}'

    if not csvData:
        return 'Error: Failed reading in student list'
        
    Headers = [item.replace('\ufeff', '').strip() if item.startswith('\ufeff') else item.strip() for item in csvData[0]]
    if not all([len(item)==len(Headers) for item in csvData[1:]]):
        return 'Error: Incosistency in columns'

    if header4SID in Headers:
        iPIN=Headers.index(header4SID)
    else:
        return f'Error: no column for {header4SID}'
    
    if header4Name in Headers:
        iName=Headers.index(header4Name)
    elif f'\ufeff{header4Name}' in Headers:
        iName=Headers.index(f'\ufeff{header4Name}')
    else:
        return f'Error: no column for {header4Name}'

    listSN={item[iPIN].strip(): item[iName].strip() for item in csvData[1:] if item[iPIN].strip()}

##    for k,v in listSN.items():
##        if '\n' in v: listSN[k]=v.replace('\n','_')

    return listSN

if __name__=='__main__':
    print(getStudList('../출석부.csv','학번','학생명'))

