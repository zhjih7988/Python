本文档仅作为视频学习过程中的参考，不可用于非法途径
'''
目标网址：http://www.5a5x.com
采集需求：获得所有E语言源代码
时间：2018-2-22
作者：刘宇
V：1.0
'''
import urllib.request
from lxml import etree
import os
import socket
socket.setdefaulttimeout(5)
# 对愿网站分类信息进行手机，一共有以下分类内容
list_data = [
  "enetwork"
]
# 根据分类，进行内容获取
for eve_list_data in list_data:
  # 先建立该分类的文件夹
  os.mkdir(eve_list_data)
  # 组合出该分类的首页
  source_url = "http://www.5a5x.com/wode_source/" + eve_list_data
  # 根据首页获得该分类的总页数
  page_total = int(etree.HTML(urllib.request.urlopen(source_url).read().decode("gbk")).xpath('//*[@id="pages"]/b[2]/text()')[0].replace("/",""))
  # 进入分类的全部页码，进行数据获取
  for eve_content_list_page in range(1,page_total+1):
    # 每个页面的数据
    url = source_url + "/" + str(eve_content_list_page) + ".html"
    # 获得网页源代码
    page_source = etree.HTML(urllib.request.urlopen(url).read().decode("gbk"))
    # 提取出每个页面中全部的内容
    content_list = page_source.xpath('//dl[@class="down_list"]/dt/a/@href')
    # 根据不同内容，进行数据下载
    for eve_content in content_list:
      try:
        # 打开内容详情页
        content_url = "http://www.5a5x.com/" + eve_content
        content_page_souce = etree.HTML(urllib.request.urlopen(content_url).read().decode("gbk"))
        # 提取出该源代码的title
        title = content_page_souce.xpath("//caption/span/text()")[0]
        # 提取出该源代码的下载页面url
        download_url = "http://www.5a5x.com/" + content_page_souce.xpath('//*[@id="down_address"]/a/@href')[0]
        # 根据下载页面url获得文件的确切url
        file_url = "http://www.5a5x.com/" + etree.HTML(urllib.request.urlopen(download_url).read().decode("gbk")).xpath('//a/@href')[0]
        # 打开文件url，并以二进制存储到本地指定的文件夹下，文件命名用title
        with open(eve_list_data + "/" + title + ".zip","wb") as f:
          f.write(urllib.request.urlopen(file_url).read())
        # 输出完成的内容
        print(eve_list_data,title)
      except Exception as e:
        print(content_url)
