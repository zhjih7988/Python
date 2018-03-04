本文档仅作为视频学习过程中的参考
不可用于非法途径
'''
目标网址：http://image.baidu.com/?fr=shitu
程序目的：实现百度识图
时间：2018-2-25
作者：刘宇
V:1.0
'''
import requests
import json
import re
# 定义统一的headers
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
}
# 图片上传
url = "http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true"
files = {
  'file':open("2.png","rb")
}
temp_data = json.loads(requests.post(url=url,headers=headers,files=files).text)
# 获得图像识别结果
ans_url = "http://image.baidu.com/pcdutu?queryImageUrl=" + str(temp_data['url']) + "&querySign" + temp_data["querySign"] + "&fm=home&uptype=upload_pc&result=result_camera"
page_source= requests.get(url=ans_url,headers=headers).text
guessWord = re.findall("'guessWord': '(.*?)'",page_source)[0]
term_data = re.findall('"name":"(.*?)","baike":{"url":"(.*?)","abstract":"(.*?)","',page_source)
# 最终展示
if guessWord:
  print("您上传的图片可能是：",guessWord)
  print("除此之外，他还可能是：")
else:
  print("您上传的图片最可能是：")
for eve in term_data:
  print("名称：",eve[0],"\t描述：",eve[2],"\t百科地址：",eve[1])
