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


url = "https://www.javbus.cc/KMI-064"

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
ret = res.read().decode("utf-8")

# x_p = r'onclick="window.open(\'(.*?)\'\,\'_self\')\">'
x_p='<table id="magnet-table" class="table table-condensed table-striped table-hover" style="margin-bottom:0;">.*?(.*?) </table>'
x_p='<a style="color:#333".*? href="(.*?)">.*?</a>'
magnetCode = re.findall(x_p, ret, re.S)
print(magnetCode)