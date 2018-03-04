'''
目标网址：http://k.360kan.com
软件目的: 视频采集
时间：2018-2-23
作者：liuyu
V：1.0
'''
import urllib.request
import json
import re
url = "http://pc.k.360kan.com/pc/list?n=10&p=3&f=json&ajax=1&uid=2a3e0fc71c8bbf9bf72302647c7a63e4&channel_id=2&dl="
for eve in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["data"]["res"]:
  title = eve["t"]
  username = eve["f"]
  id_data = re.findall("detail/(.*?)\?",eve["u"])[0]
  content_url = "http://pc.k.360kan.com/pc/play?id=" + id_data
  video_url = json.loads(urllib.request.urlopen(content_url).read().decode("utf-8"))["data"]["url"]
  with open(title + ".mp4", "wb") as f:
    f.write(urllib.request.urlopen(video_url).read())
