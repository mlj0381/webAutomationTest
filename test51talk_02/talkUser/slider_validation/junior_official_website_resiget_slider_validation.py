#!usr/bin/python
#encoding:utf-8


'''滑块验证'''


__author__ = 'zhangbo'


from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#滑块验证
def junior_official_website_resiget_slider_validation_mobile(driver):

    sleep(1)

    # driver.find_element_by_xpath("//*[@id='j_mobile_slider_outer']/dl/dd/div/div[2]").click()

    sleep(1)

    #滑块
    junior_official_website_resiget_slider_validation = "//*[@id='j_mobile_slider_outer']/dl/dd/div/div[2]"

    actione_1 = ActionChains(driver)

    source = driver.find_element_by_xpath(junior_official_website_resiget_slider_validation)

    #鼠标左键按下不放
    actione_1.click_and_hold(source).perform()

    sleep(1)

    #调用开始滑块请求
    # urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=move_start&gt=1")

    # sleep(1)

    #鼠标左键滑动坐标
    actione_1.move_by_offset(203,0)

    sleep(1)

    #释放鼠标左键
    actione_1.release().perform()

    sleep(1)

    #调用结束滑块请求
    # urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=success&gt=3")

    sleep(1)