#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from selenium import webdriver


#window--phantomjs
# obj_driver = webdriver.PhantomJS(executable_path="D:/Python27/phantomjs/bin/phantomjs")

#mac--phantomjs
# obj_driver = webdriver.PhantomJS(executable_path="/Users/zhangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")

obj_driver = webdriver.Chrome()