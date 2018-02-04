# coding: utf-8
from lxml import html
from MyFun import SaveToHtml, getHtmlSoup
import os
import re
tmp = '2.html'
def main():
    parameter = '002'
    savepath = 'STorrent.txt'
    Url = 'http://torrentkitty.kim/tk/'+ parameter +'/1-1-0.html'
    print(Url)
    # SaveToHtml(Url,tmp)
    soup = getHtmlSoup(Url)
    p = 'list">(.*?)' #正则表达式
    print(p)
    pattern = re.compile(p) #编译
    print(re.findall(pattern,soup))

if __name__ == '__main__':
    main()
# page = html.parse(path)
# # 直接定位到<h1 class="heading">Top News</h1>
# list_reg = '//div[@class="list"]/p//*'
# div_list = page.xpath(list_reg)
# # print(div_list)
# for i in div_list:
#     print(i.tag)
