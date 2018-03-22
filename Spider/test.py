# -*- coding:utf-8 -*-
from selenium import webdriver  
import os  
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

# abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") 
# driver = webdriver.Chrome(abspath) 
browser = webdriver.Chrome() 

'''
find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''
url = 'https://www.baidu.com'
browser.get(url)
input_str = browser.find_element(By.ID,"kw")

input_str.send_keys("ipad")
time.sleep(1)
input_str.clear()
input_str.send_keys("MakBook pro")
button = browser.find_element(By.ID,'su')
button.click()
time.sleep(5)
browser.close()