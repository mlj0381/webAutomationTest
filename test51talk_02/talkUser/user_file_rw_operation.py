#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


'''用户读写操作'''

from selenium import webdriver
from time import sleep
import os


#----------------------------------------------------------------------------------------------------------------------#
    #文件读操作
#----------------------------------------------------------------------------------------------------------------------#

def user_file_r_operation():

        #读入文件
        cs_dir = os.path.dirname(os.getcwd())

        cs_file = "code.txt"

        cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

        file_name = open(cs_file_dir,"rb")

        jiequ_code = file_name.read()

        file_name.close()

        print jiequ_code

        return jiequ_code


#----------------------------------------------------------------------------------------------------------------------#
    #文件写操作
#----------------------------------------------------------------------------------------------------------------------#

def user_file_w_operation(jiequ_code):

        #写入文件
        cs_dir = os.path.dirname(os.getcwd())

        cs_file = "code.txt"

        cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

        file_name = open(cs_file_dir,"wb")

        file_name.write(jiequ_code)

        file_name.close()


#----------------------------------------------------------------------------------------------------------------------#
    #订单号读操作
#----------------------------------------------------------------------------------------------------------------------#

def user_order_file_r_operation():

        #读入文件
        cs_dir = os.path.dirname(os.getcwd())

        cs_file = "order.txt"

        cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

        file_name = open(cs_file_dir,"rb")

        jiequ_order_id = file_name.read()

        file_name.close()

        return jiequ_order_id


#----------------------------------------------------------------------------------------------------------------------#
    #订单号写操作
#----------------------------------------------------------------------------------------------------------------------#

def user_order_file_w_operation(jiequ_order_id):

        #写入文件
        cs_dir = os.path.dirname(os.getcwd())

        cs_file = "order.txt"

        cs_file_dir =  cs_dir + "/" + "FileDir" + "/" + cs_file

        file_name = open(cs_file_dir,"wb")

        file_name.write(jiequ_order_id)

        file_name.close()