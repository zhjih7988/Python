本文档仅作为视频学习过程中的参考
不可用于非法途径
# 查询IP  http://ip.chinaz.com/getip.aspx
'''
{"ERRORCODE":"0","RESULT":[{"port":"31478","ip":"180.121.160.85"},{"port":"33919","ip":"182.39.11.54"},{"port":"28399","ip":"113.128.29.140"},{"port":"26890","ip":"59.56.224.218"},{"port":"22793","ip":"182.42.39.230"},{"port":"38227","ip":"183.158.23.191"},{"port":"36175","ip":"180.115.9.201"},{"port":"34122","ip":"123.53.119.226"},{"port":"29592","ip":"114.231.156.85"},{"port":"38438","ip":"180.155.142.234"}]}
'''
import urllib.request
url = "http://ip.chinaz.com/getip.aspx"
print(urllib.request.urlopen(url).read().decode("utf-8"))
# 构建一个代理IP的格式
ip_data = "144.255.49.73"
port_data = "44369"
new_data = {
  "http": ip_data + ":" + port_data,
}
# 建立相关的对象
proxy_support = urllib.request.ProxyHandler(new_data)
opener = urllib.request.build_opener(proxy_support)
# 将新的opener放进来
urllib.request.install_opener(opener)
print(urllib.request.urlopen(url).read().decode("utf-8"))
# 切换回原IP
# 建立相关的对象
proxy_support = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_support)
# 将新的opener放进来
urllib.request.install_opener(opener)
print(urllib.request.urlopen(url).read().decode("utf-8"))
print("*"*20)
import requests
print(requests.get(url).text)
print(requests.get(url, proxies=new_data).text)
print(requests.get(url, proxies={"http":""}).text)
'''
原始IP是A
切换IP是B - IP B失效了
      （访问代理IP提供者的api）我们是需要用B还是用A  - - 》 我们要做一个事情，将B切换回A
      切换IP是C
'''
