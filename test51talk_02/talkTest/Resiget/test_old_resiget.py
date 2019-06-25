#!usr/bin/python
#encoding:utf-8

'''老注册模块'''

__author__ = 'zhangbo'

import unittest
from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By

from configuration_files.accountConfigInformation import *
from configuration_files.dqTxtFile import readResigetSuccessFile
from configuration_files.driver_configurationFiles import browser_driver

from db_files.userInformation_db_query import userInformation_db_query_user_id_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success
from db_files.userInformation_db_resiget_insert import *
from db_files.userInformation_db_wealth_data_insert import userInformation_db_wealth_data_insert_success
from talkUser.admin_backstage.user_stu_list import user_stu_list_query_user_user_id
from talkUser.admin_backstage.user_stu_list import user_stu_list_verify_mobile_status
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_experience_class.user_experience_cadets import user_experience_cadets_success
from talkUser.user_identity_select import user_identity_select_info
from talkUser.user_quit_browser import *
from talkUser.user_wealth import user_experience_the_wealth_success
from talkUser.user_wealth import user_paid_the_wealth_success
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_open_class.user_open_class import user_open_class_success
from talkUser.user_fine_class.user_fine_class import user_fine_class_success



class TestOldResiget(unittest.TestCase):

    u'''老登录方式操作如下'''

    def setUp(self):

        self.driver = browser_driver()

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    # 老注册页面--成功
#----------------------------------------------------------------------------------------------------------------------#

    def test_old_resiget_info_succes(self):

        print ("*************老注册页面--成功*************")

        for xunhuan_resiget_index in range(0,xunhuan_resiget_max):

            u"""老注册页面"""

            self.url = "http://login.51talk.com/web/register"

            driver = self.driver

            driver.get(self.url)

            sleep(1)

            driver.maximize_window()

            sleep(1)

            current_window_handle = driver.current_window_handle

            sleep(1)

            # 获取当天现在时间
            current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

            sleep(1)

            #读入文件--xlsx
            # read_login_success_xlsx = dqXlsResigetSuccess()
            #
            # for i in range(1, len(read_login_success_xlsx)):
            #
            #     user_account = int(read_login_success_xlsx[i][0])
            #     user_password = int(read_login_success_xlsx[i][1])
            #     user_english_name = read_login_success_xlsx[i][2]
            #     user_tuijian_mobile = int(read_login_success_xlsx[i][3])

            #读入文件--txt
            read_login_success_txt = readResigetSuccessFile()

            for i in read_login_success_txt:

                i = i.decode("utf-8")
                user_mobile = i.split(',')[0]
                user_password = i.split(',')[1]
                user_englishName = i.split(',')[2]
                user_recommenMobile = i.split(',')[3]

            # user_mobile = raw_input("请输入用户注册手机号：")
            #
            # user_password = raw_input("请输入用户注册密码：")
            #
            # user_englishName = raw_input("请输入用户的英文名：")
            #
            # user_recommenMobile = raw_input("请输入推荐用户的手机号码：")

            #推荐码user_id默认为空
            insert_user_id = ""

            #获取推荐人user_id
            user_id = userInformation_db_query_user_id_success(user_recommenMobile)

            if user_id == () or user_id == None or user_id == "":

                pass

            else:

                insert_user_id = user_id

            sleep(1)

            driver.find_element_by_id("mobile").send_keys(user_mobile)
            sleep(1)

            driver.find_element_by_id("password2").send_keys(user_password)
            sleep(1)

            driver.find_element_by_id("nickname").send_keys(user_englishName)
            sleep(1)

            driver.find_element_by_id("recMobile").send_keys(user_recommenMobile)
            sleep(1)

            #注册按钮
            driver.find_element_by_id("register").click()
            sleep(1)

            flag_resiget_succes_tips = False

            #判断元素是否找到
            try:

                driver.find_element(By.XPATH,"//*[@id='usersSelect']/div[4]/div/div[1]/h3")
                # print (u"找到该元素！！！")

                sleep(2)

                flag_resiget_succes_tips = True

                # 调取后台stu_list表，验证手机号
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

                #插入新数据
                userInformation_db_resiget_insert_success(user_id,user_mobile,user_password,user_englishName,insert_user_id,current_now_time)

                #-----------------------------------#

                print ("该用户注册信息写入成功，请查看！！！")

                #-----------------------------------#

            except:

                # print (u"没有找到该元素！！！")
                flag_resiget_succes_tips =  False

            sleep(1)

            if flag_resiget_succes_tips == True:

                #获取用户user_id数据
                # db_user_id = userInformation_db_query_user_id_success(user_mobile)

                sleep(4)

                #调取学员身份选择功能
                user_identity_select_info(driver)

                resiget_after_link = driver.current_url

                #成人/青少付费账号
                if resiget_after_link == "https://www.51talk.com/user/index" or \
                   resiget_after_link == "http://www.51talk.com/user/index":

                        #----------------------------------------------------#

                        print ("该账号为成人/青少付费学员类型，直接进入会员中心啦～")

                        #----------------------------------------------------#

                        try:

                            user_center_layer_operation(driver)

                        except:

                            pass

                        sleep(2)

                        #查询付费用户财富信息
                        # wealth_data = user_paid_the_wealth_success(driver, str(user_id), str(user_mobile))

                        sleep(2)

                        #预约公开课
                        # user_open_class_success(driver, current_window_handle, resiget_after_link,wealth_data, str(user_id), str(user_mobile))

                        sleep(2)

                        #预约精品小班课
                        # user_fine_class_success(driver,current_window_handle,wealth_data,str(user_id), str(user_mobile))

                #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
                elif resiget_after_link == "http://trial.51talk.com/trial/index" or \
                     resiget_after_link == "https://trial.51talk.com/trial/index":

                        #---------------------------------------------------------------------------------#

                        print (str(user_mobile) + "该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入会员中心查看记录")

                        #---------------------------------------------------------------------------------#

                        try:

                            user_center_layer_operation(driver)

                        except:

                            pass

                        sleep(2)

                        # 调用约体验课
                        # user_experience_cadets_success(driver, current_window_handle, str(user_id), str(user_mobile))

                        #查询体验用户财富信息
                        # wealth_data = user_experience_the_wealth_success(driver,resiget_after_link,str(user_id),str(user_mobile))

                        #预约公开课
                        # user_open_class_success(driver,current_window_handle,resiget_after_link,wealth_data,str(user_id),str(user_mobile))

                        #预约精品小班课
                        # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                #成人/青少体验账号，进入体验约课页面
                elif resiget_after_link == "http://trial.51talk.com/trial/reserve" or \
                     resiget_after_link == "https://trial.51talk.com/trial/reserve":

                        #---------------------------------------------------------------#

                        print (str(user_mobile) + "该账号为成人/青少体验学员类型，还没有约课，请先进行体验课约课")

                        #---------------------------------------------------------------#

                        # 获取用户user_wealth表point
                        db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)

                        sleep(1)

                        if db_wealth_data == ():

                            point = "1"

                            point_validity = None

                            classtime = ""

                            # 插入user_wealth表point
                            userInformation_db_wealth_data_insert_success(user_id, user_mobile, point, point_validity,
                                                                          classtime, current_now_time)

                            # -----------------------------------#

                            print ("该用户信息财富写入成功，请查看！！！")

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
                        # user_experience_cadets_success(driver, current_window_handle, str(user_id), str(user_mobile))

                        #查询体验用户财富信息
                        # wealth_data = user_experience_the_wealth_success(driver, resiget_after_link,str(user_id),str(user_mobile))

                        #预约公开课
                        # user_open_class_success(driver, current_window_handle,resiget_after_link, wealth_data,str(user_id),str(user_mobile))

                        #预约精品小班课
                        # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                #美小付费账号
                elif resiget_after_link == "http://aa.51talk.com/user/index" or \
                     resiget_after_link == "https://aa.51talk.com/user/index":

                        #------------------------------------------------------#

                        print (str(user_mobile) + "该账号为美小付费学员类型")

                        #------------------------------------------------------#

                        try:

                            user_center_layer_operation(driver)

                        except:

                            pass

                #美小体验账号，直接进入体验约课页面
                elif resiget_after_link == "http://aa.51talk.com/nat/trial/reserve_new?date=" or \
                     resiget_after_link == "https://aa.51talk.com/nat/trial/reserve_new?date=":

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
                elif resiget_after_link == "http://aa.51talk.com/trial/index" or \
                     resiget_after_link == "https://aa.51talk.com/trial/index":

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

                    #---------------------------------------#

                    print ("注册成功，但不能操作，请查看原因：")

                    #---------------------------------------#

                #退出51TALK会员中心
                try:

                    driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                    sleep(2)

                    driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                    sleep(2)

                except:

                    pass

                sleep(2)

                if xunhuan_resiget_index == xunhuan_resiget_max -1:

                        pass

                else:

                    print ("\n")

            else:

                #----------------------------#

                print ("注册页面异常，请查看原因：")

                #----------------------------#

        cursor_onlie_test.close()

        conn_onlie_test.close()

        print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

        QuitBrowser(self.driver)