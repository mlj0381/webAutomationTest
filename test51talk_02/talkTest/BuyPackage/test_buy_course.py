#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

import unittest

from selenium import webdriver

from time import sleep

from configuration_files.accountConfigInformation import xunhuan_login_max

from talkUser.user_purchase.user_old_sale_package import user_old_sale_package_success
from talkUser.user_purchase.user_new_sale_package import user_new_sale_package_success
from talkUser.user_quit_browser import *

from Initializ_page.login_page_Initializ import login_page_Initializ_success


class TestBuyPackage(unittest.TestCase):

        def setUp(self):

            self.driver = webdriver.Chrome()

            # self.driver = config_driver.obj_phantomjs_mac_driver

            # self.driver = config_driver.obj_phantomjs_window_driver

            self.url    = "http://www.51talk.com"

            sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    # 购买课程
#----------------------------------------------------------------------------------------------------------------------#

        def test_buy_course_info(self):

            '''购买课程'''

            for xunhuan_login_index in range(0, xunhuan_login_max):

                print ("****************购买课程****************")

                driver = self.driver

                user_mobile_value = ""

                user_password_value = ""

                user_user_id_value = ""

                # 调用login页获取登录信息
                db_user = login_page_Initializ_success(driver, self.url)

                if db_user == 0:

                    print ("登录失败，请查看原因！！！")

                else:

                    user_mobile_value   = db_user[0]
                    user_password_value = db_user[1]
                    user_user_id_value  = db_user[2]

                    sleep(1)

                    #购买课程
                    try:

                        #购买课程（成人付费、青少付费、美小体验与付费）
                        driver.find_element_by_css_selector("body > div.g-hd > div.m-head > div > ul > li:nth-child(3) > a")

                        sleep(2)

                        driver.find_element_by_css_selector("body > div.g-hd > div.m-head > div > ul > li:nth-child(3) > a").click()

                    except:

                        #成人、青少体验学员：无财富时
                        try:

                            driver.find_element_by_css_selector("#head > div > div.m-head > div > ul > li:nth-child(3) > a")

                            sleep(2)

                            driver.find_element_by_css_selector("#head > div > div.m-head > div > ul > li:nth-child(3) > a").click()

                        except:

                            print ("没有找到课程购买模块或者登录失败，请查看原因！！！")

                            break;

                    sleep(2)

                    one_window_handle = driver.current_window_handle

                    buyCourse_url = driver.current_url

                    #美小套餐老售卖
                    if buyCourse_url == 'https://aa.51talk.com/nat/pay/product' or \
                       buyCourse_url == 'http://aa.51talk.com/nat/pay/product':

                        print ("*************************")
                        print ("开启美小旧版售卖包装页面！！！  ")
                        print ("*************************")

                        sleep(1)

                        #调用美小老版售卖列表
                        user_old_sale_package_success(one_window_handle, driver, user_mobile_value, user_user_id_value)

                    #成人与青少套餐新售卖
                    elif buyCourse_url == 'http://sale.51talk.com/point_package' or \
                         buyCourse_url == 'https://sale.51talk.com/point_package' or \
                         buyCourse_url == 'http://sale.51talk.com/mix_point' or \
                         buyCourse_url == 'https://sale.51talk.com/mix_point' or \
                         buyCourse_url == 'http://sale.51talk.com/' or \
                         buyCourse_url == 'https://sale.51talk.com/':

                            print ("*****************************")
                            print ("开启成人与青少新版售卖包装页面！！！")
                            print ("*****************************")

                            sleep(1)

                            #调用成人与青少新版售卖列表
                            user_new_sale_package_success(one_window_handle,driver,user_mobile_value,user_user_id_value)

                    else:

                        print ("没有找到课程套餐列表，无法购买套餐，请查看原因！！！")

                        sleep(2)

                        #退出
                        driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                        sleep(2)

            print ("************************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

        def tearDown(self):

            QuitBrowser(self.driver)