'''
Created on 2016年6月17日

@author: duomai
'''
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#mac下的设置
# chromedriver = "/Users/duomai/Documents/chromedriver/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

driver = webdriver.Chrome()

driver.get('http://c99.yunpan.360.cn/')

driver.maximize_window() #最大化

driver.find_element_by_name("account").send_keys("18814887520") #输入用户名

driver.find_element_by_name("password").send_keys("chenmai") #输入密码


# driver.find_element_by_xpath("//*[@id='login']/div/div[2]/form/p[5]/input").click() #点击登录

sleep(20)

m=driver.find_element_by_xpath("//*[@id='topPanel']/div/div")
driver.find_element_by_xpath("//*[@id='topPanel']/div/div").click()
ActionChains(driver).move_to_element(m)
print(m.find_element_by_xpath("//*[@id='lottery-everyday']/i").is_displayed())
# js="var q=m.find_element_by_xpath(\"//*[@id='lottery-everyday']/i\").menu .icon, .menu .text ={    cursor: pointer;}"
# driver.execute_script(js)
print(m.find_element_by_xpath("//*[@id='lottery-everyday']/i").is_displayed())
m.find_element_by_xpath("//*[@id='lottery-everyday']/i").click()


# 验证码导致延后
#driver.find_element_by_xpath("//*[@id='lottery-everyday']/i").click()


print (driver.title)
sleep(5)
driver.quit()
