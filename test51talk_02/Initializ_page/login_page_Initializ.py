#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'



from time import localtime
from time import sleep
from time import strftime
from time import time

from configuration_files.dqTxtFile import readLoginSuccessFile
from configuration_files.dqXlsFile import dqXlsLoginSuccess
from db_files.userInformation_db_old_data_insert import userInformation_db_old_data_insert_success
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success
from db_files.userInformation_db_query import userInformation_db_query_user_id_success
from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_user_id_success
from talkTest.StartPage.startPagePopLayer import startPageComeInto
from talkUser.admin_backstage.user_stu_list import user_stu_list_query_user_user_id
from talkUser.user_center.user_center_layer import user_center_layer_operation


def login_page_Initializ_success(driver,login_url):

    driver.get(login_url)

    sleep(1)

    driver.maximize_window()

    sleep(1)

    # 调用启动页进入青少儿官网
    startPageComeInto(driver)

    sleep(1)

    current_window_handle = driver.current_window_handle

    sleep(1)

    # 点击登录
    driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div[2]/div[2]/div/a[1]").click()

    # 获取当天现在时间
    current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

    sleep(1)

    #读入文件--xlsx
    read_login_success_xlsx = dqXlsLoginSuccess()

    for i in range(1, len(read_login_success_xlsx)):

        user_mobile = int(read_login_success_xlsx[i][0])
        user_password = int(read_login_success_xlsx[i][1])

    # 读入文件--txt
    # read_login_success_txt = readLoginSuccessFile()
    #
    # for i in read_login_success_txt:
    #
    #     user_mobile = i.split(',')[0]
    #
    #     user_password = i.split(',')[1]

    # user_mobile = raw_input("请输入用户登录手机号：")

    sleep(1)

    # user_password = raw_input("请输入用户登录密码：")

    sleep(1)

    # 输入账号
    driver.find_element_by_xpath("//*[@id='accountId']").send_keys(user_mobile)

    sleep(1)

    # 输入密码
    driver.find_element_by_xpath("//*[@id='password']").send_keys(user_password)

    sleep(1)

    # 登录按钮
    driver.find_element_by_xpath("//*[@id='accountLoginBtn']").click()

    sleep(1)

    try:

        user_center_layer_operation(driver)

    except:

        pass

    sleep(1)

    #登录成功后，退出按钮是否存在
    try:

        driver.find_element_by_xpath("//*[@id='jsHead']/div[1]/div/a[3]")

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

            print ("用户信息写入成功，请查看！！！")

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

        return user_mobile,user_password,user_id

    except:

        return 0