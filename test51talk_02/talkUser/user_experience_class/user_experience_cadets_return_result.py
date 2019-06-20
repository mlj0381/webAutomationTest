#!usr/bin/python
#encoding:utf-8


'''返回值'''


__author__ = 'zhangbo'

import datetime
import random
from time import *

from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_wealth import user_experience_the_wealth_success
from db_files.userInformation_db_wealth_data_update import userInformation_db_wealth_data_update_success

from Initializ_page.experience_cadets_week_timetable_Initializ import experience_cadets_week_timetable_Initializ_success



def user_experience_cadets_return_result_success(driver,current_window_handle,user_id,user_mobile):

    current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

    current_now_time_year = int(current_now_time[0:4])
    # print current_now_time_year

    current_now_time_month = int(current_now_time[5:7])
    # print current_now_time_month

    current_now_time_day = int(current_now_time[8:10])
    # print current_now_time_day

    current_now_time_hour = int(current_now_time[11:13])
    # print current_now_time_hour

    current_now_time_minute = int(current_now_time[14:16])
    # print current_now_time_minute

    current_now_time_second = int(current_now_time[17:19])
    # print current_now_time_second

    # 获取当前时间
    # current_time_hour = int(strftime('%H',localtime(time())))
    # current_time_minute = int(strftime('%M',localtime(time())))

    about_class_on = False

    about_class_entry_on = False

    yk_success_on = False

    yk_cancel_on = False

    # 约课时间
    dict = {'00:30': '45', '01:00': '44', '01:30': '43', '02:00': '42', '02:30': '41', '03:00': '40', '03:30': '39',
            '04:00': '38',
            '04:30': '37', '05:00': '36', '05:30': '35', '06:00': '34', '06:30': '33', '07:00': '32', '07:30': '31',
            '08:00': '30',
            '08:30': '29', '09:00': '28', '09:30': '27', '10:00': '26', '10:30': '25', '11:00': '24', '11:30': '23',
            '12:00': '22',
            '12:30': '21', '13:00': '20', '13:30': '19', '14:00': '18', '14:30': '17', '15:00': '16', '15:30': '15',
            '16:00': '14',
            '16:30': '13', '17:00': '12', '17:30': '11', '18:00': '10', '18:30': '09', '19:00': '08', '19:30': '07',
            '20:00': '06',
            '20:30': '05', '21:00': '04', '21:30': '03', '22:00': '02', '22:30': '01'}

    # 当天时间段
    try:

        driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span")

        time_interval_hour_text = driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span").text

        time_interval_minute_text = driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span").text

        time_interval_hour_minute_text = driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span").text

        time_interval_hour = int(time_interval_hour_text[0:2])

        time_interval_minute = int(time_interval_minute_text[3:5])

        time_interval_hour_minute = time_interval_hour_minute_text[0:5]

        about_class_on = True

    except:

        print (u"没有找到约课时间或者体验课已经预约或当前账户财富为空！！！")

    if about_class_on == True:

        if current_now_time_hour < time_interval_hour:

            time_interval_sum = int(dict[time_interval_hour_minute])

            time_interval_sum = time_interval_sum + 1

        elif current_now_time_hour == time_interval_hour and current_now_time_minute < 30:

            time_interval_sum = int(dict[time_interval_hour_minute])

            time_interval_sum = time_interval_sum + 1

        # 跳出多重循环try: ... raise Exception()  except Exception: ...
        try:

            for week_time_index in range(1, 8):

                # 周几切换
                week_time_01 = "//*[@id='classTime']/div/ul[1]/li["
                week_time_02 = week_time_index
                week_time_03 = "]"
                week_time_04 = week_time_01 + str(week_time_02) + week_time_03

                sleep(2)

                if week_time_index > 1:

                    #调用初始化周几课表，返回课表当前日期
                    week_time_date = experience_cadets_week_timetable_Initializ_success(driver,week_time_index)

                    #切换到周几时，初始化点击默认第一个约课时间
                    driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span").click()

                    sleep(2)

                    time_interval_hour_minute_text = driver.find_element_by_xpath("//*[@id='classTime']/div/ul[2]/li[1]/span").text

                    sleep(2)

                    time_interval_hour_minute = time_interval_hour_minute_text[0:5]

                    time_interval_sum = int(dict[time_interval_hour_minute])

                    time_interval_sum = time_interval_sum + 1

                    print (u"明天开始以后约课时间段循环次数为：" + str(time_interval_sum - 1))

                    sleep(1)

                else:

                    print (u"当前约课时间段循环次数为：" + str(time_interval_sum - 1))

                sleep(1)

                for time_interval_index in range(1, time_interval_sum):

                    time_interval_01 = "//*[@id='classTime']/div/ul[2]/li["
                    time_interval_02 = time_interval_index
                    time_interval_03 = "]/span"
                    time_interval_04 = time_interval_01 + str(time_interval_02) + time_interval_03

                    sleep(1)

                    yk_check = driver.find_element_by_xpath(time_interval_04).get_attribute("class")

                    yk_time_text = driver.find_element_by_xpath(time_interval_04).text

                    yk_time_hour_text = int(yk_time_text[0:2])

                    yk_time_minute_text = int(yk_time_text[3:5])

                    sleep(1)

                    if yk_check == "full":

                        print (u"该时段:" + yk_time_text[0:5] + ",约课已满，不能约课，请换一个时间段")

                    elif yk_check == "check":

                        sleep(1)
                        now_time = datetime.datetime(current_now_time_year, current_now_time_month,
                                                     current_now_time_day, current_now_time_hour,
                                                     current_now_time_minute, 0)

                        sleep(1)

                        #周二 至 周日取这个时间
                        if week_time_index != 1:

                            yk_now_time = datetime.datetime(week_time_date[0], week_time_date[1],
                                                            week_time_date[2], yk_time_hour_text,
                                                            yk_time_minute_text, 0)

                        #周一取这个时间
                        else:

                            yk_now_time = datetime.datetime(current_now_time_year,current_now_time_month,
                                                            current_now_time_day,yk_time_hour_text,
                                                            yk_time_minute_text, 0)

                        sleep(1)

                        yk_now_time_1 = int((yk_now_time - now_time).total_seconds() / 60)

                        sleep(1)

                        # 约一小时后的课程 or 约大于半小时小于一小时内的课程
                        if yk_now_time_1 > 60 or yk_now_time_1 > 30 and yk_now_time_1 <= 60:

                            # 约一小时后的课程
                            if yk_now_time_1 > 60:

                                print (u"该时段:" + yk_time_text[0:5] + ",可以约课,也可以同时修改教材")

                                sleep(1)

                                about_class_entry_on = True

                                raise Exception()

                            # 约大于半小时小于一小时内的课程
                            else:

                                print (u"该时段:" + yk_time_text[0:5] + ",可以约课,但是不能修改教材")

                                sleep(1)

                                # about_class_entry_on = True

                                # raise Exception()

                        # 半小时以内不能约课
                        elif yk_now_time_1 <= 30:

                            print (u"该时段:" + yk_time_text[0:5] + "为半小时以内约课，暂时忽略此时段约课")

                            sleep(1)

                    # 当天最后一个时间段
                    if time_interval_index == time_interval_sum - 1:

                        # 切换到第二天时间段
                        week_time_02 = week_time_index + 1
                        week_time_04 = week_time_01 + str(week_time_02) + week_time_03

                        driver.find_element_by_xpath(week_time_04).click()

                    # 当天非最后一个时间段
                    else:

                        # 切换到当天下一个时间段
                        time_interval_02 = time_interval_index + 1
                        time_interval_03 = "]/span"
                        time_interval_04 = time_interval_01 + str(time_interval_02) + time_interval_03

                        driver.find_element_by_xpath(time_interval_04).click()

                    sleep(1)

        except Exception:

            pass

        sleep(2)

        if about_class_entry_on == True:

            # 验证码滑块老是失败，过不去
            # sleep(1)
            # #手机号验证
            # try:
            #
            #     #手机验证(便于接收上课短信通知)
            #     driver.find_element_by_xpath("//*[@id='mobileCode']/h3")
            #
            #     print ("该手机号没有验证，请先验证手机号吧～")
            #
            #     sleep(1)
            #
            #     #触发滑块验证平台
            #     user_experience_class_slider_validation_mobile(driver)
            #
            #     sleep(1)
            #
            #     #调取手机短信平台
            #     # js ='window.open("http://sms.51talk.com/Admin/Login/login")'
            #
            #     #调取后台stu_list表，验证手机号
            #     js ='window.open("http://www.51talk.com/admin/admin_login.php")'
            #
            #     driver.execute_script(js)
            #
            #     handles = driver.window_handles
            #
            #     for current_handle in handles:
            #
            #         if current_handle != current_window_handle:
            #
            #             driver.switch_to_window(current_handle)
            #
            #             sleep(1)
            #
            #             #调取后台stu_list表，验证手机号
            #             #user_stu_list_verify_mobile_status(driver,user_mobile)
            #
            #             #调取手机短信平台
            #             jiequ_code = user_sms_platform_info(driver,user_mobile)
            #
            #             sleep(2)
            #
            #     driver.switch_to_window(current_window_handle)
            #
            #     print ("333")
            #     #验证码输入框
            #     driver.find_element_by_xpath("//*[@id='mobileCode']/div/ul/li[3]/div/input").send_keys(jiequ_code)
            #
            #     sleep(2)
            #
            #     # driver.refresh()
            #
            #     sleep(2)
            #
            # #直接约成人/青少体验课
            # except:
            #
            #     #------------------------------------#
            #
            #     print ("该手机号已验证，请选择体验课吧～")
            #
            #     #------------------------------------#
            #
            #     sleep(2)

            # 下一步
            driver.find_element_by_xpath("//*[@id='indexSelsectTime']/div[2]/div[2]/div[3]/a").click()

            sleep(1)

            # 判断成人还是青少预约体验课（成人只有：ac上课方式、青少包含：ac上课方式、igs上课方式）
            try:

                # 51Talk青少课堂选择按钮
                driver.find_element_by_xpath("//*[@id='indexMethod']/div[2]/div[2]/ul/li[2]/span")

                the_way_of_class_index = random.randint(1, 2)

                # AC上课方式
                if the_way_of_class_index == 1:

                    pass

                # igs上课方式
                elif the_way_of_class_index == 2:

                    # 切换到igs上课方式
                    driver.find_element_by_xpath("//*[@id='indexMethod']/div[2]/div[2]/ul/li[2]/span").click()

            except:

                pass

            sleep(1)

            # 完成预约
            driver.find_element_by_xpath("//*[@id='indexMethod']/div[2]/div[2]/div/a").click()

            try:

                driver.switch_to_alert()
                sleep(2)

                alter_text = driver.switch_to_alert().text()
                sleep(2)

                print ("alter_text = " + alter_text)

                driver.switch_to_alert().accept()
                sleep(2)

                # 返回数值为3，约课失败
                return 3

            except:

                sleep(1)

                # 体验课预约成功
                try:

                    # 体验课预约成功！
                    driver.find_element_by_xpath("//*[@id='success']/div/div[1]/dl[1]/dd[1]")

                    experience_cadets_success_text = driver.find_element_by_xpath(
                        "//*[@id='success']/div/div[1]/dl[1]/dd[1]").text

                    sleep(2)

                    # 以下为您预约的课程信息：
                    Reservations_for_course_information_text = driver.find_element_by_xpath(
                        "//*[@id='success']/div/div[1]/dl[2]/dd[1]").text

                    # 上课时间
                    class_time_text = driver.find_element_by_xpath("//*[@id='success']/div/div[1]/dl[2]/dd[2]").text

                    # 上课时间：2018-04-24 16:00-16:25

                    class_hm_time_text = class_time_text[16:21]

                    # 教材
                    teaching_material_text_1 = driver.find_element_by_xpath(
                        "//*[@id='success']/div/div[1]/dl[2]/dd[3]/span[1]").text

                    # 教材
                    teaching_material_text_2 = driver.find_element_by_xpath(
                        "//*[@id='success']/div/div[1]/dl[2]/dd[3]/span[2]").text

                    # 上课方式
                    the_way_of_class_text = driver.find_element_by_xpath(
                        "//*[@id='success']/div/div[1]/dl[2]/dd[4]").text

                    if class_hm_time_text == yk_time_text:

                        print ("")
                        print ("***************************************")
                        print (Reservations_for_course_information_text)
                        print ("")
                        print (class_time_text)
                        print (u"教材名称：" + teaching_material_text_1 + " " + teaching_material_text_2)
                        print (the_way_of_class_text)
                        print ("***************************************")
                        print ("")

                        sleep(2)

                        yk_success_on = True

                    else:

                        # 约课时间不对
                        return 4
                except:

                    # 约课完成页面错误
                    return 2

            if yk_success_on == True:

                # 首页
                driver.find_element_by_xpath("//*[@id='head']/div/div[2]/div/ul/li[1]/a").click()

                sleep(2)

                # 查询弹出层后关闭
                try:

                    user_center_layer_operation(driver)

                except:

                    pass

                sleep(1)

                yk_after_url = driver.current_url

                if yk_after_url == u"http://trial.51talk.com/trial/index":

                    db_wealth_point = "0"

                    db_wealth_classtime = ""

                    # 更新user_wealth表point
                    userInformation_db_wealth_data_update_success(user_mobile, db_wealth_point, db_wealth_classtime,current_now_time)

                    sleep(1)

                    # -----------------------------------#

                    print ("约课成功后--财富数据更新成功！！！")

                    # -----------------------------------#

                    # 返回数值为1，调用修改教材、取消约体验课
                    return 1

    else:

        #会员中心修改教材按钮 or 左侧已预约课程按钮 or 更多按钮是否存在

        # 取消课程按钮
        try:

            driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[3]/a")

            sleep(1)

            try:

                # 找到一小时之外的课程
                driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[3]/a").get_attribute("onclick")

                sleep(1)

                yk_cancel_on = True

            except:

                yk_cancel_on = False

        except:

            # 会员中心取消课程按钮
            try:

                driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a")

                sleep(1)

                try:

                    #找到一小时之外的课程
                    driver.find_element_by_xpath("//*[@id='orderClass']/div/div[2]/ul/li[2]/a").get_attribute("onclick")

                    sleep(1)

                    yk_cancel_on = True

                except:

                    yk_cancel_on = False

            except:

                # 会员中心更多按钮
                try:

                    driver.find_element_by_xpath("//*[@id='orderClass']/div/h3/a")

                    sleep(1)

                    yk_cancel_on = True

                except:

                    # 返回数值为5，不能约课，无财富值
                    return 5

        if yk_cancel_on == True:


            sleep(1)

            # 返回数值为6，调用修改教材、取消约体验课
            return 6
