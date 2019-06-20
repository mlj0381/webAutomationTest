#!usr/bin/python
#encoding:utf-8


'''公用退出浏览器'''


__author__ = 'zhangbo'

from time import sleep


#----------------------------------------------------------------------------------------------------------------------#
    #关闭浏览器
#----------------------------------------------------------------------------------------------------------------------#

# # def QuitBrowser(driver):
# #
#         sleep(1)
#
#         #调用phantomjs浏览器时：
#
#         #mac：开启浏览器退出
#         # self.driver.quit()
#
#         #window：注释浏览器退出
#         # self.driver.quit()
#
#         #调用其他浏览器时：
#         driver.quit()

def QuitBrowser(driver):

        sleep(1)

        #调用phantomjs浏览器时：

        #mac：开启浏览器退出
        # self.driver.quit()

        #window：注释浏览器退出
        # self.driver.quit()

        #调用其他浏览器时：
        driver.quit()