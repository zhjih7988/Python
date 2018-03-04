# -*- UTF-8 -*-
'''
爬取bilibili专栏文章
'''
from MyFun import etreeHTML
import os
# url = 'https://frontendmasters.com/courses/javascript-foundations/'
# https://frontendmasters.com/courses/

def Clawer(url):
    html_source = etreeHTML(url,"Utf-8")
    source = html_source.xpath('/html/body/div[2]/div[5]/p/text()')
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
            f.write(i + "\n")

if __name__ == '__main__':
    filename = "input.txt"
    http = 'https://www.bilibili.com/read/cv'
    # url = 'https://www.bilibili.com/read/cv251313'
    # Clawer(url)
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                url = http + line.strip('\n')
                print(url + " ...")
                Clawer(url)