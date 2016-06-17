'''
Created on 2016年6月17日

@author: duomai
'''
from selenium import webdriver
import os
# from time import sleep

#mac下的设置
chromedriver = "/Users/duomai/Documents/chromedriver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# driver = webdriver.Chrome()

driver.get('http://c99.yunpan.360.cn/')

print (driver.title)
# sleep(5)
driver.quit()