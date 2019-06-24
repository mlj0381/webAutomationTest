#!/usr/bin/python3
#encoding:utf-8

__author__ = 'zhangbo'

import sys
# sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")

#初始化设置编码格式
# reload(sys)
# sys.setdefaultencoding('utf8')

import unittest
import os
import HTMLTestRunnerCN
from time import sleep


from talkTest.StartPage import test_startPage
from talkTest.HomePage import test_homePage
from talkTest.HomePage import test_adultHomePage
from talkTest.HomePage import test_aaHomePage
from talkTest.NavigationBar import test_homePageNavigationBar
from talkTest.NavigationBar import test_adult_NavigationBar
from talkTest.NavigationBar import test_aa_NavigationBar
from talkTest.Carousel import test_homeCarousel
from talkTest.Login import test_new_login
from talkTest.Resiget import test_new_resiget
from talkTest.AccountSettings import test_account_settings


import test_old_login_insert
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

from generation_report.generate_testReports import generate_testreports

from no_generation_report.no_report import no_testports

from talkTest.BuyPackage import test_buy_course

from talkTest.Login import test_old_login

from talkTest.Resiget import test_old_resiget

from talkTest.OpenClass import test_open_class

from talkTest.FineClass import test_fine_class

 
def creatsuite():

    print ("调用creatsuite()成功，开始执行自动化测试：" + "\n")

    testunit = unittest.TestSuite()

    '''启动页弹出层切换'''
    # testunit.addTest(test_startPage.TestStartPage("test_start_page"))

    '''主站模块TAB切换'''
    # testunit.addTest(test_homePage.TestHomePage("test_homepage_tabpage_switch"))

    '''成人主站TAB切换'''
    # testunit.addTest(test_adultHomePage.TestAdultHomePage("test_adulthomepage_tabpage_switch"))

    '''美小主站TAB切换--主站美小官网下线，入口没有找到'''
    # testunit.addTest(test_aaHomePage.TestAaHomePage("test_aahomepage_tabpage_switch"))

    '''主站顶部导航条'''
    # testunit.addTest(test_homePageNavigationBar.TestHomePageNavigationBar("test_home_page_navigation_bar"))

    '''成人顶部导航条'''
    # testunit.addTest(test_adult_NavigationBar.TestAdultNavigationBar("test_adult_navigation_bar"))

    '''美小顶部导航条--主站美小官网下线，入口没有找到'''
    testunit.addTest(test_aa_NavigationBar.TestAaNavigationBar("test_aa_navigation_bar"))

    '''首页模块轮播图'''
    # testunit.addTest(test_homeCarousel.TestHomeCarousel("test_homepage_carousel"))

    '''登录页面登录'''
    testunit.addTest(test_new_login.TestNewLogin("test_new_account_password_login_info_success"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_account_password_login_info_fail"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_account_resiget_link"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_account_forget_password_link"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_account_liji_resiget_link"))


    #------------------------------------------------------------------------------------#
    #手机号验证码登录，验证码老是提示登录不了
    # testunit.addTest(test_new_login.TestNewLogin("test_new_mobile_login_info_success"))
    #------------------------------------------------------------------------------------#
    # testunit.addTest(test_new_login.TestNewLogin("test_new_mobile_login_info_fail"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_mobile_resiget_link"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_mobile_forget_password_link"))
    # testunit.addTest(test_new_login.TestNewLogin("test_new_mobile_liji_resiget_link"))


    '''老登录页'''
    # testunit.addTest(test_old_login.TestOldLogin("test_old_login_info_success"))


    '''青少官网首页面板注册'''
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_info_success"))
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_info_fail"))


    '''注册页面注册'''
    #------------------------------------------------------------------------------------#
    #手机号注册，验证码老是提示错误
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_Page_info_success"))
    #------------------------------------------------------------------------------------#
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_Page_info_fail"))
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_Page_user_protocol"))
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_Page_privacy_statement"))
    # testunit.addTest(test_new_resiget.TestNewResiget("test_new_Resiget_Page_goto_login"))


    '''老注册页'''
    # testunit.addTest(test_old_resiget.TestOldResiget("test_old_resiget_info_succes"))


    '''购买'''
    # testunit.addTest(test_buy_course.TestBuyPackage("test_buy_course_info"))


    '''账号设置'''
    # testunit.addTest(test_account_settings.TestAccountSettings("test_account_settings_success"))


    '''公开课'''
    # testunit.addTest(test_open_class.TestOpenClass("test_open_class_success"))


    '''精品小班课'''
    # testunit.addTest(test_fine_class.TestFineClass("test_fine_class_success"))


    '''插入登录老数据'''
    # testunit.addTest(test_old_login_insert.TestOldLoginINsert("test_old_login_insert_info_success"))


#---------------------------------------------不生成测试报告-------------------------------------------------------------#

    no_testports(testunit)

#---------------------------------------------不生成测试报告-------------------------------------------------------------#



#---------------------------------------------调生成测试报告方法----------------------------------------------------------#

    # generate_testreports(testunit)

#---------------------------------------------调生成测试报告方法----------------------------------------------------------#
