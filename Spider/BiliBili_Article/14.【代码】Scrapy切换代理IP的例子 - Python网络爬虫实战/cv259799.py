本文档仅作为视频学习过程中的参考
不可用于非法途径
 ChangeProxy(object):
需要思考的几个问题：
1）什么时候需要切换IP
本身的IP被ban，被拉黑了，无法继续使用该IP请求目标网站了
2）切换ip是否需要支出
（一般需要购买）免费的IP，不需要花钱，不免费的IP，需要花钱，但是，大部分绝大部分很大一部分的免费IP是不能用
3）如何更优秀的切换IP
A）代理IP给我们的API，是有一个请求限制的，例如有的限制3S，有的限制5S，还有的限制1S
B）可能我们的一个代理IP获得之后，很快就会失效了，所以，一般情况下，代理IP都是先验证，后使用
C）很有可能一个代理IP，我们可以访问网页多次，才会被ban
I）我们一次获得多少代理IP？
小批量多次获取
II）我们一个代理IP用多少次，再切换
完善代理IP切换功能要考虑的几个问题：
1）IP是否可用
2）IP用几次清除掉
3）每次获得多少IP
1 2 3(不可用) 4 5 6 7 8 9 10
'''
 __init__(self):
初始化变量
get_url 是请求的api
temp_url 是验证的地址
ip_list 是ip
'''
"http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=be36e0a411c546d8a5fb38bb26ff43fe&orderno=YZ20173293618kDUVrD&returnType=2&count=10"
"http://ip.chinaz.com/getip.aspx"
self.ip_list = []
# 用来记录使用ip的个数，或者是目前正在使用的是第几个IP,本程序，我一次性获得了10个ip，所以count最大默认为9
self.count = 
# 用来记录每个IP的使用次数,此程序，我设置为最大使用4次换下一个ip
self.evecount = 
 getIPData(self):
这部分是获得ip，并放入ip池（先清空原有的ip池）
:return:
'''
temp_data = requests.get(url=self.get_url).text
self.ip_list.clear()
 eve_ip 
 json.loads(temp_data)[
]:
(eve_ip)
self.ip_list.append({
:eve_ip[
],
:eve_ip[
]
})
 changeProxy(self,request):
修改代理ip
:param request: 对象
:return:
'''
request.meta[
] = 
 + str(self.ip_list[self.count
][
]) + 
 + str(self.ip_list[self.count
][
])
 yanzheng(self):
验证代理ip是否可用，默认超时5s
:return:
'''
requests.get(url=self.temp_url,proxies={
:str(self.ip_list[self.count
][
]) + 
 + str(self.ip_list[self.count
][
])},timeout=
)
 ifUsed(self,request):
切换代理ip的跳板
:param request:对象
:return:
'''
:
self.changeProxy(request)
self.yanzheng()
:
 self.count == 
 
 self.count == 
:
self.getIPData()
self.count = 
self.count = self.count + 
self.ifUsed(request)
 process_request(self, request, spider):
 self.count == 
 
 self.count==
:
self.getIPData()
self.count = 
 self.evecount == 
:
self.count = self.count + 
self.evecount = 
:
self.evecount = self.evecount + 
self.ifUsed(request)
