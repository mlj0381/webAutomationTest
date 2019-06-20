#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

import random


#双师套餐开始上课日期初始化数据
def sstc_class_date_Initializ_start_date_success(driver):

    try:

        driver.find_element_by_xpath("//*[@id='js_date_list']/li[3]")

        return 3

    except:

        try:

            driver.find_element_by_xpath("//*[@id='js_date_list']/li[2]")

            return 2

        except:

            try:

                driver.find_element_by_xpath("//*[@id='js_date_list']/li[1]")

                return 1

            except:

                return 0


#双师套餐上课时间初始化数据
def sstc_class_date_Initializ_class_time_success(driver):

    try:

        driver.find_element_by_xpath("//*[@id='js_time_list']/li[3]")

        return 3

    except:

        try:

            driver.find_element_by_xpath("//*[@id='js_time_list']/li[2]")

            return 2

        except:

            try:

                driver.find_element_by_xpath("//*[@id='js_time_list']/li[1]")

                return 1

            except:

                return 0