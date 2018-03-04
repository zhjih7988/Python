本文档仅作为视频学习过程中的参考
不可用于非法途径
items.py
# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
http://doc.scrapy.org/en/latest/topics/items.html
 scrapy
 ZhihuItem(scrapy.Item):
# define the fields for your item here like:
# name = scrapy.Field()
name = scrapy.Field()
url_token = scrapy.Field()
headline = scrapy.Field()
follower_count = scrapy.Field()
answer_count = scrapy.Field()
articles_count = scrapy.Field()
uid = scrapy.Field()
gender = scrapy.Field()
type = scrapy.Field()
spiders.py
# -*- coding: utf-8 -*-
 scrapy
import
import
 zhihu.items 
 ZhihuItem
 scrapy_redis.spiders 
 RedisCrawlSpider
 UserinforSpider(RedisCrawlSpider):
name = 
'myspider:start_urls'
allowed_domains = [
]
https://www.zhihu.com/api/v4/members/liuyu-43-97/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
 parse(self, response):
temp_data = json.loads(response.body.decode(
))[
]
count = len(temp_data)
 count < 
:
:
page_offset = int(re.findall(
, response.url)[
])
new_page_offset = page_offset + 
next_page_url = response.url.replace(
 + str(page_offset) + 
,
 + str(new_page_offset) + 
)
 scrapy.Request(url=next_page_url, callback=self.parse)
 eve_user 
 temp_data:
item = ZhihuItem()
item[
] = eve_user[
]
item[
] = eve_user[
]
item[
] = eve_user[
]
'follower_count'
'follower_count'
item[
] = eve_user[
]
'articles_count'
'articles_count'
item[
] = eve_user[
]
item[
] = eve_user[
]
item[
] = eve_user[
]
 open(
) 
 f:
user_list = f.read()
 eve_user[
] 
 
 user_list:
 open(
, 
) 
 f:
f.write(eve_user[
] + 
)
 item
"https://www.zhihu.com/api/v4/members/"
"/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20"
 scrapy.Request(url=new_url, callback=self.parse)
settings.py
# -*- coding: utf-8 -*-
# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
http://doc.scrapy.org/en/latest/topics/settings.html
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
BOT_NAME = 
SPIDER_MODULES = [
]
NEWSPIDER_MODULE = 
MONGODB_HOST = 
MONGODB_PORT = 
MONGODB_DBNAME = 
MONGODB_DOCNAME = 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# Configure a delay for requests for the same website (default: 0)
http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'application/json, text/plain, */*'
'zh-CN,zh;q=0.9,en;q=0.8'
'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
"Cache-Control"
"Connection"
'_zap=74a1bc89-5927-46f1-a903-26b9d4f9906c; q_c1=679bbf981bc54edaa36a718a757d7110|1506423740000|1502849291000; d_c0="AFBCMYYIigyPTn-w9gPOx5CNrckgcsQKrhk=|1508201688"; q_c1=f3521e394ce8459094ba76547cddd3e5|1517535767000|1502849291000; aliyungf_tc=AQAAACykS2tz0ggA5KAxJPLJJw8rf8SF; _xsrf=c8e59c5f-190a-4b71-ad56-1425517c7a9b; r_cap_id="Yjc3Y2Y1ODkxYzcxNGZkOGFhMDUwZjBhNjFhZTEyYjI=|1519810983|a19b0558ddd2a119ed7581c8fd59427ab2298d03"; cap_id="ZDM1Y2UzZTBhZTQ2NDc3OWIzYmE3YzczYmY0YmVlNzE=|1519810983|4c6504306036f99443b659ce4f8ea2723ebb6a96"; l_cap_id="NDcyOGU5YzUyNTdmNDc1OTlhMGU1Mzc3MjQ4NDY5YjI=|1519810983|ed1d25b9a6905ad1891a94984d8cecd51b8a96e0"; __utma=51854390.1002977338.1508201688.1516880301.1519810987.10; __utmc=51854390; __utmz=51854390.1519810987.10.10.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/liuyu-43-97/activities; __utmv=51854390.000--|2=registration_date=20160118=1^3=entry_date=20170816=1; capsion_ticket="2|1:0|10:1519878553|14:capsion_ticket|44:N2NhNTJmNGQ5M2EyNDUzODk1MzIxYjgzNjFkM2FiZmY=|6b0b25b31dbdc0c80f49a9db073ec4953c5c4f6edd1bb1978bcee89c9b64f0b9"'
'www.zhihu.com'
'no-cache'
'https://www.zhihu.com/'
'AFBCMYYIigyPTn-w9gPOx5CNrckgcsQKrhk='
}
# Enable or disable spider middlewares
http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#
'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
# }
# Enable or disable downloader middlewares
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
# 'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
'zhihu.middlewares.ChangeProxy'
543
}
# Enable or disable extensions
http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#
'scrapy.extensions.telnet.TelnetConsole': None,
# }
# Configure item pipelines
http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
'zhihu.pipelines.ZhihuPipeline'
300
}
# Enable and configure the AutoThrottle extension (disabled by default)
http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
"scrapy_redis.scheduler.Scheduler"
"scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
'scrapy_redis.queue.SpiderQueue'
middlewares.py
# -*- coding: utf-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
http://doc.scrapy.org/en/latest/topics/spider-middleware.html
 scrapy 
 signals
 requests
import
 ZhihuSpiderMiddleware(object):
# Not all methods need to be defined. If a method is not defined,
# scrapy acts as if the spider middleware does not modify the
# passed objects.
@classmethod
 from_crawler(cls, crawler):
# This method is used by Scrapy to create your spiders.
s = cls()
crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
 s
 process_spider_input(response, spider):
# Called for each response that goes through the spider
# middleware and into the spider.
# Should return None or raise an exception.
return
None
 process_spider_output(response, result, spider):
# Called with the results returned from the Spider, after
# it has processed the response.
# Must return an iterable of Request, dict or Item objects.
 i 
 result:
 i
 process_spider_exception(response, exception, spider):
# Called when a spider or process_spider_input() method
# (from other spider middleware) raises an exception.
# Should return either None or an iterable of Response, dict
# or Item objects.
 process_start_requests(start_requests, spider):
# Called with the start requests of the spider, and works
# similarly to the process_spider_output() method, except
# that it doesn’t have a response associated.
# Must return only requests (not items).
 r 
 start_requests:
 r
 spider_opened(self, spider):
spider.logger.info(
 % spider.name)
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
"http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=e805d7cd7baa41ef87dfc5cec0ed9614&orderno=YZ20173293618kDUVrD&returnType=2&count=10"
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
self.evecount = 
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
pipelines.py
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
http://doc.scrapy.org/en/latest/topics/item-pipeline.html
 scrapy.conf 
 settings
 pymongo
 ZhihuPipeline(object):
 __init__(self):
host = settings[
]
port = settings[
]
dbName = settings[
]
client = pymongo.MongoClient(host=host,port=port)
tdb = client[dbName]
self.post = tdb[settings[
]]
 process_item(self, item, spider):
zhihu = dict(item)
self.post.insert(zhihu)
 item
