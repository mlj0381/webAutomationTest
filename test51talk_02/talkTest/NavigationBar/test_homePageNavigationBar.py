#!usr/bin/python
#encoding:utf-8


'''主站顶部导航条'''



__author__ = 'zhangbo'

from selenium import webdriver
from time import sleep
import unittest
from talkTest.StartPage.startPagePopLayer import startPageComeInto
from selenium.webdriver.common.action_chains import *
from configuration_files import configurationFiles as config_driver
from talkUser.user_quit_browser import *


class TestHomePageNavigationBar(unittest.TestCase):

    u'''首页操作如下:'''

    def setUp(self):

        self.driver = webdriver.Chrome()

        # self.driver = config_driver.obj_phantomjs_mac_driver

        # self.driver = config_driver.obj_phantomjs_window_driver

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#主站顶部导航条
#----------------------------------------------------------------------------------------------------------------------#
    #主站顶部导航条
    def test_home_page_navigation_bar(self):

        print ("**************************************************主站顶部导航条**********************************" + "\n")

        driver = self.driver
        driver.get(self.url)
        sleep(2)

        # 调用启动页进入青少儿官网
        startPageComeInto(driver)

        driver.maximize_window()

        for hp_nb_index in range(1,3,1):

            currey_handles = driver.current_window_handle

            action1 = ActionChains(driver)

            if hp_nb_index == 1:

                #成人英语
                driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/a").click()

                sleep(2)

                all_handles = driver.window_handles

                sleep(2)

                for window_handle in  all_handles:

                    if window_handle != currey_handles:

                        driver.switch_to_window(window_handle)

                        sleep(2)

                        driver.close()

                        driver.switch_to_window(currey_handles)

            else:

                #关注微信
                gzwx = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/span[2]")

                action1.move_to_element(gzwx).perform()

                sleep(2)

                #关注微博
                gzwb = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/span[4]")

                action1.move_to_element(gzwb).perform()

                sleep(2)

                #关注按钮
                driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/span[4]/div/a").click()

                sleep(2)

                driver.back()

                sleep(2)

        print ("***********************************************************************************************" + "\n")

# ----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
# ----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)