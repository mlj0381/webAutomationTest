#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from time import sleep


def experience_cadets_week_timetable_Initializ_success(driver,week_time_index):

    week_time_date_1 = "//*[@id='classTime']/div/ul[1]/li["
    week_time_date_2 = str(week_time_index)
    week_time_date_3 = "]/span[2]"
    week_time_date_4 = week_time_date_1 + week_time_date_2 + week_time_date_3

    week_time_date = driver.find_element_by_xpath(week_time_date_4).text

    week_time_date_year  = int(week_time_date[0:4])
    week_time_date_month = int(week_time_date[5:7])
    week_time_date_day   = int(week_time_date[8:10])

    return week_time_date_year,week_time_date_month,week_time_date_day

    sleep(1)
