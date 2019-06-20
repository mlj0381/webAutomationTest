#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


'''调取短信平台'''

from selenium import webdriver
from time import sleep
from configuration_files import accountConfigInformation as accountConfig
import os
from user_file_rw_operation import *


#----------------------------------------------------------------------------------------------------------------------#
    #短信平台操作
#----------------------------------------------------------------------------------------------------------------------#

def user_sms_platform_info(driver,user_account):

        #Username
        driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/input").send_keys(accountConfig.userName)

        sleep(1)

        #Password
        driver.find_element_by_xpath("/html/body/div[2]/form/div[3]/div/input").send_keys(accountConfig.userPass)

        sleep(1)

        #Login
        driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/button").click()

        sleep(1)

        #短信管理
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a").click()

        sleep(1)

        #短信下发记录
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/ul/li/a").click()

        sleep(1)

        #输入手机号输入框
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/div[4]/input").send_keys(user_account)

        sleep(1)

        #查询手机号
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/button").click()

        sleep(1)

        #获取下方短信内容
        sms_text1 = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/div[2]/table[1]/tbody/tr/td[3]").text

        print sms_text1

        a_len = len(sms_text1)

        if a_len == 46:

           jiequ_code = sms_text1[0:6]
           return jiequ_code

        if a_len == 54:

           jiequ_code = sms_text1[8:14]
           return jiequ_code

        sleep(1)

        #调取文件写操作
        # user_file_w_operation(jiequ_code)

        sleep(1)

        driver.close()


# driver = webdriver.Chrome()
#
# sleep(2)
#
# driver.get("http://sms.51talk.com/Admin/Login/login")
#
# sleep(2)
#
# driver.maximize_window()
#
# sleep(2)
#
# user_mobile = "18666600000"
#
# user_sms_platform_info(driver,user_mobile)