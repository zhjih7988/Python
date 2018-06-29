# -*- UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup

def getHtmlSoup(Url):
    '''
    get Url Response
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    rep = request.Request(Url, headers = headers)
    response = request.urlopen(rep, timeout = 5000)
    soup = BeautifulSoup(response, 'html.parser')
    return soup.prettify()

def SaveToHtml(Url, Path=""):
    '''
    解析Url,存成html,返回soup
    '''
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }
        rep = request.Request(Url, headers = headers)
        response = request.urlopen(rep, timeout = 5000)
        soup = BeautifulSoup(response, 'html.parser')
        soup.prettify()
        with open(Path,'w',encoding="utf-8") as fw:
            fw.write(soup.prettify())
    except:
        print("Error")


if __name__ == '__main__':
    SaveToHtml('','')