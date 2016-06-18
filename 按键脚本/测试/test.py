'''
Created on 2016年6月18日

@author: hasee
'''
#coding=utf-8
from selenium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = '1660213905'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit5").click() #ID方法点击

print("点击完成")

driver.quit()
