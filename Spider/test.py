# -*- UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import os, re
import threading

exe_Count = 1
aList = []
url = "http://www.xunleicang.com/vod-read-id-2038.html"
directoryPath = "./OnePiece"


try:
    listAvalue = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    rep = request.Request(url, headers = headers)
    response = request.urlopen(rep, timeout = 5000)
    soup = BeautifulSoup(response, 'html.parser')
    soup.prettify()
    # print(soup)
    # 获取a标签href 属性并写入list
    # li id="li4_0" --> li4_73
    s = "li4_0"
    # for li in soup.find_all("li"):
    #     print(li.get("id"))
    #     if li.get('id') == s:
    #         str = li.contents
    #         # print(str[0].get('href'))
    for i in range(1, 74),:
        s = "li4_" + i.__str__()
        # print(s)

    #for a in soup.find_all("a"):
    #     if a.string == "海贼王-第747集.mp4":
    #         print(a)
    #         print(a.get('href'))
    # 创建不存在的目录
    if not os.path.exists(directoryPath):
        os.mkdir(directoryPath)
        print("新目录：" + directoryPath)
except:
    print("Error")