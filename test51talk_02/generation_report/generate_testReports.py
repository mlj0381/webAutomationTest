#!/usr/bin/python
#encoding:utf-8

import os
import time
import HTMLTestRunner
from send_Mail import send_mail

#---------------------------------------------生成测试报告---------------------------------------------------------------#

# 生成测试报告
def generate_testreports(testunit):

    test_dir = os.getcwd() + '/report/'
    now_data = time.strftime("%Y-%m-%d_%H_%M_%S_")
    filename_dir = test_dir + now_data + "result.html"
    fp = file(filename_dir,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'51Talk前端测试报告',description=u'测试用例执行情况如下:')

    runner.run(testunit)

    fp.close()

    #调查找最新测试报告
    send_eport(test_dir)

#---------------------------------------------查找最新测试报告---------------------------------------------------------------#

# 查找最新测试报告
def send_eport(testreport):

    result_dir = testreport

    lists = os.listdir(result_dir)

    lists.sort(key= lambda x: os.path.getmtime(result_dir))

    file_name = lists[-1]

    file_dir = os.path.join(result_dir,file_name)

    #调发送邮件
    send_mail(file_dir,file_name)