# -*- UTF-8 -*-
from urllib import request
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
url = 'https://frontendmasters.com/courses/javascript-foundations/'
#https://frontendmasters.com/courses/
url = 'http://www.5a5x.com'

url='https://www.bilibili.com/read/cv251299'
html_source = etree.HTML(request.urlopen(url).read().decode("utf-8"))
source = html_source.xpath('/html/body/div[2]/div[5]/p[2]')[0]
print(source)