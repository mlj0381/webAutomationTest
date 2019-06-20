#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

import time
from configuration_files.accountConfigInformation import *
import os
from db_files.userInformation_db_query import *


'''
调取后台处理订单：
                    1）申请订单
                    2）处理订单
                    3）允许拆单
'''

from selenium import webdriver
from time import sleep
import random
from configuration_files import accountConfigInformation as accountConfig
# from configuration_files import testAccountConfigInformation as accountConfig
from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_order_id_success


#----------------------------------------------------------------------------------------------------------------------#
    #后台登录，进入处理订单表
#----------------------------------------------------------------------------------------------------------------------#

def houtai_login_success_stu_list(driver):

        #Accout
        driver.find_element_by_xpath("//*[@id='user_name']").send_keys(accountConfig.houTaiAccout)
        sleep(2)

        #Password
        driver.find_element_by_xpath("//*[@id='pwd']").send_keys(accountConfig.houTaiPassword)
        sleep(2)

        #Login
        driver.find_element_by_xpath("//*[@id='Submit']").click()
        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    #后台处理订单，查询订单
#----------------------------------------------------------------------------------------------------------------------#

def user_order_list_quest(driver,user_mobile,user_id,order_id):

        houtai_login_success_stu_list(driver)

        sleep(2)

        start_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        end_time   = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        # start_time = "2018-03-23"
        # end_time   = "2018-03-23"

        process_order_url_01 = houtai_order_query_url_01
        process_order_url_02 = houtai_order_query_url_02
        process_order_url_03 = houtai_order_query_url_03

        process_order_url_04 = process_order_url_01 + start_time + process_order_url_02 + end_time + process_order_url_03

        sleep(2)

        driver.get(process_order_url_04)

        sleep(2)

        #输入用户手机号
        driver.find_element_by_xpath("html/body/input[4]").send_keys(user_mobile)

        sleep(2)

        #search
        driver.find_element_by_xpath("html/body/input[5]").click()

        sleep(2)

        query_order_on = False

        try:

            #获取订单列表第一行订单信息
            driver.find_element_by_xpath("html/body/table/tbody/tr[3]/td[1]")

            query_order_on = True

        except:

            print (u"没有找到该用户提交的相关订单数据！！！")

        if query_order_on == True:

            order_sum_01 = "body > table > tbody > tr:nth-child("
            order_sum_02 = ") > td:nth-child(1)"

            order_start_row = 3
            order_end_row   = 23

            # 获取查询的订单数据
            order_info = userInformation_db_query_order_id_success(order_id)

            sleep(1)

            for order_row in range(order_start_row,order_end_row):

                order_sum_03 = order_sum_01 + str(order_row) + order_sum_02

                sleep(2)

                #订单号是否存在
                try:

                     driver.find_element_by_css_selector(order_sum_03)

                     find_order_id = driver.find_element_by_css_selector(order_sum_03).text

                     if order_info == () or order_info == None or order_info == "":

                         print (u"数据库中没有找到要查询的订单数据，无法和后台数据进行比对，直接更新数据记录表！！！")

                         sleep(1)

                         userInformation_db_user_data_update_order_id_success(user_id,order_id,find_order_id)

                         sleep(1)

                         break;

                     else:

                         if find_order_id == order_info:

                            print (u"已找到该订单，订单号为：" + str(find_order_id))

                            break;

                except:

                    print (u"后台系统无法找到该订单，请查看原因！！！")

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    #后台处理订单，处理订单
#----------------------------------------------------------------------------------------------------------------------#

def user_order_list_process_order(driver,user_mobile):

        user_order_list_quest(driver,user_mobile)

        sleep(2)

        try:

            #处理
            driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[16]/span")

            sleep(2)

            driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[16]/span").click()

            print (u"找到处理订单按钮！！！")

        except:

            print (u"没有找到处理订单按钮！！！")

        sleep(2)

        driver.close()

#----------------------------------------------------------------------------------------------------------------------#
    #后台处理订单，
#----------------------------------------------------------------------------------------------------------------------#

# def user_order_list_quest(driver,user_mobile):
#
        pass


# driver = webdriver.Chrome()
#
# sleep(2)
#
# driver.get("http://www.51talk.com/admin/admin_login.php")
#
# sleep(2)
#
# driver.maximize_window()
#
# sleep(2)
#
# user_mobile = "18666600277"
#
# order_id = ""
#
# user_id  = "38312600"
#
# user_order_list_quest(driver,user_mobile,user_id,order_id)
#
# sleep(5)
#
# driver.quit()