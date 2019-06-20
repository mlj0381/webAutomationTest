#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


import unittest
from selenium import webdriver
from time import sleep
from Initializ_page.login_page_Initializ import login_page_Initializ_success
from talkUser.user_quit_browser import QuitBrowser
from talkUser.user_open_class.user_open_class import user_open_class_success
from talkUser.user_wealth import user_experience_the_wealth_success
from talkUser.user_wealth import user_paid_the_wealth_success


#公开课
class TestOpenClass(unittest.TestCase):

#----------------------------------------------------------------------------------------------------------------------#
# 初始化浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def setUp(self):

        self.driver = webdriver.Chrome()

        # self.driver = config_driver.obj_phantomjs_mac_driver

        # self.driver = config_driver.obj_phantomjs_window_driver

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
# 公开课
#----------------------------------------------------------------------------------------------------------------------#

    def test_open_class_success(self):

        u'''公开课'''

        driver = self.driver

        user_mobile_value   = ""

        user_password_value = ""

        user_user_id_value  = ""

        # 调用login页获取登录信息
        db_user = login_page_Initializ_success(driver, self.url)

        if db_user == 0:

            print ("登录失败，请查看原因！！！")

        else:

            user_mobile_value   = db_user[0]
            user_password_value = db_user[1]
            user_user_id_value  = db_user[2]

            sleep(1)

            current_window_handle = driver.current_window_handle

            login_after_url_link = driver.current_url

            sleep(1)

            #成人/青少付费账号
            if login_after_url_link == "https://www.51talk.com/user/index" or \
               login_after_url_link == "http://www.51talk.com/user/index":

                # 查询付费用户财富信息
                wealth_data = user_paid_the_wealth_success(driver, str(user_user_id_value), str(user_mobile_value))

            # 成人/青少体验账号，直接进入会员中心 or 体验课约课页面
            elif login_after_url_link == "http://trial.51talk.com/trial/index" or \
                 login_after_url_link == "https://trial.51talk.com/trial/index" or \
                 login_after_url_link == "http://trial.51talk.com/trial/reserve" or \
                 login_after_url_link == "https://trial.51talk.com/trial/reserve":

                # 查询体验用户财富信息
                wealth_data = user_experience_the_wealth_success(driver,login_after_url_link,str(user_user_id_value),str(user_mobile_value))

            #调用公开课
            user_open_class_success(driver, current_window_handle, login_after_url_link, wealth_data, str(user_user_id_value),str(user_mobile_value))

#----------------------------------------------------------------------------------------------------------------------#
# 退出浏览器
#----------------------------------------------------------------------------------------------------------------------#

def tearDown(self):

        QuitBrowser(self.driver)

