# coding: utf-8
from lxml import html
from MyFun import SaveToHtml

parameter = '123'
Url = 'http://torrentkitty.kim/tk/'+ parameter +'/1-1-0.html'
page = html.parse(Url)
root = page.getroot()

list_divs = root.cssselect('list')
# print(list_divs)
