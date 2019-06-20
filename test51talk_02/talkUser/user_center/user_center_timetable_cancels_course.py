#!usr/bin/python
#encoding:utf-8


'''会员中心取消课程'''


__author__ = 'zhangbo'


from time import *
from configuration_files.member_center_Config import *


#会员中心课表取消课程
def user_center_timetable_cancels_course_success(driver,course_type_tag_text,week_timetable):

    center_cancels_course_button_on = False

    class_record_tag_text = ""

    cancels_course = 0

    find_timetable_record_on = True

    sleep(2)

    for class_week_index in range(week_timetable,week_timetable + 3):

        try:

            #上课记录条数
            driver.find_element_by_xpath("//*[@id='m-c-schedule']/li")

            sleep(1)

            #会员中心上课类型记录标识
            class_record_tag_text = driver.find_element_by_xpath("//*[@id='m-c-schedule']/li/div[1]/div/div[1]").text

            sleep(1)

            if class_record_tag_text == "付费公开课":

                #付费公开课
                if class_record_tag_text == course_type_tag_text:

                    cancels_course = driver.find_element_by_xpath("//*[@id='m-c-schedule']/li/div[2]/div/ul/li[3]/a")

                    cancels_course.click()

                    sleep(1)

                    center_cancels_course_button_on = True

                    break;

                else:

                    find_timetable_record_on = False

                sleep(1)

            elif class_record_tag_text == "精品小班课":

                #付费精品小班课
                if class_record_tag_text == course_type_tag_text:

                    cancels_course = driver.find_element_by_xpath("//*[@id='m-c-schedule']/li/div[2]/div/ul/li[2]/a")

                    cancels_course.click()

                    sleep(1)

                    center_cancels_course_button_on = True

                    break;

                else:

                    find_timetable_record_on = False

                sleep(1)

        except:

            find_timetable_record_on = False

        #没有找到上课记录或者不满足条件
        if find_timetable_record_on == False:

            if class_week_index == week_timetable + 2:

                break;

            elif class_week_index == 7:

                #查看下周
                driver.find_element_by_xpath("//*[@id='toggleCourse']/div[1]/h3/a").click()

            else:

                if class_week_index == 8:

                    class_week_index = 1

                timetable_information_1 = member_center_timetable_information_1
                timetable_information_2 = member_center_timetable_information_2
                timetable_information_3 = class_week_index + 1
                timetable_information_4 = timetable_information_1 + str(timetable_information_3) + timetable_information_2

                sleep(2)

                #切换周几课表
                driver.find_element_by_xpath(timetable_information_4).click()

                sleep(2)

    if center_cancels_course_button_on == True:

        try:

            driver.switch_to_alert()

            sleep(1)

            #alert中的取消按钮
            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

            sleep(1)

            #取消课程按钮
            cancels_course.click()

            sleep(1)

            #alert中的确定按钮
            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

            sleep(1)

            #alert中取消课程成功提示
            cancels_course_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

            sleep(1)

            if class_record_tag_text == "付费公开课":

                cancels_course_success_text = cancels_course_success_text[0:21]

            elif class_record_tag_text == "精品小班课":

                cancels_course_success_text = cancels_course_success_text[0:5]

            sleep(1)

            #alert中的确定按钮
            driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

            sleep(1)

            if cancels_course_success_text == "取消成功！":

                print ("付费精品小班课取消成功！！！")

            elif cancels_course_success_text == "取消成功,其他公开课也很精彩,欢迎提前预约":

                print ("付费公开课取消成功！！！")

            sleep(1)

        except:

            print ("没有找到" + course_type_tag_text + "的上课记录，无法取消课程！！！")


