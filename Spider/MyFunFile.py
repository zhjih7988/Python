import re
num=['零','一','二','三','四','五','六','七','八','九']
key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k=['十','百','千','万']
def getTen(s):
    if s not in num:
        AA = 10
    else:
        AA = num.index(s)
    return AA

def getNumber(strNum):
    '''
    将中文的数字改成纯数字
    '''
    Num = re.findall(r'第(.*?)[课|讲|节]', strNum, re.S)
    try:
        if len(Num[0]) == 1: # 十以内
            AA = getTen(Num[0])
        elif len(Num[0]) == 2: # 二十以内
            if Num[0][:1] in k[0]: # 十
                AA = 10
                the = Num[0][-1:]
            AA = AA + getTen(the)
    except (IndexError, ValueError):
        return
    finally:
        pass
    out = re.sub(r'[^?=第].*(?=课|讲|节)', str(AA), strNum)
    return out

# print(getNumber('第十课_自动摘要及正文抽取'))