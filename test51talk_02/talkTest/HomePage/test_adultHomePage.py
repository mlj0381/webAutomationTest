#!usr/bin/python
#encoding:utf-8

'''成人官网TAB切换'''


__author__ = 'zhangbo'

from selenium import webdriver

from time import sleep

import unittest

from talkTest.StartPage.startPagePopLayer import *

from configuration_files.driver_configurationFiles import browser_driver

from talkUser.user_quit_browser import *

import random

class TestAdultHomePage(unittest.TestCase):

    u'''首页操作如下:'''

    def setUp(self):

        self.driver = browser_driver()

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#成人官网TAB切换
#----------------------------------------------------------------------------------------------------------------------#
    # 成人主站TAB切换
    def test_adulthomepage_tabpage_switch(self):

        print ("**************************************************成人主站TAB切换**************************************************"+'\n')

        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        sleep(1)


        currey_handles = driver.current_window_handle

        adult_random_index = random.randint(0,1)

        if adult_random_index == 0:

            #调用启动页进入青少官网
            startPageComeInto(driver)

            sleep(2)

            #青少官网--页面顶部链接(成人英语)进入成人官网
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/a").click()

            sleep(2)

            all_current = driver.window_handles

            sleep(2)

            for window_hanle in all_current:

                if window_hanle != currey_handles:

                    driver.close()

                    driver.switch_to_window(window_hanle)

        else:

            #调用启动页进入成人官网
            startPageComeIntoAdult(driver)

        #--------------------------------------------------------------------------------------------------------------#
        #成人英语TAB页面
        sleep(2)

        #成人英语TAB页切换展示
        for y in range(1,6):

            tab1_str1 = "/html/body/div[1]/div[3]/div/ul/li["
            tab1_str2 = str(y)
            tab1_str3 = "]/a"
            tab1_str4 = tab1_str1+tab1_str2+tab1_str3
            sleep(1)

            driver.find_element_by_xpath(tab1_str4).click()
            sleep(1)

            text_url_3 = driver.find_element_by_xpath(tab1_str4).text
            sleep(1)

            title_url_3 = driver.current_url
            sleep(1)

            print (text_url_3+u"的'标签链接'是：" + title_url_3 + '\n')
            sleep(1)

        print ("******************************************************************************************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
#关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)