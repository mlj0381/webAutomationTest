#!usr/bin/python
#encoding:utf-8

'''主站模块TAB切换'''


__author__ = 'zhangbo'

from selenium import webdriver

from time import sleep

import unittest

from talkTest.StartPage.startPagePopLayer import startPageComeInto

from configuration_files.driver_configurationFiles import browser_driver

from talkUser.user_quit_browser import *


class TestHomePage(unittest.TestCase):

    u'''首页操作如下:'''

    def setUp(self):

        self.driver = browser_driver()

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#主站模块TAB切换
#----------------------------------------------------------------------------------------------------------------------#
    # 主站模块TAB切换
    def test_homepage_tabpage_switch(self):

        print ("**************************************************主站模块TAB切换**************************************************")

        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        sleep(1)


        #调用启动页进入青少儿官网
        startPageComeInto(driver)

        sleep(2)

        currey_handles = driver.current_window_handle

        for j_index in range(1,7,1):

            junior_tab_index_01 = "/html/body/div[1]/div[2]/div[1]/ul/li["
            junior_tab_index_02 = "]/a"
            junior_tab_index_03 = junior_tab_index_01 + str(j_index) + junior_tab_index_02

            driver.find_element_by_xpath(junior_tab_index_03).click()

            sleep(1)

            widows_handles = driver.window_handles

            sleep(1)

            # if j_index == 7:
            #
            #     j_index_aa_url = driver.current_url
            #     print (u'美国小学英语URL链接为：' + j_index_aa_url + '\n')
            #
            # else:

            j_text = driver.find_element_by_xpath(junior_tab_index_03).text
            j_url = driver.current_url

            print (u'青少儿英语TAB标题为：' + j_text)
            print (u'青少儿英语TAB链接为：' + j_url + '\n')

        print ("******************************************************************************************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
#关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)