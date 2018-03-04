本文档仅作为视频学习过程中的参考
不可用于非法途径
'''
目标网址：http://cjcx.neea.edu.cn/html1/folder/1508/206-1.htm?sid=280
爬取目标：识别验证码，获得结果
时间：2018-2-25
作者：刘宇
V:1.0
'''
import urllib.request
import urllib.parse
def getHeaders(temp_data=""):
  headers = {
    "Cookie": "Hm_lvt_dc1d69ab90346d48ee02f18510292577=1519519634; UM_distinctid=161ca6d94bf38e-04db895cea8111-32697a04-1aeaa0-161ca6d94c0e29; esessionid=4D636D42A99527D6D9E83612C981F892; BIGipServersearchtest.neea.edu.cn_search.neea.cn_pool=1923139594.37407.0000; language=1; Hm_lpvt_dc1d69ab90346d48ee02f18510292577=1519521069; " + temp_data,
    "Host": "search.neea.edu.cn",
    "Pragma": "no-cache",
    "Referer": "http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryCond&sid=280&pram=results&ksnf=2Ba049ynilaf8I9J7JxJnIu&sf=11&bkjb=1&zkzh=&name=%E5%88%98%E5%AE%87&sfzh=200000000000000000",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
  }
  return headers
image_pic = "http://search.neea.edu.cn/Imgs.do?act=verify&t=0.18753489364159748"
image_data = urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders()))
with open("verify.png", "wb") as f:
  f.write(image_data.read())
verify = input("Please input verify:")
post_url = "http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryResults"
post_data = {
  "pram": "results",
  "ksxm": "280",
  "nexturl": "/QueryMarkUpAction.do?act=doQueryCond&sid=280&pram=results&ksnf=2Ba049ynilaf8I9J7JxJnIu&sf=11&bkjb=1&zkzh=&name=刘宇&sfzh=200000000000000000",
  "ksnf": "2Ba049ynilaf8I9J7JxJnIu",
  "sf": "11",
  "bkjb": "1",
  "zkzh": "",
  "name": "刘宇",
  "sfzh": "200000000000000000",
  "verify": verify,
}
print(urllib.request.urlopen(urllib.request.Request(url=post_url,data=urllib.parse.urlencode(post_data).encode("utf-8") , headers=getHeaders(image_data.headers["Set-Cookie"]))).read().decode("utf-8"))
