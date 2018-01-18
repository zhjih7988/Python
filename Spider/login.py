# -*- UTF-8 -*-
#telephone=free&password=surfree33333&action=login
import requests
url = 'http://cs.zaza666.com/Center/login.html?flag=hidden'
data = {
    "telephone" : "",
    "password" : "",
    "action" : "login"
}
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    r = requests.get(url, headers=headers,data=data)
    print(r.text)
except expression as identifier:
    print(identifier)