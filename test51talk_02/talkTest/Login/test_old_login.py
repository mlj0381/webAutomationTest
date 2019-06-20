#!usr/bin/python
#encoding:utf-8


'''老登录模块'''


__author__ = 'zhangbo'


import unittest
from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By

from configuration_files.db_config import *
from configuration_files.dqXlsFile import dqXlsLoginSuccess
from configuration_files.dqTxtFile import readLoginSuccessFile
from db_files.userInformation_db_old_data_insert import userInformation_db_old_data_insert_success
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success
from db_files.userInformation_db_query import userInformation_db_query_user_id_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success
from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_user_id_success
from db_files.userInformation_db_wealth_data_insert import userInformation_db_wealth_data_insert_success
from talkUser.admin_backstage.user_stu_list import user_stu_list_query_user_user_id
from talkUser.admin_backstage.user_stu_list import user_stu_list_verify_mobile_status
from talkUser.user_account_select import *
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_identity_select import user_identity_select_info
from talkUser.user_quit_browser import *
from talkUser.user_wealth import user_experience_the_wealth_success
from talkUser.user_wealth import user_paid_the_wealth_success
from talkUser.user_open_class.user_open_class import user_open_class_success
from talkUser.user_fine_class.user_fine_class import user_fine_class_success
from talkUser.user_experience_class.user_experience_cadets import user_experience_cadets_success




class TestOldLogin(unittest.TestCase):

    u'''老登录方式操作如下'''

    def setUp(self):

        self.driver = webdriver.Chrome()

        # self.driver = config_driver.obj_phantomjs_mac_driver

        # self.driver = config_driver.obj_phantomjs_window_driver

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    # 老登录页面--成功
#----------------------------------------------------------------------------------------------------------------------#

    def test_old_login_info_success(self):

        print ("***************老登录页面--成功***************" + "\n")

        for xunhuan_login_index in range(0,xunhuan_login_max):

            u"""老登录页面"""

            self.url    = "http://login.51talk.com/web/login?client=1"

            driver = self.driver

            driver.get(self.url)

            sleep(2)

            driver.maximize_window()

            sleep(2)

            current_window_handle = driver.current_window_handle

            sleep(2)

            wealth_data = []

            # 获取当天现在时间
            current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

            sleep(2)

            #读入文件--xlsx
            read_login_success_xlsx = dqXlsLoginSuccess()

            for i in range(1, len(read_login_success_xlsx)):

                user_mobile = int(read_login_success_xlsx[i][0])
                user_password = int(read_login_success_xlsx[i][1])

            #读入文件--txt
            # read_login_success_txt = (readLoginSuccessFile)
            #
            # for i in read_login_success_txt:
            #
            #     user_mobile = i.split(',')[0]
            #     user_password = i.split(',')[1]

            # user_mobile = raw_input("请输入用户登录手机号：")

            sleep(0.5)

            # user_password = raw_input("请输入用户登录密码：")

            sleep(2)

            #输入账号
            driver.find_element_by_xpath("//*[@id='username']").send_keys(user_mobile)

            sleep(2)

            #输入密码
            driver.find_element_by_xpath("//*[@id='password2']").send_keys(user_password)

            sleep(2)

            #登录按钮
            driver.find_element_by_xpath("//*[@id='login']").click()

            sleep(2)

            #判断手机号是否被注册
            flag_login_succes_tips = False

            #判断元素是否找到
            try:
                driver.find_element(By.XPATH,"//*[@id='usersSelect']/div[4]/div/div[1]/h3")
                # print (u"找到该元素！！！")

                flag_login_succes_tips = True

            except:

                # print (u"没有找到该元素！！！")

                flag_login_succes_tips =  False

            # 查询user表mobile,password
            db_user = userInformation_db_query_mobile_password_success(user_mobile)

            sleep(1)

            # 获取用户user_id数据
            db_user_id = userInformation_db_query_user_id_success(user_mobile)

            if db_user == ():

                # 调取后台stu_list表，查询user_id
                js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

                driver.execute_script(js)

                handles = driver.window_handles

                for current_handle in handles:

                    if current_handle != current_window_handle:

                        driver.switch_to_window(current_handle)

                        sleep(2)

                        # 调用后台stu_list查询user_id
                        user_id = user_stu_list_query_user_user_id(driver,user_mobile)

                        driver.close()

                sleep(1)

                driver.switch_to_window(current_window_handle)

                sleep(1)

                # 插入之前注册过的用户信息
                userInformation_db_old_data_insert_success(user_id,user_mobile,user_password,current_now_time)

                #-----------------------------------#

                print ("用户信息写入正确，请查看！！！")

                #-----------------------------------#

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
                            user_id = user_stu_list_query_user_user_id(driver,user_mobile)

                            driver.close()

                    sleep(1)

                    driver.switch_to_window(current_window_handle)

                    sleep(1)

                    # 更新user表user_id数据
                    userInformation_db_user_data_update_user_id_success(str(user_mobile),str(user_id))

                else:

                    user_id = db_user_id

            sleep(1)

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

                    #查询弹出层后关闭
                    try:

                        user_center_layer_operation(driver)

                    except:

                        pass

                    sleep(2)

                    #查询付费用户财富信息
                    # wealth_data = user_paid_the_wealth_success(driver,str(user_id),str(user_mobile))

                    #预约公开课
                    # user_open_class_success(driver,current_window_handle,login_after_link,wealth_data,str(user_id),str(user_mobile))

                    #预约精品小班课
                    # user_fine_class_success(driver,current_window_handle,wealth_data,str(user_id),str(user_mobile))

            #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
            elif login_after_link == "http://trial.51talk.com/trial/index" or \
                 login_after_link == "https://trial.51talk.com/trial/index":

                    #---------------------------------------------------------------------------------#

                    print ("该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入体验账号会员中心啦~")

                    #---------------------------------------------------------------------------------#

                    #查询弹出层后关闭
                    try:

                        user_center_layer_operation(driver)

                    except:

                        pass

                    sleep(2)

                    #调用约体验课
                    # user_experience_cadets_success(driver,current_window_handle,str(user_id),str(user_mobile))

                    #查询体验用户财富信息
                    # wealth_data = user_experience_the_wealth_success(driver,login_after_link,str(user_id),str(user_mobile))

                    #预约公开课
                    # user_open_class_success(driver,current_window_handle,login_after_link,wealth_data,str(user_id),str(user_mobile))

                    #预约精品小班课
                    # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

            #成人/青少体验账号，进入体验约课页面
            elif login_after_link == "http://trial.51talk.com/trial/reserve" or \
                 login_after_link == "https://trial.51talk.com/trial/reserve":

                    #---------------------------------------------------------------#

                    print (str(user_mobile) + "该账号为成人/青少体验学员类型，还没有约课，请先进行体验课约课啦~")

                    #---------------------------------------------------------------#

                    # 获取用户user_wealth表point
                    db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)

                    sleep(1)

                    if db_wealth_data == ():

                        point = "1"

                        point_validity = None

                        classtime = ""

                        # 插入user_wealth表point
                        userInformation_db_wealth_data_insert_success(user_id,user_mobile,point,point_validity,classtime,current_now_time)

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

                        sleep(1)

                        #触发滑块验证平台，获取验证码老是失败，通过不了
                        # user_experience_class_slider_validation_mobile(driver,current_window_handle)

                        #调取手机短信平台
                        # js ='window.open("http://sms.51talk.com/Admin/Login/login")'

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
                                # jiequ_code = user_sms_platform_info(driver,user_account)

                                sleep(2)

                        driver.switch_to_window(current_window_handle)

                        #验证码输入框
                        # driver.find_element_by_xpath("//*[@id='mobileCode']/div/ul/li[3]/div/input").send_keys(jiequ_code)

                        sleep(2)

                        driver.refresh()

                        sleep(2)

                    #直接约成人/青少体验课
                    except:

                        #------------------------------------#

                        print ("该手机号已验证，请选择体验课吧～")

                        #------------------------------------#

                        sleep(2)

                    #调用约体验课
                    user_experience_cadets_success(driver,current_window_handle,str(user_id),str(user_mobile))

                    #查询体验用户财富信息
                    # wealth_data = user_experience_the_wealth_success(driver,login_after_link,str(user_id),str(user_mobile))

                    #预约公开课
                    # user_open_class_success(driver, current_window_handle, login_after_link,wealth_data,str(user_id),str(user_mobile))

                    #预约精品小班课
                    # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

            #美小付费账号
            elif login_after_link == "http://aa.51talk.com/user/index" or \
                 login_after_link == "https://aa.51talk.com/user/index":

                    #------------------------------------------------------#

                    print ("该账号为美小付费学员类型，直接进入体验账号会员中心啦~")

                    #------------------------------------------------------#

                    #查询弹出层后关闭
                    try:

                        user_center_layer_operation(driver)

                    except:

                        pass

            #美小体验账号，直接进入体验约课页面
            elif login_after_link == "http://aa.51talk.com/nat/trial/reserve_new?date=" or \
                 login_after_link == "https://aa.51talk.com/nat/trial/reserve_new?date=":

                    #查询弹出层后关闭
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

                        sleep(2)

                    #直接约美小体验课
                    except:

                        #------------------------------------#

                        print ("该手机号已验证，请选择体验课吧～")

                        #------------------------------------#

            #美小体验账号，直接进入会员中心
            elif login_after_link == "http://aa.51talk.com/trial/index" or \
                 login_after_link == "https://aa.51talk.com/trial/index":

                    #查询弹出层后关闭
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

            #退出51TALK会员中心
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

        print ("\n" + "***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

            QuitBrowser(self.driver)