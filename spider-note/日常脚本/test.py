'''
Created on 2016年6月19日

@author: hasee
'''
#-*-coding=utf-8
from selenium import webdriver
import os,time
driver= webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//*[@id='u1']/a[8]").click()
#进入搜索设置页
time.sleep(2)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)
#设置每页搜索结果为100条
m=driver.find_element_by_xpath("//*[@id='nr']")
m.find_element_by_xpath("//*[@id='nr']/option[3]").click()
time.sleep(2)
#保存设置的信息
driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
time.sleep(2)
#弹窗接受
driver.switch_to_alert().accept()
#跳转到百度首页后，进行搜索表（一页应该显示100条结果）
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
