#!usr/bin/python
#encoding:utf-8


'''新主站登录模块'''


__author__ = 'zhangbo'


import unittest
# import urllib2
from time import *

from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from configuration_files import driver_configurationFiles as config_driver
from configuration_files.db_config import *
from configuration_files.dqTxtFile import readLoginSuccessFile, readLoginFailFile
from db_files.userInformation_db_old_data_insert import userInformation_db_old_data_insert_success
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success
from db_files.userInformation_db_query import userInformation_db_query_user_id_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success
from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_user_id_success
from db_files.userInformation_db_wealth_data_insert import userInformation_db_wealth_data_insert_success
from talkTest.StartPage.startPagePopLayer import startPageComeInto
from talkUser.admin_backstage.user_stu_list import user_stu_list_query_user_user_id
from talkUser.admin_backstage.user_stu_list import user_stu_list_verify_mobile_status
from talkUser.user_account_select import *
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_experience_class.user_experience_cadets import user_experience_cadets_success
from talkUser.user_identity_select import user_identity_select_info
from talkUser.user_quit_browser import *
from talkUser.user_sms_platform import user_sms_platform_info
from talkUser.user_wealth import user_experience_the_wealth_success
from talkUser.user_wealth import user_paid_the_wealth_success
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_open_class.user_open_class import user_open_class_success
from talkUser.user_fine_class.user_fine_class import user_fine_class_success




class TestNewLogin(unittest.TestCase):

        def setUp(self):

            self.driver = config_driver.obj_driver

            self.url    = "http://www.51talk.com"

            sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    #主站登录页面--账号密码登录成功
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_account_password_login_info_success(self):

            print ("*************主站登录页面--账号密码登录成功*************")

            for xunhuan_login_index in range(0, xunhuan_login_max):

                u"""账号密码注册信息正确，正常登录."""

                driver = self.driver

                driver.get(self.url)

                sleep(1)

                driver.maximize_window()

                sleep(1)

                #调用启动页进入青少儿官网
                startPageComeInto(driver)

                sleep(1)

                current_window_handle = driver.current_window_handle

                sleep(1)

                # 获取当天现在时间
                current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                sleep(1)

                #点击登录
                driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

                sleep(1)

                #读入文件--xlsx
                # read_login_success_xlsx = dqXlsLoginSuccess()
                #
                # for i in range(1, len(read_login_success_xlsx)):
                #
                #     user_account = int(read_login_success_xlsx[i][0])
                #     user_password = int(read_login_success_xlsx[i][1])
                #     user_english_name = read_login_success_xlsx[i][2]
                #     user_tuijian_mobile = int(read_login_success_xlsx[i][3])

                #读入文件--txt
                read_login_success_txt = readLoginSuccessFile()

                print (read_login_success_txt)

                for i in read_login_success_txt:
                    print (type(i))
                    i = i.decode("utf-8")
                    print (type(i))
                    user_mobile = i.split(',')[0]
                    user_password = i.split(',')[1]

                # user_mobile = raw_input("请输入用户登录手机号：")

                sleep(1)

                # user_password = raw_input("请输入用户登录密码：")

                sleep(1)

                #输入账号
                driver.find_element_by_xpath("//*[@id='accountId']").send_keys(user_mobile)

                sleep(2)

                #输入密码
                driver.find_element_by_xpath("//*[@id='password']").send_keys(user_password)

                sleep(2)

                #登录按钮
                driver.find_element_by_xpath("//*[@id='accountLoginBtn']").click()

                sleep(2)

                #错误提示
                try:

                    if driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[1]/div[2]/div") or \
                       driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[2]/div[2]/div"):

                        login_info_arrey=['请输入您的账号',
                                          '请输入密码'
                                          '密码长度只能是6-20位字符']

                        refresh_flag = False

                        #请输入您的账号
                        login_info_error_text_1 = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[1]/div[2]/div").text

                        #请输入密码、密码长度只能是6-20位字符
                        login_info_error_text_2 = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[2]/div[2]/div").text

                        if login_info_error_text_1 == u"请输入您的账号" and login_info_error_text_2 == u"请输入密码":

                            print ("#-------------------------------#")

                            print (u"该手机号输入为空，请重新输入！！！")
                            print (u"该密码输入为空，请重新输入！！！")

                            print ("#-------------------------------#" + "\n")

                            refresh_flag = True

                        elif login_info_error_text_2 == u"请输入密码":

                            print ("#-----------------------------#")

                            print (u"该账号为：" + user_mobile)
                            print (u"该密码输入为空，请重新输入！！！")

                            print ("#-----------------------------#" + "\n")

                            refresh_flag = True

                        elif login_info_error_text_2 == u"密码长度只能是6-20位字符":

                            print ("#-------------------------------------------------------------#")

                            print (u"该账号为：" + user_mobile)
                            print (u"该密码为：" + user_password + u",该密码格式错误，请重新输入！！！")

                            print ("#-------------------------------------------------------------#" + "\n")

                            refresh_flag = True

                        else:

                            #判断手机号是否被注册
                            try:

                                #您的用户名或密码错误
                                driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                # print (driver.find_element_by_xpath("//*[@id='contentInfo1']").text)

                                sleep(1)

                                #我知道了按钮
                                driver.find_element_by_xpath("//*[@id='sureId']").click()

                            except:

                                #密码错误，请立即找回
                                driver.find_element_by_xpath("//*[@id='contentInfo3']")

                                # print (driver.find_element_by_xpath("//*[@id='contentInfo3']").text)

                                sleep(1)

                                #找回密码按钮
                                driver.find_element_by_xpath("//*[@id='layer3']/div[2]/div[2]/a").click()

                                sleep(1)

                                forget_password_url = driver.current_url

                                sleep(1)

                                if forget_password_url == "http://login.51talk.com/password/forgot" or \
                                   forget_password_url == "https://login.51talk.com/password/forgot":

                                    #------------------------------#

                                    # print ("找回密码打开链接正确啦～")

                                    #------------------------------#

                                    pass

                        if refresh_flag == True:

                            driver.refresh()

                            #---------------------------------------#

                            print ("需要刷新页面，更新当前页面状态啦～")

                            #---------------------------------------#

                except:

                        flag_login_succes_tips = False

                        # 查询user表mobile,password
                        db_user = userInformation_db_query_mobile_password_success(user_mobile)

                        sleep(1)

                        # 获取用户user_id数据
                        db_user_id = userInformation_db_query_user_id_success(user_mobile)

                        if db_user == ():

                            # 调取后台stu_list表，验证手机号
                            js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

                            driver.execute_script(js)

                            handles = driver.window_handles

                            for current_handle in handles:

                                if current_handle != current_window_handle:

                                    driver.switch_to_window(current_handle)

                                    sleep(2)

                                    # 调用后台stu_list查询user_id
                                    user_id = user_stu_list_query_user_user_id(driver, user_mobile)

                                    driver.close()

                            sleep(1)

                            driver.switch_to_window(current_window_handle)

                            sleep(1)

                            # 插入之前注册过的用户信息
                            userInformation_db_old_data_insert_success(user_id, user_mobile, user_password,current_now_time)

                            # -----------------------------------#

                            print ("用户信息写入正确，请查看！！！")

                            # -----------------------------------#

                        else:

                            if db_user_id == "" or db_user_id == None:

                                sleep(1)

                                # 调取后台stu_list表，验证手机号
                                js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

                                driver.execute_script(js)

                                sleep(1)

                                handles = driver.window_handles

                                for current_handle in handles:

                                    if current_handle != current_window_handle:

                                        driver.switch_to_window(current_handle)

                                        sleep(2)

                                        # 调用后台stu_list查询user_id
                                        user_id = user_stu_list_query_user_user_id(driver, user_mobile)

                                        driver.close()

                                sleep(1)

                                driver.switch_to_window(current_window_handle)

                                sleep(1)

                                # 更新user表user_id数据
                                userInformation_db_user_data_update_user_id_success(str(user_mobile), str(user_id))

                            else:

                                user_id = db_user_id

                        sleep(1)

                        #判断元素是否找到
                        try:
                            driver.find_element(By.XPATH,"//*[@id='usersSelect']/div[4]/div/div[1]/h3")
                            # print (u"找到该元素！！！")

                            flag_login_succes_tips = True

                        except:

                            # print (u"没有找到该元素！！！")
                            flag_resiget_succes_tips =  False

                        if flag_login_succes_tips == True:

                            #调取学员身份选择功能
                            user_identity_select_info(driver)

                        login_after_link = driver.current_url

                        #成人/青少付费账号
                        if login_after_link == "https://www.51talk.com/user/index" or \
                           login_after_link == "http://www.51talk.com/user/index":

                                #----------------------------------------------------#

                                print (user_mobile + "该账号为成人/青少付费学员类型，直接进入会员中心啦～")

                                #----------------------------------------------------#

                                try:

                                    user_center_layer_operation(driver)

                                except:

                                    pass

                                sleep(2)

                                # 查询付费用户财富信息
                                # wealth_data = user_paid_the_wealth_success(driver,str(user_id),str(user_mobile))

                                # 预约公开课
                                # user_open_class_success(driver,current_window_handle,login_after_link,wealth_data,str(user_id),str(user_mobile))

                                # 预约精品小班课
                                # user_fine_class_success(driver,current_window_handle,wealth_data,str(user_id),str(user_mobile))

                        #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
                        elif login_after_link == "http://trial.51talk.com/trial/index" or \
                             login_after_link == "https://trial.51talk.com/trial/index":

                                #---------------------------------------------------------------------------------#

                                print (user_mobile + "该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入体验账号会员中心啦~")

                                #---------------------------------------------------------------------------------#

                                try:

                                    user_center_layer_operation(driver)

                                except:

                                    pass

                                # 调用约体验课
                                # user_experience_cadets_success(driver, current_window_handle, str(user_id),str(user_mobile))

                                # 查询体验用户财富信息
                                # wealth_data = user_experience_the_wealth_success(driver, login_after_link,str(user_id), str(user_mobile))

                                # 预约公开课
                                # user_open_class_success(driver, current_window_handle,login_after_link, wealth_data, str(user_id),str(user_mobile))

                                # 预约精品小班课
                                # user_fine_class_success(driver, current_window_handle, wealth_data, str(user_id),str(user_mobile))

                        #成人/青少体验账号，进入体验约课页面
                        elif login_after_link == "http://trial.51talk.com/trial/reserve" or \
                             login_after_link == "https://trial.51talk.com/trial/reserve":

                                #---------------------------------------------------------------#

                                print (user_mobile + "该账号为成人/青少体验学员类型，还没有约课，请先进行体验课约课啦~")

                                #---------------------------------------------------------------#

                                # 获取用户user_wealth表point
                                db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)

                                sleep(1)

                                if db_wealth_data == ():

                                    point = "1"

                                    point_validity = None

                                    classtime = ""

                                    # 插入user_wealth表point
                                    userInformation_db_wealth_data_insert_success(user_id, user_mobile, point,point_validity, classtime,current_now_time)

                                    # -----------------------------------#

                                    print ("用户信息写入成功，请查看！！！")

                                    # -----------------------------------#

                                    sleep(1)

                                #手机号验证
                                try:

                                    #手机验证(便于接收上课短信通知)
                                    driver.find_element_by_xpath("//*[@id='mobileCode']/h3")

                                    #-----------------------------------------------------#

                                    print (user_mobile + "该手机号没有验证，请先验证手机号吧～")

                                    #-----------------------------------------------------#

                                    sleep(2)

                                    #触发滑块验证平台，获取验证码老是失败，通过不了
                                    # user_experience_class_slider_validation_mobile(driver,current_window_handle)

                                    #调取手机短信平台
                                    # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                    #调取后台stu_list表，验证手机号
                                    js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                    driver.execute_script(js)

                                    handles = driver.window_handles

                                    for current_handle in handles:

                                        if current_handle != current_window_handle:

                                            driver.switch_to_window(current_handle)

                                            sleep(2)

                                            #调取后台stu_list表，验证手机号
                                            user_stu_list_verify_mobile_status(driver,user_mobile)

                                            #调取手机短信平台
                                            # user_sms_platform_info(driver,user_mobile)

                                            sleep(2)

                                    driver.switch_to_window(current_window_handle)

                                    sleep(2)

                                    driver.refresh()

                                    sleep(2)

                                #直接约成人/青少体验课
                                except:

                                    #------------------------------------#

                                    print (user_mobile + "该手机号已验证，请选择体验课吧～")

                                    #------------------------------------#

                                    sleep(2)

                                # 调用约体验课
                                # user_experience_cadets_success(driver, current_window_handle, str(user_id),str(user_mobile))

                                # 查询体验用户财富信息
                                # wealth_data = user_experience_the_wealth_success(driver, login_after_link,str(user_id), str(user_mobile))

                                # 预约公开课
                                # user_open_class_success(driver, current_window_handle, login_after_link,wealth_data,str(user_id),str(user_mobile))

                                # 预约精品小班课
                                # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                        #美小付费账号
                        elif login_after_link == "http://aa.51talk.com/user/index" or \
                             login_after_link == "https://aa.51talk.com/user/index":

                                #------------------------------------------------------#

                                print (user_mobile + "该账号为美小付费学员类型，直接进入体验账号会员中心啦~")

                                #------------------------------------------------------#

                                try:

                                    user_center_layer_operation(driver)

                                except:

                                    pass

                        #美小体验账号，直接进入体验约课页面
                        elif login_after_link == "http://aa.51talk.com/nat/trial/reserve_new?date=" or \
                             login_after_link == "https://aa.51talk.com/nat/trial/reserve_new?date=":

                                try:

                                    user_center_layer_operation(driver)

                                except:

                                    pass

                                #手机号验证
                                try:

                                    #手机验证(便于接收上课短信通知)
                                    driver.find_element_by_xpath("/html/body/div[2]/div[5]/h3")

                                    #-----------------------------------------------------#

                                    print (user_mobile + "该手机号没有验证，请先验证手机号吧～")

                                    #-----------------------------------------------------#

                                    sleep(2)

                                    #调取手机短信平台
                                    # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                    #调取后台stu_list表，验证手机号
                                    js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                    driver.execute_script(js)

                                    handles = driver.window_handles

                                    for current_handle in handles:

                                        if current_handle != current_window_handle:

                                            driver.switch_to_window(current_handle)

                                            sleep(2)

                                            #调取后台stu_list表，验证手机号
                                            user_stu_list_verify_mobile_status(driver,user_mobile)

                                            #调取手机短信平台
                                            # user_sms_platform_info(driver,user_mobile)

                                            sleep(2)

                                    driver.switch_to_window(current_window_handle)

                                    sleep(2)

                                    driver.refresh()

                                    sleep(2)

                                #直接约美小体验课
                                except:

                                    #------------------------------------#

                                    print (user_mobile + "该手机号已验证，请选择体验课吧～")

                                    #------------------------------------#

                        #美小体验账号，直接进入会员中心
                        elif login_after_link == "http://aa.51talk.com/trial/index" or \
                             login_after_link == "https://aa.51talk.com/trial/index":

                                try:

                                    user_center_layer_operation(driver)

                                except:

                                    pass


                                #判断美小预约课程按钮是否存在
                                try:

                                    #预约体验课按钮
                                    driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div[2]/a")

                                    sleep(2)

                                    #预约体验课按钮点击
                                    driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div[2]/a").click()

                                    #手机号验证
                                    try:

                                        #手机验证(便于接收上课短信通知)
                                        driver.find_element_by_xpath("/html/body/div[2]/div[5]/h3")

                                        #-----------------------------------------------------#

                                        print (user_mobile + "该手机号没有验证，请先验证手机号吧～")

                                        #-----------------------------------------------------#

                                        sleep(2)

                                        #调取手机短信平台
                                        # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                        #调取后台stu_list表，验证手机号
                                        js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                        driver.execute_script(js)

                                        handles = driver.window_handles

                                        for current_handle in handles:

                                            if current_handle != current_window_handle:

                                                driver.switch_to_window(current_handle)

                                                sleep(2)

                                                #调取后台stu_list表，验证手机号
                                                user_stu_list_verify_mobile_status(driver,user_mobile)

                                                #调取手机短信平台
                                                # user_sms_platform_info(driver,user_mobile)

                                                sleep(2)

                                        driver.switch_to_window(current_window_handle)

                                        sleep(2)

                                        driver.refresh()

                                    #直接约美小体验课
                                    except:

                                        #-------------------------------------------------#

                                        print (user_mobile + "该手机号已验证，请选择体验课吧～")

                                        #-------------------------------------------------#

                                except:

                                    #--------------------------------------------------#

                                    print ("没有找到美小预约体验课按钮，无法进行约体验课哦~")

                                    #--------------------------------------------------#

                        else:

                            #------------------------------------------#

                            print ("该用户登录成功，但是不能操作，请查看原因：")

                            #------------------------------------------#

                        # 退出51TALK会员中心
                        try:

                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                            sleep(2)

                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                            sleep(2)

                        except:

                            pass

                        sleep(2)

                if xunhuan_login_index == xunhuan_login_max -1:

                    pass

                else:

                    print ("\n")

            cursor_onlie_test.close()

            conn_onlie_test.close()

            print ("***********************************************************")

#----------------------------------------------------------------------------------------------------------------------#
    #主站登录页面--账号密码登录失败
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_account_password_login_info_fail(self):

            print ("*************主站登录页面--账号密码登录失败*************")

            u"""账号密码注册信息异常，不能登录."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            # 读入文件--xlsx
            # read_login_fail_xlsx = dqXlsLoginFail()

            # for i in range(1, len(read_login_fail_xlsx)):
            #
            #     user_account = int(read_login_fail_xlsx[i][0])
            #     user_password = int(read_login_fail_xlsx[i][1])
            #     user_english_name = read_login_fail_xlsx[i][2]
            #     user_tuijian_mobile = int(read_login_fail_xlsx[i][3])

            # 读入文件--txt
            read_login_fail_txt = readLoginFailFile()

            for line in read_login_fail_txt:

                user_account     = line.split(',')[0]
                user_password   = line.split(',')[1]

                #输入账号
                driver.find_element_by_xpath("//*[@id='accountId']").send_keys(user_account)

                sleep(2)

                #输入密码
                driver.find_element_by_xpath("//*[@id='password']").send_keys(user_password)

                sleep(2)

                #登录按钮
                driver.find_element_by_xpath("//*[@id='accountLoginBtn']").click()

                sleep(2)

                #错误提示
                try:

                    if driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[1]/div[2]/div") or \
                       driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[2]/div[2]/div"):

                        login_info_arrey=['请输入您的账号',
                                          '请输入密码'
                                          '密码长度只能是6-20位字符']

                        refresh_flag = False

                        #请输入您的账号
                        login_info_error_text_1 = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[1]/div[2]/div").text

                        #请输入密码、密码长度只能是6-20位字符
                        login_info_error_text_2 = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[2]/div[2]/div").text

                        if login_info_error_text_1 == u"请输入您的账号" and login_info_error_text_2 == u"请输入密码":

                            print ("#-------------------------------#")

                            print (u"该手机号输入为空，请重新输入！！！")
                            print (u"该密码输入为空，请重新输入！！！")

                            print ("#-------------------------------#" + "\n")

                            refresh_flag = True

                        elif login_info_error_text_2 == u"请输入密码":

                            print ("#-----------------------------#")

                            print (u"该账号为：" + user_account)
                            print (u"该密码输入为空，请重新输入！！！")

                            print ("#-----------------------------#" + "\n")

                            refresh_flag = True

                        elif login_info_error_text_2 == u"密码长度只能是6-20位字符":

                            print ("#-------------------------------------------------------------#")

                            print (u"该账号为：" + user_account)
                            print (u"该密码为：" + user_password + u",该密码格式错误，请重新输入！！！")

                            print ("#-------------------------------------------------------------#" + "\n")

                            refresh_flag = True

                        else:

                            #判断手机号是否被注册
                            try:

                                #您的用户名或密码错误
                                driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                # print (driver.find_element_by_xpath("//*[@id='contentInfo1']").text)

                                sleep(1)

                                #我知道了按钮
                                driver.find_element_by_xpath("//*[@id='sureId']").click()

                            except:

                                #密码错误，请立即找回
                                driver.find_element_by_xpath("//*[@id='contentInfo3']")

                                # print (driver.find_element_by_xpath("//*[@id='contentInfo3']").text)

                                sleep(1)

                                #找回密码按钮
                                driver.find_element_by_xpath("//*[@id='layer3']/div[2]/div[2]/a").click()

                                sleep(1)

                                forget_password_url = driver.current_url

                                sleep(1)

                                if forget_password_url == "http://login.51talk.com/password/forgot" or \
                                   forget_password_url == "https://login.51talk.com/password/forgot":

                                    #------------------------------#

                                    # print ("找回密码打开链接正确啦～")

                                    #------------------------------#

                                    pass

                        if refresh_flag == True:

                            driver.refresh()

                            #---------------------------------------#

                            print ("需要刷新页面，更新当前页面状态啦～")

                            #---------------------------------------#

                except:

                    pass

            print ("***********************************************")

#----------------------------------------------------------------------------------------------------------------------#
    #主站登录页面--手机号登录成功
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_mobile_login_info_success(self):

            print ("*************主站登录页面--手机号登录成功*************")

            for xunhuan_login_index in range(0, xunhuan_login_max):

                u"""手机号注册信息正确，正常登录."""

                driver = self.driver

                driver.get(self.url)

                sleep(1)

                driver.maximize_window()

                sleep(1)

                #调用启动页进入青少儿官网
                startPageComeInto(driver)

                sleep(1)

                current_window_handle = driver.current_window_handle

                #点击登录
                driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

                sleep(1)

                #点手机号登录TAB
                driver.find_element_by_xpath("//*[@id='loginTab']/li[2]").click()

                sleep(1)

                #获取当天现在时间
                current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                sleep(1)

                #读入文件--xlsx
                # read_login_success_xlsx = dqXlsLoginSuccess()
                #
                # for i in range(1, len(read_login_success_xlsx)):
                #
                #     user_account = int(read_login_success_xlsx[i][0])
                #     user_password = int(read_login_success_xlsx[i][1])
                #     user_english_name = read_login_success_xlsx[i][2]
                #     user_tuijian_mobile = int(read_login_success_xlsx[i][3])

                #读入文件--txt
                read_login_success_txt = readLoginSuccessFile()

                for i in read_login_success_txt:

                    user_mobile = i.split(',')[0]
                    user_password = i.split(',')[1]

                user_mobile = raw_input("请输入用户登录手机号：")

                sleep(0.5)

                user_password = raw_input("请输入用户登录密码：")

                #输入手机号
                driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

                sleep(1)

                #点击滑块
                driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[2]/div/div[2]").click()

                sleep(1)

                #手机号错误提示
                try:

                        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[1]/div[2]/div")

                        mobile_login_error_info_arrey=['请输入手机号',
                                                       '手机号格式错误，请重新输入'
                                                       '请您先注册']
                        mobile_clear_flag = False

                        #请输入您的账号
                        mobile_login_error_info_text_1 = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[1]/div[2]/div").text

                        if mobile_login_error_info_text_1 == u"请输入手机号":

                            print ("#-------------------------------#")

                            print (u"该手机号输入为空，请重新输入！！！")

                            print ("#-------------------------------#" + "\n")

                            mobile_clear_flag = True

                        elif mobile_login_error_info_text_1 == u"手机号格式错误，请重新输入":

                            print ("#-----------------------------------------------------------#")

                            print (u"该手机为：" + user_mobile + u",该手机格式错误，请重新输入！！！")

                            print ("#-----------------------------------------------------------#" + "\n")

                            mobile_clear_flag = True


                        elif mobile_login_error_info_text_1 == u"请您先注册":

                            print ("#-----------------------------------------------------------#")

                            print (u"该手机还未注册：" + user_mobile + u",请输入注册过的手机号！！！")

                            print ("#-----------------------------------------------------------#" + "\n")

                            mobile_clear_flag = True

                        #手机号错误提示
                        if mobile_clear_flag == True:

                            driver.find_element_by_xpath("//*[@id='mobile']").clear()

                        else:

                            sleep(2)

                            #滑块
                            huakuai = "//*[@id='container']/div/div[2]/form/div[2]/div/div[2]"

                            actione_1 = ActionChains(driver)

                            source = driver.find_element_by_xpath(huakuai)

                            #鼠标左键按下不放
                            actione_1.click_and_hold(source).perform()

                            sleep(1)

                            #调用开始滑块请求
                            urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=move_start&gt=1")

                            sleep(1)

                            #鼠标左键滑动坐标
                            actione_1.move_by_offset(400,0)

                            sleep(1)

                            #释放鼠标左键
                            actione_1.release().perform()

                            sleep(1)

                            #调用结束滑块请求
                            urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=success&gt=3")

                            sleep(2)

                            try:

                                driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                mobileCode_error_text = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                                if mobileCode_error_text == u"手机号发送短信次数过多，如需帮助请拨打4000515151":

                                    #------------------------------------------#

                                    print ("该手机号重复发送次数过多，请稍后再试～")

                                    #------------------------------------------#

                                    sleep(1)

                                    driver.find_element_by_xpath("//*[@id='sureId']").click()

                                    sleep(1)

                                    driver.refresh()

                                    sleep(1)

                                elif mobileCode_error_text == "滑动验证失败，请重新操作。":

                                    #-----------------------------------#

                                    print ("滑动失败，请刷新页面重新加载～")

                                    #-----------------------------------#

                                    sleep(1)

                                    driver.refresh()

                                    sleep(1)

                                else:

                                    #调取手机短信平台
                                    js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                    driver.execute_script(js)

                                    handles = driver.window_handles

                                    for current_handle in handles:

                                        if current_handle != current_window_handle:

                                            driver.switch_to_window(current_handle)

                                            sleep(1)

                                            #调取手机短信平台
                                            jiequ_code = user_sms_platform_info(driver,user_mobile)

                                            sleep(1)

                                            #调取文件读操作
                                            # jiequ_code = user_file_r_operation()

                                    driver.switch_to_window(current_window_handle)

                                    sleep(2)

                                    #判断验证码输入框是否存在
                                    try:

                                        driver.find_element_by_xpath("//*[@id='code']")

                                        #输入短信验证码
                                        driver.find_element_by_xpath("//*[@id='code']").send_keys(jiequ_code)

                                        sleep(1)

                                        #登录按钮
                                        driver.find_element_by_xpath("//*[@id='mobileLoginBtn']").click()

                                        sleep(2)

                                        try:

                                            driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                            mobile_code = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                                            if mobile_code == u"验证码输入不正确":

                                                #我知道了按钮
                                                driver.find_element_by_xpath("//*[@id='sureId']").click()

                                            elif mobile_code == u" 密码错误，请立即找回":

                                                #找回密码按钮
                                                driver.find_element_by_xpath("//*[@id='layer3']/div[2]/div[2]/a").click()

                                            else:

                                                #----------------#

                                                print ("其他错误")

                                                #----------------#

                                        except:

                                                flag_resiget_succes_tips = False

                                                # 查询user表mobile,password
                                                db_user = userInformation_db_query_mobile_password_success(user_mobile)

                                                sleep(1)

                                                # 获取用户user_id数据
                                                db_user_id = userInformation_db_query_user_id_success(user_mobile)

                                                if db_user == ():

                                                    # 调取后台stu_list表，验证手机号
                                                    js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

                                                    driver.execute_script(js)

                                                    handles = driver.window_handles

                                                    for current_handle in handles:

                                                        if current_handle != current_window_handle:
                                                            driver.switch_to_window(current_handle)

                                                            sleep(2)

                                                            # 调用后台stu_list查询user_id
                                                            user_id = user_stu_list_query_user_user_id(driver,
                                                                                                       user_mobile)

                                                            driver.close()

                                                    sleep(1)

                                                    driver.switch_to_window(current_window_handle)

                                                    sleep(1)

                                                    # 插入之前注册过的用户信息
                                                    userInformation_db_old_data_insert_success(user_id, user_mobile,
                                                                                               user_password,
                                                                                               current_now_time)

                                                    # -----------------------------------#

                                                    print ("用户信息写入正确，请查看！！！")

                                                    # -----------------------------------#

                                                else:

                                                    if db_user_id == "" or db_user_id == None:

                                                        sleep(1)

                                                        # 调取后台stu_list表，验证手机号
                                                        js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

                                                        driver.execute_script(js)

                                                        sleep(1)

                                                        handles = driver.window_handles

                                                        for current_handle in handles:

                                                            if current_handle != current_window_handle:
                                                                driver.switch_to_window(current_handle)

                                                                sleep(2)

                                                                # 调用后台stu_list查询user_id
                                                                user_id = user_stu_list_query_user_user_id(driver,
                                                                                                           user_mobile)

                                                                driver.close()

                                                        sleep(1)

                                                        driver.switch_to_window(current_window_handle)

                                                        sleep(1)

                                                        # 更新user表user_id数据
                                                        userInformation_db_user_data_update_user_id_success(
                                                            str(user_mobile), str(user_id))

                                                    else:

                                                        user_id = db_user_id

                                                sleep(1)

                                                #判断元素是否找到
                                                try:
                                                    driver.find_element(By.XPATH,"//*[@id='usersSelect']/div[4]/div/div[1]/h3")
                                                    # print (u"找到该元素！！！")

                                                    flag_resiget_succes_tips = True

                                                except:

                                                    # print (u"没有找到该元素！！！")
                                                    flag_resiget_succes_tips =  False

                                                if flag_resiget_succes_tips == True:

                                                    #调取学员身份选择功能
                                                    user_identity_select_info(driver)

                                                login_after_link = driver.current_url

                                                #成人/青少付费账号
                                                if login_after_link == "https://www.51talk.com/user/index" or \
                                                   login_after_link == "http://www.51talk.com/user/index":

                                                        #----------------------------------------------------#

                                                        print ("该账号为成人/青少付费学员类型，直接进入会员中心啦～")

                                                        #----------------------------------------------------#

                                                        try:

                                                            user_center_layer_operation(driver)

                                                        except:

                                                            pass

                                                        sleep(2)

                                                        # 查询付费用户财富信息
                                                        # wealth_data = user_paid_the_wealth_success(driver,str(user_id),str(user_mobile))

                                                        # 预约公开课
                                                        # user_open_class_success(driver,current_window_handle,login_after_link,wealth_data,str(user_id),str(user_mobile))

                                                        # 预约精品小班课
                                                        # user_fine_class_success(driver,current_window_handle,wealth_data,str(user_id),str(user_mobile))

                                                #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
                                                elif login_after_link == "http://trial.51talk.com/trial/index" or \
                                                     login_after_link == "https://trial.51talk.com/trial/index":

                                                        #---------------------------------------------------------------------------------#

                                                        print ("该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入体验账号会员中心啦~")

                                                        #---------------------------------------------------------------------------------#

                                                        try:

                                                            user_center_layer_operation(driver)

                                                        except:

                                                            pass

                                                        # 调用约体验课
                                                        user_experience_cadets_success(driver, current_window_handle,str(user_id), str(user_mobile))

                                                        # 查询体验用户财富信息
                                                        # wealth_data = user_experience_the_wealth_success(driver,login_after_link,str(user_id),str(user_mobile))

                                                        # 预约公开课
                                                        # user_open_class_success(driver, current_window_handle,login_after_link,wealth_data, str(user_id),str(user_mobile))

                                                        # 预约精品小班课
                                                        # user_fine_class_success(driver, current_window_handle,wealth_data, str(user_id),str(user_mobile))

                                                #成人/青少体验账号，进入体验约课页面
                                                elif login_after_link == "http://trial.51talk.com/trial/reserve" or \
                                                     login_after_link == "https://trial.51talk.com/trial/reserve":

                                                        #---------------------------------------------------------------#

                                                        print (user_mobile + "该账号为成人/青少体验学员类型，还没有约课，请先进行体验课约课啦~")

                                                        #---------------------------------------------------------------#

                                                        # 获取用户user_wealth表point
                                                        db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)

                                                        sleep(1)

                                                        if db_wealth_data == ():

                                                            point = "1"

                                                            point_validity = None

                                                            classtime = ""

                                                            # 插入user_wealth表point
                                                            userInformation_db_wealth_data_insert_success(user_id,
                                                                                                          user_mobile,
                                                                                                          point,
                                                                                                          point_validity,
                                                                                                          classtime,
                                                                                                          current_now_time)

                                                            # -----------------------------------#

                                                            print ("用户信息写入成功，请查看！！！")

                                                            # -----------------------------------#

                                                            sleep(1)

                                                        #手机号验证
                                                        try:

                                                            #手机验证(便于接收上课短信通知)
                                                            driver.find_element_by_xpath("//*[@id='mobileCode']/h3")

                                                            #----------------------------------------#

                                                            print ("该手机号没有验证，请先验证手机号吧～")

                                                            #----------------------------------------#

                                                            sleep(2)

                                                            #触发滑块验证平台，获取验证码老是失败，通过不了
                                                            # user_experience_class_slider_validation_mobile(driver,current_window_handle)

                                                            #调取手机短信平台
                                                            # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                                            #调取后台stu_list表，验证手机号
                                                            js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                                            driver.execute_script(js)

                                                            handles = driver.window_handles

                                                            for current_handle in handles:

                                                                if current_handle != current_window_handle:

                                                                    driver.switch_to_window(current_handle)

                                                                    sleep(2)

                                                                    #调取后台stu_list表，验证手机号
                                                                    user_stu_list_verify_mobile_status(driver,user_mobile)

                                                                    #调取手机短信平台
                                                                    # user_sms_platform_info(driver,user_mobile)

                                                                    sleep(2)

                                                            driver.switch_to_window(current_window_handle)

                                                            sleep(2)

                                                            driver.refresh()

                                                        #直接约成人/青少体验课
                                                        except:

                                                            #------------------------------------#

                                                            print ("该手机号已验证，请选择体验课吧～")

                                                            #------------------------------------#

                                                            sleep(2)

                                                        # 调用约体验课
                                                        user_experience_cadets_success(driver, current_window_handle,str(user_id), str(user_mobile))

                                                        # 查询体验用户财富信息
                                                        # wealth_data = user_experience_the_wealth_success(driver,login_after_link,str(user_id),str(user_mobile))

                                                        # 预约公开课
                                                        # user_open_class_success(driver, current_window_handle,login_after_link, wealth_data,str(user_id),str(user_mobile))

                                                        # 预约精品小班课
                                                        # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                                                #美小付费账号
                                                elif login_after_link == "http://aa.51talk.com/user/index" or \
                                                     login_after_link == "https://aa.51talk.com/user/index":

                                                        #------------------------------------------------------#

                                                        print ("该账号为美小付费学员类型，直接进入体验账号会员中心啦~")

                                                        #------------------------------------------------------#

                                                        try:

                                                            user_center_layer_operation(driver)

                                                        except:

                                                            pass

                                                #美小体验账号，直接进入体验约课页面
                                                elif login_after_link == "http://aa.51talk.com/nat/trial/reserve_new?date=" or \
                                                     login_after_link == "https://aa.51talk.com/nat/trial/reserve_new?date=":

                                                        try:

                                                            user_center_layer_operation(driver)

                                                        except:

                                                            pass

                                                        #手机号验证
                                                        try:

                                                            #手机验证(便于接收上课短信通知)
                                                            driver.find_element_by_xpath("/html/body/div[2]/div[5]/h3")

                                                            #----------------------------------------#

                                                            print ("该手机号没有验证，请先验证手机号吧～")

                                                            #----------------------------------------#

                                                            sleep(2)

                                                            #调取手机短信平台
                                                            # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                                            #调取后台stu_list表，验证手机号
                                                            js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                                            driver.execute_script(js)

                                                            handles = driver.window_handles

                                                            for current_handle in handles:

                                                                if current_handle != current_window_handle:

                                                                    driver.switch_to_window(current_handle)

                                                                    sleep(2)

                                                                    #调取后台stu_list表，验证手机号
                                                                    user_stu_list_verify_mobile_status(driver,user_mobile)

                                                                    #调取手机短信平台
                                                                    # user_sms_platform_info(driver,user_mobile)

                                                                    sleep(2)

                                                            driver.switch_to_window(current_window_handle)

                                                            sleep(2)

                                                            driver.refresh()

                                                        #直接约美小体验课
                                                        except:

                                                            #------------------------------------#

                                                            print ("该手机号已验证，请选择体验课吧～")

                                                            #------------------------------------#

                                                #美小体验账号，直接进入会员中心
                                                elif login_after_link == "http://aa.51talk.com/trial/index" or \
                                                     login_after_link == "https://aa.51talk.com/trial/index":

                                                        try:

                                                            user_center_layer_operation(driver)

                                                        except:

                                                            pass

                                                        #判断美小预约课程按钮是否存在
                                                        try:

                                                            #预约体验课按钮
                                                            driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div[2]/a")

                                                            sleep(2)

                                                            #预约体验课按钮点击
                                                            driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div[2]/a").click()

                                                            #手机号验证
                                                            try:

                                                                #手机验证(便于接收上课短信通知)
                                                                driver.find_element_by_xpath("/html/body/div[2]/div[5]/h3")

                                                                #----------------------------------------#

                                                                print ("该手机号没有验证，请先验证手机号吧～")

                                                                #----------------------------------------#

                                                                sleep(2)

                                                                #调取手机短信平台
                                                                # js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                                                                #调取后台stu_list表，验证手机号
                                                                js ='window.open("http://www.51talk.com/admin/admin_login.php")'

                                                                driver.execute_script(js)

                                                                handles = driver.window_handles

                                                                for current_handle in handles:

                                                                    if current_handle != current_window_handle:

                                                                        driver.switch_to_window(current_handle)

                                                                        sleep(2)

                                                                        #调取后台stu_list表，验证手机号
                                                                        user_stu_list_verify_mobile_status(driver,user_mobile)

                                                                        #调取手机短信平台
                                                                        # user_sms_platform_info(driver,user_mobile)

                                                                        sleep(2)

                                                                driver.switch_to_window(current_window_handle)

                                                                sleep(2)

                                                                driver.refresh()

                                                            #直接约美小体验课
                                                            except:

                                                                #------------------------------------#

                                                                print ("该手机号已验证，请选择体验课吧～")

                                                                #------------------------------------#

                                                        except:

                                                            #--------------------------------------------------#

                                                            print ("没有找到美小预约体验课按钮，无法进行约体验课哦~")

                                                            #--------------------------------------------------#

                                                else:

                                                    #----------------------------------------#

                                                    print ("登录成功，但是不能操作，请查看原因：")

                                                    #----------------------------------------#

                                                # 退出51TALK会员中心
                                                try:

                                                    driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                                                    sleep(2)

                                                    driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                                                    sleep(2)

                                                except:

                                                    pass

                                                sleep(2)

                                    except:

                                        pass

                            except:

                                pass
                except:

                    pass

                if xunhuan_login_index == xunhuan_login_max -1:

                    pass

                else:

                    print ("\n")

            cursor_onlie_test.close()

            conn_onlie_test.close()

            print ("***********************************************")

#----------------------------------------------------------------------------------------------------------------------#
    #主站登录页面--手机号登录失败
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_mobile_login_info_fail(self):

            print ("*************主站登录页面--手机号登录失败*************")

            u"""手机号注册信息异常，不能登录."""

            driver = self.driver

            driver.get(self.url)

            sleep(1)

            driver.maximize_window()

            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            # 读入文件--xlsx
            # read_login_fail_xlsx = dqXlsLoginFail()
            #
            # for i in range(1, len(read_login_fail_xlsx)):
            #
            #     user_account = int(read_login_fail_xlsx[i][0])
            #     user_password = int(read_login_fail_xlsx[i][1])
            #     user_english_name = read_login_fail_xlsx[i][2]
            #     user_tuijian_mobile = int(read_login_fail_xlsx[i][3])

            # 读入文件--txt
            read_login_fail_txt = readLoginFailFile()

            for line in read_login_fail_txt:

                user_mobile     = line.split(',')[0]
                user_code       = line.split(',')[2]

                sleep(2)

                #点手机号登录TAB
                driver.find_element_by_xpath("//*[@id='loginTab']/li[2]").click()

                sleep(2)

                #输入手机号
                driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

                sleep(2)

                #滑块
                huakuai = "//*[@id='container']/div/div[2]/form/div[2]/div/div[2]"

                actione_1 = ActionChains(driver)

                source = driver.find_element_by_xpath(huakuai)

                #鼠标左键按下不放
                actione_1.click_and_hold(source).perform()

                #鼠标左键滑动坐标
                actione_1.move_by_offset(319,0)

                #释放鼠标左键
                actione_1.release().perform()

                sleep(2)

                #输入短信验证码
                driver.find_element_by_xpath("//*[@id='code']").send_keys(user_code)

                sleep(2)

                #登录按钮
                driver.find_element_by_xpath("//*[@id='mobileLoginBtn']").click()

                sleep(2)

                #错误提示
                try:

                        if driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[1]/div[2]/div") or \
                           driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[3]/div[2]/div"):

                            login_error_info_arrey=['请输入手机号',
                                                    '手机号格式错误，请重新输入',
                                                    '请您先注册',
                                                    '请输入验证码',
                                                    '验证码格式有误，请重新输入']

                            #请输入您的手机号
                            login_error_info_arrey_1 = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[1]/div[2]/div").text

                            #请输入短信验证码
                            login_error_info_arrey_2 = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[3]/div[2]/div").text

                            if login_error_info_arrey_1 == u"请输入手机号" and login_error_info_arrey_2 == u"请输入验证码":

                                print ("#-------------------------------#")

                                print (u"该手机号输入为空，请重新输入！！！")
                                print (u"该短信验证码输入为空，请重新输入！！！")

                                print ("#-------------------------------#" + "\n")

                            elif login_error_info_arrey_1 == u"手机号格式错误，请重新输入":

                                print ("#-----------------------------------------------------------#")

                                print (u"该手机为：" + user_mobile + u",该手机格式错误，请重新输入！！！")

                                print ("#-----------------------------------------------------------#" + "\n")

                            elif login_error_info_arrey_1 == u"请您先注册":

                                print ("#-----------------------------------------------------------#")

                                print (u"该手机还未注册：" + user_mobile + u",请输入注册过的手机号！！！")

                                print ("#-----------------------------------------------------------#" + "\n")

                            elif login_error_info_arrey_2 == u"请输入验证码":

                                print ("#-----------------------------------------------------------#")

                                print (u"该手机为：" + user_mobile)

                                print (u"该手机验证码为空，请重新输入！！！")

                                print ("#-----------------------------------------------------------#" + "\n")

                            elif login_error_info_arrey_2 == u"验证码格式有误，请重新输入":

                                print ("#-----------------------------------------------------------#")

                                print (u"该手机为：" + user_mobile)

                                print (u"该验证码为：" + user_code + u",该手机验证码格式错误，请重新输入！！！")

                                print ("#-----------------------------------------------------------#" + "\n")

                        #错误提示弹框
                        try:

                            driver.find_element_by_xpath("//*[@id='contentInfo1']")

                            login_tankuang_error = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                            if login_tankuang_error == u"验证码输入不正确":

                                #--------------------------------------#

                                print ("该手机验证码输入错误，请稍后重试～")

                                #--------------------------------------#

                                #我知道了按钮
                                driver.find_element_by_xpath("//*[@id='sureId']").click()

                            elif login_tankuang_error == u" 密码错误，请立即找回":

                                #---------------------------------------------------#

                                print ("该手机号、手机验证码输入错误已达6次，请稍后重试～")

                                #---------------------------------------------------#

                                #找回密码按钮
                                driver.find_element_by_xpath("//*[@id='layer3']/div[2]/div[2]/a").click()

                        except:

                            pass

                        sleep(2)

                        driver.refresh()

                except:

                    pass

            print ("***********************************************")

#----------------------------------------------------------------------------------------------------------------------#
    #主站账号密码登录页面--注册链接
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_account_resiget_link(self):

            print ("*************主站账号密码登录页面--注册链接*************")

            u"""注册链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #注册链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[3]/div[2]/a[1]").click()

            sleep(2)

            resiget_url = driver.current_url

            if resiget_url == "http://login.51talk.com/register/mobile?client=1" or \
               resiget_url == "https://login.51talk.com/register/mobile?client=1":

                print (u"注册链接正确～")

            print ("***********************************************")

#----------------------------------------------------------------------------------------------------------------------#
    #主站账号密码登录页面--忘记密码
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_account_forget_password_link(self):

            print ("*************主站账号密码登录页面--忘记密码*************")

            u"""忘记密码链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #忘记密码链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[3]/div[2]/a[2]").click()

            sleep(1)

            forget_password_url = driver.current_url

            if forget_password_url == "http://login.51talk.com/password/forgot?client=1" or \
               forget_password_url == "https://login.51talk.com/password/forgot?client=1":

                print (u"忘记密码链接正确～")

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站账号密码登录页面--立即注册
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_account_liji_resiget_link(self):

            print ("*************主站账号密码登录页面--立即注册*************")

            u"""立即注册链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #立即注册链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[1]/form/div[5]/div[2]/a").click()

            sleep(1)

            liji_resiget_url = driver.current_url

            if liji_resiget_url == "http://login.51talk.com/register/mobile?client=1" or \
               liji_resiget_url == "https://login.51talk.com/register/mobile?client=1":

                print (u"立即注册链接正确～")

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站手机号登录页面--注册链接
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_mobile_resiget_link(self):

            print ("*************主站手机号登录页面--注册链接*************")

            u"""注册链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #点手机号登录TAB
            driver.find_element_by_xpath("//*[@id='loginTab']/li[2]").click()

            sleep(1)

            #注册链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[4]/div[2]/a[1]").click()

            sleep(2)

            resiget_url = driver.current_url

            if resiget_url == "http://login.51talk.com/register/mobile?client=1" or \
               resiget_url == "https://login.51talk.com/register/mobile?client=1":

                print (u"注册链接正确～")

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站手机号登录页面--忘记密码
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_mobile_forget_password_link(self):

            print ("*************主站手机号登录页面--忘记密码*************")

            u"""忘记密码链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #点手机号登录TAB
            driver.find_element_by_xpath("//*[@id='loginTab']/li[2]").click()

            sleep(1)

            #忘记密码链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[4]/div[2]/a[2]").click()

            sleep(1)

            forget_password_url = driver.current_url

            if forget_password_url == "http://login.51talk.com/password/forgot?client=1" or \
               forget_password_url == "https://login.51talk.com/password/forgot?client=1":

                print (u"忘记密码链接正确～")

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站手机号登录页面--立即注册
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_mobile_liji_resiget_link(self):

            print ("*************主站手机号登录页面--立即注册*************")

            u"""立即注册链接."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            #点击登录
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

            sleep(1)

            #点手机号登录TAB
            driver.find_element_by_xpath("//*[@id='loginTab']/li[2]").click()

            sleep(1)

            #立即注册链接
            driver.find_element_by_xpath("//*[@id='container']/div/div[2]/form/div[6]/div[2]/a").click()

            sleep(1)

            liji_resiget_url = driver.current_url

            if liji_resiget_url == "http://login.51talk.com/register/mobile?client=1" or \
               liji_resiget_url == "https://login.51talk.com/register/mobile?client=1":

                print (u"立即注册链接正确～")

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

        def tearDown(self):

            QuitBrowser(self.driver)