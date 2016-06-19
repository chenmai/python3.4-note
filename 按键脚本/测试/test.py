'''
Created on 2016年6月18日

@author: hasee
'''
#coding=utf-8
# from selenium import webdriver
from appium import webdriver

import appium


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = '1660213905'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# appiumdriver=
driver.find_element_by_id("com.android.calculator2:id/digit5").click() #ID方法点击
print("点击完成")

x = driver.get_window_size()['width']
print(x)
y = driver.get_window_size()['height']
print(y)



driver.tap([(405, 1530)], 500)  #点击该坐标位置

# print(driver.current_activity)
driver.get_screenshot_as_file('E:\战舰少女截图判断\港区大厅.png')
print("截图完成")

driver.quit()
