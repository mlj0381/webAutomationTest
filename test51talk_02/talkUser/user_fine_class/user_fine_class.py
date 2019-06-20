#!usr/bin/python
#encoding:utf-8


'''约精品小班课'''


__author__ = 'zhangbo'

from Initializ_page.fine_class_class_Initializ_list_page import *
from configuration_files import fine_class_class_page_config_information as fine_class_class_config
from talkUser.user_center.user_center_cancels_course import *
from talkUser.user_center.user_center_current_timetable_week_class_record import *
from talkUser.user_center.user_center_layer import *
from talkUser.user_center.user_center_week_timetable import *


#精品小班课约课
def user_fine_class_success(driver,current_window_handle,login_after_url_link,user_wealth_data,db_user_id,user_mobile):

    print ("***************准备开始约精品小班课***************" + "\n")

    fine_class_class_page_link_on = False

    about_class_success = False

    adult_experience_not_about_class = False

    junior_experience_not_about_class = False

    find_cancels_course_button_on = True

    course_type_tag_text = "精品小班课"

    #获取财富数据
    user_point_data = user_wealth_data[0]

    user_classtime_data = user_wealth_data[1]

    sleep(1)

    if login_after_url_link == "http://trial.51talk.com/trial/index" or login_after_url_link == "https://trial.51talk.com/trial/index":

        # 成人体验学员
        try:

            # 外教精品小班课
            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/ul[1]/li[4]/a")

            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/ul[1]/li[4]/a").click()

            sleep(1)

            adult_experience_not_about_class = True

        except:

            print ("青少体验学员用户不能约精品小班课，需要先购买课程套餐！！！")

        if adult_experience_not_about_class == True:

            print ("成人体验学员用户不能约精品小班课，需要先购买课程套餐！！！")

            sleep(1)

    elif login_after_url_link == "http://trial.51talk.com/trial/reserve" or login_after_url_link == "https://trial.51talk.com/trial/reserve":

            print ("该账号类型不能约精品小班课课程，请先约体验课吧！！！")

            sleep(1)

    else:

        #获取会员中心周几课表记录
        try:

            # 浏览器滚动条置底
            js = "var q=document.documentElement.scrollTop=600"
            driver.execute_script(js)

            sleep(1)

            #获取当前课表周几
            week_timetable = user_center_timetable_week_return_current_success()

            sleep(1)

            #获取当前课表上课记录
            return_cancels_course_button  = user_center_current_timetable_week_class_record_success(driver,login_after_url_link,week_timetable,course_type_tag_text)

            #在当前课表中查找精品小班课上课记录
            if return_cancels_course_button == 1:

                sleep(1)

                #调用会员中心取消课程
                user_center_cancels_course_success(driver,course_type_tag_text,week_timetable,db_user_id,user_mobile)

            else:

                find_cancels_course_button_on = False

        except:

            pass

        #预约精品小班课
        if find_cancels_course_button_on == False:

            #青少付费学员
            try:

                #青少1+2付费学员(精品小班课链接)
                fine_class_class_button_text = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[4]/a").text

                sleep(1)

                #青少1+2付费学员
                if fine_class_class_button_text == "精品小班课":

                    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[4]/a").click()

                #青少非1+2付费学员
                else:

                    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[1]/li[3]/a").click()

                sleep(1)

                fine_class_class_page_link_on = True

            except:

                #成人付费学员
                try:

                    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[1]/li[3]/a")

                    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[1]/li[3]/a").click()

                    sleep(1)

                    fine_class_class_page_link_on = True

                except:

                    print ("没有找到精品小班课预约链接，请查看原因！！！")

            sleep(1)

            if fine_class_class_page_link_on == True:

                handles = driver.window_handles

                for current_handle in handles:

                    if current_handle != current_window_handle:

                        driver.switch_to_window(current_handle)

                        sleep(1)

                        #获取现在时间
                        current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                        #年
                        current_now_time_year = int(current_now_time[0:4])

                        #月
                        current_now_time_month = int(current_now_time[5:7])

                        #日
                        current_now_time_day = int(current_now_time[8:10])

                        #当天现在小时
                        current_now_time_hour = int(current_now_time[11:13])

                        #当天现在分钟
                        current_now_time_minute = int(current_now_time[14:16])

                        #当天现在秒
                        current_now_time_second = int(current_now_time[17:19])

                        #浏览器滚动条置底
                        js = "var q=document.documentElement.scrollTop=380"
                        driver.execute_script(js)

                        sleep(1)

                        #精品小班课tab选项（今天、明天、后天）
                        fine_class_tab_select_sum_randint = random.randint(3,3)

                        tab_select_1 = fine_class_class_config.fine_class_class_tab_select_1
                        tab_select_2 = fine_class_class_config.fine_class_class_tab_select_2
                        tab_select_3 = fine_class_tab_select_sum_randint
                        tab_select_4 = tab_select_1 + str(tab_select_3) + tab_select_2

                        sleep(1)

                        #今天
                        if fine_class_tab_select_sum_randint == 1:

                            about_class_time_year  = current_now_time_year

                            about_class_time_month = current_now_time_month

                            about_class_time_day   = current_now_time_day

                        else:

                            driver.find_element_by_xpath(tab_select_4).click()

                            sleep(1)

                            #明天
                            if fine_class_tab_select_sum_randint == 2:

                                #获取明天的日期
                                tomorrow_day_y_m_d = datetime.datetime.now().date() + datetime.timedelta(days=1)

                                tomorrow_day_y_m_d = tomorrow_day_y_m_d.strftime('%Y-%m-%d')

                                #年
                                about_class_time_year = int(tomorrow_day_y_m_d[0:4])

                                #月
                                about_class_time_month = int(tomorrow_day_y_m_d[5:7])

                                #日
                                about_class_time_day   = int(tomorrow_day_y_m_d[8:10])

                            #后天
                            else:

                                #获取后天的日期
                                day_after_tomorrow_y_m_d = datetime.datetime.now().date() + datetime.timedelta(days=2)

                                day_after_tomorrow_y_m_d = day_after_tomorrow_y_m_d.strftime('%Y-%m-%d')

                                #年
                                about_class_time_year = int(day_after_tomorrow_y_m_d[0:4])

                                #月
                                about_class_time_month = int(day_after_tomorrow_y_m_d[5:7])

                                #日
                                about_class_time_day   = int(day_after_tomorrow_y_m_d[8:10])

                        #调用初始化精品小班课翻页按钮个数
                        fine_class_class_list_page_button_max_index = fine_class_class_Initializ_list_page_button_number_success(driver)

                        sleep(0.5)

                        #初始化精品小班课每页约课个数
                        fine_class_class_list_page_about_class_max_index = fine_class_class_Initializ_list_page_about_class_number_success(driver)

                        sleep(0.5)

                        #翻页按钮
                        for fine_class_class_page_button_index in range(1,fine_class_class_list_page_button_max_index -1):

                            #下一页按钮
                            page_button_1 = fine_class_class_config.fine_class_class_page_button_1
                            page_button_2 = fine_class_class_config.fine_class_class_page_button_2
                            page_button_3 = fine_class_class_list_page_button_max_index
                            page_button_4 = page_button_1 + str(page_button_3) + page_button_2

                            #初始化精品小班课每页约课个数
                            fine_class_class_list_page_about_class_max_index = fine_class_class_Initializ_list_page_about_class_number_success(driver)

                            sleep(1)

                            #每页个数
                            for fine_class_class_list_index in range(1,fine_class_class_list_page_about_class_max_index + 1):

                                #约课时间
                                about_class_time_1  = fine_class_class_config.fine_class_class_about_class_time_1
                                about_class_time_2  = fine_class_class_config.fine_class_class_about_class_time_2
                                about_class_time_3  = fine_class_class_list_index
                                about_class_time_4  = about_class_time_1 + str(about_class_time_3) + about_class_time_2

                                sleep(0.5)

                                #获取约课时间
                                about_class_time = driver.find_element_by_xpath(about_class_time_4).text

                                about_class_time_start_hour = int(about_class_time[0:2])

                                about_class_time_start_minute = int(about_class_time[3:5])

                                about_class_time_end_hour = int(about_class_time[8:10])

                                about_class_time_end_minute = int(about_class_time[11:13])

                                sleep(0.5)

                                now_time = datetime.datetime(current_now_time_year, current_now_time_month, current_now_time_day,
                                                             current_now_time_hour, current_now_time_minute, 0)
                                sleep(0.5)

                                yk_now_time = datetime.datetime(about_class_time_year, about_class_time_month, about_class_time_day,
                                                                about_class_time_start_hour, about_class_time_start_minute, 0)

                                sleep(0.5)

                                #精品小班课课程名称
                                course_name_1 = fine_class_class_config.fine_class_class_course_name_1
                                course_name_2 = fine_class_class_config.fine_class_class_course_name_2
                                course_name_3 = fine_class_class_list_index
                                course_name_4 = course_name_1 + str(course_name_3) + course_name_2

                                sleep(0.5)

                                #立即预约按钮
                                immediate_reservation_button_1 = fine_class_class_config.fine_class_class_immediate_reservation_button_1
                                immediate_reservation_button_2 = fine_class_class_config.fine_class_class_immediate_reservation_button_2
                                immediate_reservation_button_3 = fine_class_class_list_index
                                immediate_reservation_button_4  = immediate_reservation_button_1 + str(immediate_reservation_button_3) + immediate_reservation_button_2

                                #获取立即预约按钮text
                                immediate_reservation_button_text = driver.find_element_by_xpath(immediate_reservation_button_4).text

                                sleep(0.5)

                                if immediate_reservation_button_text == "预约已满":

                                    print ("该：" +str(about_class_time_year) + "-" + str(about_class_time_month) + "-" + str(about_class_time_day) + " " + about_class_time + " " + "时段课程已被约满，请换一个课程再约！！！")

                                    sleep(1)

                                elif immediate_reservation_button_text == "立即预约":

                                    if fine_class_tab_select_sum_randint == 1:

                                        if current_now_time_hour < about_class_time_start_hour:

                                            yk_now_time_1 = int((yk_now_time - now_time).seconds / 60)

                                            if yk_now_time_1 > 60:

                                                sleep(1)

                                                driver.find_element_by_xpath(immediate_reservation_button_4).click()

                                                about_class_success = True

                                            else:

                                                print ("该：" + str(about_class_time_year) + "-" + str(about_class_time_month) + "-" + str(about_class_time_day) + " " + about_class_time + " " + "时间段课程上课时间小于一小时，无法约课，请换一个课程再约！！！")

                                    else:

                                        driver.find_element_by_xpath(immediate_reservation_button_4).click()

                                        about_class_success = True

                                    sleep(1)

                                    if about_class_success == True:

                                        #精品小班课课程名称
                                        course_name = driver.find_element_by_xpath(course_name_4).text

                                        sleep(1)

                                        try:

                                            driver.switch_to_alert()

                                            sleep(1)

                                            #alert中取消按钮
                                            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

                                            sleep(1)

                                            #单击立即预约按钮
                                            driver.find_element_by_xpath(immediate_reservation_button_4).click()

                                            sleep(1)

                                            #alert中确定按钮
                                            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                                            sleep(1)

                                            #alert中知道了按钮
                                            driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                                            sleep(5)

                                            print ("#######################################################")
                                            print ("您预约的精品小班课课程名称为：" + course_name)
                                            print ("约课时间为：" + str(about_class_time_year) + "-" + str(about_class_time_month) + "-" + str(
                                                about_class_time_day) + " " + about_class_time)
                                            print ("#######################################################")

                                            sleep(5)

                                            break;

                                        except:

                                            pass

                            if about_class_success == True:

                                break;

                            sleep(1)

                            #翻页到最后一页按钮时
                            if fine_class_class_page_button_index == fine_class_class_list_page_button_max_index - 2:

                                print ("当天精品小班课已经约满了，无法再进行约课了，请查看原因！！！")

                                break;

                            #翻页到第二页
                            driver.find_element_by_xpath(page_button_4).click()

                            sleep(1)

                sleep(2)

                driver.close()

                sleep(2)

                driver.switch_to_window(current_window_handle)

                sleep(2)

                driver.refresh()

                sleep(2)

                #调用弹出层关闭
                try:

                    user_center_layer_operation(driver)

                except:

                    pass

                #调用会员中心取消课程
                user_center_cancels_course_success(driver,course_type_tag_text,week_timetable,db_user_id,user_mobile)

                sleep(2)

                print ("************精品小班课课程处理完毕，请查看************")