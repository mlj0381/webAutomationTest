#!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *


#----------------------------------------------------------------------------------------------------------------------#
    #更新user_wealth表数据
#----------------------------------------------------------------------------------------------------------------------#

# def userInformation_db_wealth_data_update_success(mobile,point_date,point_validity_date,classtime_date):
#
#     '''更新user_wealth数据表记录'''
#
#     try:
#
#         with conn_onlie_test.cursor() as cursor:
#
#
#             # sql_update  = "update user_wealth set point = '%s',point_validity = '%s',classtime = '%s' where mobile = '%s'" % (mobile,point_date,point_validity_date,classtime_date);
#
#             sql_update  = "update user_wealth set point = '"+ point_date +"', point_validity = '"+ point_validity_date +"',classtime = '"+ classtime_date +"' where mobile = '"+ mobile +"'"
#
#             cursor.execute(sql_update)
#
#             conn_onlie_test.commit()
#
#             sleep(2)
#
#     except Exception as e:
#
#         conn_onlie_test.rollback()
#
#         print (e)


#----------------------------------------------------------------------------------------------------------------------#
    #更新user_wealth表point
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_wealth_data_update_success(mobile,wealth_point,wealth_classtime,wealth_update_time):

    '''更新user_wealth数据表记录'''

    try:

        with conn_onlie_test.cursor() as cursor:


            # sql_update  = "update user_wealth set point = '%s',where mobile = '%s'" % (mobile,wealth_point)

            sql_update  = "update user_wealth set point = '"+ wealth_point +"',classtime = '" + wealth_classtime +"',update_time = '"+ wealth_update_time +"' where mobile = '"+ mobile +"'"

            cursor.execute(sql_update)

            conn_onlie_test.commit()

            sleep(2)

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)