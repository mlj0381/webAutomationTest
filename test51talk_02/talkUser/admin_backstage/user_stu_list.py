#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


'''
调取后台stu_list：
                    1）验证手机号
                    2）验证用户状态
                    3）验证水平级别设置
'''

from selenium import webdriver
from time import sleep
import random
from configuration_files import accountConfigInformation as accountConfig


#----------------------------------------------------------------------------------------------------------------------#
    #后台登录，进入stu_list表
#----------------------------------------------------------------------------------------------------------------------#

def houtai_login_success_stu_list(driver):

        #Accout
        driver.find_element_by_xpath("//*[@id='user_name']").send_keys(accountConfig.houTaiAccout)
        sleep(2)

        #Password
        driver.find_element_by_xpath("//*[@id='pwd']").send_keys(accountConfig.houTaiPassword)
        sleep(2)

        #Login
        driver.find_element_by_xpath("//*[@id='Submit']").click()
        sleep(4)

        #调取stu_list表
        driver.get(accountConfig.houtai_stu_list_link)
        sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
    #后台stu_list表，验证手机号
#----------------------------------------------------------------------------------------------------------------------#

def user_stu_list_verify_mobile_status(driver,user_mobile):

        houtai_login_success_stu_list(driver)

        #手机号输入框
        driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)
        sleep(2)

        #查询
        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[2]/td/span/input[8]").click()

        sleep(2)

        #修改按钮
        driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td[16]/span/a[2]").click()

        sleep(2)

        try:
                #手机验证状态下拉框
                driver.find_element_by_xpath("//*[@id='is_check']")

                sleep(2)

                driver.find_element_by_xpath("//*[@id='is_check']").click()

                sleep(2)

                #已验证
                driver.find_element_by_xpath("//*[@id='is_check']/option[1]").click()

                sleep(2)

                #确认修改
                driver.find_element_by_xpath("//*[@id='yz']").click()

                sleep(2)

                #修改成功提示
                driver.switch_to_alert().accept()

                sleep(2)

                driver.back()

                sleep(2)

        except:

                print ("手机号验证失败，请查看原因！！！")

        sleep(2)

        driver.close()

#----------------------------------------------------------------------------------------------------------------------#
    #后台stu_list表，验证用户状态
#----------------------------------------------------------------------------------------------------------------------#

def user_stu_list_dverify_user_status(driver,user_mobile):

        houtai_login_success_stu_list(driver)

        #手机号输入框
        driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

        sleep(2)

        #查询
        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[2]/td/span/input[8]").click()

        sleep(10)

        #修改按钮
        driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td[15]/span/a[2]").click()

        sleep(2)

        try:
                driver.find_element_by_xpath("//*[@id='is_buy']")

                sleep(2)

                driver.find_element_by_xpath("//*[@id='is_buy']").click()

                sleep(2)

                driver.find_element_by_xpath("//*[@id='is_buy']/option[2]").click()

                sleep(2)

                driver.find_element_by_xpath("/html/body/form/table/tbody/tr[9]/td/input").click()

                sleep(2)

                driver.switch_to_alert().accept()

                sleep(2)

                driver.back()

                sleep(2)

                print ("用户状态更新，请查看验证！！！")

        except:

                pass

        sleep(2)

        driver.close()


#----------------------------------------------------------------------------------------------------------------------#
    #后台stu_list表，水平级别设置
#----------------------------------------------------------------------------------------------------------------------#

def user_stu_list_level_setting(driver,user_mobile):

        houtai_login_success_stu_list(driver)

        #手机号输入框
        driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)
        sleep(2)

        #查询
        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[2]/td/span/input[8]").click()

        sleep(2)

        #水平设定
        driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td[8]/span/a").click()

        sleep(2)

        try:

                driver.find_element_by_xpath("//*[@id='level_type']")

                sleep(2)

                driver.find_element_by_xpath("//*[@id='level_type']").click()

                sleep(2)

                level_type_randrom = random.randint(2,3)

                # level_type_randrom = 3

                level_type_text_1 = "//*[@id='level_type']/option["

                level_type_text_2 = level_type_randrom

                level_type_text_3 = "]"

                level_type_text_4 = level_type_text_1 + str(level_type_text_2) + level_type_text_3

                sleep(2)

                driver.find_element_by_xpath(level_type_text_4).click()

                sleep(2)

        except:

                pass


        try:

                driver.find_element_by_xpath("//*[@id='top_level']")

                sleep(2)

                driver.find_element_by_xpath("//*[@id='top_level']").click()

                sleep(2)

                top_level_randrom = random.randint(2,11)

                top_level_text_1 = "//*[@id='top_level']/option["

                top_level_text_2 = top_level_randrom

                top_level_text_3 = "]"

                top_level_text_4 = top_level_text_1 + str(top_level_text_2) + top_level_text_3

                sleep(2)

                driver.find_element_by_xpath(top_level_text_4).click()

                sleep(2)

                # driver.switch_to_alert().accept()
                #
                # sleep(2)
                #
                # driver.back()
                #
                # sleep(2)

        except:

                pass


        try:

                driver.find_element_by_xpath("//*[@id='level']")

                sleep(2)

                driver.find_element_by_xpath("//*[@id='level']").click()

                sleep(2)

                driver.find_element_by_xpath("//*[@id='level']/option[2]").click()

                sleep(2)

                driver.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/th/input[2]").click()

                sleep(2)
                #
                driver.switch_to_alert().accept()

                sleep(2)

                driver.back()

                sleep(2)

                print ("级别设定成功，请查看验证！！！")

        except:

                pass

        sleep(2)

        driver.close()


#----------------------------------------------------------------------------------------------------------------------#
    #后台stu_list表，查询用户user_id
#----------------------------------------------------------------------------------------------------------------------#

def user_stu_list_query_user_user_id(driver,user_mobile):

        houtai_login_success_stu_list(driver)

        #手机号输入框
        driver.find_element_by_xpath("//*[@id='mobile']").send_keys(user_mobile)

        sleep(2)

        #查询
        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[2]/td/span/input[8]").click()

        sleep(2)

        try:

                driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td[1]/span")

                sleep(2)

                user_id_text = driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td[1]/span").text

                print ("已找到该用户user_id为：" + str(user_id_text))

                return user_id_text

        except:

                print ("没有找到该用户user_id")

        sleep(2)

        driver.close()

# driver = webdriver.Chrome()
#
# sleep(2)
#
# driver.get("http://www.51talk.com/admin/admin_login.php")
#
# sleep(2)
#
# driver.maximize_window()
#
# sleep(2)
#
# user_mobile = "18666600450"

# user_stu_list_verify_mobile_status(driver,user_mobile)

# user_stu_list_dverify_user_status(driver,user_mobile)

# user_stu_list_level_setting(driver,user_mobile)

# user_stu_list_query_user_user_id(driver,user_mobile)

# sleep(1)
#
# driver.quit()