#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from time import sleep

from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_purchase_record_success


#----------------------------------------------------------------------------------------------------------------------#
# 购买记录
#----------------------------------------------------------------------------------------------------------------------#

def test_account_purchase_record_success(driver):

    purchase_record_tag = member_center_Initializ_account_settings_page_purchase_record_success(driver)

    #付费学员购买记录链接
    if purchase_record_tag == 4:

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a").click()

    #体验学员购买记录链接
    elif purchase_record_tag == 5:

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[5]/a").click()

    #当前有无订单
    purchase_record_text = driver.find_element_by_xpath("//*[@id='container']/div/div/div/div/table/tbody/tr/td").text

    sleep(1)

    if purchase_record_text == "您还没有订单":

        print ("该账户当前无订单信息！！！")

    else:

        print ("该账户当前有订单信息！！！")

    sleep(1)