# coding utf-8
#第一步导入webdriver模块
from selenium import webdriver
from selenium.webdriver.common.by import By
# 需要导入模块: from selenium.webdriver.common.by import By [as 别名]
# 或者: from selenium.webdriver.common.by.By import xpath [as 别名]
import time

#第二步打开Chrome浏览器
driver = webdriver.Chrome()

#第三步打开网页
driver.get("https://www.baidu.com/")

# 最大化窗口
driver.maximize_window()
time.sleep(2)
# 输入用户名

# 输入密码
driver.find_element_by_xpath(".//input[@id='kw']").send_keys("王源")
time.sleep(1)
# 点击登录按钮
driver.find_element_by_xpath(".//input[@class='bg s_btn']").click()
time.sleep(1)
# driver.find_element_by_xpath(".//span[@class='c-color-gray']").click()
driver.find_element_by_xpath(".//a[@aria-label='王源，中国内地男歌手、演员、主持人、作家，中国内地男子演唱组合TFBOYS成员，百度百科']").click()
#driver.find_element(By.XPATH,'//a[contains(@href,"www.baidu.com/link?url=")]').click()
