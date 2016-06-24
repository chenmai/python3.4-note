'''
Created on 2016年6月24日

@author: duomai
'''
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from appium import webdriver
from time import sleep

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.1'
desired_caps['deviceName'] = 'iPhone 5s'
desired_caps['app'] = os.path.abspath('/Users/duomai/Music/iTunes/iTunes Media/Mobile Applications/haiuser.ipa')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    sleep(5)
    print("暂停5秒")
    try:
        print(wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[6]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[1]"))
        if wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[6]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[1]")!=None:
            wd.switch_to_alert().accept()
            print("点击接受推送通知")
    except:
        print("接受通知失败")
    
except:
    print("失败")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
    else:
        print("测试用例通过")
