'''
目标网址：http://k.360kan.com/pc/list#nogo
软件目的: 模拟登陆
时间：2018-2-24
作者：liuyu
V：1.0
'''
import urllib.parse
import urllib.request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def md5(str):
  import hashlib
  m = hashlib.md5()
  m.update(str)
  return m.hexdigest()
account = input("请输入账号：")
password = input("请输入密码：")
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}
token_url = "https://login.360.cn/?func=jQuery18309117734812244078_1519434087078&src=pcw_svideo&from=pcw_svideo&charset=UTF-8&requestScema=https&o=sso&m=getToken&userName="+account+"&_=1519435974154"
token_data = re.findall('"token":"(.*?)"',urllib.request.urlopen(urllib.request.Request(url=token_url,headers=headers)).read().decode("utf-8"))[0]
login_url = "https://login.360.cn/"
post_data = {
  "src":"pcw_svideo",
  "from":"pcw_svideo",
  "charset":"UTF-8",
  "requestScema":"https",
  "o":"sso",
  "m":"login",
  "lm":"0",
  "captFlag":"1",
  "rtype":"data",
  "validatelm":"0",
  "isKeepAlive":"1",
  "captchaApp":"i360",
  "userName":account,
  "smDeviceId":"",
  "type":"normal",
  "account":account,
  "password":md5(password.encode("utf-8")),
  "captcha":"",
  "token":token_data,
  "proxy":"http://k.360kan.com/psp_jump.html",
  "callback":"QiUserJsonp434087168",
  "func":"QiUserJsonp434087168",
}
print(urllib.parse.unquote(urllib.request.urlopen(urllib.request.Request(url=login_url,data=urllib.parse.urlencode(post_data).encode("utf-8"),headers=headers)).read().decode("utf-8")))
