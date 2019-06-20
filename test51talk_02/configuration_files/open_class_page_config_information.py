#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import *
import random



#公开课预约按钮：
#成人用户、青少用户：预约按钮
#//*[@id='container']/div[2]/div[2]/ul/li[1]/div[2]/div/p[2]/a[2]
#//*[@id='container']/div[2]/div[2]/ul/li[12]/div[2]/div/p[2]/a[2]

adult_junior_open_class_appointment_1 = "//*[@id='container']/div[2]/div[2]/ul/li["
adult_junior_open_class_appointment_2 = "]/div[2]/div/p[2]/a[2]"

#公开课约课时间：
#成人学员、青少学员：约课时间（体验、付费）
#//*[@id='container']/div[2]/div[2]/ul/li[1]/div[2]/p[1]/span[1]
#//*[@id='container']/div[2]/div[2]/ul/li[12]/div[2]/p[1]/span[1]

adult_junior_open_class_about_class_time_1 = "//*[@id='container']/div[2]/div[2]/ul/li["
adult_junior_open_class_about_class_time_2 = "]/div[2]/p[1]/span[1]"


#公开课取消课程按钮：
#成人学员、青少学员：取消课程（体验、付费）
#//*[@id='container']/div[2]/div[2]/ul/li[1]/div[2]/div/p[2]/a[1]
#//*[@id='container']/div[2]/div[2]/ul/li[12]/div[2]/div/p[2]/a[1]

adult_junior_open_class_cancel_course_1 = "//*[@id='container']/div[2]/div[2]/ul/li["
adult_junior_open_class_cancel_course_2 = "]/div[2]/div/p[2]/a[1]"


#免费、课时、次卡、金额公开课标识标识：
#//*[@id="container"]/div[2]/div[2]/ul/li[1]/div[2]/div/p[1]/span[1]
#//*[@id="container"]/div[2]/div[2]/ul/li[10]/div[2]/div/p[1]/span[1]
#//*[@id="container"]/div[2]/div[2]/ul/li[11]/div[2]/div/p[1]/span[1]
#//*[@id="container"]/div[2]/div[2]/ul/li[12]/div[2]/div/p[1]/span[1]

adult_junior_open_class_free_paid_tag_1 = "//*[@id='container']/div[2]/div[2]/ul/li["
adult_junior_open_class_free_paid_tag_2 = "]/div[2]/div/p[1]/span[1]"


#公开课tab选项（最新课程、热门课程、优选公开课）:
# //*[@id='container']/div[2]/div[1]/ul/li[1]/a
# //*[@id="container"]/div[2]/div[1]/ul/li[2]/a
# //*[@id="container"]/div[2]/div[1]/ul/li[3]/a

adult_junior_open_class_tab_select_1 = "//*[@id='container']/div[2]/div[1]/ul/li["
adult_junior_open_class_tab_select_2 = "]/a"


#公开课课程名称：
#//*[@id='container']/div[2]/div[2]/ul/li[1]/div[2]/h4/a
#//*[@id='container']/div[2]/div[2]/ul/li[12]/div[2]/h4/a

adult_junior_open_class_course_name_1 = "//*[@id='container']/div[2]/div[2]/ul/li["
adult_junior_open_class_course_name_2 = "]/div[2]/h4/a"
