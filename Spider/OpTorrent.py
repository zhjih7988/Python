# id="s4p0" --> s4p72
import re
from OpHtml import main
# Python的标准库linecache模块非常适合这个任务
import linecache
# linecache读取并缓存文件中所有的文本，


main()

p = 'thunder:.+?"' #正则表达式
pattern = re.compile(p) #编译
result = []
file_object = open('op.html',encoding="utf-8")
line_number = 0
tmp = ''
try: 
  for line in file_object:
    line_number += 1
    for i in range(0, 77):
        s = 'li4_' + str(i)
        if s in line:
          tmp = linecache.getline('op.html',line_number+1)
          if(re.findall(pattern,tmp)[0]):
            result.append(re.findall(pattern,tmp)[0])
          break
finally:
  file_object.close()


with open(r'OpTorrent.txt','w',encoding="utf-8") as fw:            #with方式不需要再进行close
  for r in result:
    fw.write(r+'\n')                 #保存入结果文件