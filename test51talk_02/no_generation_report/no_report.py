#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

import unittest

def no_testports(testunit):

    runner = unittest.TextTestRunner()

    runner.run(testunit)

    print ("\n" + "自动化测试执行结束：请查看结果" + "\n")

