'''
Created on 2016年6月17日

@author: duomai
'''
# from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

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

sleep(15)


driver.find_element_by_xpath("//*[@id='topPanel']/div/div").click()   #点击右上角个人中心


m=driver.find_element_by_xpath("//*[@id='topPanel']/div/div")



ActionChains(driver).move_to_element(m)    #鼠标移至个人中心


j=driver.find_element_by_xpath("//*[@id='lottery-everyday']/i")
ActionChains(driver).move_to_element(j)
sleep(2)
# 鼠标移至个人中心下方的隐藏列表中

print(driver.find_element_by_xpath("//*[@id='lottery-everyday']/i").is_displayed())   #显示该隐藏元素现在是不是可以操控

driver.find_element_by_xpath("//*[@id='lottery-everyday']/i").click()   #点击每日抽奖


print (driver.title)
sleep(5)
driver.quit()



'''
总结:对于不可见元素,需要逐级点击使之可见
'''
