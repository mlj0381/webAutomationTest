#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from selenium import webdriver
from time import sleep
import unittest
from configuration_files import configurationFiles as config_driver
from talkUser.user_quit_browser import *

class TestPaidAboutClass(unittest.TestCase):

        def setUp(self):

            self.driver = webdriver.Chrome()

            # self.driver = config_driver.obj_phantomjs_mac_driver

            # self.driver = config_driver.obj_phantomjs_window_driver

            self.url    = "http://www.51talk.com"

            sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    # 付费学员约课成功
#----------------------------------------------------------------------------------------------------------------------#

        def test_paid_cadets_success(self):

            print ("*************付费学员约课成功*************")

            print ("*********************************************" + "\n")

# ----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
# ----------------------------------------------------------------------------------------------------------------------#

        def tearDown(self):

            QuitBrowser(self.driver)