#!usr/bin/python
#encoding:utf-8


'''返回值'''


__author__ = 'zhangbo'


import random

from talkUser.user_experience_class.user_experience_cancels_cadets import *


def user_revising_the_textbook_success(driver):

        #浏览器滚动条置底
        js="var q=document.documentElement.scrollTop=550"
        driver.execute_script(js)

        sleep(2)

        #左侧和更多已预约课程开关
        reserved_courses_on = False

        #确定修改开关
        modify_course_on = False

        #教材
        textbook_name_text = driver.find_element_by_xpath("//*[@id='orderClass']/div/div[1]/dl/dd[1]").text

        # print ("")
        # print ("***************************************")
        # print (u"教材名称：" + textbook_name_text)
        # print ("***************************************")
        # print ("")

        sleep(1)

        revising_the_textbook_index = random.randint(0,2)

        #会员中心修改教材按钮 or 左侧已预约课程按钮 or 更多按钮是否存在

        if revising_the_textbook_index == 0:

                try:

                        #会员中心：修改教材（3个按钮）
                        revising_textbook_button_text = driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a").text

                        if revising_textbook_button_text == "修改教材":

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a").click()

                                sleep(2)

                                modify_course_on = True

                        else:

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[1]/a").click()

                except:

                        #会员中心：修改教材（2个按钮）
                        # try:
                        #
                        #         # 会员中心：修改教材（3个按钮）
                        #         revising_textbook_button_text = driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a").text
                        #
                        #         if revising_textbook_button_text == "修改教材":
                        #
                        #                 driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a").click()
                        #
                        #                 sleep(2)
                        #
                        #                 modify_course_on = True
                        #
                        #                 print ("已找到2")
                        #
                        # except:

                        print ("没有找到修改教材按钮，无法修改，请从其它途径修改教材！！！")

                sleep(2)

        elif revising_the_textbook_index == 1 or revising_the_textbook_index == 2:

                if revising_the_textbook_index == 1:

                        #左侧区域已预约课程按钮
                        try:
                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[3]/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[3]/a").click()

                                reserved_courses_on = True

                        except:

                                print ("没有找到已预约课程按钮，请从其它途径修改教材！！！")

                elif revising_the_textbook_index == 2:

                        #我预约的体验课--右侧“更多”按钮
                        try:

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/h3/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='orderClass']/div/h3/a").click()

                                reserved_courses_on = True

                        except:

                                print ("没有找到更多按钮，请从其它途径修改教材！！！")

                if reserved_courses_on == True:

                        #课表页信息
                        try:
                                #修改课程按钮
                                driver.find_element_by_xpath("//*[@id='container']/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/a")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='container']/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/a").click()

                                sleep(1)

                                modify_course_on = True

                        except:

                                print ("当前未预约体验课 或者 当前体验课教材无法修改，请从其它途径修改教材！！！")
        sleep(2)

        if modify_course_on == True:

                #浏览器滚动条置底
                js="var q=document.documentElement.scrollTop=400"
                driver.execute_script(js)

                sleep(1)

                try:

                        #修改课程和教材控件
                        driver.find_element_by_xpath("//*[@id='upCourseForm']/div[2]/dl[4]/dd[1]/div/h5").click()
                        sleep(2)

                        #修改课程和教材控件下拉框数据
                        driver.find_element_by_xpath("//*[@id='upCourseForm']/div[2]/dl[4]/dd[1]/div/ul/li[2]").click()
                        sleep(2)

                        #教材控件
                        driver.find_element_by_xpath("//*[@id='selectCourseNext']/div/h5").click()
                        sleep(2)

                        #取列表下的教材总数
                        select_count = driver.find_elements_by_xpath("//span[@class='orderText']")

                        for i in range(0,len(select_count)):

                                teaching_material_random = random.randint(2,len(select_count))
                                teaching_material_index_01 = "//*[@id='selectCourseNext']/div/ul/li["
                                teaching_material_index_02 = teaching_material_random
                                teaching_material_index_03 = "]/span"
                                teaching_material_index_04 = teaching_material_index_01 + str(teaching_material_index_02) + teaching_material_index_03
                                sleep(1)

                                driver.find_element_by_xpath(teaching_material_index_04).click()
                                sleep(1)

                                #获取选中的教材名称
                                textbook_name_text_new = driver.find_element_by_xpath("//*[@id='selectCourseNext']/div/h5").text
                                sleep(1)

                                if textbook_name_text == textbook_name_text_new:

                                        print ("教材名称修改重复，请重新选择！！！")

                                        #教材控件
                                        driver.find_element_by_xpath("//*[@id='selectCourseNext']/div/h5").click()
                                        sleep(2)

                                else:
                                        #重新选择新的教材成功
                                        break;

                        sleep(2)

                        #确定修改
                        driver.find_element_by_xpath("//*[@id='updateSubmit']/span[1]").click()

                        sleep(5)

                        print ("")
                        print ("*****************************************************************")
                        print (u"原教材名称为：" + textbook_name_text + " " + "->" + " " + u"新教材名称为：" + textbook_name_text_new)
                        print ("*****************************************************************")
                        print ("")

                except:

                        print ("没有找到确定修改按钮，无法修改教材，请查看原因！！！")