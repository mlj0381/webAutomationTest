#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from time import sleep


#----------------------------------------------------------------------------------------------------------------------#
# 账号设置链接
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_url_success(driver,login_after_url_link):

    # 成人/青少付费账号
    if login_after_url_link == "https://www.51talk.com/user/index" or \
       login_after_url_link == "http://www.51talk.com/user/index":


            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[2]/a").click()

            sleep(1)

            return 1

    # 成人/青少体验账号，直接进入会员中心 or 体验课约课页面

    elif login_after_url_link == "http://trial.51talk.com/trial/index" or \
         login_after_url_link == "https://trial.51talk.com/trial/index" or \
         login_after_url_link == "http://trial.51talk.com/trial/reserve" or \
         login_after_url_link == "https://trial.51talk.com/trial/reserve":

            driver.find_element_by_xpath("//*[@id='head']/div/div[2]/div/ul/li[2]/a").click()

            sleep(1)

            return 2

    sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置我要请假选项
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_class_leave_success(driver):

        #我要请假
        try:

            driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[4]/a")

            sleep(1)

            class_leave_text = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[4]/a").text

            #付费学员
            if class_leave_text == "我要请假":

                return 0

            #体验学员
            elif class_leave_text == "代金券":

                return 1

        except:

            sleep(1)

        sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置代金券选项
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_cash_coupon_success(driver):

        try:

            driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[5]/a")

            sleep(1)

            cash_coupon_text = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[5]/a").text

            #付费学员
            if cash_coupon_text == "代金券":

                return 2

            #体验学员
            elif cash_coupon_text == "购买记录":

                return 3

        except:

            sleep(1)

        sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置购买记录选项
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_purchase_record_success(driver):

        try:

            driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a")

            sleep(1)

            purchase_record_text = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a").text

            #付费学员
            if purchase_record_text == "购买记录":

                return 4

            #体验学员
            elif purchase_record_text == "我的课次":

                return 5

        except:

            sleep(1)

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置我的课次选项
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_wealth_record_success(driver):

        try:

            driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[7]/a")

            sleep(1)

            wealth_record_text = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[7]/a").text

            # 付费学员
            if wealth_record_text == "我的课次":

                return 6

        except:

            try:

                driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a")

                sleep(1)

                wealth_record_text = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a").text

                # 付费学员
                if wealth_record_text == "我的课次":

                    return 7

            except:

                pass

#----------------------------------------------------------------------------------------------------------------------#
# 账号设置个人信息选项
#----------------------------------------------------------------------------------------------------------------------#

def member_center_Initializ_account_settings_page_personal_information_success(driver,account_type):

    #判断手机号是否被验证
    try:

        driver.find_element_by_xpath("//*[@id='sendCode']")

        print ("该用户手机号还未验证通过，请先验证手机号")

    except:

        try:

            # 获取真实姓名
            driver.find_element_by_xpath("//*[@id='name']").get_attribute("value")

            sleep(2)

            real_name_text = driver.find_element_by_xpath("//*[@id='name']").get_attribute("value")

            sleep(2)

            if real_name_text == u'':

                driver.find_element_by_xpath("//*[@id='name']").send_keys(u"我是测试人员")

                sleep(2)

            # 付费学员
            if account_type == 1:

                driver.find_element_by_xpath("//*[@id='baseMsg']/div[17]/input[2]").click()

                sleep(2)

            # 体验学员
            elif account_type == 2:

                driver.find_element_by_xpath("//*[@id='baseMsg']/div[11]/input[2]").click()

                sleep(2)

        except:

            print ("未找到真实姓名输入框，无法保存个人信息！！！")