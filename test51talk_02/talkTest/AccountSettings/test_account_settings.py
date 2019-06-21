#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


import unittest
from time import sleep
from selenium import webdriver

from talkUser.user_quit_browser import QuitBrowser
from talkTest.StartPage.startPagePopLayer import startPageComeInto

from Initializ_page.login_page_Initializ import login_page_Initializ_success
from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_url_success

from talkUser.user_account.test_account_class_settings import test_account_class_settings_success
from talkUser.user_account.test_account_personal_information import test_account_personal_information_success
from talkUser.user_account.test_account_change_password import test_account_change_password_success
from talkUser.user_account.test_account_class_leave import test_account_class_leave_success
from talkUser.user_account.test_account_cash_coupon import test_account_cash_coupon_success
from talkUser.user_account.test_account_purchase_record import test_account_purchase_record_success
from talkUser.user_account.test_account_wealth_record import test_account_wealth_record_success
from configuration_files import driver_configurationFiles as config_driver


#账号设置
class TestAccountSettings(unittest.TestCase):

#----------------------------------------------------------------------------------------------------------------------#
# 初始化浏览器
#----------------------------------------------------------------------------------------------------------------------#

        def setUp(self):

            # self.driver = config_driver.obj_phantomjs_mac_driver

            # self.driver = config_driver.obj_phantomjs_window_driver

            self.driver = config_driver.obj_driver

            self.url    = "http://www.51talk.com"

            sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置
#----------------------------------------------------------------------------------------------------------------------#

        def test_account_settings_success(self):

            u'''账号设置'''

            driver = self.driver

            user_mobile_value = ""

            user_password_value = ""

            user_user_id_value = ""

            #调用login页获取登录信息
            db_user = login_page_Initializ_success(driver,self.url)

            if db_user == 0:

                print ("登录失败，请查看原因！！！")

            else:

                user_mobile_value = db_user[0]

                sleep(1)

                login_after_url_link = driver.current_url

                sleep(1)

                account_type = 0

                #会员中心初始化账号设置链接
                account_type = member_center_Initializ_account_settings_page_url_success(driver,login_after_url_link)

                #调用账号设置--上课设置
                test_account_class_settings_success(driver,account_type)

                #调用账号设置--个人信息
                # test_account_personal_information_success(driver,account_type)

                #调用账号设置--修改密码
                test_account_change_password_success(driver,user_mobile_value)

                #调用账号设置--我要请假
                # test_account_class_leave_success(driver)

                #调用账号设置--代金券
                # test_account_cash_coupon_success(driver)

                #调用账号设置--购买记录
                # test_account_purchase_record_success(driver)

                #调用账号设置--我的课次
                # test_account_wealth_record_success(driver)

            sleep(5)

#----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

        def tearDown(self):

            QuitBrowser(self.driver)