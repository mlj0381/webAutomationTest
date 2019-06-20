#!usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from selenium import webdriver
from time import sleep
import unittest
import sys,os
from time import *
import datetime

#查询目录结构
# print (sys.path)

#当前脚本路径
curPath = os.path.abspath(os.path.dirname(__file__))
# print (curPath)
# print (os.path.dirname(curPath))

#当前脚本的上一级目录路径
rootPath = os.path.split(curPath)[0]
# print (rootPath)

#目录路径添加到目录结构中
sys.path.append(rootPath)
# print (sys.path)

# sleep(20)
#初始化设置编码格式
#reload(sys)
#sys.setdefaultencoding('utf8')





import all_51talk_1


class TestTalk():

      def setUp(self):

          pass

      def tearDown(self):

          sleep(1)

all_51talk_1.creatsuite()