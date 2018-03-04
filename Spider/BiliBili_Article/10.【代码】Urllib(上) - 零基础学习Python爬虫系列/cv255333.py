本文是视频av20146314的相关代码文档
# urllib(上)
# get ：是通过网址传递参数或者直接打开页面，请求页面
# post：是通过form，并不在网址上体现内容，进行数据传递
# www.xxxyyy.com/temp.html?a=1&b=2
# form_data = {"C":1,"D":2}
# username,password  一般都是post传递，   我就想通过url?username=xxxxx&password=y
# https://www.baidu.com/s?wd=hello
# https://www.baidu.com/s
# ?意味着开始传递参数了
# wd = hello
# 抓包的方法需要大家记住，主要就是检查元素->network(网络)
# 简单的get进行网页的数据获取例子
# 如果，这个请求是https的，我们要在开始加上这样语句话：
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 当然，如果不是https的请求，我们可以不写这两行
# 进行简单的get操作：
import urllib.request
input_data = input("请您输入IP地址：")
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=" + input_data + "&co=&resource_id=6006"
# 在本次请求中，可以不带入request_headers(请求头)，也可以获得结果，但是，对于初学者来说，我们就要带着他，来作为练习
headers = {
  "Accept": "*/*",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive",
  "Cookie": "",
  "Host": "sp0.baidu.com",
  "Pragma": "no-cache",
  "Referer": "https://www.baidu.com/s?wd=ip%E5%9C%B0%E5%9D%80&rsv_spt=1&rsv_iqid=0xc0a30a7d00052b5d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=id&inputT=396&rsv_t=17eaouGpLbNXKYoRVkLXpn2VPRoRUUmxLsKp%2B77R%2FAOH8xFdVo617vj%2FgaFR%2BU5Bekz7&rsv_pq=f2eeecad00055c08&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&bs=id",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
}
# 构建请求的对象
request_attr = urllib.request.Request(url=url, headers=headers)
# 获得response，并且进行转码
response_data = urllib.request.urlopen(request_attr).read().decode("gbk")
# 如果我们不需要带着headers请求，我们可以直接使用urlopen
# response_data = urllib.request.urlopen(url=url).read().decode("gbk")
import json
print(json.loads(response_data)["data"][0]["location"])
