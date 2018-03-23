import re
num=['零','一','二','三','四','五','六','七','八','九']
key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k=['十','百','千','万']
def getNum(s=""):
    if s not in num:
        AA = 10
    else:
        AA = num.index(s)
    return AA
def getNumber(strNum):
    Num = re.findall(r'第(.*?)课', strNum, re.S)
    if len(Num[0]) == 1: # 十以内
        AA = getNum(Num[0])
    elif len(Num[0]) == 2: # 二十以内
        if Num[0][:1] in k[0]: # 十
            AA = 10
        the = Num[0][-1:]
        AA = AA+getNum(the)
    out = re.sub(r'.(?=课)', str(AA), strNum)
    return out


print(getNumber('第十二课'))