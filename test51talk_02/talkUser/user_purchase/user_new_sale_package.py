#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from time import sleep
from selenium.webdriver.common.by import By
import random
from configuration_files.courseConfig import *
from talkUser.user_purchase.user_order_payment import user_order_payment_success


#---------------------------------------------新版成人与青少售卖---------------------------------------------------------------#
    # 新版成人与青少售卖
#----------------------------------------------------------------------------------------------------------------------#

def user_new_sale_package_success(one_window_handle,driver,user_mobile,user_id):

    #售卖列表触发
    newPage_on      = True

    #教材套餐开关
    js_tc_on = False

    #外教立即购买开关
    wj_li_pay_on = False

    #全册班上课时间开关
    qcb_courser_time_on = False

    #成人、青少体验与付费次卡开关
    # adult_junior_point_tiyan_py_on = False

    #外教1对1双师课程套餐购买开关
    wj_ss_tc_on = False

    #成人付费强化、青少体验强化、青少付费强化、青少体验单元、青少付费单元
    # adult_junior_tiyan_py_qh_unit_on = False

    #判断进入订单支付页
    enter_order_payment_page = True

    #双师套餐上课时间已经选中
    sstc_class_time_select = False


    #浏览器滚动条置底
    js="var q=document.documentElement.scrollTop=380"
    driver.execute_script(js)

    sleep(2)

    try:
            #套餐是否存在
            driver.find_element(By.XPATH,".//*[@id='tabId']")

    except:

            print ("没有找到新版售卖页相应模块！")

            newPage_on = False

#----------------------------------------------------------------------------------------------------------------------#
    if  newPage_on== True:

        #外教1对1双师课程套餐标签
        junior_ss_point_taocan_unint = driver.find_element_by_xpath("//*[@id='tabId']/li[1]/a").text

        #成人课程套餐标签
        adult__point_taocan_unint = driver.find_element_by_xpath("//*[@id='tabId']/li[3]/a").text

        if junior_ss_point_taocan_unint == u"外教1对1双师课程套餐":

            #购买：强化套餐、青少单元套餐、次卡套餐类型
            taocan_unint_index = random.randint(junior_ss_start_taocan_type_sum,junior_ss_end_taocao_type_sum)

            if taocan_unint_index == 1:

                #外教1对1双师课程套餐购买开关
                wj_ss_tc_on = True

                sleep(1)

        else:

            if adult__point_taocan_unint == u"成人配套教材":

                #套餐类型切换
                taocan_unint_index = random.randint(adult_start_taocao_type_sum,adult_end_taocao_type_sum)

                sleep(1)

            elif adult__point_taocan_unint == u"次卡学习套餐":

                #套餐类型切换
                taocan_unint_index = random.randint(junior_start_taocan_type_sum,junior_end_taocan_type_sum)

                sleep(1)

        taocan_unint_index_a = ".//*[@id='tabId']/li["
        taocan_unint_index_b = taocan_unint_index
        taocan_unint_index_c = "]/a"
        taocan_unint_index_d = taocan_unint_index_a + str(taocan_unint_index_b) + taocan_unint_index_c

#----------------------------------------------------------------------------------------------------------------------#

        if taocan_unint_index_b == 1:

            pass

        else:

            driver.find_element_by_xpath(taocan_unint_index_d).click()

            sleep(2)
            #浏览器滚动条置底
            js="var q=document.documentElement.scrollTop=500"
            driver.execute_script(js)

            sleep(2)

            try:

                #成人教材套餐标签
                if driver.find_element_by_xpath("//*[@id='teacingCourse']/div[2]/h2"):

                    sleep(2)

                    js_tc_on = True

            except:

                pass

            #同下面的注释同时注释掉
            # try:
            #
            #     #次卡套餐标签
            #     if driver.find_element_by_xpath("//*[@id='infoBox']/h2"):
            #
            #         sleep(2)
            #
            #         #次卡学习套餐标签
            #         qs_unint_tc_text = driver.find_element_by_xpath("//*[@id='infoBox']/h2").text
            #
            #         sleep(2)
            #
            #         if qs_unint_tc_text == u"次卡学习套餐":
            #
            #             # adult_junior_point_tiyan_py_on = True
            #
            #             pass
            #
            # except:
            #
            #     pass

#----------------------------------------------------------------------------------------------------------------------#

        #教材开关，设置教材sku数量
        if js_tc_on == True:

            #教材套餐标签
            try:

                #教材套餐标签
                if driver.find_element_by_xpath("//*[@id='teacingCourse']/div[2]/h2"):

                    tc_sum = js_sum

                    print ("jc_tc_sum = " + str(tc_sum))

            except:

                pass

#----------------------------------------------------------------------------------------------------------------------#

        #进入非教材套餐
        else:

#----------------------------------------------------------------------------------------------------------------------#

            #外教1对1双师课程套餐购买开关，设置双师套餐sku数量
            if wj_ss_tc_on == True:

                #外教1对1套餐
                try:

                    tc_sum = wj_ss_tc_sum

                except:

                    pass

#----------------------------------------------------------------------------------------------------------------------#
            #设置非双师套餐sku数量
            else:

                # 成人付费次卡、青少付费次卡、青少体验单元、青少付费单元
                try:

                    driver.find_element_by_xpath("//*[@id='courseInfo']/li[3]")

                    tc_sum = adult_junior_tc_three_sum

                    # print ("adult_junior_tc_three_sum = " + str(tc_sum))

                    sleep(1)

                except:

                    # 成人体验强化、成人体验次卡、成人付费强化、青少体验强化、青少体验次卡、青少付费强化
                    try:

                        driver.find_element_by_xpath("//*[@id='courseInfo']/li[2]")

                        tc_sum = adult_junior_tc_two_sum

                        # print ("adult_junior_tc_two_sum = " + str(tc_sum))

                        sleep(1)

                    except:

                        print ("套餐sku数量，返回错误！！！")

                        #             #成人体验次卡、成人付费次卡、青少体验次卡、青少付费次卡（False：次卡套餐不能进入）
    #             if adult_junior_point_tiyan_py_on == False:
    #
    #                 #成人体验强化
    #                 try:
    #
    #                     #套餐sku数量
    #                     if driver.find_element_by_xpath("//*[@id='courseInfo']/li[4]"):
    #
    #                             tc_sum = adult_tiyan_qh_tc_sum
    #
    #                             print ("adult_tiyan_qh_tc_sum = " + str(tc_sum))
    #
    #                 #成人付费强化、青少体验强化、青少付费强化、青少体验单元、青少付费单元
    #                 except:
    #
    #                     sleep(2)
    #
    #                     adult_junior_tiyan_py_qh_unit_on = True
    #
    #                     #套餐sku数量
    #                     if driver.find_element_by_xpath("//*[@id='courseInfo']/li[3]"):
    #
    #                         qs_unint_tc_text = driver.find_element_by_xpath("//*[@id='infoBox']/h2").text
    #
    #                         if qs_unint_tc_text == u'强化学习效果套餐':
    #
    #                                 tc_sum = adult_junior_tiyan_py_qh_tc_sum
    #
    #                                 print ("adult_junior_tiyan_py_qh_tc_sum = " + str(tc_sum))
    #
    #                         elif qs_unint_tc_text == u"青少单元学习套餐":
    #
    #                                 tc_sum = junior_tiyan_py_unit_tc_sum
    #
    #                                 print ("junior_tiyan_py_unit_tc_sum = " + str(tc_sum))
    #
    #                 sleep(2)
    #
    # #----------------------------------------------------------------------------------------------------------------------#
    #
    #             sleep(2)
    #
    #             if adult_junior_point_tiyan_py_on == True:
    #
    #                 #成人体验次卡、成人付费次卡、青少体验次卡、青少付费次卡
    #                 try:
    #
    #                     qs_unint_tc_text = driver.find_element_by_xpath("//*[@id='infoBox']/h2").text
    #
    #                     if qs_unint_tc_text == u"次卡学习套餐":
    #
    #                         #次卡套餐数量
    #                         tc_sum = adult_junior_tiyan_py_point_tc_sum
    #
    #                         print ("adult_junior_tiyan_py_point_tc_sum = " + str(tc_sum))
    #
    #                 except:
    #
    #                     pass
    #
    #             sleep(2)

#----------------------------------------------------------------------------------------------------------------------#

        #套餐sku选中
        #外教1对1双师课程套餐购买开关
        if wj_ss_tc_on == True:

            #外教1对1双师课程套餐sku
            try:

                print (u"外教1对1双师课程套餐sku_1")

                wj_taocan_sum_index = random.randint(1,tc_sum)

                # 浏览器滚动条置底
                js = "var q=document.documentElement.scrollTop=600"
                driver.execute_script(js)

                sleep(1)

                #外教1对1双师课程套餐区域（半册班）
                if wj_taocan_sum_index == 1:

                    pass

                #外教1对1双师课程套餐区域（全册班）
                elif wj_taocan_sum_index == 2:

                    driver.find_element_by_xpath("//*[@id='116']").click()

                    qcb_courser_time_on = True

                    sleep(1)

                #单击开始上课的日期
                driver.find_element_by_xpath("//*[@id='js_date_title']").click()

                sleep(1)

                #调用开始上课日期操作选中元素
                start_class_date_select_element = start_class_time_return(driver)

                sleep(1)

                #获取开始上课日期list数据
                start_class_date_text = driver.find_element_by_xpath(start_class_date_select_element).text

                sleep(1)

                #选中开始上课日期list数据
                driver.find_element_by_xpath(start_class_date_select_element).click()

                sleep(1)

                #周五、周六、周日
                for time_index in range(1,4):

                    #周五、周六、周日
                    time_index_1 = "//*[@id='js_date_tab']/a["
                    time_index_2 = time_index
                    time_index_3 = "]"
                    time_index_4 = time_index_1 + str(time_index_2) + time_index_3

                    driver.find_element_by_xpath(time_index_4).click()

                    sleep(1)

                    #周五、周六、周日按钮选中文字
                    time_date_text = driver.find_element_by_xpath(time_index_4).text

                    #上午、下午、晚上
                    for time_interval_index in range(1,4):

                        sleep(1)

                        #时段:上午、下午、晚上
                        time_interval_index_1 = "//*[@id='js_time_tab']/a["
                        time_interval_index_2 = time_interval_index
                        time_interval_index_3 = "]"
                        time_interval_index_4 = time_interval_index_1 + str(time_interval_index_2) + time_interval_index_3

                        driver.find_element_by_xpath(time_interval_index_4).click()

                        sleep(1)

                        #上午、下午、晚上按钮选中文字
                        time_interval_text = driver.find_element_by_xpath(time_interval_index_4).text

                        sleep(1)

                        #上课时间:请选择上课时间
                        course_time_text = driver.find_element_by_xpath("//*[@id='js_time_title']").text

                        if course_time_text == u"请选择上课时间":

                            driver.find_element_by_xpath("//*[@id='js_time_title']").click()

                            sleep(1)

                            #调用上课时间操作选中元素
                            class_course_time_select_element = china_teacher_class_time_return(driver)

                            sleep(1)

                            #获取上课时间list数据
                            class_course_time_text = driver.find_element_by_xpath(class_course_time_select_element).text

                            sleep(1)

                            #选中上课时间list数据
                            driver.find_element_by_xpath(class_course_time_select_element).click()

                            sleep(1)

                            print (u"您预约了：" + start_class_date_text + "，" + class_course_time_text + "，" + time_interval_text + u"准时开班上课，请您准时出席。")

                            sleep(1)

                            wj_li_pay_on = True

                            sstc_class_time_select = True

                            break;

                        elif course_time_text == u"---":

                                print (start_class_date_text + "，" + time_date_text + time_interval_text + u"时段，" + u"该时段没有上课时间，请重新选择上课时间")

                                sleep(2)

                                continue;

                    if sstc_class_time_select == True:

                            break;

                if wj_li_pay_on == True:

                    driver.find_element_by_xpath("//*[@id='buyBtn']").click()

                    sleep(1)

            except:

                print("没有找到相应的外教1对1套餐！！！")

#----------------------------------------------------------------------------------------------------------------------#

        #非外教购买开关
        else:

            try:

                #成人、青少：强化、次卡、青少单元、成人套餐区域sku
                driver.find_element(By.XPATH,"//*[@id='courseInfo']")

                #套餐选中
                taocan_sum_index = random.randint(1,tc_sum)
                taocan_sum_index_a = "//*[@id='courseInfo']/li["
                taocan_sum_index_b = taocan_sum_index
                taocan_sum_index_c = "]"
                taocan_sum_index_d = taocan_sum_index_a + str(taocan_sum_index_b) + taocan_sum_index_c

                # print ("taocan_sum_index = " + str(taocan_sum_index_b))

                sleep(2)

                if taocan_sum_index_b == 1:

                    pass

                else:

                    #套餐选中
                    driver.find_element_by_xpath(taocan_sum_index_d).click()

                    sleep(2)

                sleep(2)

                #判断立即购买还是加入购物车:1(立即购买)、2(加入购物车)
                ljgm_jrgwc_on = random.randint(1,2)
                # print ("ljgm_jrgwc_on = " + str(ljgm_jrgwc_on))

                sleep(2)

            except:

                pass

#----------------------------------------------------------------------------------------------------------------------#

            #教材
            if js_tc_on == True:

                jc_not_pay_a = taocan_sum_index_d + "[@data-price='50']"

                sleep(2)

                jc_not_pay_b = driver.find_element_by_xpath(jc_not_pay_a).get_attribute("class")

                sleep(2)

                if jc_not_pay_b == 'n-chose':

                    print ("该教材不可购买！！！")

                    #不能支付订单
                    enter_order_payment_page = False

                else:

                    sleep(1)

                    #立即购买
                    if ljgm_jrgwc_on == 1:

                        #教材：立即购买
                        driver.find_element_by_xpath(".//*[@id='purchaseImmediately']").click()

                        #体验用户不能单独购买教材
                        try:

                            #温馨提示
                            driver.find_element_by_xpath(".//*[@id='layerBox']/div/div[1]")

                            print ("体验用户购买教材，必须同时购买其他套餐！！！")

                            sleep(1)

                            #提示框确定按钮关闭
                            driver.find_element_by_xpath(".//*[@id='layerBtn']").click()

                            sleep(1)

                            #不能支付订单
                            enter_order_payment_page = False

                        except:

                            print ("进入套餐支付页面!!!")

                            sleep(2)

                    #加入购物车
                    elif ljgm_jrgwc_on == 2:

                            sleep(1)

                            #加入购物车按钮
                            driver.find_element_by_xpath("//*[@id='cartBtn']").click()

                            sleep(1)

                            #查找购物车提交订单按钮
                            try:

                                #购物车中的提交订单按钮
                                driver.find_element(By.XPATH,"//*[@id='cart']/div[2]/div/div[6]/input")

                                sleep(1)

                                driver.find_element_by_xpath("//*[@id='cart']/div[2]/div/div[6]/input").click()

                            except:

                                print ("没有找到提交订单按钮")

                                # 不能支付订单
                                enter_order_payment_page = False

                            sleep(2)

                            #体验用户不能单独购买教材
                            try:

                                #温馨提示
                                driver.find_element_by_xpath(".//*[@id='layerBox']/div/div[1]")

                                print ("体验用户购买教材，必须同时购买其他套餐！！！")

                                sleep(2)

                                #提示框确定按钮关闭
                                driver.find_element_by_xpath(".//*[@id='layerBtn']").click()

                                sleep(2)

                                #不能支付订单
                                enter_order_payment_page = False

                            except:

                                print ("进入套餐支付页面!!!")

                                sleep(2)

#----------------------------------------------------------------------------------------------------------------------#

            #非教材
            else:

                #立即购买
                if ljgm_jrgwc_on == 1:

                    sleep(2)

                    driver.find_element_by_xpath(".//*[@id='buyBtn']").click()

                    sleep(2)

                #加入购物车
                elif ljgm_jrgwc_on == 2:

                        sleep(2)

                        #加入购物车
                        driver.find_element_by_xpath(".//*[@id='tInfoBox']/div[4]/a[2]").click()

                        sleep(0.5)

                        #查找购物车提交订单按钮
                        try:
                            driver.find_element(By.XPATH,"//*[@id='cart']/div[2]/div/div[6]/input")

                            sleep(0.5)

                            driver.find_element_by_xpath("//*[@id='cart']/div[2]/div/div[6]/input").click()

                            sleep(2)

                        except:

                            print ("没有找到提交订单按钮")

                            # 不能支付订单
                            enter_order_payment_page = False

        if enter_order_payment_page == False:

            print ("*********************************")
            print ("不能提交订单进入支付确认页面！！！   ")
            print ("*********************************")

        else:

            print ("*************************")
            print ("进入订单支付确认页面！！！  ")
            print ("*************************")

            user_order_payment_success(one_window_handle,driver,user_mobile,user_id)