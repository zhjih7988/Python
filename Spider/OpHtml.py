# -*- UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import os, re
exe_Count = 1
aList = []
url = "http://www.xunleicang.com/vod-read-id-2038.html"

def main():
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
        with open('op.html','w',encoding="utf-8") as fw:
            fw.write(soup.prettify())
    except:
        print("Error")

if __name__ == '__main__':
    main()