#!usr/bin/python
#encoding:utf-8


'''成人顶部导航条'''



__author__ = 'zhangbo'

from selenium import webdriver
from time import sleep
import unittest
from talkTest.StartPage.startPagePopLayer import *
from selenium.webdriver.common.action_chains import *
from configuration_files import configurationFiles as config_driver
from talkUser.user_quit_browser import *
import random


class TestAdultNavigationBar(unittest.TestCase):

    u'''首页操作如下:'''

    def setUp(self):

        self.driver = webdriver.Chrome()

        # self.driver = config_driver.obj_phantomjs_mac_driver

        # self.driver = config_driver.obj_phantomjs_window_driver

        self.url = "http://www.51talk.com"

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
#成人顶部导航条
#----------------------------------------------------------------------------------------------------------------------#
    #成人顶部导航条
    def test_adult_navigation_bar(self):

        print ("**************************************************成人顶部导航条**********************************" + '\n')

        driver = self.driver
        driver.get(self.url)
        sleep(1)

        driver.maximize_window()

        currey_handles = driver.current_window_handle

        action1 = ActionChains(driver)

        adult_random_index = random.randint(1,1)

        if adult_random_index == 0:

            #调用启动页进入青少官网
            startPageComeInto(driver)

            sleep(2)

            #青少官网--页面顶部链接(成人英语)进入成人官网
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[2]/ul/li/a").click()

            sleep(2)

            all_current = driver.window_handles

            sleep(2)

            for window_handle in all_current:

                if window_handle != currey_handles:

                    driver.close()

                    driver.switch_to_window(window_handle)

                    adult_currey_window_handles = driver.current_window_handle

        else:

            #调用启动页进入成人官网
            startPageComeIntoAdult(driver)

            adult_currey_window_handles = currey_handles

        # all_current = driver.window_handles
        #
        # for window_handle in all_current:
        #
        #     if window_handle != currey_handles:
        #
        #         driver.switch_to_window(window_handle)
        #
        #         adult_currey_window_handles = driver.current_window_handle

        #--------------------------------------------------------------------------------------------------------------#
        sleep(2)

        #登录标签
        driver.find_element_by_link_text("登录").click()

        top_login_text = driver.find_element_by_link_text("登录").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_login = driver.current_url
                sleep(1)

                print (top_login_text+u"--标签的链接是：" + text_url_top_login)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #免费注册标签
        driver.find_element_by_link_text("免费注册").click()

        top_resgiet_text = driver.find_element_by_link_text("免费注册").text

        top_handles = driver.window_handles

        # for handles in top_handles:
        #
        #     if handles != currey_handles:
        #
        #         driver.switch_to_window(handles)

        text_url_top_resgiet = driver.current_url
        sleep(1)

        print (top_resgiet_text+u"--标签的链接是：" + text_url_top_resgiet)
        sleep(1)

        driver.back()
        # driver.close()
        # driver.switch_to_window(currey_handles)
        sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #关于我们标签
        driver.find_element_by_link_text("关于我们").click()

        top_about_text = driver.find_element_by_link_text("关于我们").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_about = driver.current_url
                sleep(1)

                print (top_about_text+u"--标签的链接是：" + text_url_top_about)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #企业培训标签
        driver.find_element_by_link_text("企业培训").click()

        top_cet_text = driver.find_element_by_link_text("企业培训").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_cet = driver.current_url
                sleep(1)

                print (top_cet_text+u"--标签的链接是：" + text_url_top_cet)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #学习社区标签
        driver.find_element_by_link_text("学习社区").click()

        top_Forum_text = driver.find_element_by_link_text("学习社区").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_Forum = driver.current_url
                sleep(1)

                print (top_Forum_text+u"--标签的链接是：" + text_url_top_Forum)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #关注微博标签
        gzwb = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul/li[3]/span[1]")

        action1.move_to_element(gzwb).perform()

        sleep(2)

        #微博关注按钮
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul/li[3]/span[1]/div/a").click()

        sleep(2)

        top_weibo_text = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul/li[3]/span[1]").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_Forum = driver.current_url
                sleep(1)

                print (top_weibo_text+u"--标签的链接是：" + text_url_top_Forum)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #关注微信标签
        gzwx = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul/li[3]/span[2]")

        action1.move_to_element(gzwx).perform()

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
        #手机客户端标签
        driver.find_element_by_link_text("手机客户端").click()

        top_appdown_text = driver.find_element_by_link_text("手机客户端").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_appdown = driver.current_url
                sleep(1)

                print (top_appdown_text+u"--标签的链接是：" + text_url_top_appdown)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        #桌面AC教室标签
        driver.find_element_by_link_text("桌面AC教室").click()

        top_AC_text = driver.find_element_by_link_text("桌面AC教室").text

        top_handles = driver.window_handles

        for handles in top_handles:

            if handles != adult_currey_window_handles:

                driver.switch_to_window(handles)

                text_url_top_AC = driver.current_url
                sleep(1)

                print (top_AC_text+u"--标签的链接是：" + text_url_top_AC)
                sleep(1)

                driver.close()
                driver.switch_to_window(adult_currey_window_handles)
                sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
        # iPad端青少课堂
        # driver.find_element_by_link_text("iPad客户端").click()
        #
        # top_iPad_text = driver.find_element_by_link_text("iPad客户端").text
        #
        # top_handles = driver.window_handles
        #
        # for handles in top_handles:
        #
        #     if  handles != currey_handles:
        #
        #         driver.switch_to_window(handles)
        #
        #         text_url_top_iPad = driver.current_url
        #         sleep(1)
        #
        #         print (top_iPad_text+u"--标签的链接是：" + text_url_top_iPad)
        #         sleep(1)
        #
        #         driver.close()
        #         driver.switch_to_window(currey_handles)
        #         sleep(1)
        print ('\n' + "****************************************************************************************" + "\n")

# ----------------------------------------------------------------------------------------------------------------------#
# 关闭浏览器
# ----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)