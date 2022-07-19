# coding utf-8
#第一步导入webdriver模块
from selenium import webdriver
import time

#第二步打开Chrome浏览器
driver = webdriver.Chrome()

#第三步打开网页
# driver.get("https://www.baidu.com/")
# driver.get("http://172.31.47.182:8080/login?logout=exit")
# driver.get("http://172.31.22.15/#/login")
driver.get("http://172.31.23.41/#/login")
# 最大化窗口
driver.maximize_window()
time.sleep(2)
# 输入用户名
driver.find_element_by_xpath(".//input[@id='username']").send_keys("admin")
time.sleep(1)
# 输入密码
driver.find_element_by_xpath(".//input[@id='password']").send_keys("dxcs12345")
time.sleep(1)
# 点击登录按钮
driver.find_element_by_xpath(".//button[@class='btn btn-primary login-btn']").click()
