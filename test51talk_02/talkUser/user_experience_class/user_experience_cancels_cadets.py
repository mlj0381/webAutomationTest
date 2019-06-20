#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from selenium import webdriver
from time import *
import unittest
import random
import datetime
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success
from db_files.userInformation_db_wealth_data_update import userInformation_db_wealth_data_update_success


#----------------------------------------------------------------------------------------------------------------------#
    # 体验学员取消约课成功
#----------------------------------------------------------------------------------------------------------------------#

def user_experience_cancels_cadets_success(driver,user_id,user_mobile):

        #浏览器滚动条置底
        js="var q=document.documentElement.scrollTop=550"
        driver.execute_script(js)

        sleep(2)

        #左侧和更多已预约课程开关
        reserved_courses_on = False

        #一对一课表信息开关
        one_to_one_table_information_on = False

        #确定取消开关
        cancel_course_on = False

        reserved_courses_index = random.randint(0,2)

        if reserved_courses_index == 0:

                try:

                        #会员中心：取消课程（3个按钮）
                        cancel_course_button_text = driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[3]/a").text

                        if cancel_course_button_text == "取消课程":

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[3]/a").click()

                                sleep(2)

                                cancel_course_on = True

                except:

                        #会员中心：取消课程（3个按钮）
                        # try:
                        #
                        #         driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[3]/a").click()
                        #
                        #         sleep(2)
                        #
                        #         cancel_course_on = True
                        #
                        # except:

                        print ("没有找到取消课程按钮，无法取消，请从其它途径取消体验课！！！")

                sleep(2)

        elif reserved_courses_index == 1 or reserved_courses_index == 2:

                if reserved_courses_index == 1:

                        #左侧区域已预约课程按钮
                        try:
                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[3]/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[3]/a").click()

                                reserved_courses_on = True

                        except:

                                print ("没有找到已预约课程按钮，无法取消，请从其它途径取消体验课！！！")

                elif reserved_courses_index == 2:

                        #我预约的体验课--右侧“更多”按钮
                        try:

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/h3/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/h3/a").click()

                                reserved_courses_on = True

                        except:

                                print ("没有找到更多按钮，无法取消，请从其它途径取消体验课！！！")

                if reserved_courses_on == True:

                        #课表页信息
                        try:
                                #取消课程按钮
                                driver.find_element_by_xpath("//*[@id='container']/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[4]/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='container']/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[4]/a").click()

                                sleep(1)

                                one_to_one_table_information_on = True

                                #确定弹框
                                if one_to_one_table_information_on == True:

                                        try:
                                                #确定弹框确定按钮
                                                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]")

                                                sleep(1)

                                                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                                                sleep(1)

                                                cancel_course_on = True

                                        except:

                                                print ("没有找到弹框！！！")

                        except:

                                print ("当前未预约体验课 或者 当前体验课无法取消，请从其它途径取消体验课！！！")
        sleep(2)

        if cancel_course_on == True:

                try:

                        # 获取当天现在时间
                        db_wealth_update_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                        sleep(1)

                        #取消课程页：确定取消
                        driver.find_element_by_xpath("//*[@id='cancelSubmit']").click()

                        sleep(4)

                        try:

                                #当天限制只能最多取消20次弹框
                                driver.switch_to_alert()

                                sleep(1)

                                print ("当天取消次数过多，无法完成操作，返回会员中心啦！！！")

                        except:

                                #获取用户user_wealth表point
                                db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)
                                sleep(1)

                                db_wealth_point = int(db_wealth_data[1]) + 1
                                sleep(1)

                                db_wealth_point = str(db_wealth_point)

                                #更新user_wealth表point
                                userInformation_db_wealth_data_update_success(user_mobile,db_wealth_point,db_wealth_data[0],db_wealth_update_time)

                                # -----------------------------------#

                                print ("取消约课后--财富数据更新成功！！！")

                                # -----------------------------------#

                                sleep(2)

                                #取消课程后返回约课页面第一个时间段
                                try:

                                        driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span")

                                        print ("课程取消成功，返回到预约体验课页面！！！")

                                except:

                                        print ("返回的预约体验课页面有错误信息，请查看原因！！！")

                except:

                        print ("没有找到确定取消按钮，无法取消体验课，请查看原因！！！")

                sleep(2)