'''
Created on 2016年7月5日

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
# desired_caps['platformVersion'] = '9.1'
# desired_caps['deviceName'] = 'iPhone 5s'
# desired_caps['app'] = os.path.abspath('/Users/duomai/Desktop/1/haiuser.ipa')
desired_caps['platformVersion'] = '8.3'
desired_caps['deviceName'] = 'iPhone 6 Plus'
desired_caps['app'] = os.path.abspath('/Users/duomai/Desktop/appium/haiuser 2016-07-11 15-33-13/haiuser.ipa')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
#     首次安装必然弹出的接收通知
    try:
        if wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]")!=None:
            wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]").click()
            print("点击接受推送通知")
    except:
        print("接受通知失败:找不到推送通知")
    
#     首次安装出现的新人h5页面的返回键(按钮是独立的),点击返回
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]").click()
#     小蜜圈的蒙版提示,点击消失
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[4]").click()
#     点击跳转至我页面
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]").click()
#     弹出登录框
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
#     切换至快捷登录
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[2]").click()
#     弹出键盘,输入账号
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[3]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[2]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[4]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[5]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[6]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[7]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[8]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[9]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[8]").click()
#     弹出键盘,输入密码
    wd.implicitly_wait(5)    
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[11]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[11]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[11]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[28]").click()   #键盘更多
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[2]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAKey[3]").click()
#     点击登录
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
#     跳转买好货
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[2]").click()
#     点击搜索框
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
#     点击店铺
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[8]").click()
# #     输入mandy的
#     wd.implicitly_wait(5)
#     wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]").send_keys("mandy")
# #     点击键盘搜索
#     wd.implicitly_wait(5)
#     wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAKeyboard[1]/UIAButton[6]").click()

#     点击热搜第三个,mandy
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[3]/UIATableCell[2]/UIAButton[3]").click()
#     全部宝贝第一个商品
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[3]/UIACollectionView[1]/UIACollectionCell[1]").click()
#     点击立即购买
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[9]").click()
#     选择规格和购买数量
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").click()
#     点击立即购买
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[9]").click()
#     选择余额支付
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[11]/UIAButton[1]").click()
#     提交订单
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
#     输入支付密码
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[1]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[2]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[3]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[4]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[5]").click()
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[5]/UIAKeyboard[1]/UIAKey[6]").click()
#     点击确认支付,进入付款成功页面
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]").click()
#     上传清关证明
    wd.implicitly_wait(5)
    
    
except:
    print("失败")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")