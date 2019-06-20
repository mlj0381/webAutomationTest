#!usr/bin/python
#encoding:utf-8


'''老登录模块'''


__author__ = 'zhangbo'

import operator
import unittest
from time import *

from db_files.userInformation_db_old_data_insert import *
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success
from talkUser.user_center.user_center_layer import *
from talkUser.user_quit_browser import *


class TestOldLoginINsert(unittest.TestCase):

    u'''老登录方式操作如下'''

    def setUp(self):

        self.driver = webdriver.Chrome()

        # self.driver = config_driver.obj_phantomjs_mac_driver

        # self.driver = config_driver.obj_phantomjs_window_driver

        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    # 老登录页面--成功
#----------------------------------------------------------------------------------------------------------------------#

    def test_old_login_insert_info_success(self):

        print ("*************老登录页面--成功*************")

        u"""老登录页面"""

        # dict_user_id_list = ['2627311','38312253','38312494','38312569','38348417','38570432']
        # dict_user_accout = {'18611772708':'123456','18666600272':'307143','18666600304':'111111',
        #                    '18666600275':'107411','18666600314':'111111','18666600276':'331870'}

        dict_user_id_list = ['40376248','1887807']
        dict_user_accout = {'18666600555':'123456','18666600554':'123456'}

        # dict_user_accout = {'18611772708':'123456','18666600272':'307143','18666600304':'111111','18666600275':'107411'}

        #按字典顺序排序
        # sorted(dict_user_accout.items(), key=operator.itemgetter(0))

        for user_accout in sorted(dict_user_accout.items(), key=operator.itemgetter(0)):

            self.url    = "http://login.51talk.com/web/login?client=1"

            driver = self.driver

            driver.get(self.url)

            sleep(1)

            driver.maximize_window()

            sleep(1)

            current_window_handle = driver.current_window_handle


            # 获取当天现在时间
            current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

            user_mobile  = user_accout[0]
            user_password = user_accout[1]

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

            try:

                driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

                sleep(1)

                #获取数据库中的密码
                db_user = userInformation_db_query_mobile_password_success(user_mobile)

                if db_user == ():

                    # 调用数据库插入语句
                    userInformation_db_old_data_insert_success(dict_user_id_list[0], user_mobile, user_password,current_now_time)

                    #-----------------------------------#

                    print ("用户信息写入正确，请查看！！！")

                    #-----------------------------------#

                sleep(4)

                user_center_layer_operation(driver)

                #退出
                driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]").click()

                sleep(2)

            except:

                print ("该账号：" + user_mobile +" 与 " + user_password + " 登录失败，请查看原因！！！")

            # del dict_user_id_list[0]

            dict_user_id_list.pop(0)

        cursor_onlie_test.close()

        conn_onlie_test.close()

        print ("******************************************" + "\n")

#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

    def tearDown(self):

            QuitBrowser(self.driver)