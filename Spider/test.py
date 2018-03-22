import re
num=['零','一','二','三','四','五','六','七','八','九']
k=['十','百','千','万']

strNum = '第九课XXXXX'
Num = re.findall(r'第(.*?)课', strNum, re.S)

if len(strNum[0]) == 1:
    if Num[0] not in num:
        AA = 10
    else:
        AA = num.index(Num[0])

print(AA)

pattern = '.*?课'
out = re.sub(pattern, str(AA), strNum)
print(out)


# regex = re.findall(r'第(.*?)课', strNum, re.S)
# # 替换所有匹配的子串用newstring替换subject中所有与正则表达式regex匹配的子串
# result, number = re.subn(regex, Num, strNum)
# print(result,number)