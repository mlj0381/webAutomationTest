#!usr/bin/python
#encoding:utf-8

'''美小官网TAB切换'''


__author__ = 'zhangbo'

from selenium import webdriver

from time import sleep

import unittest

from talkTest.StartPage.startPagePopLayer import startPageComeInto

from configuration_files.driver_configurationFiles import browser_driver

from talkUser.user_quit_browser import *


class TestAaHomePage(unittest.TestCase):

    u'''首页操作如下:'''

    def setUp(self):

        self.driver = browser_driver()

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#美小官网TAB切换
#----------------------------------------------------------------------------------------------------------------------#
    # 美小主站TAB切换
    def test_aahomepage_tabpage_switch(self):

        print ("**************************************************美小主站TAB切换**************************************************")

        driver = self.driver
        driver.get(self.url)
        sleep(1)

        driver.maximize_window()

        #调用启动页关闭弹出层
        startPageComeInto(driver)

        sleep(2)

        currey_handles = driver.current_window_handle

        #美国小学
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/ul/li[7]/a").click()

        sleep(2)

        all_current = driver.window_handles

        sleep(2)

        for a1_current in all_current:

            if a1_current != currey_handles:

                driver.switch_to_window(a1_current)

                sleep(2)

                #美国小学TAB页切换展示
                for y in range(1,5):

                    tab1_str1 = "/html/body/div[1]/div[3]/div/ul/li["
                    tab1_str2 = str(y)
                    tab1_str3 = "]/a"
                    tab1_str4 = tab1_str1+tab1_str2+tab1_str3

                    sleep(1)
                    driver.find_element_by_xpath(tab1_str4).click()
                    sleep(1)

                    text_url_1 = driver.find_element_by_xpath(tab1_str4).text
                    # text_url_1 = driver.find_element_by_css_selector("body > div.wrap-nav.north-nav-list "
                    #                                                  "> div.nav-list > div > ul > li.crt > a").text
                    sleep(1)

                    title_url_1 = driver.current_url
                    sleep(1)

                    print (text_url_1+u"标签链接是：" + title_url_1)
                    sleep(1)

                driver.close()
                sleep(0.5)

        driver.switch_to_window(currey_handles)

        print ("******************************************************************************************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
#关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)