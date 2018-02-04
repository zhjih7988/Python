# coding: utf-8
import re
from MyFun import SaveToHtml
# Python的标准库linecache模块非常适合这个任务
import linecache
# linecache读取并缓存文件中所有的文本，

url = "http://www.xunleicang.com/vod-read-id-2038.html"
#SaveToHtml(url,'op.html')

p = 'thunder:.+?"' #正则表达式
pattern = re.compile(p) #编译
result = []
line_number = 0
tmp = ''
start = ''
end = ''

file_object = open('op.html',encoding="utf-8")
try: 
  for line in file_object:
    line_number += 1
    for i in range(0, 999):
        '''爬取li4_0-li4_76的链接  最新的链接'''
        '''li2_0-li4_999  更改rang(0,999)即可'''
        s = 'li4_' + str(i)
        if s in line:
          tmp = linecache.getline('op.html',line_number+1)
          if start:
            end = linecache.getline('op.html',line_number+2)
          else:
            start = linecache.getline('op.html',line_number+2)
          if(re.findall(pattern,tmp)[0]):
            result.append(re.findall(pattern,tmp)[0])
          break
finally:
  file_object.close()

title = start.strip()[5:-5]+"-"+end.strip()[5:-5]
with open(title+'.txt','w',encoding="utf-8") as fw:            #with方式不需要再进行close
  for r in result:
    fw.write(r+'\n')                 #保存入结果文件