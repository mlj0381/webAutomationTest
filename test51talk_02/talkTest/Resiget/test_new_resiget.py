#!usr/bin/python
#encoding:utf-8


'''新主站注册模块'''


__author__ = 'zhangbo'

import random
import unittest
from time import *

from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from configuration_files.accountConfigInformation import *
from configuration_files.dqTxtFile import readResigetSuccessFile, readResigetFailFile
from configuration_files.dqXlsFile import dqXlsResigetFail
from db_files.userInformation_db_old_data_insert import userInformation_db_old_data_insert_success
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success
from db_files.userInformation_db_query import userInformation_db_query_user_id_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success
from db_files.userInformation_db_resiget_insert import *
from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_user_id_success
from db_files.userInformation_db_wealth_data_insert import userInformation_db_wealth_data_insert_success
from talkTest.StartPage.startPagePopLayer import startPageComeInto
from talkUser.admin_backstage.user_stu_list import user_stu_list_query_user_user_id
from talkUser.admin_backstage.user_stu_list import user_stu_list_verify_mobile_status
from talkUser.user_center.user_center_layer import user_center_layer_operation
from talkUser.user_experience_class.user_experience_cadets import user_experience_cadets_success
from talkUser.user_identity_select import user_identity_select_info
from talkUser.user_quit_browser import *
from talkUser.user_sms_platform import user_sms_platform_info
from talkUser.user_open_class.user_open_class import user_open_class_success
from talkUser.user_fine_class.user_fine_class import user_fine_class_success
from talkUser.user_wealth import user_experience_the_wealth_success
from talkUser.user_wealth import user_paid_the_wealth_success
from talkUser.slider_validation.junior_official_website_resiget_slider_validation import junior_official_website_resiget_slider_validation_mobile


class TestNewResiget(unittest.TestCase):

        def setUp(self):

            self.driver = webdriver.Chrome()

            # self.driver = config_driver.obj_phantomjs_mac_driver

            # self.driver = config_driver.obj_phantomjs_window_driver

            self.url    = "http://www.51talk.com"

            sleep(2)


#----------------------------------------------------------------------------------------------------------------------#
    #官网首页，面板注册--注册成功
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_info_success(self):

            print ("*************官网首页，面板注册--注册成功*************")

            u"""注册信息正确，正常注册."""

            driver = self.driver

            driver.get(self.url)

            sleep(1)

            driver.maximize_window()

            sleep(1)

            # 调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            list_mobile = []
            list_password = []

            flag_mobile = False

            # 读入文件--xlsx
            # read_resiget_success_xlsx = dqXlsResigetSuccess()
            #
            # for i in range(1, len(read_resiget_success_xlsx)):
            #
            #     user_mobile = int(read_resiget_success_xlsx[i][0])
            #     user_password = int(read_resiget_success_xlsx[i][1])

            # 读入文件--txt
            read_resiget_success_txt = readResigetSuccessFile()



            for i in read_resiget_success_txt:

                user_mobile = i.split(',')[0]
                user_password = i.split(',')[1]

                list_mobile.append(user_mobile)
                list_password.append(user_password)

            for xunhuan_resiget_index in range(0, xunhuan_resiget_max):

                current_window_handle = driver.current_window_handle

                sleep(1)

                # 获取当天现在时间
                current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                sleep(1)

                # user_mobile = raw_input("请输入用户注册手机号：")

                # user_password = raw_input("请输入用户注册密码：")

                user_mobile = list_mobile[xunhuan_resiget_index]

                user_password = list_password[xunhuan_resiget_index]

                #手机号输入框
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").send_keys(user_mobile)
                sleep(1)

                # 点击密码框
                driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").send_keys(user_password)
                sleep(1)

                if int(len(user_mobile)) == 11 and int(len(user_password)) >=6:

                    flag_mobile = True

                    #点击滚动条按钮
                    driver.find_element_by_xpath("//*[@id='j_mobile_slider_outer']/dl/dd/div/div[2]").click()

                else:

                    print (user_mobile + ',' + user_password + "：当前手机号位数或登录密码不符合规则，请检查数据是否正确！！！")
                    print ("title：" + "手机号与密码规则如下：手机号11位、登录密码6位字符以上")
                    sleep(1)


                    # 清空手机号输入框
                    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").clear()
                    sleep(1)

                    # 清空密码输入框
                    driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").clear()
                    sleep(1)

                if flag_mobile == True:

                    sleep(1)

                    #判断面板手机号是否重复注册
                    try:

                        #手机号重复注册弹框，我知道了按钮
                        driver.find_element_by_xpath("//*[@id='sureId']").click()
                        sleep(1)

                    # except:

                        # pass

                    # try:

                        # driver.find_element_by_xpath("//*[@class='layer-box']/div[@class='mian-box']/div[@class='tit-box']/span[@id='closeId']")

                        # driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[1]")
                        # sleep(1)

                        # driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[1]").click()
                        # sleep(1)


                        flag_resiget_duplicate = True

                        sleep(1)

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

                    except:

                        flag_resiget_duplicate = False

                        #调用滑块验证
                        junior_official_website_resiget_slider_validation_mobile(driver)
                        sleep(1)

                    if flag_resiget_duplicate == True:

                        sleep(2)

                        # duplicate_randint = random.randint(0,1)

                        # print ("#---------------------------------------------------------#")
                        #
                        # print (u"该手机号" + user_mobile + u",已注册，请登录吧！！！")
                        #
                        # print ("#---------------------------------------------------------#" + "\n")
                        #
                        # if duplicate_randint == 0:
                        #
                        #     #直接登录
                        #     driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[1]").click()
                        #
                        #     sleep(2)
                        #
                        #     login_url = driver.current_url
                        #
                        #
                        #     if login_url == "http://login.51talk.com/login/index" or login_url == "https://login.51talk.com/login/index":
                        #
                        #         #-----------------------#
                        #
                        #         # print ("登录链接正确～")
                        #
                        #         #-----------------------#
                        #
                        #         pass
                        #
                        # else:
                        #
                        #     #找回密码
                        #     driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[2]").click()
                        #
                        #     zhaohuimima_url = driver.current_url
                        #
                        #     if zhaohuimima_url == "http://login.51talk.com/password/forgot" or zhaohuimima_url == "https://login.51talk.com/password/forgot":
                        #
                        #         # print ("找回密码链接正确～")
                        #
                        #         pass

                        # sleep(1)

                        # driver.back()

                        # sleep(1)

                        # startPageComeInto(driver)

                        # sleep(1)

                        #关闭弹框
                        # driver.find_element_by_xpath("//*[@class='layer-box']/div[@class='mian-box']/div[@class='tit-box']/span[@id='closeId']").click()

                        #点击手机号输入框
                        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").click()

                        #清空手机号输入框
                        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").clear()
                        sleep(1)

                        #清空密码输入框
                        driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").clear()
                        sleep(1)

                        print ("重新获取用户信息，验证吧！！！")

                    else:

                        sleep(1)

                        # 滑动验证码时判断滑块，手机号发送短信过多情况
                        try:


                            # 手机号发送短信过多，我知道了按钮
                            driver.find_element_by_xpath("//*[@id='sureId']").click()
                            sleep(1)

                            # -----------------------------------------------#

                            print ("手机号发送短信过多，请查看原因！！！" + "\n")

                            # -----------------------------------------------#

                        except:

                            # 调取手机短信平台
                            js ='window.open("http://sms.51talk.com/Admin/Login/login");'

                            driver.execute_script(js)

                            handles = driver.window_handles

                            for current_handle in handles:

                                if current_handle != current_window_handle:

                                    driver.switch_to_window(current_handle)

                                    sleep(2)

                                    # 调取手机短信平台
                                    code_mobile = user_sms_platform_info(driver,user_mobile)

                                    sleep(2)

                            driver.close()

                            driver.switch_to_window(current_window_handle)
                            sleep(2)

                            #输入验证码
                            driver.find_element_by_xpath("//*[@id='j_mobileCode']").send_keys(code_mobile)
                            sleep(2)

                            print(code_mobile)

                            #立即领取
                            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[2]").click()
                            sleep(2)

                            # 判断输入验证码超时，注册失败
                            try:

                                print ("验证码超时")
                                # 判断输入验证码超时，注册失败
                                driver.find_element_by_xpath("//*[@id='sureId']").click()
                                sleep(1)

                                # ----------------------------------------------------------#

                                print ("输入手机验证码超时，注册失败，请重新获取验证码！！" + "\n")

                                # ----------------------------------------------------------#

                            except:

                                print ("注册成功")
                                # resiget_info_arrey=['手机号码不能为空',
                                #                     '请填写正确的手机号码'
                                #                     '密码不能为空',
                                #                     '密码格式错误']

                                #点“注册”后，获取的url地址
                                resiget_after_url = driver.current_url

                                flag_resiget_after = False

                                #注册成功，进入学员选择身份页
                                if resiget_after_url == "http://trial.51talk.com/trial/reserve":

                                    flag_resiget_after = True

                                #注册失败，出错误提示
                                # elif driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[1]/div") or \
                                #      driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/div"):
                                #
                                #         resiget_text_info_1 = driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[1]/div").text
                                #
                                #         resiget_text_info_2 = driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/div").text
                                #
                                #         if resiget_text_info_1 == u'*手机号码不能为空':
                                #
                                #             print ("#-------------------------------#")
                                #
                                #             print (u"该手机号输入为空，请重新输入！！！")
                                #
                                #             print ("#-------------------------------#" + "\n")
                                #
                                #
                                #         if resiget_text_info_1 == u'*请填写正确的手机号码':
                                #
                                #             print ("#------------------------------------------------------#")
                                #
                                #             print (u"该手机号：" + user_mobile + u",格式错误，请重新输入！！！")
                                #
                                #             print ("#------------------------------------------------------#" + "\n")
                                #
                                #         if resiget_text_info_2 == u'*密码不能为空':
                                #
                                #             print ("#-----------------------------#")
                                #
                                #             print (u"该手机为：" + user_mobile)
                                #             print (u"该密码输入为空，请重新输入！！！")
                                #
                                #             print ("#-----------------------------#" + "\n")
                                #
                                #         if resiget_text_info_2 == u'*密码格式错误':
                                #
                                #             print ("#-------------------------------------------------------------#")
                                #
                                #             print (u"该手机为：" + user_mobile)
                                #             print (u"该密码为：" + user_password + u",格式错误，请重新输入6--20位字符")
                                #
                                #             print ("#-------------------------------------------------------------#" + "\n")
                                #
                                #         sleep(2)
                                #
                                #         driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").clear()
                                #
                                #         driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").clear()

                                if flag_resiget_after == True:

                                    sleep(2)
                                    print ("调用后台stu_list查询user_id")
                                    flag_resiget_succes_tips = False

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

                                    #面板注册信息写入数据库
                                    userInformation_db_resiget_mb_insert_success(user_id,user_mobile,user_password,current_now_time)

                                    # -----------------------------------#

                                    print ("用户信息写入正确，请查看！！！")

                                    # -----------------------------------#

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

                                        sleep(2)

                                        login_after_link = driver.current_url

                                        #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
                                        if login_after_link == "http://trial.51talk.com/trial/index" or \
                                           login_after_link == "https://trial.51talk.com/trial/index":

                                            #----------------------------------------------------------------------------------#

                                            print ("该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入体验账号会员中心啦~")

                                            #----------------------------------------------------------------------------------#

                                            try:

                                                user_center_layer_operation(driver)

                                            except:

                                                pass

                                            sleep(2)

                                            # 调用约体验课
                                            user_experience_cadets_success(driver, current_window_handle, str(user_id),str(user_mobile))

                                            #查询体验用户财富信息
                                            # wealth_data = user_experience_the_wealth_success(driver,login_after_link,str(user_id),str(user_mobile))

                                            #预约公开课
                                            # user_open_class_success(driver,current_window_handle,login_after_link,wealth_data,str(user_id),str(user_mobile))

                                            #预约精品小班课
                                            # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                                        #成人/青少体验账号，进入体验约课页面
                                        elif login_after_link == "http://trial.51talk.com/trial/reserve" or \
                                             login_after_link == "https://trial.51talk.com/trial/reserve":

                                                #--------------------------------------------------------#

                                                print (user_mobile + "该账号为成人/青少体验学员，进入成人/青少体验约课页面～")

                                                # -------------------------------------------------------#

                                                # 获取用户user_wealth表point
                                                db_wealth_data = userInformation_db_query_wealth_point_success(user_mobile)

                                                sleep(1)

                                                if db_wealth_data == ():

                                                    point = "1"

                                                    point_validity = None

                                                    classtime = ""

                                                    # 插入user_wealth表point
                                                    userInformation_db_wealth_data_insert_success(user_id, user_mobile, point,
                                                                                                  point_validity, classtime,
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

                                                    #--------------------------------------------#

                                                    print ("该手机号已验证，请选择成人/青少体验课吧～")

                                                    #--------------------------------------------#

                                                    sleep(2)

                                                # 调用约体验课
                                                user_experience_cadets_success(driver, current_window_handle, str(user_id),str(user_mobile))

                                                #查询体验用户财富信息
                                                # wealth_data = user_experience_the_wealth_success(driver, login_after_link,str(user_id),str(user_mobile))

                                                #预约公开课
                                                # user_open_class_success(driver, current_window_handle, login_after_link,wealth_data,str(user_id),str(user_mobile))

                                                #预约精品小班课
                                                # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                                        #美小体验课
                                        elif login_after_link == "http://aa.51talk.com/nat/trial/reserve_new?date=" or \
                                             login_after_link == "https://aa.51talk.com/nat/trial/reserve_new?date=":

                                            #-------------------------------------------------#

                                              print ("该账号为美小体验学员，进入美小体验约课页面～")

                                            #-------------------------------------------------#

                                              #手机号验证
                                              try:

                                                    #手机验证(便于接收上课短信通知)
                                                    driver.find_element_by_xpath("//*[@id='mobileCode']/h3")

                                                    #----------------------------------------#

                                                    print ("该手机号没有验证，请先验证手机号吧～")

                                                    #----------------------------------------#

                                                    sleep(2)

                                                    #调取短信平台
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

                                                    #----------------------------------------#

                                                    print ("该手机号已验证，请选择美小体验课吧～")

                                                    #----------------------------------------#
                                        else:

                                            #--------------------------------------#

                                            print ("注册成功，但不能操作，请查看原因：")

                                            #--------------------------------------#

                                        # 退出51TALK会员中心
                                        try:

                                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                                            sleep(2)

                                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                                            sleep(2)

                                            startPageComeInto(driver)

                                            sleep(2)

                                        except:

                                            pass

                                        sleep(2)

                                        if xunhuan_resiget_index == xunhuan_resiget_max - 1:

                                            pass

                                        else:

                                            print ("\n")

                                else:

                                    #-----------------------------------#

                                    print ("注册异常，请查看原因：" + "\n")

                                    #-----------------------------------#

            cursor_onlie_test.close()

            conn_onlie_test.close()

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #官网首页，面板注册--注册失败
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_info_fail(self):

            print ("*************官网首页，面板注册--注册失败*************")

            u"""注册信息错误，错误注册."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            # 读入文件--xlsx
            # read_resiget_fail_xlsx = dqXlsResigetFail()
            #
            # for i in range(1, len(read_resiget_fail_xlsx)):
            #
            #     user_mobile = int(read_resiget_fail_xlsx[i][0])
            #     user_password = int(read_resiget_fail_xlsx[i][1])
            #     user_english_name = read_resiget_fail_xlsx[i][2]
            #     user_tuijian_mobile = int(read_resiget_fail_xlsx[i][3])

            # 读入文件--txt
            read_resiget_fail_txt = readResigetFailFile()

            for line in read_resiget_fail_txt:

                user_mobile     = line.split(',')[0]
                user_password   = line.split(',')[1]

                sleep(2)

                #首页注册面板

                #手机号输入框
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").send_keys(user_mobile)
                sleep(1)

                #点击密码框
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").click()
                sleep(1)

                #面板手机号判重复弹框
                try:
                    driver.find_element_by_xpath("//*[@class='layer-box']/div[@class='mian-box']/div[@class='tit-box']/span[@id='closeId']")

                    flag_resiget_duplicate = True
                    sleep(1)

                except:

                    flag_resiget_duplicate = False

                if flag_resiget_duplicate == True:

                    sleep(2)

                    duplicate_randint = random.randint(0,1)

                    print ("#---------------------------------------------------------#")

                    print (u"该手机号" + user_mobile + u",已注册，请登录吧！！！")

                    print ("#---------------------------------------------------------#" + "\n")

                    if duplicate_randint == 0:

                        #直接登录
                        driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[1]").click()

                        sleep(2)

                        login_url = driver.current_url

                        if login_url == "http://login.51talk.com/login/index":

                            #---------------------#

                            print ("登录链接正确～")

                            #---------------------#

                    else:

                        #找回密码
                        driver.find_element_by_xpath("//*[@id='layer2']/div[2]/div[2]/a[2]").click()

                        zhaohuimima_url = driver.current_url

                        if zhaohuimima_url == "http://login.51talk.com/password/forgot":

                            #------------------------#

                            print ("找回密码链接正确～")

                            #------------------------#

                    sleep(1)

                    driver.back()

                    sleep(1)

                    startPageComeInto(driver)

                    sleep(1)

                    #关闭弹框
                    # driver.find_element_by_xpath("//*[@class='layer-box']/div[@class='mian-box']/div[@class='tit-box']/span[@id='closeId']").click()

                    #点击手机号输入框
                    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").click()

                    #清空手机号输入框
                    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").clear()

                else:

                    #密码输入框
                    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").send_keys(user_password)
                    sleep(1)

                    #立即领取
                    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/input[2]").click()
                    sleep(1)

                    resiget_info_arrey=['手机号码不能为空',
                                        '请填写正确的手机号码'
                                        '密码不能为空',
                                        '密码格式错误']

                    #点“注册”后，获取的url地址
                    resiget_after_url = driver.current_url

                    flag_resiget_after = False

                    #注册成功，进入学员选择身份页
                    if resiget_after_url == "http://trial.51talk.com/trial/reserve":

                        flag_resiget_after = True

                    #注册失败，出错误提示
                    elif driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[1]/div") or \
                         driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/div"):

                        resiget_text_info_1 = driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[1]/div").text

                        resiget_text_info_2 = driver.find_element_by_xpath("//*[@id='index']/div/div/div[2]/div/form/ul[2]/li[2]/div").text

                        if resiget_text_info_1 == u'*手机号码不能为空':

                            print ("#-------------------------------#")

                            print (u"该手机号输入为空，请重新输入！！！")

                            print ("#-------------------------------#" + "\n")


                        if resiget_text_info_1 == u'*请填写正确的手机号码':

                            print ("#------------------------------------------------------#")

                            print (u"该手机号：" + user_mobile + u",格式错误，请重新输入！！！")

                            print ("#------------------------------------------------------#" + "\n")

                        if resiget_text_info_2 == u'*密码不能为空':

                            print ("#-----------------------------#")

                            print (u"该手机为：" + user_mobile)
                            print (u"该密码输入为空，请重新输入！！！")

                            print ("#-----------------------------#" + "\n")

                        if resiget_text_info_2 == u'*密码格式错误':

                            print ("#-------------------------------------------------------------#")

                            print (u"该手机为：" + user_mobile)
                            print (u"该密码为：" + user_password + u",格式错误，请重新输入6--20位字符")

                            print ("#-------------------------------------------------------------#" + "\n")

                        sleep(2)

                        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[1]/dl/dd/input").clear()

                        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/ul[2]/li[2]/dl/dd/input").clear()

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站注册页面--注册成功
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_Page_info_success(self):

            print ("*************主站注册页面--注册成功*************")

            for xunhuan_resiget_index in range(0, xunhuan_resiget_max):

                u"""注册信息正确，正常登录."""

                driver = self.driver

                driver.get(self.url)

                sleep(1)

                driver.maximize_window()

                sleep(1)

                #调用启动页进入青少儿官网
                startPageComeInto(driver)

                sleep(1)

                current_window_handle = driver.current_window_handle

                #点击注册
                driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[2]").click()

                sleep(1)

                current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

                sleep(1)

                #读入文件--xlsx
                # read_resiget_success_xlsx = dqXlsResigetSuccess()
                #
                # for i in range(1, len(read_resiget_success_xlsx)):
                #
                #     user_account = int(read_resiget_success_xlsx[i][0])
                #     user_password = int(read_resiget_success_xlsx[i][1])
                #     user_tuijian_mobile = int(read_resiget_success_xlsx[i][2])

                #读入文件--txt
                read_resiget_success_txt = readResigetSuccessFile()

                for i in read_resiget_success_txt:

                    user_mobile = i.split(',')[0]
                    user_password = i.split(',')[1]
                    user_recommenMobile = i.split(',')[3]

                # user_mobile = raw_input("请输入用户注册手机号：")
                #
                # user_password = raw_input("请输入用户注册密码：")
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

                sleep(2)

                #输入手机号
                driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

                sleep(2)

                #点击滑块
                driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[2]/div/div[2]").click()

                sleep(2)

                # try:
                #
                #     driver.find_element_by_xpath("//*[@id='code']")
                #
                #     print ("初始状态找到短信验证码输入框！！！")
                #
                # except:
                #
                #     print ("初始状态没有找到短信验证码输入框！！！")

                #错误提示
                try:

                    if driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[1]/div[2]/div"):

                        resiget_info_arrey=['请输入手机号',
                                            '手机号格式错误，请重新输入'
                                            '该手机号码已存在，请直接登录，或使用其他号码注册']

                        resiget_error_text = driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[1]/div[2]/div").text

                        resiget_error_flag = False

                        if resiget_error_text == u"请输入手机号":

                            print ("#------------------------------#")

                            print ("该手机号输入为空，请重新输入！！！")

                            print ("#------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text == u"手机号格式错误，请重新输入":

                            print ("#-----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile + "，该手机格式错误，请重新输入！！！")

                            print ("#-----------------------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text == u"该手机号码已存在，请直接登录，或使用其他号码注册":

                            print ("#----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile + "，该手机已注册，请重新输入！！！")

                            print ("#----------------------------------------------------------#")

                            resiget_error_flag = True

                        else:

                            print ("#--------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile + "，未注册，此号码可以继续注册啦！！！")

                            print ("#--------------------------------------------------------#")

                        if resiget_error_flag == True:

                            driver.find_element_by_xpath("//*[@id='mobile']").clear()

                        else:

                            #滑块
                            huakuai = "//*[@id='container']/form/div/div/div[2]/div/div[2]"

                            actione_1 = ActionChains(driver)

                            source = driver.find_element_by_xpath(huakuai)

                            #鼠标左键按下不放
                            actione_1.click_and_hold(source).perform()

                            #鼠标左键滑动坐标
                            actione_1.move_by_offset(319,0)

                            #释放鼠标左键
                            actione_1.release().perform()

                            sleep(2)

                            try:

                                driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                mobileCode_error_text = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                                if mobileCode_error_text == u"操作频繁，请你稍后重试，如需帮助请拨打4000515151" or \
                                   mobileCode_error_text == u"手机号发送短信次数过多，如需帮助请拨打4000515151":

                                    #-------------------------------------------------#

                                    print ("该手机号重复发送次数过多，请稍后再试～" + "\n")

                                    #-------------------------------------------------#

                                    sleep(1)

                                    driver.find_element_by_xpath("//*[@id='sureId']").click()

                                    sleep(1)

                                    driver.refresh()

                                    sleep(1)

                                elif mobileCode_error_text == u"滑动验证失败，请重新操作。":

                                    # -------------------------------------------------#

                                    print ("滑动失败，请刷新页面重新加载～" + "\n")

                                    #-------------------------------------------------#

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

                                            sleep(2)

                                            #调取手机短信平台
                                            jiequ_code = user_sms_platform_info(driver,user_mobile)

                                            sleep(2)

                                            #调取文件读操作
                                            # jiequ_code = user_file_r_operation()

                                    driver.switch_to_window(current_window_handle)

                                    sleep(2)

                                    #输入短信验证码
                                    driver.find_element_by_xpath("//*[@id='code']").send_keys(jiequ_code)

                                    sleep(2)

                                    #输入密码
                                    driver.find_element_by_xpath("//*[@id='password']").send_keys(user_password)

                                    sleep(2)

                                    #输入邀请人手机号
                                    driver.find_element_by_xpath("//*[@id='recommenMobile']").send_keys(user_recommenMobile)

                                    sleep(2)

                                    #免费注册
                                    driver.find_element_by_xpath("//*[@id='registerBtn']").click()

                                    sleep(2)

                                    try:

                                        driver.find_element_by_xpath("//*[@id='contentInfo1']")

                                        resiget_error_text_2 = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                                        if resiget_error_text_2 == u"验证码输入不正确。" or \
                                           resiget_error_text_2 == u"错误的密码格式" or \
                                           resiget_error_text_2 == u"推荐人的手机号码或推荐码格式不正确！" or \
                                           resiget_error_text_2 == u"推荐人手机号不可以写自己的手机号哦，亲！" or \
                                           resiget_error_text_2 == u"您填写的推荐人的手机号码在51talk上没有注册，请填写推荐人在51talk注册的手机号码！":

                                            #我知道了按钮
                                            driver.find_element_by_xpath("//*[@id='sureId']").click()

                                            #------------------------------------------------------#

                                            print ("该验证码、密码或推荐人输入错误，请重新输入～" + "\n")

                                            #------------------------------------------------------#

                                            sleep(1)

                                            driver.refresh()

                                            sleep(1)

                                        else:

                                            #输入密码为空
                                            if driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[4]/div[2]/div"):

                                                password_error_text = driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[4]/div[2]/div").text

                                                if password_error_text == u"请输入密码":

                                                    #----------------------------------------#

                                                    print ("该密码输入为空，请重新输入～" + "\n")

                                                    #----------------------------------------#

                                                    sleep(1)

                                                    driver.refresh()

                                                    sleep(1)

                                            else:

                                                    flag_resiget_succes_tips = False

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

                                                    #注册页注册信息写入数据库
                                                    userInformation_db_resiget_page_insert_success(user_id,user_mobile,user_password,insert_user_id,current_now_time)

                                                    # -----------------------------------#

                                                    print ("用户信息写入正确，请查看！！！")

                                                    # -----------------------------------#

                                                    #判断元素是否找到
                                                    try:
                                                        driver.find_element(By.XPATH,"//*[@id='usersSelect']/div[4]/div/div[1]/h3")
                                                        # print (u"找到该元素！！！")

                                                        flag_resiget_succes_tips = True

                                                    except:

                                                        # print (u"没有找到该元素！！！")
                                                        flag_resiget_succes_tips =  False

                                                    if flag_resiget_succes_tips == True:

                                                        sleep(2)

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
                                                                # user_open_class_success(driver, current_window_handle,resiget_after_link, wealth_data, str(user_id), str(user_mobile))

                                                                sleep(2)

                                                                #预约精品小班课
                                                                # user_fine_class_success(driver,current_window_handle,wealth_data,str(user_id), str(user_mobile))

                                                        #成人/青少体验账号，直接进入会员中心 or 体验课约课页面
                                                        elif resiget_after_link == "http://trial.51talk.com/trial/index" or \
                                                             resiget_after_link == "https://trial.51talk.com/trial/index":

                                                                #---------------------------------------------------------------------------------#

                                                                print ("该账号为成人/青少体验学员类型：财富已过期或已预约体验课，直接进入体验账号会员中心啦~")

                                                                #---------------------------------------------------------------------------------#

                                                                try:

                                                                    user_center_layer_operation(driver)

                                                                except:

                                                                    pass

                                                                sleep(2)

                                                                # 调用约体验课
                                                                user_experience_cadets_success(driver,current_window_handle,str(user_id),str(user_mobile))

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
                                                                user_experience_cadets_success(driver,current_window_handle,str(user_id),str(user_mobile))

                                                                #查询体验用户财富信息
                                                                #wealth_data = user_experience_the_wealth_success(driver,resiget_after_link, str(user_id),str(user_mobile))

                                                                #预约公开课
                                                                # user_open_class_success(driver, current_window_handle,resiget_after_link, wealth_data,str(user_id),str(user_mobile))

                                                                #预约精品小班课
                                                                # user_fine_class_success(driver, current_window_handle, wealth_data,str(user_id),str(user_mobile))

                                                        #美小付费账号
                                                        elif resiget_after_link == "http://aa.51talk.com/user/index" or \
                                                             resiget_after_link == "https://aa.51talk.com/user/index":

                                                                #------------------------------------------------------#

                                                                print ("该账号为美小付费学员类型，直接进入体验账号会员中心啦~")

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

                                                            #--------------------------------------#

                                                            print ("注册成功，但不能操作，请查看原因：")

                                                            #--------------------------------------#

                                                        # 退出51TALK会员中心
                                                        try:

                                                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                                                            sleep(2)

                                                            driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                                                            sleep(2)

                                                        except:

                                                            pass

                                                        sleep(2)

                                                        if xunhuan_resiget_index == xunhuan_resiget_max - 1:

                                                            pass

                                                        else:

                                                            print ("\n")

                                                    else:

                                                        #----------------------------#

                                                        print ("注册异常，请查看原因：")

                                                        #----------------------------#

                                    except:

                                        pass
                            except:

                                pass

                except:

                    pass

            cursor_onlie_test.close()

            conn_onlie_test.close()

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站注册页面--注册失败
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_Page_info_fail(self):

            print ("*************主站注册页面--注册失败*************")

            u"""注册信息异常，登录失败."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击注册
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[2]").click()

            sleep(1)

            # 读入文件--xlsx
            read_login_fail_xlsx = dqXlsResigetFail()

            for i in range(1, len(read_login_fail_xlsx)):

                user_account = int(read_login_fail_xlsx[i][0])
                user_password = int(read_login_fail_xlsx[i][1])
                user_english_name = read_login_fail_xlsx[i][2]
                user_tuijian_mobile = int(read_login_fail_xlsx[i][3])

            # 读入文件--txt
            read_resiget_fail_txt = readResigetFailFile()

            for line in read_resiget_fail_txt:

                user_mobile         = line.split(',')[0]
                user_password       = line.split(',')[1]
                user_code           = line.split(',')[2]
                user_recommenMobile = line.split(',')[3]

                sleep(2)

                #输入手机号
                driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

                sleep(2)

                #滑块
                huakuai = "//*[@id='container']/form/div/div/div[2]/div/div[2]"

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

                #输入密码
                driver.find_element_by_xpath("//*[@id='password']").send_keys(user_password)

                sleep(2)

                #输入邀请人手机号
                driver.find_element_by_xpath("//*[@id='recommenMobile']").send_keys(user_recommenMobile)

                sleep(2)

                #免费注册
                driver.find_element_by_xpath("//*[@id='registerBtn']").click()
                sleep(2)

                #错误提示
                try:

                    if driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[1]/div[2]/div") or \
                       driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[3]/div[2]/div") or \
                       driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[4]/div[2]/div"):

                        resiget_info_arrey=['请输入手机号',
                                            '手机号格式错误，请重新输入',
                                            '该手机号码已存在，请直接登录，或使用其他号码注册',
                                            '请输入验证码',
                                            '验证码格式有误，请重新输入',
                                            '请输入密码',
                                            '密码长度只能是6-20位字符',]

                        resiget_error_text_1 = driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[1]/div[2]/div").text

                        resiget_error_text_2 = driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[3]/div[2]/div").text

                        resiget_error_text_3 = driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[4]/div[2]/div").text

                        resiget_error_flag = False

                        if resiget_error_text_1 == u"请输入手机号" and resiget_error_text_2 == u"请输入验证码" and resiget_error_text_3 == u"请输入密码":

                            print ("#--------------------------------------------#")

                            print ("该手机号、验证码、密码都输入为空，请重新输入！！！")

                            print ("#--------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_1 == u"请输入手机号":

                            print ("#--------------------------------------------#")

                            print ("该手机号输入为空，请重新输入！！！")

                            print ("#--------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_1 == u"手机号格式错误，请重新输入":

                            print ("#-----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile + "，该手机格式错误，请重新输入！！！")

                            print ("#-----------------------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_1 == u"该手机号码已存在，请直接登录，或使用其他号码注册":

                            print ("#----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile + "，该手机已注册，请重新输入！！！")

                            print ("#----------------------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_2 == u"请输入验证码":

                            print ("#------------------------#")

                            print ("该手机号为：" + user_mobile)

                            print ("该验证码输入为空，请重新输入！！！")

                            print ("#------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_2 == u"验证码格式有误，请重新输入":

                            print ("#-----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile)

                            print ("该验证码为：" + user_code + "，该验证码格式错误，请重新输入！！！")

                            print ("#-----------------------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_3 == u"请输入密码":

                            print ("#-----------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile)

                            print ("该验证码为：" + user_code)

                            print ("该密码为输入为空，请重新输入！！！")

                            print ("#-----------------------------------------------------------#")

                            resiget_error_flag = True

                        elif resiget_error_text_3 == u"密码长度只能是6-20位字符":

                            print ("#------------------------------------------------------------#")

                            print ("该手机号为：" + user_mobile)

                            print ("该验证码为：" + user_code)

                            print ("该密码为：" + user_password + "，该密码格式错误，请重新输入！！！")

                            print ("#------------------------------------------------------------#")

                            resiget_error_flag = True

                        print ("\n")

                        if resiget_error_flag == True:

                            # driver.refresh()

                            sleep(1)

                        try:

                            driver.find_element_by_xpath("//*[@id='contentInfo1']")

                            mobileCode_error_text = driver.find_element_by_xpath("//*[@id='contentInfo1']").text

                            if mobileCode_error_text == u"错误的邮箱地址或手机号":

                                    #----------------------------------------#

                                    print ("验证码输入错误，请重新输入～" + "\n")

                                    #----------------------------------------#

                            elif mobileCode_error_text == u"验证码输入不正确。":

                                    #----------------------------------------#

                                    print ("验证码输入错误，请重新输入～" + "\n")

                                    #----------------------------------------#

                            #我知道了按钮
                            driver.find_element_by_xpath("//*[@id='sureId']").click()

                            sleep(1)

                            driver.refresh()

                        except:

                            pass

                        driver.refresh()

                except:

                    pass

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站注册页面--用户协议
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_Page_user_protocol(self):

            print ("*************主站注册页面--用户协议*************")

            u"""注册页，用户协议."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击注册
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[2]").click()

            sleep(1)

            current_window_handle = driver.current_window_handle

            sleep(1)

            #用户协议
            driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[6]/div[1]/p/a[1]").click()

            sleep(1)

            windows_handle = driver.window_handles

            sleep(1)

            for handles in windows_handle:

                if handles != current_window_handle:

                    driver.switch_to_window(handles)

                    sleep(5)

                    driver.close()

            driver.switch_to_window(current_window_handle)

            sleep(2)

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站注册页面--隐私声明
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_Page_privacy_statement(self):

            print ("*************主站注册页面--隐私声明*************")

            u"""注册页，隐私声明."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击注册
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[2]").click()

            sleep(1)

            current_window_handle = driver.current_window_handle

            sleep(1)

            #隐私声明
            driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[6]/div[1]/p/a[2]").click()

            sleep(1)

            windows_handle = driver.window_handles

            sleep(1)

            for handles in windows_handle:

                if handles != current_window_handle:

                    driver.switch_to_window(handles)

                    sleep(5)

                    driver.close()

            driver.switch_to_window(current_window_handle)

            sleep(2)

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #主站注册页面--前往登录
#----------------------------------------------------------------------------------------------------------------------#

        def test_new_Resiget_Page_goto_login(self):

            print ("*************主站注册页面--前往登录*************")

            u"""注册页，前往登录页."""

            driver = self.driver
            driver.get(self.url)
            sleep(1)

            driver.maximize_window()
            sleep(1)

            #调用启动页进入青少儿官网
            startPageComeInto(driver)

            sleep(1)

            current_window_handle = driver.current_window_handle

            #点击注册
            driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[2]").click()

            sleep(1)

            #前往登录
            driver.find_element_by_xpath("//*[@id='container']/form/div/div/div[8]/a").click()

            sleep(5)

            print ("***********************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

        def tearwDon(self):

            QuitBrowser(self.driver)