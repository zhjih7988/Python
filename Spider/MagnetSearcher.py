#coding = utf-8
import re
import base64
from urllib import parse
from urllib import request
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def strDecode(uriCode):
    a = re.sub('[+"]', '', uriCode)
    b = parse.unquote(a)
    c = re.compile(r'<[^>]+>',re.S)
    str = c.sub('', b)
    return str

def getInfo(word):
    bytesKeyWord = word.encode(encoding="utf-8")
    decodeWord = base64.b64encode(bytesKeyWord)
    keyCode = decodeWord.decode()

    urlPart1 = "http://www.btwhat.info/search/b-"
    urlPart2 = keyCode + "/"
    urlPart4 = "-3.html"

    for pageNum in range(1, 2):
        url = urlPart1+urlPart2+str(pageNum)+urlPart4
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        ret = res.read().decode("utf-8")

        itemTitleCode = re.findall(r'<div class="item-title">.*?decodeURIComponent\((.*?)\)\);', ret, re.S)
        magnetCode = re.findall(r'<div class="item-title">.*?<a href="/wiki/(.*?).html" target', ret, re.S)
        fileType = re.findall(r'<span class=\"cpill.*?\">(.*?)</span>', ret, re.S)
        fileSize = re.findall(r'<div class="item-bar">.*?File Size.*?<b.*?>(.*?)</b>', ret, re.S)

        titleList = []
        fileTypeList = []
        fileSizeList = []
        magnetList = []

        itemAmount = len(itemTitleCode)

        with open('STorrent.txt', 'a', encoding="utf-8") as f:
            for m in range(itemAmount):

                itemTitle=strDecode(itemTitleCode[m])
                titleList.append(itemTitle)
                fileTypeList.append(fileType[m])
                fileSizeList.append(fileSize[m])
                magnetPart1 = "magnet:?xt=urn:btih:"
                magnetPart2 = magnetCode[m]
                magnet = magnetPart1+magnetPart2
                magnetList.append(magnet)

                title = "".join(titleList[m])
                magnet = "".join(magnetList[m])
                type = "".join(fileTypeList[m])
                size = "".join(fileSizeList[m])

                print("\r")
                print("资源名称：" + title)
                print("资源类型：" + type)
                print("资源大小：" + size)
                print("磁力链接：" + magnet)
                print("\r")
                f.write(magnet + '\n')

if __name__ == '__main__':
    filename = "input.txt"
    with open('STorrent.txt', 'w', encoding="utf-8") as f:
        f.write("")
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                word = line.strip('\n')
                print(word+" ...")
                getInfo(word)