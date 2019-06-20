#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

import random

from Initializ_page.sstc_class_date_Initializ import sstc_class_date_Initializ_start_date_success
from Initializ_page.sstc_class_date_Initializ import sstc_class_date_Initializ_class_time_success



#------------------------------------------------------------------#
#强化学习套餐
#次卡学习套餐
#成人配套教材
#青少单元套餐
#美小套餐
#外教1对1双师课程套餐

buyCourse_index_adult = ['强化学习效果套餐：自由预约，每月进步！',
                         '次卡学习套餐：自由预约，一天可约多节课！',
                         '中教零基础套餐',
                         '推荐教材']

buyCourse_index_junior = ['强化学习效果套餐：自由预约，每月进步！',
                          '青少经典英语学习套餐',
                          '次卡学习套餐：自由预约，一天可约多节课！',
                          '推荐教材']

buyCourse_index_na = ['美国小学课程套餐']
#------------------------------------------------------------------#




#------------------------------------------------------------------#
#美国课程--购买按钮

aa_random = random.randint(1,6)
aa_element_text_01 = ".//*[@id='paycourse']/div[3]/table/tbody/tr["
aa_element_text_02 = aa_random
aa_element_text_03 = "]/td[6]/form/input[3]"
aa_element_text_04 = aa_element_text_01+str(aa_element_text_02)+aa_element_text_03
#------------------------------------------------------------------#



#------------------------------------------------------------------#
#成人课程元素


#------------------------------------------------------------------#




#------------------------------------------------------------------#
#青少课程元素


#------------------------------------------------------------------#




#------------------------------------------------------------------#
#成人体验&青少体验：强化学习:1-6
# .//*[@id='paycourse']/div[3]/table/tbody/tr[1]/td[6]/a

#成人体验：次卡:1-2
# .//*[@id='paycourse']/div[5]/table/tbody/tr[1]/td[6]/a


#成人付费&青少付费：强化学习:1-4
# .//*[@id="paycourse"]/div[3]/table/tbody/tr[1]/td[5]/a

#成人付费：次卡:1-3
# .//*[@id="paycourse"]/div[5]/table/tbody/tr[1]/td[5]/a

#成人&青少：推荐教材:1-9
# .//*[@id="level"]/div[2]/ul/li[1]/a[1]

#青少体验：次卡:1-2
# .//*[@id="paycourse"]/div[6]/table/tbody/tr[1]/td[6]/a

#青少付费：次卡:1-3
# .//*[@id="paycourse"]/div[6]/table/tbody/tr[1]/td[5]/a

#青少套餐：1-3
# .//*[@id="paycourse"]/div[4]/ul/li[1]/div[2]/a


#美小体验&美小付费：1-6
# .//*[@id="paycourse"]/div[3]/table/tbody/tr[1]/td[6]/form/input[3]
#------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------------------------#
#美小服务协议
aa_course_service_protocol = "#ordeForm > div > div.add-new-agreement > div.add-agreement-check > p:nth-child(1) > span"
#-----------------------------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------------------------#
# 美小银行付款
aa_confirm_bank_payment_tiyanuser = "//*[@id='ordeForm']/div/div[9]/div[5]/label/span[1]"

aa_confirm_bank_payment_payuser = "//*[@id='ordeForm']/div/div[9]/label/span[1]"
#-----------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------#
# 美小支付提交页--确认付款
aa_confirm_payment_submit = "//*[@id='payBtn']/input"
#-----------------------------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------------------------#

#成人与青少套餐设置


#成人与青少套餐类型数量

#青少外教套餐：双师套餐、强化套餐、青少单元套餐、次卡套餐
junior_ss_start_taocan_type_sum   = 1
junior_ss_end_taocao_type_sum   = 4

#青少外教套餐：强化套餐、青少单元套餐、次卡套餐
junior_start_taocan_type_sum = 1
junior_end_taocan_type_sum   = 3

#成人外教套餐：强化套餐、次卡套餐、成人配套教材
adult_start_taocao_type_sum   = 1
adult_end_taocao_type_sum   = 2


#套餐数量
tc_sum          = 0

#成人体验强化、成人体验次卡、成人付费强化、青少体验强化、青少体验次卡、青少付费强化
adult_junior_tc_two_sum = 2

#成人付费次卡、青少体验单元、青少付费次卡、青少付费单元
adult_junior_tc_three_sum = 3


#成人体验强化套餐数量
#adult_tiyan_qh_tc_sum = 4

#成人青少体验付费强化套餐数量
#adult_junior_tiyan_py_qh_tc_sum = 3

#青少体验付费单元套餐数量
#junior_tiyan_py_unit_tc_sum    = 3

#体验&付费次卡套餐数量
#adult_junior_tiyan_py_point_tc_sum    = 2



#-----------------------------------------------------------------------------------------------------------------------#
#1+2 套餐设置



#外教1对1双师套餐数量
wj_ss_tc_sum = 2

#教材数量
js_sum          = 18

#全册班上午时段上课时间数量
# sw_course_time_sum = 2

#全册班下午时段上课时间数量
# xw_course_time_sum = 3

#全册班上午时段上课时间数量
# ws_course_time_sum = 2

#周六、周日时间
# start_time_sum = 2
# end_time_sum   = 3

#时段
# start_time_interval_sum = 1
# end_time_interval_sum   = 3

#----------------------------------------------------------------------------------------------------------------------#

#1+2套餐，开始上课日期设置

#半册班上课日期
# half_volume_class_time_randint = random.randint(1,1)
# half_volume_class_time_1 = "//*[@id='js_date_list']/li["
# half_volume_class_time_2 = half_volume_class_time_randint
# half_volume_class_time_3 = "]"
# half_volume_class_time_4 = half_volume_class_time_1 + str(half_volume_class_time_2) + half_volume_class_time_3
#
# #全册班上课日期
# whole_class_class_randint = random.randint(1,2)
# whole_class_class_time_1 = "//*[@id='js_date_list']/li["
# whole_class_class_time_2 = whole_class_class_randint
# whole_class_class_time_3 = "]"
# whole_class_class_time_4 = whole_class_class_time_1 + str(whole_class_class_time_2) + whole_class_class_time_3


#1+2套餐，上课时间

# class_course_time_randint = random.randint(1, course_time_sum)
# class_course_time_1 = "//*[@id='js_time_list']/li["
# class_course_time_2 = qcb_course_time_randint
# class_course_time_3 = "]"
# class_course_time_4 = qcb_course_time_1 + str(qcb_course_time_2) + qcb_course_time_3

#-----------------------------------------------------------------------------------------------------------------------#

#开始上课日期返回
def start_class_time_return(driver):

    #调用双师套餐开始上课日期个数
    start_class_time_sum = sstc_class_date_Initializ_start_date_success(driver)

    #开始上课日期
    start_class_date_randint = random.randint(1,start_class_time_sum)
    start_class_date_1 = "//*[@id='js_date_list']/li["
    start_class_date_2 = start_class_date_randint
    start_class_date_3 = "]"
    start_class_date_time_4 = start_class_date_1 + str(start_class_date_2) + start_class_date_3

    return start_class_date_time_4

#-----------------------------------------------------------------------------------------------------------------------#

#中教老师上课时间返回
def china_teacher_class_time_return(driver):

    #调用双师套餐上课时间个数
    class_course_time_sum = sstc_class_date_Initializ_class_time_success(driver)

    class_course_time_randint = random.randint(1, class_course_time_sum)
    class_course_time_1 = "//*[@id='js_time_list']/li["
    class_course_time_2 = class_course_time_sum
    class_course_time_3 = "]"
    class_course_time_4 = class_course_time_1 + str(class_course_time_2) + class_course_time_3

    return class_course_time_4
