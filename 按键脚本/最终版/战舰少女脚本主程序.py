'''
Created on 2016年6月18日

@author: hasee
'''
from appium import webdriver

import appium
from time import sleep
import time



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = '1660213905'
desired_caps['appPackage'] = 'com.huanmeng.zhanjian2'
desired_caps['appActivity'] = 'org.cocos2dx.cpp.AppActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 游戏已经启动

def getpage():
    sleep(5)
    temp=driver.page_source
    print(temp)

# 打印页面控件信息





sleep(5)
# print("等待5秒后登陆")
driver.tap([(980, 950)], 500)
# print("点击登陆")



try:
    sleep(3)
    if driver.find_element_by_id("[公告]")!=0:
        driver.find_element_by_id("[公告]").close()
#         driver.tap([(1865, 65)], 500)
        print("公告关闭成功")
except:
    print("公告窗没有，不需要关闭")
    pass
# 公告处理


sleep(2)
driver.tap([(1000, 850)], 500)
sleep(2)
driver.tap([(1000, 850)], 500)
print("找不到签到控件，已坐标处理")
# 签到确定




# 等待15秒后登陆