#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from time import sleep


#初始化精品小班课翻页按钮个数
def fine_class_class_Initializ_list_page_button_number_success(driver):

    #翻页按钮数量
    try:

        sleep(1)

        driver.find_element_by_xpath("//*[@id='pagination']/li[8]/a")

        sleep(1)

        return 8

    except:

        try:

            sleep(1)

            driver.find_element_by_xpath("//*[@id='pagination']/li[7]/a")

            sleep(1)

            return 7

        except:

            try:

                sleep(1)

                driver.find_element_by_xpath("//*[@id='pagination']/li[6]/a")

                sleep(1)

                return 6

            except:

                try:

                    sleep(1)

                    driver.find_element_by_xpath(".//*[@id='pagination']/li[5]/a")

                    sleep(1)

                    return 5

                except:

                    try:

                        sleep(1)

                        driver.find_element_by_xpath(".//*[@id='pagination']/li[4]/a")

                        sleep(1)

                        return 4

                    except:

                        try:

                            sleep(1)

                            driver.find_element_by_xpath(".//*[@id='pagination']/li[3]/a")

                            sleep(1)

                            return 3

                        except:

                            print ("没有找到当前页数据！！！")

                            return 2


#初始化精品小班课每页约课个数
def fine_class_class_Initializ_list_page_about_class_number_success(driver):

    #每页个数
    try:

        sleep(1)

        driver.find_element_by_xpath("//*[@id='classList']/li[9]/div/a")

        sleep(1)

        return 9

    except:

        try:

            sleep(1)

            driver.find_element_by_xpath("//*[@id='classList']/li[8]/div/a")

            sleep(1)

            return 8

        except:

            try:

                sleep(1)

                driver.find_element_by_xpath("//*[@id='classList']/li[7]/div/a")

                sleep(1)

                return 7

            except:

                try:

                    sleep(1)

                    driver.find_element_by_xpath("//*[@id='classList']/li[6]/div/a")

                    sleep(1)

                    return 6

                except:

                    try:

                        sleep(1)

                        driver.find_element_by_xpath("//*[@id='classList']/li[5]/div/a")

                        sleep(1)

                        return 5

                    except:

                        try:

                            sleep(1)

                            driver.find_element_by_xpath("//*[@id='classList']/li[4]/div/a")

                            sleep(1)

                            return 4

                        except:

                            try:

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='classList']/li[3]/div/a")

                                sleep(1)

                                return 3

                            except:

                                try:

                                    sleep(1)

                                    driver.find_element_by_xpath("//*[@id='classList']/li[2]/div/a")

                                    sleep(1)

                                    return 2

                                except:

                                    try:

                                        sleep(1)

                                        driver.find_element_by_xpath("//*[@id='classList']/li[1]/div/a")

                                        sleep(1)

                                        return 1

                                    except:

                                        print ("当前页没有可预约的精品小班课数据！！！")

