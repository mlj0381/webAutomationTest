##!usr/bin/python
#encoding:utf-8

from time import sleep
from configuration_files.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询user表mobile,password
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_query_mobile_password_success(user_mobile):

    '''查询mobile,password'''

    return_value = []

    try:

        with conn_onlie_test.cursor() as cursor:

            #查询
            sql_query  = "select mobile,password from user where mobile = %s" % (user_mobile)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            if user_info_result == ():

                return user_info_result

            else:

                for user_dict in user_info_result:

                    for key,valuse in sorted(user_dict.items(), key=operator.itemgetter(0)):

                        if key == "mobile":

                                if valuse == str(user_mobile):

                                        return_value.append(valuse)

                        elif key == "password":

                                return_value.append(valuse)

                return return_value

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询user表user_id
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_query_user_id_success(user_mobile):

    '''查询用户user_id'''

    try:

        with conn_onlie_test.cursor() as cursor:

            # 查询
            sql_query = "select user_id from user where mobile = '%s'" % (user_mobile)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            if user_info_result == ():

                return user_info_result

            else:

                for user_dict in user_info_result:

                    for key, valuse in sorted(user_dict.items(), key=operator.itemgetter(0)):

                        if key == "user_id":

                            return valuse

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询user_order表order_id
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_query_order_id_success(order_id):

    '''查询用户order_id'''

    try:

        with conn_onlie_test.cursor() as cursor:

            # 查询
            sql_query = "select order_id from user_order where order_id = '%s'" % (order_id)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            if user_info_result == ():

                return user_info_result

            else:

                for user_dict in user_info_result:

                    for key, valuse in sorted(user_dict.items(), key=operator.itemgetter(0)):

                        if key == "order_id":

                            return valuse

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询user_wealth表mobile
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_query_wealth_mobile_success(mobile):

    '''查询用户mobile'''

    try:

        with conn_onlie_test.cursor() as cursor:

            # 查询
            sql_query = "select mobile from user_wealth where mobile = '%s'" % (mobile)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            if user_info_result == ():

                return user_info_result

            else:

                for user_dict in user_info_result:

                    for key, valuse in sorted(user_dict.items(), key=operator.itemgetter(0)):

                        if key == "mobile":

                            return valuse

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)

#----------------------------------------------------------------------------------------------------------------------#
    # 查询user_wealth表point
#----------------------------------------------------------------------------------------------------------------------#

def userInformation_db_query_wealth_point_success(mobile):

    '''查询用户point'''

    return_value = []

    try:

        with conn_onlie_test.cursor() as cursor:

            # 查询
            sql_query = "select point,classtime from user_wealth where mobile = '%s'" % (mobile)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            if user_info_result == ():

                return user_info_result

            else:

                for user_dict in user_info_result:

                    for key, valuse in sorted(user_dict.items(), key=operator.itemgetter(0)):

                        if key == "point":

                            return_value.append(valuse)

                        elif key == "classtime":

                            return_value.append(valuse)

                return return_value

    except Exception as e:

        conn_onlie_test.rollback()

        print (e)
