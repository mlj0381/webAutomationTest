#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from time import sleep

from Initializ_page.member_center_Initializ_account_settings_page import member_center_Initializ_account_settings_page_wealth_record_success


#----------------------------------------------------------------------------------------------------------------------#
# 财富记录
#----------------------------------------------------------------------------------------------------------------------#

def test_account_wealth_record_success(driver):

    wealth_record_tag = member_center_Initializ_account_settings_page_wealth_record_success(driver)

    #我的课次
    if wealth_record_tag == 6:

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[7]/a").click()

        sleep(1)

    elif wealth_record_tag == 7:

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[6]/a").click()

        sleep(1)

    #有无财富信息
    try:

        driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[2]/div/h3")

        sleep(1)

        wealth_record_text = driver.find_element_by_xpath("//*[@id='container']/div/div/div/div[2]/div/h3").text

        if wealth_record_text == "暂无相关信息":

            print ("该账户暂无财富信息！！！")

    except:

            print ("该账户有财富信息，请查看！！！")

    sleep(1)