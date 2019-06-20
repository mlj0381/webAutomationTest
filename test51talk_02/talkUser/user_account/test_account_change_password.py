#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


from time import sleep

from db_files.userInformation_db_user_data_update import userInformation_db_user_data_update_password_success
from db_files.userInformation_db_query import userInformation_db_query_mobile_password_success


#----------------------------------------------------------------------------------------------------------------------#
# 修改密码
#----------------------------------------------------------------------------------------------------------------------#

def test_account_change_password_success(driver,user_mobile_value):

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[3]/a").click()

        sleep(1)

        # 查询user表mobile,password
        db_user = userInformation_db_query_mobile_password_success(user_mobile_value)

        sleep(1)

        # 获取密码
        user_old_password = db_user[1]

        print ("您有五次机会更改密码请输入：" + "\n")

        for change_password_index in range(0,5):

                # user_old_password = raw_input("请输入该用户原登录密码：")

                sleep(1)

                driver.find_element_by_xpath("//*[@id='old_pass']").send_keys(user_old_password)

                sleep(1)

                user_one_new_password = raw_input("第一次输入新密码：")

                sleep(1)

                driver.find_element_by_xpath("//*[@id='new_pass']").send_keys(user_one_new_password)

                sleep(1)

                user_second_new_password = raw_input("第二次输入新密码：" + "\n")

                sleep(1)

                driver.find_element_by_xpath("//*[@id='new_pass2']").send_keys(user_second_new_password)

                sleep(1)

                #原密码输入错误提示
                old_password_incorrect_text = driver.find_element_by_xpath("//*[@id='changePWD']/div[1]/label/span[2]").text

                sleep(1)

                #第一次新密码输入错误提示
                one_new_password_incorrect_text = driver.find_element_by_xpath("//*[@id='changePWD']/div[2]/label/span[2]").text

                sleep(1)

                if user_old_password == user_one_new_password == user_second_new_password:

                        print ("原密码与新密码相同，请重新输入！！！" + "\n")

                        driver.refresh()

                        sleep(1)

                        continue;

                if old_password_incorrect_text == "原密码不正确" or one_new_password_incorrect_text == "新密码格式错误":

                        driver.refresh()

                        sleep(1)

                        continue;

                elif old_password_incorrect_text == "" and one_new_password_incorrect_text == "":

                        #提交修改
                        driver.find_element_by_xpath("//*[@id='changePWD']/div[4]/input").click()

                        sleep(1)

                        try:

                               #两次输入密码错误提示
                               driver.find_element_by_xpath("//*[@id='changePWD']/div[3]/label/span[2]")

                               one_and_second_new_password = driver.find_element_by_xpath("//*[@id='changePWD']/div[3]/label/span[2]").text

                               if one_and_second_new_password == "两次输入的密码不一致":

                                       driver.refresh()

                                       sleep(1)

                                       continue;

                        except:

                                print ("密码修改成功！！！")

                                sleep(1)

                                #更新user表用户密码数据
                                userInformation_db_user_data_update_password_success(user_mobile_value,user_second_new_password)

                                sleep(1)

                                # -----------------------------------#

                                print ("用户密码更新成功，请查看！！！")

                                # -----------------------------------#

                                break;

                if change_password_index == 4:

                        print ("\n" + "原密码输入超过" + str(change_password_index+1) + "次，请申请密码找回吧！！！" + "\n")

                        break;

        sleep(1)