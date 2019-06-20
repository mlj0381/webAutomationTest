#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from time import sleep

from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_cash_coupon_success


#----------------------------------------------------------------------------------------------------------------------#
# 代金券
#----------------------------------------------------------------------------------------------------------------------#

def test_account_cash_coupon_success(driver):

        cash_coupon_tag = member_center_Initializ_account_settings_page_cash_coupon_success(driver)

        #付费学员代金券链接
        if cash_coupon_tag == 2:

                driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[5]/a").click()

                sleep(1)

        #体验学员代金券链接
        elif cash_coupon_tag == 3:

                driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[4]/a").click()

                sleep(1)

        try:

                cash_coupon_text = driver.find_element_by_xpath("//*[@id='container']/div/div/div/div/table[1]/tbody/tr[1]/td[4]").text

                if driver.find_element_by_xpath("//*[@id='container']/div/div/div/div/table[1]/thead/tr/th") or cash_coupon_text == "未使用":

                        sleep(1)

                        print ("暂无未使用的代金券数据！！！")

        except:

                print ("找到未使用的代金券数据！！！")


        sleep(1)
