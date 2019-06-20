#!usr/bin/python
#encoding:utf-8


'''约公开课'''


__author__ = 'zhangbo'

from Initializ_page.open_class_Initializ_list_page import *
from configuration_files import open_class_page_config_information as open_class_config
from talkUser.user_center.user_center_cancels_course import *
from talkUser.user_center.user_center_current_timetable_week_class_record import *
from talkUser.user_center.user_center_week_timetable import *



def user_open_class_success(driver,current_window_handle,login_after_link,user_wealth_data,db_user_id,user_mobile):

        print ("***************准备开始约公开课课程***************" + "\n")

        open_class_page_link_on = False

        paid_open_class = False

        free_open_class = False

        adult_junior_experience_class = True

        #当前公开课list页面条数
        open_class_list_page_max_index = 0

        #公开课tab选项sum
        open_class_tab_select_sum = 0

        #获取财富数据
        user_point_data = user_wealth_data[0]

        user_classtime_data = user_wealth_data[1]

        course_type_tag_text = "付费公开课"

        find_cancels_course_button_on = True

        all_stop_operation_on = False

        paid_stop_operation_on = False


        #获取登录后的url地址
        user_login_after_link = driver.current_url

        if user_login_after_link == "http://trial.51talk.com/trial/index" or user_login_after_link == "https://trial.51talk.com/trial/index":

            free_open_class = True

            adult_junior_experience_class = False

            open_class_tab_select_sum = 2

        elif user_login_after_link == "http://www.51talk.com/user/index" or user_login_after_link == "https://www.51talk.com/user/index":

            paid_open_class = True

            adult_junior_experience_class = False

            open_class_tab_select_sum = 3

        else:

            print ("当前账户还未约体验课，请先约体验课！！！" + "\n")

        sleep(1)

        if adult_junior_experience_class == False:

            #获取会员中心周几课表记录
            try:

                #浏览器滚动条置底
                js = "var q=document.documentElement.scrollTop=600"
                driver.execute_script(js)

                sleep(1)

                #获取当前课表周几
                week_timetable = user_center_timetable_week_return_current_success()

                sleep(1)

                #获取当前付费课表上课记录
                return_cancels_course_button = user_center_current_timetable_week_class_record_success(driver, login_after_link,week_timetable,course_type_tag_text)

                #在当前课表中查找付费公开课上课记录
                if return_cancels_course_button == 1:

                    sleep(1)

                    #调用会员中心取消课程
                    user_center_cancels_course_success(driver, course_type_tag_text, week_timetable, db_user_id, user_mobile)

                elif return_cancels_course_button == 0:

                    print ('找到上课记录，显示老师或者学生缺席，或者上课已经完成，请查看原因...')

                elif return_cancels_course_button == 2:

                    print ("今日、明天、后天：三天都未找到上课记录...")

                    find_cancels_course_button_on = False

                elif return_cancels_course_button == 3:

                    print ("成人或青少体验用户，可以约免费公开课！！！")

                    find_cancels_course_button_on = False

            except:

                print ("获取失败，请查看原因！！！")

            if find_cancels_course_button_on == False:

                sleep(1)

                #公开课访问方式（0：会员中心左侧栏、1：直接访问公开课页面）
                open_class_open_mode_randint = random.randint(0,1)

                sleep(1)

                if open_class_open_mode_randint == 0:

                    #成人付费学员约公开课
                    try:

                        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[4]/li[2]/a")

                        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/ul[4]/li[2]/a").click()

                        open_class_page_link_on = True

                        sleep(2)

                    except:

                        #青少付费学员约公开课
                        try:

                            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[4]/li[3]/a")

                            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/ul[4]/li[3]/a").click()

                            open_class_page_link_on = True

                            sleep(2)

                        except:

                            #青少体验学员约公开课
                            try:

                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[9]/a")

                                driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[9]/a").click()

                                open_class_page_link_on = True

                                sleep(2)

                            except:

                                #成人体验学员约公开课
                                try:

                                    driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[10]/a")

                                    driver.find_element_by_xpath("//*[@id='sidebar']/div/ul[1]/li[10]/a").click()

                                    open_class_page_link_on = True

                                    sleep(2)

                                except:

                                    print ("没有找到公开课入口，请查看原因！！！")

                else:

                    #打开约公开课页面
                    js = 'window.open("https://bbs.51talk.com/openclass")'

                    driver.execute_script(js)

                    open_class_page_link_on = True

                    sleep(2)

                if open_class_page_link_on == True:

                    handles = driver.window_handles

                    for current_handle in handles:

                        if current_handle != current_window_handle:

                            driver.switch_to_window(current_handle)

                            sleep(2)

                            #公开课tab选项（最新课程、热门课程、优选公开课）
                            # open_class_tab_select_sum_randint = random.randint(1,open_class_tab_select_sum)
                            open_class_tab_select_sum_randint = random.randint(1,1)

                            tab_select_1 = open_class_config.adult_junior_open_class_tab_select_1
                            tab_select_2 = open_class_config.adult_junior_open_class_tab_select_2
                            tab_select_3 = open_class_tab_select_sum_randint
                            tab_select_4 = tab_select_1 + str(tab_select_3) + tab_select_2

                            sleep(2)

                            if open_class_tab_select_sum_randint == 1:

                                pass

                            else:

                                driver.find_element_by_xpath(tab_select_4).click()

                            sleep(1)

                            #当前公开课tab下的url地址
                            open_class_tab_select_link_url = driver.current_url

                            #获取翻页按钮最大数量
                            open_class_list_page_button_max_index = driver.find_element_by_xpath("//*[@id='container']/div[2]/div[3]/div/a[11]").text

                            sleep(1)

                            #当前页按钮
                            for page_number_index in range(2,int(open_class_list_page_button_max_index)):

                                #调用初始化公开课list数据
                                open_class_list_page_max_index = open_class_Initializ_list_page_success(driver)

                                #浏览器滚动条置底
                                js = "var q=document.documentElement.scrollTop=500"
                                driver.execute_script(js)

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

                                #每页多少条数据
                                for open_class_list_index in range(1,open_class_list_page_max_index + 1):

                                    #免费、课时、次卡、金额公开课标识
                                    free_paid_tag_1 = open_class_config.adult_junior_open_class_free_paid_tag_1
                                    free_paid_tag_2 = open_class_config.adult_junior_open_class_free_paid_tag_2
                                    free_paid_tag_3 = open_class_list_index
                                    free_paid_tag_4 = free_paid_tag_1 + str(free_paid_tag_3) + free_paid_tag_2

                                    sleep(1)

                                    #公开课预约按钮
                                    class_appointment_1 = open_class_config.adult_junior_open_class_appointment_1
                                    class_appointment_2 = open_class_config.adult_junior_open_class_appointment_2
                                    class_appointment_3 = open_class_list_index
                                    class_appointment_4 = class_appointment_1 + str(class_appointment_3) + class_appointment_2

                                    sleep(1)

                                    #公开课取消课程按钮
                                    cancel_course_1 = open_class_config.adult_junior_open_class_cancel_course_1
                                    cancel_course_2 = open_class_config.adult_junior_open_class_cancel_course_2
                                    cancel_course_3 = open_class_list_index
                                    cancel_course_4 = cancel_course_1 + str(cancel_course_3) + cancel_course_2

                                    sleep(1)

                                    #公开课约课时间
                                    about_class_time_1 = open_class_config.adult_junior_open_class_about_class_time_1
                                    about_class_time_2 = open_class_config.adult_junior_open_class_about_class_time_2
                                    about_class_time_3 = open_class_list_index
                                    about_class_time_4 = about_class_time_1 + str(about_class_time_3) + about_class_time_2

                                    sleep(1)

                                    #公开课课程名称
                                    course_name_1 = open_class_config.adult_junior_open_class_course_name_1
                                    course_name_2 = open_class_config.adult_junior_open_class_course_name_2
                                    course_name_3 = open_class_list_index
                                    course_name_4 = course_name_1 + str(course_name_3) + course_name_2

                                    #免费、课时、次卡、金额公开课标识
                                    free_paid_open_class_tage_text = driver.find_element_by_xpath(free_paid_tag_4).text

                                    #次卡标识
                                    paid_point_open_class_tage_text = free_paid_open_class_tage_text[1:3]

                                    #课时标识
                                    paid_classtime_open_class_tage_text = free_paid_open_class_tage_text[1:3]

                                    #金额标识
                                    paid_money_open_class_tage_text = free_paid_open_class_tage_text[1:3]

                                    #课程名称+课程标识
                                    course_name = driver.find_element_by_xpath(course_name_4).text

                                    #课程名称长度
                                    course_name_jiequ_name_len = len(course_name)

                                    sleep(1)

                                    #获取上课时间
                                    open_class_time = driver.find_element_by_xpath(about_class_time_4).text

                                    #年
                                    open_class_time_year = int(open_class_time[0:4])

                                    #月
                                    open_class_time_month = int(open_class_time[5:7])

                                    #日
                                    open_class_time_day = int(open_class_time[8:10])

                                    #约课开始小时
                                    open_class_time_start_hour = int(open_class_time[15:17])

                                    #约课开始分钟
                                    open_class_time_start_minute = int(open_class_time[18:20])

                                    #约课结束小时
                                    open_class_time_end_hour = int(open_class_time[21:23])

                                    #约课结束分钟
                                    open_class_time_end_minute = int(open_class_time[24:26])

                                    sleep(1)

                                    #当前现在时间
                                    now_time = datetime.datetime(current_now_time_year, current_now_time_month, current_now_time_day,
                                                                 current_now_time_hour, current_now_time_minute, 0)
                                    sleep(1)

                                    #公开课约课时间
                                    yk_now_time = datetime.datetime(open_class_time_year, open_class_time_month, open_class_time_day,
                                                                    open_class_time_start_hour, open_class_time_start_minute, 0)

                                    sleep(1)

                                    if current_now_time_hour < open_class_time_start_hour or open_class_time_day > current_now_time_day:

                                        #时间差：分钟
                                        yk_now_time_1 = int((yk_now_time - now_time).seconds / 60)

                                        sleep(1)

                                        if yk_now_time_1 > 60:

                                            sleep(1)

                                            #体验学员约课
                                            if free_open_class == True:

                                                if free_paid_open_class_tage_text == "免费":

                                                    sleep(1)

                                                    #预约按钮
                                                    driver.find_element_by_xpath(class_appointment_4).click()

                                                    sleep(1)

                                                    #预约免费公开课
                                                    try:

                                                        driver.switch_to_alert()

                                                        sleep(1)

                                                        #alert中预约免费课成功提示
                                                        free_open_class_about_class_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]/div").text

                                                        sleep(1)

                                                        free_open_class_about_class_success_text = free_open_class_about_class_success_text[0:37]

                                                        sleep(1)

                                                        #alert中约课成功后确定按钮
                                                        driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                                                        sleep(1)

                                                        if free_open_class_about_class_success_text == "预约成功，当前课程将使用音视频优化技术，上课前请保证您的客户端是最新版本。":

                                                            print ("免费公开课约课成功，5s倒计时后，自动取消免费公开课")

                                                    except:

                                                        print ("弹框未弹起，请查看原因！！！")

                                                    #倒计时5s后，取消免费公开课
                                                    time_countdow_index = 5

                                                    while(time_countdow_index > 0):

                                                        print ("倒计时:" + str(time_countdow_index) + "s")

                                                        time_countdow_index = time_countdow_index - 1

                                                        sleep(1)

                                                    #取消课程按钮
                                                    driver.find_element_by_xpath(cancel_course_4).click()

                                                    sleep(1)

                                                    #取消预约免费公开课
                                                    try:

                                                        driver.switch_to_alert()

                                                        sleep(1)

                                                        #alert中取消预约免费课成功提示
                                                        free_open_class_cancel_about_class_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

                                                        sleep(1)

                                                        free_open_class_cancel_about_class_success_text = free_open_class_cancel_about_class_success_text[0:21]

                                                        sleep(1)

                                                        #alert中约课取消后确定按钮
                                                        driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                                                        sleep(1)

                                                        if free_open_class_cancel_about_class_success_text == "取消成功,其他公开课也很精彩,欢迎提前预约":

                                                            print ("免费公开课取消约课成功！！！")

                                                            sleep(1)

                                                            all_stop_operation_on = True

                                                            #只操作一次免费公开课
                                                            break;

                                                    except:

                                                        print ("弹框未弹起，请查看原因！！！")

                                                elif paid_point_open_class_tage_text == "次卡" or \
                                                     paid_classtime_open_class_tage_text == "课时":

                                                        sleep(1)

                                                        #预约按钮
                                                        driver.find_element_by_xpath(class_appointment_4).click()

                                                        sleep(1)

                                                        #体验账号约付费公开课不能约课
                                                        try:

                                                            driver.switch_to_alert()

                                                            sleep(1)

                                                            #alert中约付费公开课失败提示
                                                            paid_open_class_about_class_fail_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

                                                            sleep(1)

                                                            paid_open_class_about_class_fail_text = paid_open_class_about_class_fail_text[0:13]

                                                            sleep(1)

                                                            if paid_open_class_about_class_fail_text == "请您购买课时套餐后再预约！":

                                                                print ("该体验账号约付费公开课程失败，请购买套餐后在约吧！！！")

                                                                sleep(1)

                                                                driver.refresh()

                                                                sleep(1)

                                                        except:

                                                            print ("弹框未弹起，请查看原因！！！")

                                            #付费学员约课
                                            elif paid_open_class == True:

                                                if user_point_data == "0" and user_classtime_data == "0" or user_point_data == "0" and user_classtime_data == "":

                                                    print ("该付费用户财富已过期或已失效，请重新购买套餐！！！")

                                                    all_stop_operation_on = True

                                                    break;

                                                else:

                                                    if paid_point_open_class_tage_text == "次卡" or \
                                                       paid_classtime_open_class_tage_text == "课时":

                                                        #公开课课程名称
                                                        course_name_jiequ_name = course_name[3:course_name_jiequ_name_len]

                                                        #课程标识（优选、精品）
                                                        # course_name_jiequ_tag = course_name[0:2]

                                                        sleep(1)

                                                        #预约按钮
                                                        driver.find_element_by_xpath(class_appointment_4).click()

                                                        sleep(1)

                                                        #预约付费公开课
                                                        try:

                                                            driver.switch_to_alert()

                                                            sleep(1)

                                                            #alert中约课成功前取消按钮
                                                            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

                                                            sleep(1)

                                                            #预约按钮
                                                            driver.find_element_by_xpath(class_appointment_4).click()

                                                            sleep(1)

                                                            #alert中约课成功前确定按钮
                                                            driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                                                            sleep(1)

                                                            #alert中预约付费课成功提示
                                                            paid_open_class_about_class_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]/div").text

                                                            sleep(1)

                                                            paid_open_class_about_class_success_text = paid_open_class_about_class_success_text[0:37]

                                                            #alert中约课成功后确定按钮
                                                            driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                                                            sleep(1)

                                                            if paid_open_class_about_class_success_text == "预约成功，当前课程将使用音视频优化技术，上课前请保证您的客户端是最新版本。":

                                                                print ("###############################################")
                                                                print ("公开课课程名称为：" + course_name_jiequ_name )
                                                                print ("公开课约课时间为：" + open_class_time)
                                                                print ("###############################################")


                                                        except:

                                                            print ("弹框未弹起，请查看原因！！！")

                                                        print ("付费公开课约课成功，5s倒计时后，自动取消付费公开课！！！")

                                                        # 倒计时5s后，取消付费公开课
                                                        time_countdow_index = 5

                                                        while (time_countdow_index > 0):

                                                            print ("倒计时:" + str(time_countdow_index) + "s")

                                                            time_countdow_index = time_countdow_index - 1

                                                            sleep(1)

                                                        #公开课页面取消、会员中心取消
                                                        paid_open_class_cancel_about_class_mode_randint = random.randint(0,1)

                                                        #直接在公开课页面取消付费公开课
                                                        if paid_open_class_cancel_about_class_mode_randint == 0:

                                                            #取消课程按钮
                                                            driver.find_element_by_xpath(cancel_course_4).click()

                                                            sleep(1)

                                                            #取消预约付费公开课
                                                            try:

                                                                driver.switch_to_alert()

                                                                sleep(1)

                                                                #alert中约课取消前取消按钮
                                                                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[2]").click()

                                                                sleep(1)

                                                                #取消课程按钮
                                                                driver.find_element_by_xpath(cancel_course_4).click()

                                                                sleep(1)

                                                                #alert中约课取消前确定按钮
                                                                driver.find_element_by_xpath("//*[@id='m-confirm']/div/div[3]/div/span[1]").click()

                                                                sleep(1)

                                                                #alert中约课取消后成功提示
                                                                paid_open_class_cancel_about_class_success_text = driver.find_element_by_xpath("//*[@id='m-alert']/div/div[2]").text

                                                                sleep(1)

                                                                paid_open_class_cancel_about_class_success_text = paid_open_class_cancel_about_class_success_text[0:21]

                                                                sleep(1)

                                                                #alert中约课取消后确定按钮
                                                                driver.find_element_by_xpath("//*[@id='m-alert']/div/div[3]/div/span").click()

                                                                sleep(1)

                                                                if paid_open_class_cancel_about_class_success_text == "取消成功,其他公开课也很精彩,欢迎提前预约":

                                                                    print ("付费公开课取消约课成功！！！")

                                                                    sleep(1)

                                                                    all_stop_operation_on = True

                                                                    #只操作一次付费公开课
                                                                    break;

                                                            except:

                                                                print ("弹框未弹起，请查看原因！！！")

                                                        #调用会员中心取消课程
                                                        elif paid_open_class_cancel_about_class_mode_randint == 1:

                                                            all_stop_operation_on = True

                                                            paid_stop_operation_on = True

                                                            #只操作一次付费公开课
                                                            break;

                                                    elif paid_money_open_class_tage_text == "25" or \
                                                         paid_money_open_class_tage_text == "50":

                                                            # 预约按钮
                                                            driver.find_element_by_xpath(class_appointment_4).click()

                                                            sleep(1)

                                                            print ("该付费账号财富值已经用完，请直接购买付费公开课程后，才能继续上课！！！")

                                                            sleep(1)

                                                            all_stop_operation_on = True

                                                            break;

                                                    elif free_paid_open_class_tage_text == "免费":

                                                        print ("当前账户类型为付费学员，需要预约付费课程！！！")

                                        else:

                                            print ("当前要预约的时间已经小于1小时，不能约此时间课程！！！")
                                    else:

                                        print ("当前时间为：" + current_now_time + "分钟，该时间不在约课范围内，目前只能预约1小时之后的课程，请重新约课吧！！！")

                                if all_stop_operation_on == True:

                                    break;

                                driver.get(open_class_tab_select_link_url + "?page=" + str(page_number_index))

                                sleep(2)

                sleep(2)

                if all_stop_operation_on == True:

                    sleep(2)

                    driver.close()

                    sleep(2)

                    driver.switch_to_window(current_window_handle)

                    sleep(2)

                    if paid_stop_operation_on == True:

                        driver.refresh()

                        sleep(2)

                        #调用会员中心取消课程
                        user_center_cancels_course_success(driver,course_type_tag_text,week_timetable,db_user_id,user_mobile)

                print ("************公开课课程处理完毕，请查看************" + "\n")






