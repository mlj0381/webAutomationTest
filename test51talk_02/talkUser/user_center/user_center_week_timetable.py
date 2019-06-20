#!usr/bin/python
#encoding:utf-8


'''会员中心获取当前周几课表'''


__author__ = 'zhangbo'


from time import *
import datetime


def user_center_timetable_week_return_current_success():

    #获取周期
    current_now_time = strftime('%Y-%m-%d %w',localtime(time()))

    #周几
    current_now_time_week = int(current_now_time[11:12])

    #周一
    if current_now_time_week == 1:

        return 1

    #周二
    elif current_now_time_week == 2:

        return 2

    #周三
    elif current_now_time_week == 3:

        return 3

    #周四
    elif current_now_time_week == 4:

        return 4

    #周五
    elif current_now_time_week == 5:

        return 5

    #周六
    elif current_now_time_week == 6:

        return 6

    #周日
    elif current_now_time_week == 0:

        return 7