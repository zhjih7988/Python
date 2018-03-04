# -*- UTF-8 -*-
'''
功能：爬取bilibili专栏文章
参数: Url
V：1.0
'''
from urllib import request
from lxml import etree
import os
import re
from MyFun import listToStr,getHtmlSoup

def clawer(url):
    path = 'BiliBili_Article/'
    userID = re.findall("bilibili.com/(.*?)#",url)
    # 建立该用户的文件夹
    if not os.path.exists(path):
        os.makedirs(path + listToStr(userID))
    # html_source = getHtmlSoup(url) 
    html_source = request.urlopen(url).read().decode("UTF-8")
    my_xpath = '//*[@class="be-pager-total"]/text()'
     # 根据首页获得该分类的总页数
    page_total = etree.HTML(html_source).xpath(my_xpath)
    print(html_source)
    print(page_total)


if __name__ == '__main__':
    url = 'https://space.bilibili.com/35850273#/article'
    clawer(url)