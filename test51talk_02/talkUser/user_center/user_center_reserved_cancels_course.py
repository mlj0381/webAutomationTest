#!usr/bin/python
#encoding:utf-8


'''会员中心取消课程'''


__author__ = 'zhangbo'

from talkUser.user_center.user_center_layer import *



#会员中心已预约课程取消课程
def user_center_reserved_cancels_course_success(driver,course_type_tag_text):

    reserved_courses_link_on = False

    reserved_courses_tab_tag_text = ""

    reserved_courses_tab_sum = 3

    reserved_courses_cancels_courses_on = False


    #青少付费学员已预约课程
    try:

        #青少1+2付费学员
        reserved_courses_button_text = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[5]/a").text

        sleep(1)

        #青少1+2付费学员
        if reserved_courses_button_text == "已预约课程":

            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[5]/a").click()

        #青少非1+2付费学员
        else:

            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[4]/a").click()

        sleep(1)

        reserved_courses_link_on = True

    except:

        #成人付费学员已预约课程
        try:

            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[1]/li[4]/a")

            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[1]/li[4]/a").click()

            sleep(1)

            reserved_courses_link_on = True

        except:

            print ("没有找到已预约课程链接入口，请查看原因！！！")

    if reserved_courses_link_on == True:

        sleep(1)

        for reserved_courses_tab_index in range(1,reserved_courses_tab_sum + 1):

            reserved_courses_tab_1 = "//*[@id='container']/div/div/div[1]/ul/li["
            reserved_courses_tab_2 = "]/a"
            reserved_courses_tab_3 = reserved_courses_tab_index
            reserved_courses_tab_4 = reserved_courses_tab_1 + str(reserved_courses_tab_3) + reserved_courses_tab_2

            sleep(1)

            #付费公开课tab文字
            if reserved_courses_tab_index == 3:

                #已预约课程记录tab文字
                reserved_courses_tab_tag_text = driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[1]/ul/li[3]/a").text

            #1对1课程、精品小班课tab文字
            else:

                #已预约课程记录tab文字
                reserved_courses_tab_tag_text = driver.find_element_by_xpath(reserved_courses_tab_4).text

            sleep(1)

            if reserved_courses_tab_tag_text == course_type_tag_text:

                reserved_courses_cancels_courses_on = True

                sleep(1)

                # print ("已找到:" + course_type_tag_text)

                sleep(1)

                #1对1课程
                if reserved_courses_tab_index == 1:

                    pass

                #付费公开课tab
                elif reserved_courses_tab_index == 3:

                    driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[1]/ul/li[3]/a").click()

                #1对1课程tab、精品小班课tab
                elif reserved_courses_tab_index == 2:

                    driver.find_element_by_xpath(reserved_courses_tab_4).click()

                break;

            else:

                #1对1课程
                if reserved_courses_tab_index == 1:

                    pass

                #付费公开课tab
                elif reserved_courses_tab_index == 3:

                    driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[1]/ul/li[3]/a").click()

                #1对1课程tab、精品小班课tab
                elif reserved_courses_tab_index == 2:

                    driver.find_element_by_xpath(reserved_courses_tab_4).click()

        sleep(2)

        if reserved_courses_cancels_courses_on == True:

            try:

                #取消课程按钮
                cancels_course_button = driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[2]/div/div[2]/ul/li[2]/a")

                cancels_course_button.click()

                sleep(1)

                driver.switch_to_alert()

                sleep(1)

                #alert中的取消按钮
                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

                sleep(1)

                #取消课程按钮
                cancels_course_button.click()

                sleep(1)

                #alert中的确定按钮
                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                sleep(1)

                #alert中取消课程成功提示
                cancels_course_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

                sleep(1)

                if reserved_courses_tab_tag_text == "付费公开课":

                    cancels_course_success_text = cancels_course_success_text[0:21]

                elif reserved_courses_tab_tag_text == "精品小班课":

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

        else:

            print ("没有找到" + course_type_tag_text + "的上课记录，无法取消课程！！！")


