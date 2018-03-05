'''
目标网址：https://tieba.baidu.com/index.html
程序目的：批量签到
时间：2018-2-23
作者：刘宇
V：1.0
'''
import urllib.request
import urllib.parse
import re
import json
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
  "Cookie": "",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}
def SignAdd(kw,tbs_data):
  url = "https://tieba.baidu.com/sign/add"
  post_data = {
    "ie": "utf-8",
    "kw": kw,
    "tbs": tbs_data,
  }
  data = urllib.parse.urlencode(post_data).encode("utf-8")
  post_req = urllib.request.Request(url=url, data=data, headers=headers)
  try:
    return (kw,json.loads(urllib.request.urlopen(post_req).read().decode("utf-8"))["data"]["errmsg"])
  except:
    return (kw,"faild")
forum_list = re.findall('"forum_id":(.*?),"forum_name":"(.*?)"',urllib.request.urlopen(urllib.request.Request(url="https://tieba.baidu.com/index.html",headers=headers)).read().decode())
for eve_forum in forum_list:
  kw = eve_forum[1].encode('latin-1').decode("unicode_escape")
  forum_url = "https://tieba.baidu.com/f?kw=" + urllib.parse.quote(kw)
  # time.sleep(3)
  # tbs_data = re.findall('\'tbs\': "(.*?)" ',urllib.request.urlopen(urllib.request.Request(url=forum_url,headers=headers)).read().decode("utf-8"))[0]
  print(kw)
  # print(" - ".join(SignAdd(kw,tbs_data)))
