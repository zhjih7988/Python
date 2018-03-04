本文档仅作为视频学习过程中的参考
不可用于非法途径
Videoinfor.py
# -*- coding: utf-8 -*-
 scrapy
import
import
 VideoinforSpider(scrapy.Spider):
"videoinfor"
allowed_domains = [
]
 start_requests(self):
https://api.bilibili.com/x/web-interface/newlist?rid=24&type=0&pn=2&ps=20&jsonp=jsonp&_=1519706909231
 page_num 
 range(
,
):
"https://api.bilibili.com/x/web-interface/newlist?rid=24&type=0&pn="
"&ps=20&jsonp=jsonp&_=1519706909231"
 scrapy.Request(url=url, callback=self.parse)
 parse(self, response):
 eve 
 json.loads(response.body.decode(
))[
][
]:
 eve
http://docs.pythontab.com/scrapy/scrapy0.24/index.html
pipelines.py
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
http://doc.scrapy.org/en/latest/topics/item-pipeline.html
 scrapy.conf 
 settings
 pymongo
 BilibiliPipeline(object):
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
video_infor = dict(item)
self.post.insert(video_infor)
 item
settings.py
# -*- coding: utf-8 -*-
# Scrapy settings for bilibili project
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
http://www.yourdomain.com)'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
# Configure a delay for requests for the same website (default: 0)
http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
# 
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 
'Accept-Language': 'en',
#}
# Enable or disable spider middlewares
http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#
'bilibili.middlewares.BilibiliSpiderMiddleware': 543,
#}
# Enable or disable downloader middlewares
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#
'bilibili.middlewares.MyCustomDownloaderMiddleware': 543,
#}
# Enable or disable extensions
http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#
'scrapy.extensions.telnet.TelnetConsole': None,
#}
# Configure item pipelines
http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
'bilibili.pipelines.BilibiliPipeline'
300
}
# Enable and configure the AutoThrottle extension (disabled by default)
http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
