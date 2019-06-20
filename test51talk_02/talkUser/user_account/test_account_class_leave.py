#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import sleep
from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_class_leave_success


#----------------------------------------------------------------------------------------------------------------------#
# 上课请假
#----------------------------------------------------------------------------------------------------------------------#

def test_account_class_leave_success(driver):

        class_leave_tag = member_center_Initializ_account_settings_page_class_leave_success(driver)

        #付费学员上课请假链接
        if class_leave_tag == 0:

                driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[4]/a").click()

                sleep(1)

                #确定请假按钮
                driver.find_element_by_xpath("//*[@id='sub_leave']").click()

                sleep(1)

                #弹框取消按钮
                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

                sleep(1)

                #确定请假按钮
                driver.find_element_by_xpath("//*[@id='sub_leave']").click()

                sleep(1)

                #弹框确定按钮
                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                sleep(1)

                class_leave_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

                if class_leave_text == "您没有请假机会!":

                        print ("当前账户不能请假！！！")

                #确定按钮
                driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                sleep(1)

        elif class_leave_tag == 1:

                print ("体验用户，暂时无我要请假功能")

        sleep(1)