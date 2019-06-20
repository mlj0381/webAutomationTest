#!usr/bin/python
#encoding:utf-8


'''会员中心获取周几课表选中'''


__author__ = 'zhangbo'

from configuration_files.member_center_Config import *
from time import *


#获取当前周期课表上课记录
def user_center_current_timetable_week_class_record_success(driver,login_after_url_link,week_timetable,course_type_tag_text):

    class_record_tag_text = ""

    find_timetable_record_on = False


    for week_randint_index in range(week_timetable,week_timetable + 3):

        try:

            #上课记录
            driver.find_element_by_xpath("//*[@id='m-c-schedule']/li")

            sleep(1)

            #会员中心上课类型记录标识
            class_record_tag_text = driver.find_element_by_xpath("//*[@id='m-c-schedule']/li/div[1]/div/div[1]").text

            sleep(1)

            #付费公开课
            if class_record_tag_text == "付费公开课":

                #精品小班课
                if class_record_tag_text == course_type_tag_text:

                    find_timetable_record_on = True

                    print ("已找到:" + course_type_tag_text + "的上课记录，可以进行取消课程操作了！！！")

                    sleep(1)

            elif class_record_tag_text == "精品小班课":

                #精品小班课
                if class_record_tag_text  == course_type_tag_text:

                    find_timetable_record_on = True

                    print ("已找到:" + course_type_tag_text + "的上课记录，可以进行取消课程操作了！！！")

                    sleep(1)

            sleep(1)

        except:

            pass

        if find_timetable_record_on == True:

            return 1

        else:

            if week_randint_index == week_timetable + 2:

                sleep(1)

                return 2

            elif week_randint_index == 7:

                #查看下周
                driver.find_element_by_xpath("//*[@id='toggleCourse']/div[1]/h3/a").click()

            else:

                if week_randint_index == 8:

                    week_randint_index = 1

                timetable_information_1 = member_center_timetable_information_1
                timetable_information_2 = member_center_timetable_information_2
                timetable_information_3 = week_randint_index + 1
                timetable_information_4 = timetable_information_1 + str(timetable_information_3) + timetable_information_2

                sleep(1)

                try:

                    #切换周几课表
                    driver.find_element_by_xpath(timetable_information_4).click()

                    sleep(1)

                except:

                    return 0

