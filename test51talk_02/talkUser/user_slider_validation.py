#!usr/bin/python
#encoding:utf-8


'''滑块验证'''


__author__ = 'zhangbo'


from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#滑块验证
def user_experience_class_slider_validation_mobile(driver):

    sleep(1)

    driver.find_element_by_xpath("//*[@id='mobileCode']/div/ul/li[2]/div/div/div/div[2]").click()

    #滑块
    huakuai = "//*[@id='mobileCode']/div/ul/li[2]/div/div/div/div[2]"

    actione_1 = ActionChains(driver)

    source = driver.find_element_by_xpath(huakuai)

    #鼠标左键按下不放
    actione_1.click_and_hold(source).perform()

    sleep(1)

    #调用开始滑块请求
    # urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=move_start&gt=1")

    # sleep(1)

    #鼠标左键滑动坐标
    actione_1.move_by_offset(252,0)

    sleep(1)

    #释放鼠标左键
    actione_1.release().perform()

    sleep(1)

    #调用结束滑块请求
    # urllib2.urlopen("http://login.51talk.com/ajax/event/slide?action=success&gt=3")

    sleep(1)

    print ("123+")

    sleep(2)