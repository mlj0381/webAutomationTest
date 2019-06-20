#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import sleep
from talkUser.user_quit_browser import QuitBrowser

from talkUser.user_experience_class.user_experience_cadets_return_result import user_experience_cadets_return_result_success
from talkUser.user_experience_class.user_experience_cancels_cadets import user_experience_cancels_cadets_success
from talkUser.user_revising_the_textbook import user_revising_the_textbook_success


#----------------------------------------------------------------------------------------------------------------------#
    # 体验学员约课成功
#----------------------------------------------------------------------------------------------------------------------#

def user_experience_cadets_success(driver,current_window_handle,user_id,user_mobile):

    #调用约体验课，返回约课成功数值
    not_yk = user_experience_cadets_return_result_success(driver,current_window_handle,user_id,user_mobile)

    if not_yk == "NoneType":

        print ("出错了，请查看原因1。")

        QuitBrowser(driver)

    elif not_yk == None:

        print ("出错了，请查看原因2。")

        QuitBrowser(driver)

    else:

        not_yk = int(not_yk)

        sleep(2)

        if not_yk == 3:

            print (u"约课出错，请查看原因！！！")

            QuitBrowser(driver)

        elif not_yk == 2:

            print (u"约课完成页面，没有找到，请查看原因！！！")

        elif not_yk == 4:

            print (u"约课时间与实际不符合，请查看原因！！！")

        elif not_yk == 5:

            print (u"当前学员次卡或课时财富为零，不能约课，请操作其它功能！！！")

        elif not_yk == 6 or not_yk == 1:

            #调用修改体验课教材
            user_revising_the_textbook_success(driver)

            sleep(4)

            #调用取消约体验课
            user_experience_cancels_cadets_success(driver,user_id,user_mobile)