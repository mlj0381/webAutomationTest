#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from time import sleep


#初始化公开课list数据
def open_class_Initializ_list_page_success(driver):

    try:

        sleep(1)

        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[13]")

        sleep(1)

        return 13

    except:

            try:

                sleep(1)

                driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[12]")

                sleep(1)

                return 12

            except:

                try:

                    sleep(1)

                    driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[11]")

                    sleep(1)

                    return 11

                except:

                    sleep(1)

                    driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/ul/li[10]")

                    sleep(1)

                    return 10


