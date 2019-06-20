#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from time import sleep


#----------------------------------------------------------------------------------------------------------------------#
# 上课设置设置
#----------------------------------------------------------------------------------------------------------------------#

def test_account_class_settings_success(driver,account_type):

        #付费用户保存设置按钮
        if account_type == 1:

                driver.find_element_by_xpath("//*[@id='container']/div/div/div/div/div[10]/form/input[7]").click()

        #体验用户保存设置按钮
        elif account_type == 2:

                driver.find_element_by_xpath("//*[@id='container']/div/div/div/div/div[6]/form/input[5]").click()

        sleep(5)