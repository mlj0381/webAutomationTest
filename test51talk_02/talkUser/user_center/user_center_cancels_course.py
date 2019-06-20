#!usr/bin/python
#encoding:utf-8


'''会员中心取消课程'''


__author__ = 'zhangbo'

import random

from talkUser.user_center.user_center_layer import *
from talkUser.user_center.user_center_reserved_cancels_course import user_center_reserved_cancels_course_success
from talkUser.user_center.user_center_timetable_cancels_course import user_center_timetable_cancels_course_success
from talkUser.user_wealth import user_paid_the_wealth_success


#会员中心取消课程
def user_center_cancels_course_success(driver,course_type_tag_text,week_timetable,db_user_id,user_mobile):

    cancels_course_randint = random.randint(1,1)

    if cancels_course_randint == 0:

        sleep(1)

        #浏览器滚动条置底
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)

        sleep(1)

        try:

            #调用会员中心已预约课程取消操作
            user_center_reserved_cancels_course_success(driver,course_type_tag_text)

            #返回首页
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[1]/a").click()

            sleep(2)

            #调用弹出层关闭
            try:

                user_center_layer_operation(driver)

            except:

                pass

        except:

            pass

    else:

        sleep(1)

        try:

            #调用会员中心课表取消课程操作
            user_center_timetable_cancels_course_success(driver,course_type_tag_text,week_timetable)

            #调用弹出层关闭
            try:

                user_center_layer_operation(driver)

            except:

                pass

        except:

            pass

    #查询付费用户财富信息
    user_paid_the_wealth_success(driver,db_user_id,user_mobile)

    sleep(1)