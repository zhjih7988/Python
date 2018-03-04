本文档仅作为视频学习过程中的参考
不可用于非法途径
'''
编程目的：编写微信机器人
时间：2018-2-25
作者：刘宇
V:1.0
'''
import urllib.request
import urllib.parse
import json
import itchat
# 自动聊天
def autoChat(input_data,userid):
  api_url = "http://www.tuling123.com/openapi/api"
  post_data = {
    "key": "",
    "info": input_data,
    "loc": "北京市中关村",
    "userid": userid,
  }
  re_content = json.loads(urllib.request.urlopen(urllib.request.Request(url=api_url,data=urllib.parse.urlencode(post_data).encode("utf-8"))).read().decode("utf-8"))["text"]
  return re_content
# 自动回复
@itchat.msg_register('Text', isGroupChat=False)
def text_reply(msg):
  content = msg["Content"]
  fromuser = msg["FromUserName"]
  message = autoChat(content,fromuser)
  itchat.send(message,fromuser)
  # itchat.send(content,我们自己的现在用的微信id)
itchat.login()
itchat.run()
