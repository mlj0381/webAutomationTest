#!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *


def userInformation_db_wealth_data_insert_success(user_id,mobile,point,point_validity,classtime,current_now_time):

    '''插入user_wealth数据表记录'''

    try:

        with conn_onlie_test.cursor() as cursor:

            #多条插入
            sql_insert  = "INSERT into user_wealth(user_id,mobile,point,point_validity,classtime,add_time)" \
                          " VALUES (%s,%s,%s,%s,%s,%s)"

            cursor.execute(sql_insert,(user_id,mobile,point,point_validity,classtime,current_now_time))

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)