'''
Created on 2016年6月17日

@author: duomai
'''
from selenium import webdriver
import os
from time import sleep

#mac下的设置
chromedriver = "/Users/duomai/Documents/chromedriver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# driver = webdriver.Chrome()

driver.get('http://c99.yunpan.360.cn/')

driver.maximize_window() #最大化

driver.find_element_by_name("account").send_keys("18814887520") #输入用户名

driver.find_element_by_name("password").send_keys("chenmai") #输入密码


driver.find_element_by_xpath("//*[@id='login']/div/div[2]/form/p[5]/input").click() #点击登录

sleep(5)

# 验证码导致延后
#driver.find_element_by_xpath("//*[@id='lottery-everyday']/i").click()


print (driver.title)
sleep(5)
driver.quit()