#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import *

from selenium.webdriver.common.by import By

from db_files.userInformation_db_insert_order import userInformation_db_insert_order_success
from talkUser.admin_backstage.user_order_list import *


#---------------------------------------------新版订单支付---------------------------------------------------------------#
    # 新版订单支付
#----------------------------------------------------------------------------------------------------------------------#

def user_order_payment_success(one_window_handle,driver,user_mobile,user_id):

        #信用卡分期开关
        xykfq_on  = False

        #银行汇款订单提交
        wxzf_zssh_yhhk_order_on = False

        #勾选课程协议开关
        checkout_agreement_on = False

        #付款类型
        payment_type = False

        #写入订单数据，调取后台
        write_order_on = False

        #支付提交成功开关
        payment_order_after_on = False

        #银行汇款开关
        yhhk_on = False

        pay_dsf_payment_index = 0

        pay_xykfq_payment_index = 0

        jiequ_order_ID = ""

        #已阅读课程服务协议
        try:

            driver.find_element(By.XPATH,"//*[@id='form']/div[3]/div[3]/p/span")

            sleep(0.5)

            driver.find_element_by_xpath("//*[@id='form']/div[3]/div[3]/p/span").click()

            checkout_agreement_on = True

            sleep(0.5)

        except:

            print("没有找到要勾选的协议 或者 套餐购买失败！！！")

        if checkout_agreement_on == True:

            sleep(0.5)

            #查找3种支付类型存在
            try:

                driver.find_element(By.XPATH,"//*[@id='navPay']/li[3]")

                sleep(2)

                payment_type = True

            except:

                pass

            #3种支付类型
            if payment_type == True:

                payment_type_index = random.randint(1,3)

                xykfq_on  = True

            #2种、或1种支付类型
            else:

                try:

                    driver.find_element_by_xpath("//*[@id='navPay']/li[2]")

                    sleep(2)

                    payment_type_index = random.randint(1,2)

                except:

                    payment_type_index = random.randint(1,1)

            sleep(0.5)

            payment_type_index_a = "//*[@id='navPay']/li["
            payment_type_index_b = payment_type_index
            payment_type_index_c = "]"
            payment_type_index_d = payment_type_index_a + str(payment_type_index_b) + payment_type_index_c

            if payment_type_index_b == 1:

                pass

            else:

                driver.find_element_by_xpath(payment_type_index_d).click()

                sleep(0.5)

            #全额支付2个支付方式
            if payment_type_index_b == 1:

                pay_quaner_payment_index = random.randint(1,2)

                #第三方支付平台付款（支付宝、微信、快钱）
                if pay_quaner_payment_index == 1:

                    pay_dsf_payment_index = random.randint(1,3)

                    pay_dsf_payment_a = "//*[@id='payStyle']/div[3]/ul/li["
                    pay_dsf_payment_b = pay_dsf_payment_index
                    pay_dsf_payment_c = "]/label/img"
                    pay_dsf_payment_d = pay_dsf_payment_a + str(pay_dsf_payment_b) + pay_dsf_payment_c

                    sleep(2)

                    if pay_dsf_payment_index == 2:

                        wxzf_zssh_yhhk_order_on = True

                    driver.find_element_by_xpath(pay_dsf_payment_d).click()

                    sleep(2)

                #网银付款
                else:

                    pay_wy_payment_index = random.randint(1,17)

                    pay_wy_payment_a = "//*[@id='payStyle']/div[5]/ul/li["
                    pay_wy_payment_b = pay_wy_payment_index
                    pay_wy_payment_c = "]/label/img"
                    pay_wy_payment_d = pay_wy_payment_a + str(pay_wy_payment_b) + pay_wy_payment_c

                    sleep(2)

                    driver.find_element_by_xpath(pay_wy_payment_d).click()

            #信用卡支付、银行汇款
            elif payment_type_index_b == 2:

                    #信用卡支付
                    if xykfq_on == True:

                        try:

                            #有3种信用卡支付方式(掌上生活、招商银行、百度有钱花)
                            driver.find_element_by_xpath("//*[@id='payStyle']/div[3]/ul/li[3]/label/img")

                            pay_xykfq_payment_index = random.randint(1,3)

                            sleep(2)

                        except:

                            #有2种信用卡支付方式(掌上生活、招商银行)
                            pay_xykfq_payment_index = random.randint(1,2)

                            sleep(2)

                        pay_xykfq_payment_a = "//*[@id='payStyle']/div[3]/ul/li["
                        pay_xykfq_payment_b = pay_xykfq_payment_index
                        pay_xykfq_payment_c = "]/label/img"
                        pay_xykfq_payment_d = pay_xykfq_payment_a + str(pay_xykfq_payment_b) + pay_xykfq_payment_c

                        sleep(2)

                        if pay_xykfq_payment_index == 1:

                            wxzf_zssh_yhhk_order_on = True

                        driver.find_element_by_xpath(pay_xykfq_payment_d).click()

                    #银行汇款
                    else:

                        #银行汇款支付方式
                        try:

                            driver.find_element(By.XPATH,"//*[@id='payStyle']/div[3]/ul/li/label/div")

                            sleep(2)


                            driver.find_element_by_xpath("//*[@id='payStyle']/div[3]/ul/li/label/div").click()

                            wxzf_zssh_yhhk_order_on = True

                            yhhk_on = True

                        except:

                            print("没有找到银行汇款支付方式")

            #银行汇款
            elif payment_type_index_b == 3:

                #银行汇款支付方式
                try:

                    driver.find_element(By.XPATH,"//*[@id='payStyle']/div[3]/ul/li/label/div")

                    sleep(2)

                    driver.find_element_by_xpath("//*[@id='payStyle']/div[3]/ul/li/label/div").click()

                    wxzf_zssh_yhhk_order_on = True

                    yhhk_on = True

                except:

                    print("没有找到银行汇款支付方式")

            sleep(2)

            #应付总额
            total_payment_text = driver.find_element_by_xpath("//*[@id='payStyle']/div[1]/b/span").text

            #unicode转换为str
            total_payment_text = total_payment_text.encode('gbk')

            total_payment_text = str(int(float(total_payment_text)))

            sleep(2)

            #立即支付按钮
            try:

                driver.find_element(By.XPATH,"//*[@id='form']/div[4]/div[4]/span")

                sleep(0.5)

                driver.find_element_by_xpath("//*[@id='form']/div[4]/div[4]/span").click()

                # 获取当天现在时间
                current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time.time()))

                payment_order_after_on = True

            except:

                print("没有找到支付提交按钮")

            sleep(2)

            if payment_order_after_on == True:

                sleep(2)

                payment_order_after_window_handles = driver.window_handles

                for payment_order_after_handles in payment_order_after_window_handles:

                    if payment_order_after_handles != one_window_handle:

                        sleep(2)

                        driver.switch_to_window(payment_order_after_handles)

                sleep(2)

                if wxzf_zssh_yhhk_order_on == True:

                    #银行汇款
                    if yhhk_on == True:

                        pay_hou_cuerry_url     = driver.current_url

                        jiequ_http   = pay_hou_cuerry_url[0:4]
                        jiequ_https  = pay_hou_cuerry_url[0:5]

                        if jiequ_http == "http":

                            #线上环境获取订单id
                            jiequ_order_ID = pay_hou_cuerry_url[37:45]

                            #测试环境获取订单id
                            # jiequ_order_ID = pay_hou_cuerry_url[37:46]


                        elif jiequ_https == "https":

                            #线上环境获取订单id
                            jiequ_order_ID = pay_hou_cuerry_url[38:46]

                            #测试环境获取订单id
                            # jiequ_order_ID = pay_hou_cuerry_url[38:47]

                        #输入订单号
                        print ("获取的订单号为：" + str(jiequ_order_ID))

                        sleep(2)

                        #调取订单号写入文件
                        # user_order_file_w_operation(jiequ_order_ID)

                        write_order_on = True

                        sleep(2)

                        print ("***********************************************")
                        print ("银行汇款订单已提交，需要财务部确认支付信息！！！     ")
                        print ("***********************************************")

                    #微信支付、信用卡掌上生活
                    elif pay_dsf_payment_index == 2 or pay_xykfq_payment_index == 1:

                          pay_hou_cuerry_url     = driver.current_url

                          jiequ_http   = pay_hou_cuerry_url[0:4]
                          jiequ_https  = pay_hou_cuerry_url[0:5]

                          if jiequ_http == "http":

                                #线上环境获取订单id
                                jiequ_order_ID = pay_hou_cuerry_url[39:47]

                                #测试环境获取订单id
                                # jiequ_order_ID = pay_hou_cuerry_url[39:48]


                          elif jiequ_https == "https":

                                #线上环境获取订单id
                                jiequ_order_ID = pay_hou_cuerry_url[40:48]

                                #测试环境获取订单id
                                # jiequ_order_ID = pay_hou_cuerry_url[40:49]

                          #输入订单号
                          print ("获取的订单号为：" + str(jiequ_order_ID))

                          sleep(2)

                          #调取订单号写入文件
                          # user_order_file_w_operation(jiequ_order_ID)

                          write_order_on = True

                          sleep(2)

                          print ("*******************************************************************")
                          print ("微信支付或信用卡掌上生活订单已提交，需要第三方平台确认支付信息！！！        ")
                          print ("*******************************************************************")

                else:
                          write_order_on = True

                          sleep(2)

                          print ("***************************************************************************")
                          print ("支付宝、快钱、招商银行、百度有钱花或网银付款订单已提交，需要第三方平台确认支付信息！！！")
                          print ("***************************************************************************")


        driver.close()
        sleep(2)

        driver.switch_to_window(one_window_handle)
        sleep(2)

        if write_order_on == True:

              # 订单写入数据库
              userInformation_db_insert_order_success(user_id,jiequ_order_ID,total_payment_text,current_now_time)

              sleep(2)

              #调取后台处理订单表，查询订单号
              js ='window.open("http://www.51talk.com/admin/admin_login.php")'

              driver.execute_script(js)

              all_window_handles = driver.window_handles

              sleep(2)

              for hout_window_handles in all_window_handles:

                  if hout_window_handles != one_window_handle:

                         driver.switch_to_window(hout_window_handles)

                         sleep(2)

                         #调取后台处理订单表，查询订单号
                         user_order_list_quest(driver,user_mobile,user_id,jiequ_order_ID)

                         driver.close()

                         sleep(2)