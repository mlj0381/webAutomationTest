#!usr/bin/python
#encoding:utf-8


'''启动页弹出层切换'''


__author__ = 'zhangbo'

from selenium import webdriver
from time import sleep
import unittest
import random
from configuration_files.driver_configurationFiles import browser_driver
from talkUser.user_quit_browser import *


class TestStartPage(unittest.TestCase):

    def setUp(self):

        self.driver = browser_driver()

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#启动页弹出层切换
#----------------------------------------------------------------------------------------------------------------------#
    # 启动页弹出层切换
    def test_start_page(self):

        print ("**************************************************启动页弹出层切换**************************************************")
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        sleep(1)

        a1_current = driver.current_window_handle

        qd_index = random.randint(1,2)

        try:

            #启动页：青少儿英语、成人英语
            qdtc_01 = "//*[@id='container']/div[6]/div[2]/ul/li["
            qdtc_02 = "]/a/i"
            qdtc_03 = qdtc_01 + str(qd_index) + qdtc_02

            if qd_index == 1:

                driver.find_element_by_xpath(qdtc_03).click()
                sleep(1)

                title_1 = driver.title
                url_1   = driver.current_url
                print (u'青少儿英语官网标题为：'+title_1)
                print (u'青少儿英语官网链接为：'+url_1+'\n')

                # driver.refresh()
                sleep(1)

            elif qd_index == 2:

                driver.find_element_by_xpath(qdtc_03).click()
                sleep(1)

                # a2_current = driver.window_handles
                # sleep(1)

                # for a3_current in a2_current:
                #
                #     if a3_current != a1_current:

                       # driver.switch_to_window(a3_current)

                sleep(1)
                title_2 = driver.title
                url_2   = driver.current_url
                print (u'成人英语官网标题位：'+title_2)
                print (u'成人英语官网链接为：'+url_2+'\n')
                sleep(1)
                # driver.close()
                # sleep(1)
                # driver.switch_to_window(a1_current)


        except:

              print ("没有找到启动页弹出层！！！")

        print ("******************************************************************************************************************" + "\n")

# ----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
# ----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)