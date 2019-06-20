#!usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'


from time import sleep


'''启动页弹出框'''


#启动页进入青少儿官网
def startPageComeInto(driver_1):

    driver_1.find_element_by_xpath("//*[@id='container']/div[6]/div[2]/ul/li[1]/a/i").click()

    sleep(5)


def startPageComeIntoAdult(driver_1):

    driver_1.find_element_by_xpath("//*[@id='container']/div[6]/div[2]/ul/li[2]/a/i").click()

    sleep(5)

