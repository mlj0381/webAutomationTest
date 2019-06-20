##!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *


def userInformation_db_insert_order_success(user_id,order_id,order_money,current_now_time):

    '''插入数据表记录'''

    try:

        with conn_onlie_test.cursor() as cursor:

            sql_insert  = "INSERT into user_order(order_id,user_id,order_money,add_time) VALUES (%s,%s,%s,%s)"

            cursor.execute(sql_insert,(order_id,user_id,order_money,current_now_time))

            conn_onlie_test.commit()

            sleep(2)

            print ("---------------")
            print ("订单写入成功！！！")
            print ("---------------")

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)