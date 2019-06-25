#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from selenium import webdriver


def browser_driver():

    #服务器：jenkins连接构建时找不到chrome报错时启用
    option = webdriver.ChromeOptions()

    option.binary_location = r"C:\Users\admin\AppData\Local\Google\Chrome\Application\chrome.exe"

    obj_driver = webdriver.Chrome(chrome_options=option,
    							   executable_path=r"D:\python3\chromedriver.exe")


    #window--phantomjs
    # obj_driver = webdriver.PhantomJS(executable_path="D:/Python27/phantomjs/bin/phantomjs")

    #mac--phantomjs
    # obj_driver = webdriver.PhantomJS(executable_path="/Users/zhangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")

    # obj_driver = webdriver.Chrome()

    return obj_driver