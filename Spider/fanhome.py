#coding: utf-8
import urllib.request
from lxml import etree
import os
import socket

url = 'http://www.fanhome.info/lei/%E8%BF%9E%E8%A3%A4%E8%A2%9C'

# 根据首页获得该分类的总页数
x_p = '/html/body/div[1]/div/div[1]/ul/li[11]/a/text()'
page_total = etree.HTML(urllib.request.urlopen(url).read().decode("utf-8")).xpath(x_p)
page_total = int((str(page_total[0]).replace(".","")).strip())
# page_total = page_total.replace(" ",'')
print(page_total)
for o in range(page_total):
    surl = url + "/" + str(o+1) + ".htm"
    print(str(o+1) + "..." + url)
    # 获得网页源代码
    page_source = etree.HTML(urllib.request.urlopen(surl).read().decode("utf-8"))
    # # 提取出每个页面中全部的内容
    start = '/html/body/div[1]/div/div[1]/div/table/tbody/tr[' 
    for i in range(40):
        s = start + str(i+1) +']/td[1]/a/text()' 
        lei = page_source.xpath(s)
        with open('./input.txt',"a") as f:
            f.write(str(lei[0])+'\n')

# 进入分类的全部页码，进行数据获取
# for eve_content_list_page in range(1, page_total +1):
#     # 每个页面的数据
#     surl = url + "/" + str(eve_content_list_page) + ".htm"
#     print(str(eve_content_list_page) +"..." + url)
#     # 获得网页源代码
#     page_source = etree.HTML(urllib.request.urlopen(surl).read().decode("utf-8"))
#     # # 提取出每个页面中全部的内容
#     start = '/html/body/div[1]/div/div[1]/div/table/tbody/tr[' 
#     for i in range(40):
#         s = start + str(i+1) +']/td[1]/a/text()' 
#         print(s)
#         lei = page_source.xpath(s)
#         print(lei)
    # content_list = page_source.xpath('/html/body/div[1]/div/div[1]/div/table/tbody/tr[1]/td[1]/a')
    # /html/body/div[1]/div/div[1]/div/table/tbody/tr[2]/td[1]/a
    # /html/body/div[1]/div/div[1]/div/table/tbody/tr[40]/td[1]/a
    
    # # 根据不同内容，进行数据下载
    # for eve_content in content_list:
    #     try:
    #         pass
    # #         # 打开文件url，并以二进制存储到本地指定的文件夹下，文件命名用title
    # #         with open(eve_list_data + "/" + title + ".zip","wb") as f:
    # #             f.write(urllib.request.urlopen(file_url).read())
    # #         # 输出完成的内容
    # #         print(eve_list_data,title)
    #     except Exception as e:
    #         print(e)