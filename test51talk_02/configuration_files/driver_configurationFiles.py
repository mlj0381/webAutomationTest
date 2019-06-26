#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from selenium import webdriver


def browser_driver():

    """
        jenkins服务器连接方式
        服务器：jenkins连接构建时找不到chrome报错时启用
    """
    # option = webdriver.ChromeOptions()
    #
    # option.binary_location = r"C:\Users\admin\AppData\Local\Google\Chrome\Application\chrome.exe"
    #
    # obj_driver = webdriver.Chrome(chrome_options=option,
    # 							   executable_path=r"D:\python3\chromedriver.exe")


    """
        本地电脑连接方式：PhantomJS
    """
    #window--phantomjs
    # obj_driver = webdriver.PhantomJS(executable_path="D:/Python27/phantomjs/bin/phantomjs")

    #mac--phantomjs
    # obj_driver = webdriver.PhantomJS(executable_path="/Users/zhangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")

    """
        pc与mac普通连接方式
    # """
    obj_driver = webdriver.Chrome()


    return obj_driver