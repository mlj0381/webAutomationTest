#!usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'


from time import sleep
import sys
import os


#----------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#

def readLoginSuccessFile():

    cs_dir = os.path.dirname(os.getcwd())

    cs_file = "cs_login_success.txt"

    cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

    aa = open(cs_file_dir,"rb")

    success_lines = aa.readlines()

    aa.close()

    return success_lines

'''
    # for line in lines:
    #
    #     user_mobile,user_password,user_mail,user_tuijian = line.split(',')
    #     print user_mobile,user_password,user_mail,user_tuijian


    # for line in lines:
    #
    #     user_mobile   = line.split(',')[0]
    #     user_password = line.split(',')[1]
    #     user_mail     = line.split(',')[2]
    #     user_tuijian  = line.split(',')[3]

        # return user_mobile,user_password,user_mail,user_tuijian
'''


#---------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#

def readLoginFailFile():

    cs_dir = os.path.dirname(os.getcwd())

    cs_file = "cs_login_fail.txt"

    cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

    aa = open(cs_file_dir,"rb")

    fail_lines = aa.readlines()

    aa.close()

    return fail_lines


#----------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#

def readResigetSuccessFile():

    cs_dir = os.path.dirname(os.getcwd())

    cs_file = "cs_resiget_success.txt"

    cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file
    # print cs_file_dir

    aa = open(cs_file_dir,"rb")

    success_lines = aa.readlines()

    aa.close()

    return success_lines

    # for line in lines:
    #
    #     user_mobile,user_password,user_mail,user_tuijian = line.split(',')
    #     print user_mobile,user_password,user_mail,user_tuijian


    # for line in lines:
    #
    #     user_mobile   = line.split(',')[0]
    #     user_password = line.split(',')[1]
    #     user_mail     = line.split(',')[2]
    #     user_tuijian  = line.split(',')[3]

        # return user_mobile,user_password,user_mail,user_tuijian


#----------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#

def readResigetFailFile():

    cs_dir = os.path.dirname(os.getcwd())

    cs_file = "cs_resiget_fail.txt"

    cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file
    # print cs_file_dir

    aa = open(cs_file_dir,"rb")

    fail_lines = aa.readlines()

    aa.close()

    return fail_lines