# -*- coding:utf-8 -*-
from selenium import webdriver  
import os  
import time
abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") 
driver = webdriver.Chrome(abspath) 

driver.get('http://www.yopmail.com/zh/email-generator.php')
time.sleep(1)
email = driver.find_element_by_id("login")
email = email.get_attribute('value')
print(email)

#打开邮箱页面后，我发现，邮箱的内容是以iframe的形式展现的，所以，这地方要处理一下：
driver.switch_to_frame(driver.find_element_by_id('ifmail'))
try:
    html = driver.find_element_by_id('mailmillieu')
except Exception as e:
    input('遇到机器识别的问题，切换到浏览器点击一下，验证完敲一下回车')
    html = driver.find_element_by_id('mailmillieu')
html = html.text
active_url = html.split('account:')[1].strip()
driver.get(active_url)
time.sleep(1)

driver.delete_all_cookies()
time.sleep(1)