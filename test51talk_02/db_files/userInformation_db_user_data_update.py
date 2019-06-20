#!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *


#----------------------------------------------------------------------------------------------------------------------#
    #更新user表password数据
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_user_data_update_password_success(user_mobile_value,user_second_new_password):

    '''更新user数据表用户密码记录'''

    try:

        with conn_onlie_test.cursor() as cursor:


            # sql_update  = "update user_wealth set point = '%s',point_validity = '%s',classtime = '%s' where mobile = '%s'" % (mobile,point_date,point_validity_date,classtime_date);

            sql_update  = "update user set password = '"+ user_second_new_password +"' where mobile = '"+ user_mobile_value +"'"

            cursor.execute(sql_update)

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print ("e = " + str(e))


#----------------------------------------------------------------------------------------------------------------------#
    #更新user表user_id数据
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_user_data_update_user_id_success(user_mobile,user_id):

    '''更新user数据表user_id数据'''

    try:

        with conn_onlie_test.cursor() as cursor:

            # sql_update  = "update user_wealth set point = '%s',point_validity = '%s',classtime = '%s' where mobile = '%s'" % (mobile,point_date,point_validity_date,classtime_date);

            sql_update  = "update user set user_id = '"+ user_id +"' where mobile = '"+ user_mobile +"'"

            cursor.execute(sql_update)

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print ("e = " + str(e))


#----------------------------------------------------------------------------------------------------------------------#
    #更新user_order表order_id数据
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_user_data_update_order_id_success(user_id,order_id,find_order_id):

    '''更新user_order表order_id数据'''

    try:

        with conn_onlie_test.cursor() as cursor:

            # sql_update  = "update user_wealth set point = '%s',point_validity = '%s',classtime = '%s' where mobile = '%s'" % (mobile,point_date,point_validity_date,classtime_date);

            # sql_update  = "update user_order set order_id = '%s' where user_id = '%s' and order_id = '%s'" % (order_id,user_id,order_id)

            sql_update  = "update user_order set order_id = '"+ find_order_id +"' where user_id = '"+ user_id +"' and order_id = '"+ order_id +"'"

            cursor.execute(sql_update)

            conn_onlie_test.commit()

            sleep(2)

            print ("---------------")
            print ("订单写入成功！！！")
            print ("---------------")

    except Exception as e:

        conn_onlie_test.rollback()

        print ("e = " + str(e))