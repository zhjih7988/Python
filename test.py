# -*- coding:utf-8 -*-
# https://github.com/rg3/youtube-dl/blob/master/README.md#readme
# Regular Expression 
'''
. 代表任何一个字符（包括它本身）
+ 前面一个字符或一个子表达式重复一遍或者多遍
* 匹配到它0次或多次
[]代表匹配里面的字符中的任意一个

[0-9]	0123456789任意之一
[a-z]	小写字母任意之一
[A-Z]	大写字母任意之一
\d	等同于[0-9]
\D	等同于[^0-9]匹配非数字
\w	等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
\W	等同于[^a-z0-9A-Z_]等同于上一条取非
'''
import re

def main():
    str = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
    p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
    pattern1 = re.compile(p1)#我们在编译这段正则表达式
    
    print(pattern1.findall(str))
    matcher1 = re.search(pattern1,str)#在源文本中搜索符合正则表达式的部分
    print(matcher1.group(0))#打印出来

    key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
    p1 = r"chuxiuhong@hit\.edu\.cn"
    pattern1 = re.compile(p1)
    print(pattern1.findall(key))


if __name__ == '__main__':
    main()
