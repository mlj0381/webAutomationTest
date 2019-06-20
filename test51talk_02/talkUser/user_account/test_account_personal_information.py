#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import sleep

from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_personal_information_success


#----------------------------------------------------------------------------------------------------------------------#
# 个人信息
#----------------------------------------------------------------------------------------------------------------------#

def test_account_personal_information_success(driver,account_type):

    #个人信息链接
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[2]/a").click()

    sleep(2)

    member_center_Initializ_account_settings_page_personal_information_success(driver,account_type)

    sleep(2)