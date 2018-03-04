# -*- UTF-8 -*-
'''
爬取bilibili专栏文章
'''
from urllib import request
from lxml import etree
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
url = 'https://frontendmasters.com/courses/javascript-foundations/'
#https://frontendmasters.com/courses/

url='https://www.bilibili.com/read/cv251299'
html_source = etree.HTML(request.urlopen(url).read().decode("utf-8"))

source = html_source.xpath('/html/body/div[2]/div[5]/p[3]/text()')
title = html_source.xpath('/html/body/div[2]/div[4]/div[2]/h1/text()')

path = 'BiliBili_Article/'
file_dir = path + "".join(title) + '''\\'''
if not os.path.exists(file_dir):
    os.makedirs(file_dir)
filename = file_dir + "".join(url.split("/")[-1:]) + '.py'
with open(filename, 'w', encoding="utf-8") as f:
    for i in source:
        if '\xa0' in i:
            i = i.replace("\xa0","")
        f.write(i+"\n")