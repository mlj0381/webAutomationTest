#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import sleep,strftime,localtime,time


from selenium.webdriver.common.by import By

from configuration_files.courseConfig import *

from db_files.userInformation_db_insert_order import userInformation_db_insert_order_success

from talkUser.admin_backstage.user_order_list import user_order_list_quest


#----------------------------------------------老版美小售卖---------------------------------------------------------------#
    #老版美小售卖
#-----------------------------------------------------------------------------------------------------------------------#

def user_old_sale_package_success(one_window_handle,driver,user_mobile,user_id):

    # 获取当天现在时间
    current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

    # 标签:美国小学课程套餐
    if driver.find_element(By.XPATH, ".//*[@id='paycourse']/div[2]/span"):

        sleep(2)

        #购买按钮
        driver.find_element_by_xpath(aa_element_text_04).click()

        sleep(2)

        all_window_handles = driver.window_handles

        sleep(2)

        for two_window_handles in all_window_handles:

            if two_window_handles != one_window_handle:

                driver.close()

                sleep(2)

                driver.switch_to_window(two_window_handles)

                sleep(2)

                two_window_handle = driver.current_window_handle

        # 浏览器滚动条置底
        js = "var q=document.documentElement.scrollTop=500"
        driver.execute_script(js)

        sleep(1)

        # 勾选课程服务协议
        driver.find_element_by_css_selector(aa_course_service_protocol).click()

        sleep(2)

        #应付总额
        total_payment_text = driver.find_element_by_xpath("//*[@id='total2']").text

        # unicode转换为str
        total_payment_text = total_payment_text.encode('gbk')

        total_payment_text = str(int(float(total_payment_text)))

        sleep(2)

        # 浏览器滚动条置底
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)

        sleep(2)

        try:

            # aa体验用户--银行汇款选中
            driver.find_element_by_xpath(aa_confirm_bank_payment_tiyanuser)

            sleep(2)

            driver.find_element_by_xpath(aa_confirm_bank_payment_tiyanuser).click()

        except:

            # aa付费用户--银行汇款选中
            driver.find_element_by_xpath(aa_confirm_bank_payment_payuser)

            sleep(2)

            driver.find_element_by_xpath(aa_confirm_bank_payment_payuser).click()

        # 确认付款
        driver.find_element_by_xpath(aa_confirm_payment_submit).click()

        sleep(2)

        all_window_handles = driver.window_handles

        sleep(2)

        for three_window_handles in all_window_handles:

            if three_window_handles != two_window_handle:

                driver.close()

                sleep(2)

                driver.switch_to_window(three_window_handles)

                sleep(2)

                three_window_handle = driver.current_window_handle

                buyCourseAfter_url = driver.current_url

                sleep(2)

                jiequ_https = buyCourseAfter_url[0:5]
                jiequ_http = buyCourseAfter_url[0:4]

                if jiequ_https == "https":

                    jiequ_order_id = buyCourseAfter_url[32:40]

                elif jiequ_http == 'http':

                    jiequ_order_id = buyCourseAfter_url[31:39]

                # 输入订单号
                print ("获取的订单号为：" + str(jiequ_order_id))

                print ("获取下单手机号为：" + str(user_mobile))

        # 订单号写入
        # user_order_file_w_operation(jiequ_order_id)

        sleep(2)

        # 订单写入数据库
        userInformation_db_insert_order_success(user_id, jiequ_order_id, total_payment_text,current_now_time)

        sleep(2)

        # 调取后台处理订单表，查询订单号
        js = 'window.open("http://www.51talk.com/admin/admin_login.php")'

        driver.execute_script(js)

        all_window_handles = driver.window_handles

        sleep(2)

        for four_window_handles in all_window_handles:

            if four_window_handles != three_window_handle:

                driver.switch_to_window(four_window_handles)

                sleep(2)

                # 调取后台处理订单表，查询订单号
                user_order_list_quest(driver, user_mobile, user_id,jiequ_order_id)

                driver.close()

                sleep(2)

        driver.switch_to_window(three_window_handle)