'''
Created on 2016年6月19日

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





sleep(10)
# print("等待5秒后登陆")
driver.tap([(980, 950)], 500)
# print("点击登陆")



try:
    sleep(3)
    if driver.find_element_by_id("[公告]")!=0:
#         driver.find_element_by_id("[公告]").close()
        driver.tap([(1865, 65)], 500)
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


sleep(2)
driver.tap([(1450, 750)], 500)
# 到船坞
# print("到船坞")

sleep(3)
driver.tap([(410, 440)], 500)
# 选择第一艘船
# print("选择第一艘船")


sleep(3)
driver.tap([(1810, 300)], 500)
# 点开排序
# print("点开排序")

sleep(3)
driver.tap([(1350, 610)], 500)
# 选择升序
# print("升序")

sleep(3)
driver.tap([(300, 410)], 500)
# 选择最低船

sleep(2)
driver.tap([(100, 950)], 500)
# 返回船港


sleep(2)
driver.tap([(1400, 350)], 500)
# 点开出征

sleep(2)
driver.swipe(570,950,1400,950,2000)
# 左移章节
sleep(1)
driver.swipe(570,950,1400,950,2000)
# 左移章节

sleep(1)
driver.tap([(570, 950)], 500)
# 点击第一章节


sleep(2)
driver.tap([(850, 500)], 500)
# 选择1-1

sleep(2)
driver.tap([(950, 970)], 500)
# 开战


sleep(10)
driver.tap([(1300, 910)], 500)
# 如果索敌失败，点击开始战斗

sleep(25)
# 战斗动画等待

driver.tap([(1100, 470)], 500)
# 不夜战

# driver.tap([(1100, 470)], 500)
# 不夜战

sleep(2)
driver.tap([(1500, 770)], 500)
# 点击屏幕，战斗结算
sleep(2)
driver.tap([(1730, 970)], 500)
# 点击屏幕，战斗结算确认

sleep(2)
driver.tap([(1170, 720)], 500)

# 取消锁定

sleep(2)
driver.tap([(1100, 470)], 500)
# 回港

print("首次炼钢结束")
# 首次炼钢结束

for i in range(30):
    
    sleep(2)
    driver.tap([(1450, 750)], 500)
    # 到船坞
#     print("到船坞")
    
    sleep(3)
    driver.tap([(410, 440)], 500)
    # 选择第一艘船
#     print("选择第一艘船")
    
    
    sleep(3)
    driver.tap([(1810, 300)], 500)
    # 点开排序
#     print("点开排序")
    
    sleep(3)
    driver.tap([(1350, 610)], 500)
    # 选择升序
#     print("升序")
    
    sleep(3)
    driver.tap([(300, 410)], 500)
    # 选择最低船
    
    sleep(2)
    driver.tap([(100, 950)], 500)
    # 返回船港
    
    
    sleep(2)
    driver.tap([(1400, 350)], 500)
    # 点开出征
    
    sleep(2)
    driver.tap([(850, 500)], 500)
    # 选择1-1
    
    sleep(2)
    driver.tap([(950, 970)], 500)
    # 开战
    
    
    sleep(10)
    driver.tap([(1300, 910)], 500)
    # 如果索敌失败，点击开始战斗
    
    sleep(25)
    # 战斗动画等待
    
    driver.tap([(1100, 470)], 500)
    # 不夜战
    
    # driver.tap([(1100, 470)], 500)
    # 不夜战
    
    sleep(2)
    driver.tap([(1500, 770)], 500)
    # 点击屏幕，战斗结算
    sleep(2)
    driver.tap([(1730, 970)], 500)
    # 点击屏幕，战斗结算确认
    
    sleep(2)
    driver.tap([(1170, 720)], 500)
    
    # 取消锁定
    
    sleep(2)
    driver.tap([(1100, 470)], 500)
    
    print("第",i+2,"次炼钢结束")
    
    
driver.quit()    



# 等待15秒后登陆