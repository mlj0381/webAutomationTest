#!usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'


'''青少儿官网模块轮播图'''

from selenium import webdriver

import unittest

from time import sleep

from talkTest.StartPage.startPagePopLayer import startPageComeInto

from configuration_files import driver_configurationFiles as config_driver

from talkUser.user_quit_browser import *


class TestHomeCarousel(unittest.TestCase):

    def setUp(self):

        self.driver = config_driver.obj_driver

        self.url = "http://www.51talk.com"

        sleep(2)


#----------------------------------------------------------------------------------------------------------------------#
#青少儿官网轮播图
#----------------------------------------------------------------------------------------------------------------------#
    #青少儿官网轮播图
    def test_homepage_carousel(self):

        print ("**************************************************青少儿官网轮播图********************************" + "\n")

        driver = self.driver
        driver.get(self.url)
        sleep(1)

        driver.maximize_window()

        sleep(1)

        #调用启动页
        startPageComeInto(driver)

        currey_handles = driver.current_window_handle

        # 浏览器滚动条滚动
        js = "var q=document.documentElement.scrollTop=100"
        driver.execute_script(js)

        lunbo_picture = driver.find_elements_by_xpath("//*[@id='index']/div/ul[2]/li")

        lunbo_cishu = 0

        for i in lunbo_picture:

            i.click()
            lunbo_cishu = lunbo_cishu + 1
            sleep(1)

        print (u"一共轮播了：" + str(lunbo_cishu) + u"次图片")

        print ("\n" + "*************************************************青少儿官网轮播图**************************" + "\n")


# ----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
# ----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)