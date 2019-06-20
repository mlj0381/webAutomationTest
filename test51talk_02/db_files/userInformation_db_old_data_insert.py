##!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *


def userInformation_db_old_data_insert_success(user_id,user_mobile,user_password,current_now_time):

    '''插入数据表记录'''

    try:

        with conn_onlie_test.cursor() as cursor:

            #多条插入
            sql_insert  = "INSERT into user(user_id,user_name,mobile,password,real_name,city,nick_name," \
                          "parent_id,occup,add_time,code,is_trail,is_buy,buy_time,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            # cursor.executemany(sql_insert,[('4003','2018-05-18','42','5','50','100','2018-05-18 20:00:00','2018-05-18 20:25:00','system_book'),
            #                                ('4003','2018-05-18','43','5','50','100','2018-05-18 20:30:00','2018-05-18 20:55:00','system_book')])

            cursor.execute(sql_insert,(user_id,'',user_mobile,user_password,'','惠州','','0','0',current_now_time,'','','',None,'1'))

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)

#插入之前注册过的用户信息
def userInformation_db_old_data_resiget_insert_success(user_mobile,user_password,current_now_time):

    '''插入数据表记录'''

    try:

        with conn_onlie_test.cursor() as cursor:

            #多条插入
            sql_insert  = "INSERT into user(user_id,user_name,mobile,password,real_name,city,nick_name," \
                          "parent_id,occup,add_time,code,is_trail,is_buy,buy_time,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            # cursor.executemany(sql_insert,[('4003','2018-05-18','42','5','50','100','2018-05-18 20:00:00','2018-05-18 20:25:00','system_book'),
            #                                ('4003','2018-05-18','43','5','50','100','2018-05-18 20:30:00','2018-05-18 20:55:00','system_book')])

            cursor.execute(sql_insert,('','',user_mobile,user_password,'','惠州','','0','0',current_now_time,'','','',None,'1'))

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)