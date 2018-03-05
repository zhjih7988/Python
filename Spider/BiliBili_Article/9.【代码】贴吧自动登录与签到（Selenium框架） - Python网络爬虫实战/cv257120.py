
'''
目标网址：https://tieba.baidu.com/index.html?traceid=#
程序目的：模拟登陆百度贴吧
时间：2018-2-26
作者：刘宇
V:1.0
'''
import selenium.webdriver
import time
driver = selenium.webdriver.Safari()
url = "https://tieba.baidu.com/index.html?traceid=#"
driver.get(url)
# 点击登录
driver.find_element_by_xpath('//div[@class="u_menu_item"]/a').click()
time.sleep(1)
# 点击用户名密码登陆
driver.find_element_by_class_name("tang-pass-footerBarULogin").click()
time.sleep(1)
# 输入用户名和密码
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("15558136363")
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
time.sleep(6)
# 一键签到   这个功能有歧视，不好用，扎心了
# driver.find_element_by_class_name("onekey_btn").click()
# time.sleep(2)
# driver.find_element_by_class_name("j_sign_btn sign_btn sign_btn_nonmember").click()
url_chi = driver.find_elements_by_xpath('//a[@class="u-f-item unsign"]/@href')
total_url = []
for eve_url in url_chi:
  eve_tieba_url = "https://tieba.baidu.com" + eve_url.text
  total_url.append(eve_tieba_url)
for eve_tieba in total_url:
  driver.get(eve_tieba)
  time.sleep(3)
  driver.find_element_by_class_name("j_signbtn sign_btn_bright j_cansign").click()
  try:
    driver.find_element_by_class_name("j_signbtn sign_btn_bright j_cansign").click()
  except:
    pass
  time.sleep(3)
driver.quit()
