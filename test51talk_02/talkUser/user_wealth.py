#!usr/bin/python
#encoding:utf-8


'''财富'''


__author__ = 'zhangbo'


from time import *

from db_files.userInformation_db_wealth_data_insert import userInformation_db_wealth_data_insert_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_mobile_success
from db_files.userInformation_db_wealth_data_update import userInformation_db_wealth_data_update_success
from db_files.userInformation_db_query import userInformation_db_query_wealth_point_success


#----------------------------------------------------------------------------------------------------------------------#
    #查询体验学员财富
#----------------------------------------------------------------------------------------------------------------------#

#查询体验学员财富
def user_experience_the_wealth_success(driver,login_after_link,user_id,mobile):

        experience_point_on = False
        experience_classtime_on = True
        experience_validity_on = False
        experience_point_classtime_wealth_write_on = False

        experience_point_wealth_value_text = ""
        jieque_experience_point_validity_wealth_value_text = None
        experience_classtime_wealth_value_text = ""

        # 获取当天现在时间
        current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

        sleep(1)

        if login_after_link == "http://trial.51talk.com/trial/reserve" or \
           login_after_link == "https://trial.51talk.com/trial/reserve":

            # 获取用户user_wealth表point
            db_wealth_data = userInformation_db_query_wealth_point_success(mobile)

            sleep(1)

            if db_wealth_data == ():

                point = "1"

                point_validity = None

                classtime = ""

                # 插入user_wealth表point
                userInformation_db_wealth_data_insert_success(user_id, mobile, point, point_validity, classtime,current_now_time)

                # -----------------------------------#

                print ("用户信息写入正确，请查看！！！")

                # -----------------------------------#

                sleep(1)

                return point,classtime

            else:

                sleep(1)

                return db_wealth_data

            # return point,classtime

        else:

            print ("----------------当前账户财富信息如下：----------------")

            #判断有无体验次卡财富
            try:

                #体验学员次卡财富
                driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[3]/span")

                experience_point_wealth_value_text = driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[3]/span").text

                experience_point_on = True

            except:

                print ("当前没有找到次卡数据，请查看原因！！！")

            #判断有无体验次卡的有效期天数
            try:

                #体验学员次卡有效期
                driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[3]/span[2]")

                experience_point_validity_wealth_value_text = driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[3]/span[2]").text

                jieque_experience_point_validity_wealth_value_text = experience_point_validity_wealth_value_text[5:15]

                experience_point_on = True

                experience_validity_on = True

            except:

                pass

            if experience_point_on == True and experience_validity_on == True:

                if int(experience_point_wealth_value_text) == 0:

                    print ("目前剩余体验次卡数额度为0，请及时购买课程进行充值！！！")

                else:

                    print ("目前剩余体验次卡数额度为" + experience_point_wealth_value_text + "次" + "," + "有效期至：" + jieque_experience_point_validity_wealth_value_text)

                experience_point_classtime_wealth_write_on = True

            if experience_point_on == True and experience_validity_on == False:

                if int(experience_point_wealth_value_text) == 0:

                    print ("目前剩余体验次卡数额度为0，请及时购买课程进行充值！！！")

                else:

                    print ("目前剩余体验次卡数额度为" + experience_point_wealth_value_text + "次,请继续学习体验课程吧！！！")

                experience_point_classtime_wealth_write_on = True

            sleep(2)

            #判断有无课时财富
            try:

                #体验学员课时财富
                driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[4]/span")

                experience_classtime_wealth_value_text=  driver.find_element_by_xpath("//*[@id='basic']/div/dl/dd[4]/span").text

                if int(experience_classtime_wealth_value_text) == 0:

                    print ("目前剩余课时数额度为0，请及时购买课程进行充值！！！")

                else:

                    print ("目前剩余课时数额度为" + experience_classtime_wealth_value_text + "课时，请继续学习免费课程吧！！！")

                experience_point_classtime_wealth_write_on = True

            except:

                experience_classtime_on = False

                print ("当前没有找到课时数据，请查看原因！！！")

                experience_point_classtime_wealth_write_on = True

            sleep(2)

            if experience_point_classtime_wealth_write_on == True:

                #获取用户user_wealth表mobile
                db_wealth_mobile = userInformation_db_query_wealth_mobile_success(mobile)

                if db_wealth_mobile == ():

                    userInformation_db_wealth_data_insert_success(user_id,mobile,experience_point_wealth_value_text,
                                                                  jieque_experience_point_validity_wealth_value_text,
                                                                  experience_classtime_wealth_value_text,current_now_time)

                    # -----------------------------------#

                    print ("用户财富数据写入成功！！！")

                    # -----------------------------------#

                else:

                    #更新user_wealth表point、classtime
                    userInformation_db_wealth_data_update_success(mobile,experience_point_wealth_value_text,experience_classtime_wealth_value_text,current_now_time)

                    #-----------------------------------#

                    print ("用户财富数据更新成功！！！")

                    #-----------------------------------#

                return experience_point_wealth_value_text,experience_classtime_wealth_value_text

            print ("------------------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------#
    #查询付费学员财富
#----------------------------------------------------------------------------------------------------------------------#

#查询付费学员财富
def user_paid_the_wealth_success(driver,user_id,mobile):

        pay_point_on = False
        pay_classtime_on = False
        pay_validity_on = False
        pay_point_classtime_wealth_write_on = False

        paid_point_wealth_value_text = ""
        paid_classtime_wealth_value_text = ""
        pay_point_validity_wealth_value_text = None


        print ("----------------当前账户财富信息如下：----------------")

        # 获取当天现在时间
        current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

        #判断有无次卡财富
        try:

            #付费学员次卡财富
            driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/ul/li[2]/span")

            sleep(1)

            paid_point_wealth_value_text=  driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/ul/li[2]/span").text

            sleep(1)

            if len(paid_point_wealth_value_text) == 6:

                    jiequ_paid_point_wealth_value_text = paid_point_wealth_value_text[5:6]

            if len(paid_point_wealth_value_text) == 7:

                    jiequ_paid_point_wealth_value_text = paid_point_wealth_value_text[5:6]

            elif len(paid_point_wealth_value_text) == 8:

                    jiequ_paid_point_wealth_value_text = paid_point_wealth_value_text[5:7]

            elif len(paid_point_wealth_value_text) == 9:

                    jiequ_paid_point_wealth_value_text = paid_point_wealth_value_text[5:8]

            elif len(paid_point_wealth_value_text) == 10:

                    jiequ_paid_point_wealth_value_text = paid_point_wealth_value_text[5:9]

            pay_point_on = True

        except:

            print ("当前没有找到次卡数据，请查看原因！！！")

        sleep(2)

        #判断有无课时财富
        try:

            #付费学员课时财富
            driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/ul/li[3]/span")

            paid_classtime_wealth_value_text=  driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/ul/li[3]/span").text

            if len(paid_classtime_wealth_value_text) == 8:

                jiequ_paid_classtime_wealth_value_text = paid_classtime_wealth_value_text[5:6]

            elif len(paid_classtime_wealth_value_text) == 9:

                jiequ_paid_classtime_wealth_value_text = paid_classtime_wealth_value_text[5:7]

            elif len(paid_classtime_wealth_value_text) == 10:

                jiequ_paid_classtime_wealth_value_text = paid_classtime_wealth_value_text[5:8]

            elif len(paid_classtime_wealth_value_text) == 11:

                jiequ_paid_classtime_wealth_value_text = paid_classtime_wealth_value_text[5:9]

            pay_classtime_on = True

        except:

            print ("当前没有找到课时数据，请查看原因！！！")

            jiequ_paid_classtime_wealth_value_text = paid_classtime_wealth_value_text

        sleep(2)

        if pay_point_on == True:

            if int(jiequ_paid_point_wealth_value_text) == 0:

                print ("目前剩余次卡数额度为0，请及时购买课程进行充值！！！")

            else:

                print ("目前剩余次卡数额度为" + jiequ_paid_point_wealth_value_text + "次，请继续学习付费课程吧！！！")

            pay_point_classtime_wealth_write_on = True

        if pay_classtime_on == True:

            if int(jiequ_paid_classtime_wealth_value_text) == 0:

                print ("目前剩余课时数额度为0，请及时购买课程进行充值！！！")

            else:

                print ("目前剩余课时数额度为" + jiequ_paid_classtime_wealth_value_text + "课时，请继续学习付费课程吧！！！")

            pay_point_classtime_wealth_write_on = True

        sleep(2)

        if pay_point_classtime_wealth_write_on == True:

            #获取用户user_wealth表mobile
            db_wealth_mobile = userInformation_db_query_wealth_mobile_success(mobile)

            if db_wealth_mobile == ():

                userInformation_db_wealth_data_insert_success(user_id,mobile,jiequ_paid_point_wealth_value_text,
                                                              pay_point_validity_wealth_value_text,
                                                              jiequ_paid_classtime_wealth_value_text,
                                                              current_now_time)

                # -----------------------------------#

                print ("用户财富数据写入成功！！！")

                # -----------------------------------#

            else:

                #更新user_wealth表point、classtime
                userInformation_db_wealth_data_update_success(mobile,jiequ_paid_point_wealth_value_text,jiequ_paid_classtime_wealth_value_text,current_now_time)

                #-----------------------------------#

                print ("用户财富数据更新成功！！！")

                #-----------------------------------#

            return jiequ_paid_point_wealth_value_text,jiequ_paid_classtime_wealth_value_text

        print ("------------------------------------------------------")

