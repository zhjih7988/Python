# -*- UTF-8 -*-
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def login():
    #验证码
    response = requests.get('https://www.douban.com/j/misc/captcha',headers=headers)
    result = response.json()
    captcharUrl = 'https:' + result['url']
    captcharToken = result['token']
    response = requests.get(captcharUrl, headers=headers)
    codeImg = response.content
    fn = open('code.png', 'wb')
    fn.write(codeImg)
    fn.close()
    return
    data = {
        'source':'index_nav',
        'form_email':'6407049@qq.com',
        'form_password':'123456..',
    }
    response = requests.post('https://www.douban.com/accounts/login', data=data, headers=headers)
    print(response.text)

login()