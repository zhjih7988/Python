# -*- coding:utf-8 -*-
from selenium import webdriver  
import os  
import time
abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") 
driver = webdriver.Chrome(abspath) 

driver.get('http://www.qq.com')
time.sleep(1)