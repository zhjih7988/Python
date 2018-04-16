# -*- coding:utf-8 -*-
# 爬取6vhao.com 推荐电影
from selenium import webdriver  
import os  
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") 
browser = webdriver.Chrome() 

url = 'http://www.minimp4.com/movie/top250_douban'
wait = WebDriverWait(browser, 10)

def search(KEYWORD):
    try:
        browser.get(url)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
            )
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#topsearch > fieldset > div > div > span > button")))
        input.send_keys(KEYWORD)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#wrapp > div.jumbotron > div > div > ul:nth-child(4) > li:nth-child(8) > a")))
        total = str((total.get_attribute("href"))).split("/")[-1:]
        return total[0]
    except TimeoutException:
        return search

def Operate(url):
    try:
        browser.get(url)
    except TimeoutException:
        return Operate
    
def main():
    KEYWORD = '电影'
    total = search(KEYWORD)
    print(total)
    newURL = 'https://www.zhongziso.com/list/'+ KEYWORD
    for i in range(1,int(total)):
        Operate(newURL+'/'+str(i))


if __name__ == '__main__':
    main()



# time.sleep(10)

# browser.delete_all_cookies()
# browser.close()