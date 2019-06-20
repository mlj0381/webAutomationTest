#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'


'''用户身份选择'''

from selenium import webdriver
from time import sleep
import random



def user_identity_select_info(driver):

    try:

        #我的孩子要学英语
        driver.find_element_by_xpath("//*[@id='usersSelect']/div[4]/div/div[1]/ul/li[1]/a")

        #我要学英语
        driver.find_element_by_xpath("//*[@id='usersSelect']/div[4]/div/div[1]/ul/li[2]/a")

        sleep(2)

        flag_identity = True


    except:

        print ("没有找到成人或青少身份类型")

    if flag_identity == True:

        #成人与青少身份
        stu_randint = random.randint(1,2)
        sleep(1)

        flag_stu_identity_01 = "//*[@id='usersSelect']/div[4]/div/div[1]/ul/li["
        flag_stu_identity_02 = stu_randint
        flag_stu_identity_03 = "]/a"
        flag_stu_identity_04 = flag_stu_identity_01 + str(stu_randint) + flag_stu_identity_03

        driver.find_element_by_xpath(flag_stu_identity_04).click()

        #进入青少身份
        if stu_randint == 1:

            #学龄阶段
            stu_age_randint = random.randint(0,2)
            # stu_age_randint = 1
            sleep(1)

            flag_stu_age = driver.find_elements_by_xpath("//*[@id='stuAge1']/dd")

            sleep(2)

            flag_stu_age[stu_age_randint].click()

            sleep(2)

            if flag_stu_age[stu_age_randint].text == u"幼儿":

                #幼儿(1`4)
                stu_youer_randint = random.randint(1,4)
                # stu_youer_randint = 4
                sleep(1)

                flag_stu_youer_01 = "//*[@id='garde5']/dd["
                flag_stu_youer_02 = stu_youer_randint
                flag_stu_youer_03 = "]"
                flag_stu_youer_04 = flag_stu_youer_01 + str(flag_stu_youer_02) + flag_stu_youer_03

                driver.find_element_by_xpath(flag_stu_youer_04).click()

                flag_stu_youer_text = driver.find_element_by_xpath(flag_stu_youer_04).text

                if flag_stu_youer_text == u"幼儿园大班":

                   #学习目的(1~2)美国小学教育－－线上去掉了该选项
                    # stu_youeryuandaban_study_mudi_randint = random.randint(1,2)
                    # # stu_youeryuandaban_study_mudi_randint = 1
                    # sleep(1)
                    # flag_stu_youeryuandaban_study_mudi_01 = "//*[@id='purpose19']/dd["
                    # flag_stu_youeryuandaban_study_mudi_02 = stu_youeryuandaban_study_mudi_randint
                    # flag_stu_youeryuandaban_study_mudi_03 = "]"
                    # flag_stu_youeryuandaban_study_mudi_04 = flag_stu_youeryuandaban_study_mudi_01 +str(flag_stu_youeryuandaban_study_mudi_02) + flag_stu_youeryuandaban_study_mudi_03

                    driver.find_element_by_xpath("//*[@id='purpose19']/dd").click()

                    flag_stu_youeryuandaban_study_mudi_text = driver.find_element_by_xpath("//*[@id='purpose19']/dd").text

                    if  flag_stu_youeryuandaban_study_mudi_text == u"提高听说能力":

                        stu_youeryuandaban_study_mudi_yysp_randint_01 = random.randint(1,4)
                        # stu_youeryuandaban_study_mudi_yysp_randint_01 = 1
                        sleep(1)

                        flag_stu_youeryuandaban_study_mudi_yysp01_01 = "//*[@id='engLevel218']/dd["
                        flag_stu_youeryuandaban_study_mudi_yysp01_02 = stu_youeryuandaban_study_mudi_yysp_randint_01
                        flag_stu_youeryuandaban_study_mudi_yysp01_03 = "]"
                        flag_stu_youeryuandaban_study_mudi_yysp01_04 = flag_stu_youeryuandaban_study_mudi_yysp01_01 +str(flag_stu_youeryuandaban_study_mudi_yysp01_02) + flag_stu_youeryuandaban_study_mudi_yysp01_03

                        driver.find_element_by_xpath(flag_stu_youeryuandaban_study_mudi_yysp01_04).click()

                        sleep(2)

                    #美国小学教育－－线上去掉了该选项
                    # else:
                    #
                    #     stu_youeryuandaban_study_mudi_yysp_randint_02 = random.randint(1,4)
                    #     # stu_youeryuandaban_study_mudi_yysp_randint_02 = 1
                    #     sleep(1)
                    #
                    #     flag_stu_youeryuandaban_study_mudi_yysp02_01 = "//*[@id='engLevel219']/dd["
                    #     flag_stu_youeryuandaban_study_mudi_yysp02_02 = stu_youeryuandaban_study_mudi_yysp_randint_02
                    #     flag_stu_youeryuandaban_study_mudi_yysp02_03 = "]"
                    #     flag_stu_youeryuandaban_study_mudi_yysp02_04 = flag_stu_youeryuandaban_study_mudi_yysp02_01 +str(flag_stu_youeryuandaban_study_mudi_yysp02_02) + flag_stu_youeryuandaban_study_mudi_yysp02_03
                    #
                    #     driver.find_element_by_xpath(flag_stu_youeryuandaban_study_mudi_yysp02_04).click()
                    #
                    #     sleep(2)

                elif flag_stu_youer_text == u"幼儿园中班":

                        #英语水平(1~4)
                        stu_youeryuanzhongban_yysp_randint = random.randint(1,4)
                        # stu_youeryuanzhongban_yysp_randint = 1
                        sleep(1)

                        flag_stu_youeryuanzhongban_yysp_01 = "//*[@id='engLevel20']/dd["
                        flag_stu_youeryuanzhongban_yysp_02 = stu_youeryuanzhongban_yysp_randint
                        flag_stu_youeryuanzhongban_yysp_03 = "]"
                        flag_stu_youeryuanzhongban_yysp_04 = flag_stu_youeryuanzhongban_yysp_01 +str(flag_stu_youeryuanzhongban_yysp_02) + flag_stu_youeryuanzhongban_yysp_03

                        driver.find_element_by_xpath(flag_stu_youeryuanzhongban_yysp_04).click()

                        sleep(2)

                elif flag_stu_youer_text == u"幼儿园小班":

                        #英语水平(1~4)
                        stu_youeryuanxiaoban_yysp_randint = random.randint(1,4)
                        # stu_youeryuanxiaoban_yysp_randint = 1
                        sleep(1)

                        flag_stu_youeryuanxiaoban_yysp_01 = "//*[@id='engLevel21']/dd["
                        flag_stu_youeryuanxiaoban_yysp_02 = stu_youeryuanxiaoban_yysp_randint
                        flag_stu_youeryuanxiaoban_yysp_03 = "]"
                        flag_stu_youeryuanxiaoban_yysp_04 = flag_stu_youeryuanxiaoban_yysp_01 +str(flag_stu_youeryuanxiaoban_yysp_02) + flag_stu_youeryuanxiaoban_yysp_03

                        driver.find_element_by_xpath(flag_stu_youeryuanxiaoban_yysp_04).click()

                        sleep(2)

                #未上幼儿园
                else:

                        #英语水平(1~4)
                        stu_weishangyoueryuan_yysp_randint = random.randint(1,4)
                        # stu_weishangyoueryuan_yysp_randint = 1
                        sleep(1)

                        flag_stu_weishangyoueryuan_yysp_01 = "//*[@id='engLevel22']/dd["
                        flag_stu_weishangyoueryuan_yysp_02 = stu_weishangyoueryuan_yysp_randint
                        flag_stu_weishangyoueryuan_yysp_03 = "]"
                        flag_stu_weishangyoueryuan_yysp_04 = flag_stu_weishangyoueryuan_yysp_01 +str(flag_stu_weishangyoueryuan_yysp_02) + flag_stu_weishangyoueryuan_yysp_03

                        driver.find_element_by_xpath(flag_stu_weishangyoueryuan_yysp_04).click()

                        sleep(2)

            elif flag_stu_age[stu_age_randint].text == u"小学生":

                    #小学(1`6)
                    stu_xiaoxue_randint = random.randint(1,6)
                    # stu_xiaoxue_randint = 6
                    sleep(1)

                    flag_stu_xiaoxue_01 = "//*[@id='garde4']/dd["
                    flag_stu_xiaoxue_02 = stu_xiaoxue_randint
                    flag_stu_xiaoxue_03 = "]"
                    flag_stu_xiaoxue_04 = flag_stu_xiaoxue_01 + str(flag_stu_xiaoxue_02) + flag_stu_xiaoxue_03

                    driver.find_element_by_xpath(flag_stu_xiaoxue_04).click()

                    flag_stu_xiaoxue_text = driver.find_element_by_xpath(flag_stu_xiaoxue_04).text

                    if flag_stu_xiaoxue_text == u"一年级":

                        #学习目的(1~2)美国小学教育－－线上去掉了该选项
                        stu_yinianji_study_mudi_randint = random.randint(1,2)
                        # stu_yinianji_study_mudi_randint = 1
                        sleep(1)

                        flag_stu_yinianji_study_mudi_01 = "//*[@id='purpose13']/dd["
                        flag_stu_yinianji_study_mudi_02 = stu_yinianji_study_mudi_randint
                        flag_stu_yinianji_study_mudi_03 = "]"
                        flag_stu_yinianji_study_mudi_04 = flag_stu_yinianji_study_mudi_01 +str(flag_stu_yinianji_study_mudi_02) + flag_stu_yinianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_yinianji_study_mudi_04).click()

                        flag_stu_yinianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_yinianji_study_mudi_04).text

                        if  flag_stu_yinianji_study_mudi_text == u"提高听说能力":

                                stu_yinianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_yinianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_yinianji_study_mudi_yysp01_01 = "//*[@id='engLevel123']/dd["
                                flag_stu_yinianji_study_mudi_yysp01_02 = stu_yinianji_study_mudi_yysp_randint_01
                                flag_stu_yinianji_study_mudi_yysp01_03 = "]"
                                flag_stu_yinianji_study_mudi_yysp01_04 = flag_stu_yinianji_study_mudi_yysp01_01 +str(flag_stu_yinianji_study_mudi_yysp01_02) + flag_stu_yinianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_yinianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_yinianji_study_mudi_text == u"听说读写会考试":

                                stu_yinianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_yinianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_yinianji_study_mudi_yysp02_01 = "//*[@id='engLevel124']/dd["
                                flag_stu_yinianji_study_mudi_yysp02_02 = stu_yinianji_study_mudi_yysp_randint_02
                                flag_stu_yinianji_study_mudi_yysp02_03 = "]"
                                flag_stu_yinianji_study_mudi_yysp02_04 = flag_stu_yinianji_study_mudi_yysp02_01 +str(flag_stu_yinianji_study_mudi_yysp02_02) + flag_stu_yinianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_yinianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         stu_yinianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                        #         # stu_yinianji_study_mudi_yysp_randint_03 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_yinianji_study_mudi_yysp03_01 = "//*[@id='engLevel125']/dd["
                        #         flag_stu_yinianji_study_mudi_yysp03_02 = stu_yinianji_study_mudi_yysp_randint_03
                        #         flag_stu_yinianji_study_mudi_yysp03_03 = "]"
                        #         flag_stu_yinianji_study_mudi_yysp03_04 = flag_stu_yinianji_study_mudi_yysp03_01 +str(flag_stu_yinianji_study_mudi_yysp03_02) + flag_stu_yinianji_study_mudi_yysp03_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_yinianji_study_mudi_yysp03_04).click()
                        #
                        #         sleep(2)

                    elif flag_stu_xiaoxue_text == u"二年级":

                        #学习目的(1~2)美国小学教育－－线上去掉了该选项
                        stu_ernianji_study_mudi_randint = random.randint(1,2)
                        # stu_ernianji_study_mudi_randint = 1
                        sleep(1)

                        flag_stu_ernianji_study_mudi_01 = "//*[@id='purpose14']/dd["
                        flag_stu_ernianji_study_mudi_02 = stu_ernianji_study_mudi_randint
                        flag_stu_ernianji_study_mudi_03 = "]"
                        flag_stu_ernianji_study_mudi_04 = flag_stu_ernianji_study_mudi_01 +str(flag_stu_ernianji_study_mudi_02) + flag_stu_ernianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_ernianji_study_mudi_04).click()

                        flag_stu_ernianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_ernianji_study_mudi_04).text

                        if  flag_stu_ernianji_study_mudi_text == u"提高听说能力":

                                stu_ernianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_ernianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_ernianji_study_mudi_yysp01_01 = "//*[@id='engLevel138']/dd["
                                flag_stu_ernianji_study_mudi_yysp01_02 = stu_ernianji_study_mudi_yysp_randint_01
                                flag_stu_ernianji_study_mudi_yysp01_03 = "]"
                                flag_stu_ernianji_study_mudi_yysp01_04 = flag_stu_ernianji_study_mudi_yysp01_01 +str(flag_stu_ernianji_study_mudi_yysp01_02) + flag_stu_ernianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_ernianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_ernianji_study_mudi_text == u"听说读写会考试":

                                stu_ernianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_ernianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_ernianji_study_mudi_yysp02_01 = "//*[@id='engLevel139']/dd["
                                flag_stu_ernianji_study_mudi_yysp02_02 = stu_ernianji_study_mudi_yysp_randint_02
                                flag_stu_ernianji_study_mudi_yysp02_03 = "]"
                                flag_stu_ernianji_study_mudi_yysp02_04 = flag_stu_ernianji_study_mudi_yysp02_01 +str(flag_stu_ernianji_study_mudi_yysp02_02) + flag_stu_ernianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_ernianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         stu_ernianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                        #         # stu_ernianji_study_mudi_yysp_randint_03 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_ernianji_study_mudi_yysp03_01 = "//*[@id='engLevel140']/dd["
                        #         flag_stu_ernianji_study_mudi_yysp03_02 = stu_ernianji_study_mudi_yysp_randint_03
                        #         flag_stu_ernianji_study_mudi_yysp03_03 = "]"
                        #         flag_stu_ernianji_study_mudi_yysp03_04 = flag_stu_ernianji_study_mudi_yysp03_01 +str(flag_stu_ernianji_study_mudi_yysp03_02) + flag_stu_ernianji_study_mudi_yysp03_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_ernianji_study_mudi_yysp03_04).click()
                        #
                        #         sleep(2)

                    elif flag_stu_xiaoxue_text == u"三年级":

                        #学习目的(1~2)美国小学教育－－线上去掉了该选项
                        stu_sannianji_study_mudi_randint = random.randint(1,2)
                        # stu_sannianji_study_mudi_randint = 3
                        sleep(1)

                        flag_stu_sannianji_study_mudi_01 = "//*[@id='purpose15']/dd["
                        flag_stu_sannianji_study_mudi_02 = stu_sannianji_study_mudi_randint
                        flag_stu_sannianji_study_mudi_03 = "]"
                        flag_stu_sannianji_study_mudi_04 = flag_stu_sannianji_study_mudi_01 +str(flag_stu_sannianji_study_mudi_02) + flag_stu_sannianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_sannianji_study_mudi_04).click()

                        flag_stu_sannianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_sannianji_study_mudi_04).text

                        if  flag_stu_sannianji_study_mudi_text == u"提高听说能力":

                                stu_sannianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_sannianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_sannianji_study_mudi_yysp01_01 = "//*[@id='engLevel153']/dd["
                                flag_stu_sannianji_study_mudi_yysp01_02 = stu_sannianji_study_mudi_yysp_randint_01
                                flag_stu_sannianji_study_mudi_yysp01_03 = "]"
                                flag_stu_sannianji_study_mudi_yysp01_04 = flag_stu_sannianji_study_mudi_yysp01_01 +str(flag_stu_sannianji_study_mudi_yysp01_02) + flag_stu_sannianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_sannianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_sannianji_study_mudi_text == u"听说读写会考试":

                                stu_sannianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_sannianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_sannianji_study_mudi_yysp02_01 = "//*[@id='engLevel154']/dd["
                                flag_stu_sannianji_study_mudi_yysp02_02 = stu_sannianji_study_mudi_yysp_randint_02
                                flag_stu_sannianji_study_mudi_yysp02_03 = "]"
                                flag_stu_sannianji_study_mudi_yysp02_04 = flag_stu_sannianji_study_mudi_yysp02_01 +str(flag_stu_sannianji_study_mudi_yysp02_02) + flag_stu_sannianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_sannianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         stu_sannianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                        #         # stu_sannianji_study_mudi_yysp_randint_03 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_sannianji_study_mudi_yysp03_01 = "//*[@id='engLevel155']/dd["
                        #         flag_stu_sannianji_study_mudi_yysp03_02 = stu_sannianji_study_mudi_yysp_randint_03
                        #         flag_stu_sannianji_study_mudi_yysp03_03 = "]"
                        #         flag_stu_sannianji_study_mudi_yysp03_04 = flag_stu_sannianji_study_mudi_yysp03_01 +str(flag_stu_sannianji_study_mudi_yysp03_02) + flag_stu_sannianji_study_mudi_yysp03_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_sannianji_study_mudi_yysp03_04).click()
                        #
                        #         sleep(2)

                    elif flag_stu_xiaoxue_text == u"四年级":

                        #学习目的(1~2)美国小学教育－－线上去掉了该选项
                        stu_sinianji_study_mudi_randint = random.randint(1,2)
                        # stu_sinianji_study_mudi_randint = 3
                        sleep(1)

                        flag_stu_sinianji_study_mudi_01 = "//*[@id='purpose16']/dd["
                        flag_stu_sinianji_study_mudi_02 = stu_sinianji_study_mudi_randint
                        flag_stu_sinianji_study_mudi_03 = "]"
                        flag_stu_sinianji_study_mudi_04 = flag_stu_sinianji_study_mudi_01 +str(flag_stu_sinianji_study_mudi_02) + flag_stu_sinianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_sinianji_study_mudi_04).click()

                        flag_stu_sinianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_sinianji_study_mudi_04).text

                        if  flag_stu_sinianji_study_mudi_text == u"提高听说能力":

                                stu_sinianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_sinianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_sinianji_study_mudi_yysp01_01 = "//*[@id='engLevel168']/dd["
                                flag_stu_sinianji_study_mudi_yysp01_02 = stu_sinianji_study_mudi_yysp_randint_01
                                flag_stu_sinianji_study_mudi_yysp01_03 = "]"
                                flag_stu_sinianji_study_mudi_yysp01_04 = flag_stu_sinianji_study_mudi_yysp01_01 +str(flag_stu_sinianji_study_mudi_yysp01_02) + flag_stu_sinianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_sinianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_sinianji_study_mudi_text == u"听说读写会考试":

                                stu_sinianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_sinianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_sinianji_study_mudi_yysp02_01 = "//*[@id='engLevel169']/dd["
                                flag_stu_sinianji_study_mudi_yysp02_02 = stu_sinianji_study_mudi_yysp_randint_02
                                flag_stu_sinianji_study_mudi_yysp02_03 = "]"
                                flag_stu_sinianji_study_mudi_yysp02_04 = flag_stu_sinianji_study_mudi_yysp02_01 +str(flag_stu_sinianji_study_mudi_yysp02_02) + flag_stu_sinianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_sinianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         flag_stu_sinianji_study_mudi_text == u"美国小学教育"
                        #
                        #         stu_sinianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                        #         # stu_sinianji_study_mudi_yysp_randint_03 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_sinianji_study_mudi_yysp03_01 = "//*[@id='engLevel170']/dd["
                        #         flag_stu_sinianji_study_mudi_yysp03_02 = stu_sinianji_study_mudi_yysp_randint_03
                        #         flag_stu_sinianji_study_mudi_yysp03_03 = "]"
                        #         flag_stu_sinianji_study_mudi_yysp03_04 = flag_stu_sinianji_study_mudi_yysp03_01 +str(flag_stu_sinianji_study_mudi_yysp03_02) + flag_stu_sinianji_study_mudi_yysp03_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_sinianji_study_mudi_yysp03_04).click()
                        #
                        #         sleep(2)

                    elif flag_stu_xiaoxue_text == u"五年级":

                        #学习目的(1~2)
                        stu_wunianji_study_mudi_randint = random.randint(1,2)
                        # stu_wunianji_study_mudi_randint = 3
                        sleep(1)

                        flag_stu_wunianji_study_mudi_01 = "//*[@id='purpose17']/dd["
                        flag_stu_wunianji_study_mudi_02 = stu_wunianji_study_mudi_randint
                        flag_stu_wunianji_study_mudi_03 = "]"
                        flag_stu_wunianji_study_mudi_04 = flag_stu_wunianji_study_mudi_01 +str(flag_stu_wunianji_study_mudi_02) + flag_stu_wunianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_wunianji_study_mudi_04).click()

                        flag_stu_wunianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_wunianji_study_mudi_04).text

                        if  flag_stu_wunianji_study_mudi_text == u"提高听说能力":

                                stu_wunianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_wunianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_wunianji_study_mudi_yysp01_01 = "//*[@id='engLevel183']/dd["
                                flag_stu_wunianji_study_mudi_yysp01_02 = stu_wunianji_study_mudi_yysp_randint_01
                                flag_stu_wunianji_study_mudi_yysp01_03 = "]"
                                flag_stu_wunianji_study_mudi_yysp01_04 = flag_stu_wunianji_study_mudi_yysp01_01 +str(flag_stu_wunianji_study_mudi_yysp01_02) + flag_stu_wunianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_wunianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_wunianji_study_mudi_text == u"听说读写会考试":

                                stu_wunianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_wunianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_wunianji_study_mudi_yysp02_01 = "//*[@id='engLevel184']/dd["
                                flag_stu_wunianji_study_mudi_yysp02_02 = stu_wunianji_study_mudi_yysp_randint_02
                                flag_stu_wunianji_study_mudi_yysp02_03 = "]"
                                flag_stu_wunianji_study_mudi_yysp02_04 = flag_stu_wunianji_study_mudi_yysp02_01 +str(flag_stu_wunianji_study_mudi_yysp02_02) + flag_stu_wunianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_wunianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         flag_stu_wunianji_study_mudi_text == u"美国小学教育"
                        #
                        #         stu_wunianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                        #         # stu_wunianji_study_mudi_yysp_randint_03 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_wunianji_study_mudi_yysp03_01 = "//*[@id='engLevel185']/dd["
                        #         flag_stu_wunianji_study_mudi_yysp03_02 = stu_wunianji_study_mudi_yysp_randint_03
                        #         flag_stu_wunianji_study_mudi_yysp03_03 = "]"
                        #         flag_stu_wunianji_study_mudi_yysp03_04 = flag_stu_wunianji_study_mudi_yysp03_01 +str(flag_stu_wunianji_study_mudi_yysp03_02) + flag_stu_wunianji_study_mudi_yysp03_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_wunianji_study_mudi_yysp03_04).click()
                        #
                        #         sleep(2)

                    #六年级
                    else:

                        #学习目的(1~3)
                        stu_liunianji_study_mudi_randint = random.randint(1,3)
                        # stu_liunianji_study_mudi_randint = 4
                        sleep(1)

                        flag_stu_liunianji_study_mudi_01 = "//*[@id='purpose18']/dd["
                        flag_stu_liunianji_study_mudi_02 = stu_liunianji_study_mudi_randint
                        flag_stu_liunianji_study_mudi_03 = "]"
                        flag_stu_liunianji_study_mudi_04 = flag_stu_liunianji_study_mudi_01 +str(flag_stu_liunianji_study_mudi_02) + flag_stu_liunianji_study_mudi_03

                        driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_04).click()

                        flag_stu_liunianji_study_mudi_text = driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_04).text

                        if  flag_stu_liunianji_study_mudi_text == u"提高听说能力":

                                stu_liunianji_study_mudi_yysp_randint_01 = random.randint(1,4)
                                # stu_liunianji_study_mudi_yysp_randint_01 = 1
                                sleep(1)

                                flag_stu_liunianji_study_mudi_yysp01_01 = "//*[@id='engLevel198']/dd["
                                flag_stu_liunianji_study_mudi_yysp01_02 = stu_liunianji_study_mudi_yysp_randint_01
                                flag_stu_liunianji_study_mudi_yysp01_03 = "]"
                                flag_stu_liunianji_study_mudi_yysp01_04 = flag_stu_liunianji_study_mudi_yysp01_01 +str(flag_stu_liunianji_study_mudi_yysp01_02) + flag_stu_liunianji_study_mudi_yysp01_03

                                driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_yysp01_04).click()

                                sleep(2)

                        elif  flag_stu_liunianji_study_mudi_text == u"听说读写会考试":

                                stu_liunianji_study_mudi_yysp_randint_02 = random.randint(1,4)
                                # stu_liunianji_study_mudi_yysp_randint_02 = 1
                                sleep(1)

                                flag_stu_liunianji_study_mudi_yysp02_01 = "//*[@id='engLevel199']/dd["
                                flag_stu_liunianji_study_mudi_yysp02_02 = stu_liunianji_study_mudi_yysp_randint_02
                                flag_stu_liunianji_study_mudi_yysp02_03 = "]"
                                flag_stu_liunianji_study_mudi_yysp02_04 = flag_stu_liunianji_study_mudi_yysp02_01 +str(flag_stu_liunianji_study_mudi_yysp02_02) + flag_stu_liunianji_study_mudi_yysp02_03

                                driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_yysp02_04).click()

                                sleep(2)

                        elif flag_stu_liunianji_study_mudi_text == u"小升初考试":

                                stu_liunianji_study_mudi_yysp_randint_03 = random.randint(1,4)
                                # stu_liunianji_study_mudi_yysp_randint_03 = 1
                                sleep(1)

                                flag_stu_liunianji_study_mudi_yysp03_01 = "//*[@id='engLevel200']/dd["
                                flag_stu_liunianji_study_mudi_yysp03_02 = stu_liunianji_study_mudi_yysp_randint_03
                                flag_stu_liunianji_study_mudi_yysp03_03 = "]"
                                flag_stu_liunianji_study_mudi_yysp03_04 = flag_stu_liunianji_study_mudi_yysp03_01 +str(flag_stu_liunianji_study_mudi_yysp03_02) + flag_stu_liunianji_study_mudi_yysp03_03

                                driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_yysp03_04).click()

                                sleep(2)

                        #美国小学教育－－线上去掉了该选项
                        # else:
                        #
                        #         stu_liunianji_study_mudi_yysp_randint_04 = random.randint(1,4)
                        #         # stu_liunianji_study_mudi_yysp_randint_04 = 1
                        #         sleep(1)
                        #
                        #         flag_stu_liunianji_study_mudi_yysp04_01 = "//*[@id='engLevel201']/dd["
                        #         flag_stu_liunianji_study_mudi_yysp04_02 = stu_liunianji_study_mudi_yysp_randint_04
                        #         flag_stu_liunianji_study_mudi_yysp04_03 = "]"
                        #         flag_stu_liunianji_study_mudi_yysp04_04 = flag_stu_liunianji_study_mudi_yysp04_01 +str(flag_stu_liunianji_study_mudi_yysp04_02) + flag_stu_liunianji_study_mudi_yysp04_03
                        #
                        #         driver.find_element_by_xpath(flag_stu_liunianji_study_mudi_yysp04_04).click()
                        #
                        #         sleep(2)
            #初中生
            else:

                #初中(1`4)
                stu_chuzhong_randint = random.randint(1,4)
                # stu_chuzhong_randint = 4
                sleep(1)

                flag_stu_chuzhong_01 = "//*[@id='garde3']/dd["
                flag_stu_chuzhong_02 = stu_chuzhong_randint
                flag_stu_chuzhong_03 = "]"
                flag_stu_chuzhong_04 = flag_stu_chuzhong_01 + str(flag_stu_chuzhong_02) + flag_stu_chuzhong_03

                driver.find_element_by_xpath(flag_stu_chuzhong_04).click()

                flag_stu_chuzhong_text = driver.find_element_by_xpath(flag_stu_chuzhong_04).text

                if flag_stu_chuzhong_text == u"初一":

                    #学习目的(1~5)
                    stu_chuyi_study_mudi_randint = random.randint(1,5)
                    # stu_chuyi_study_mudi_randint = 1
                    sleep(1)

                    flag_stu_chuyi_study_mudi_01 = "//*[@id='purpose9']/dd["
                    flag_stu_chuyi_study_mudi_02 = stu_chuyi_study_mudi_randint
                    flag_stu_chuyi_study_mudi_03 = "]"
                    flag_stu_chuyi_study_mudi_04 = flag_stu_chuyi_study_mudi_01 +str(flag_stu_chuyi_study_mudi_02) + flag_stu_chuyi_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_04).click()

                    flag_stu_chuyi_study_mudi_text = driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_04).text


                    if  flag_stu_chuyi_study_mudi_text == u"提高听说能力":

                            stu_chuyi_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_chuyi_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_chuyi_study_mudi_yysp01_01 = "//*[@id='engLevel23']/dd["
                            flag_stu_chuyi_study_mudi_yysp01_02 = stu_chuyi_study_mudi_yysp_randint_01
                            flag_stu_chuyi_study_mudi_yysp01_03 = "]"
                            flag_stu_chuyi_study_mudi_yysp01_04 = flag_stu_chuyi_study_mudi_yysp01_01 +str(flag_stu_chuyi_study_mudi_yysp01_02) + flag_stu_chuyi_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif  flag_stu_chuyi_study_mudi_text == u"提高考试成绩":

                            stu_chuyi_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_chuyi_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_chuyi_study_mudi_yysp02_01 = "//*[@id='engLevel24']/dd["
                            flag_stu_chuyi_study_mudi_yysp02_02 = stu_chuyi_study_mudi_yysp_randint_02
                            flag_stu_chuyi_study_mudi_yysp02_03 = "]"
                            flag_stu_chuyi_study_mudi_yysp02_04 = flag_stu_chuyi_study_mudi_yysp02_01 +str(flag_stu_chuyi_study_mudi_yysp02_02) + flag_stu_chuyi_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif  flag_stu_chuyi_study_mudi_text == u"出国留学":

                            stu_chuyi_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_chuyi_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_chuyi_study_mudi_yysp03_01 = "//*[@id='engLevel25']/dd["
                            flag_stu_chuyi_study_mudi_yysp03_02 = stu_chuyi_study_mudi_yysp_randint_03
                            flag_stu_chuyi_study_mudi_yysp03_03 = "]"
                            flag_stu_chuyi_study_mudi_yysp03_04 = flag_stu_chuyi_study_mudi_yysp03_01 +str(flag_stu_chuyi_study_mudi_yysp03_02) + flag_stu_chuyi_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif  flag_stu_chuyi_study_mudi_text == u"雅思":

                            stu_chuyi_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_chuyi_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_chuyi_study_mudi_yysp04_01 = "//*[@id='engLevel26']/dd["
                            flag_stu_chuyi_study_mudi_yysp04_02 = stu_chuyi_study_mudi_yysp_randint_04
                            flag_stu_chuyi_study_mudi_yysp04_03 = "]"
                            flag_stu_chuyi_study_mudi_yysp04_04 = flag_stu_chuyi_study_mudi_yysp04_01 +str(flag_stu_chuyi_study_mudi_yysp04_02) + flag_stu_chuyi_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_yysp04_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_chuyi_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_chuyi_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_chuyi_study_mudi_yysp05_01 = "//*[@id='engLevel27']/dd["
                            flag_stu_chuyi_study_mudi_yysp05_02 = stu_chuyi_study_mudi_yysp_randint_05
                            flag_stu_chuyi_study_mudi_yysp05_03 = "]"
                            flag_stu_chuyi_study_mudi_yysp05_04 = flag_stu_chuyi_study_mudi_yysp05_01 +str(flag_stu_chuyi_study_mudi_yysp05_02) + flag_stu_chuyi_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_chuyi_study_mudi_yysp05_04).click()

                            sleep(2)

                elif flag_stu_chuzhong_text == u"初二":

                    #学习目的(1~5)
                    stu_chuer_study_mudi_randint = random.randint(1,5)
                    # stu_chuer_study_mudi_randint = 1
                    sleep(1)

                    flag_stu_chuer_study_mudi_01 = "//*[@id='purpose10']/dd["
                    flag_stu_chuer_study_mudi_02 = stu_chuer_study_mudi_randint
                    flag_stu_chuer_study_mudi_03 = "]"
                    flag_stu_chuer_study_mudi_04 = flag_stu_chuer_study_mudi_01 +str(flag_stu_chuer_study_mudi_02) + flag_stu_chuer_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_chuer_study_mudi_04).click()

                    flag_stu_chuer_study_mudi_text = driver.find_element_by_xpath(flag_stu_chuer_study_mudi_04).text


                    if  flag_stu_chuer_study_mudi_text == u"提高听说能力":

                            stu_chuer_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_chuer_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_chuer_study_mudi_yysp01_01 = "//*[@id='engLevel28']/dd["
                            flag_stu_chuer_study_mudi_yysp01_02 = stu_chuer_study_mudi_yysp_randint_01
                            flag_stu_chuer_study_mudi_yysp01_03 = "]"
                            flag_stu_chuer_study_mudi_yysp01_04 = flag_stu_chuer_study_mudi_yysp01_01 +str(flag_stu_chuer_study_mudi_yysp01_02) + flag_stu_chuer_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_chuer_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif  flag_stu_chuer_study_mudi_text == u"提高考试成绩":

                            stu_chuer_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_chuer_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_chuer_study_mudi_yysp02_01 = "//*[@id='engLevel29']/dd["
                            flag_stu_chuer_study_mudi_yysp02_02 = stu_chuer_study_mudi_yysp_randint_02
                            flag_stu_chuer_study_mudi_yysp02_03 = "]"
                            flag_stu_chuer_study_mudi_yysp02_04 = flag_stu_chuer_study_mudi_yysp02_01 +str(flag_stu_chuer_study_mudi_yysp02_02) + flag_stu_chuer_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_chuer_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif  flag_stu_chuer_study_mudi_text == u"出国留学":

                            stu_chuer_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_chuer_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_chuer_study_mudi_yysp03_01 = "//*[@id='engLevel30']/dd["
                            flag_stu_chuer_study_mudi_yysp03_02 = stu_chuer_study_mudi_yysp_randint_03
                            flag_stu_chuer_study_mudi_yysp03_03 = "]"
                            flag_stu_chuer_study_mudi_yysp03_04 = flag_stu_chuer_study_mudi_yysp03_01 +str(flag_stu_chuer_study_mudi_yysp03_02) + flag_stu_chuer_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_chuer_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif  flag_stu_chuer_study_mudi_text == u"雅思":

                            stu_chuer_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_chuer_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_chuer_study_mudi_yysp04_01 = "//*[@id='engLevel31']/dd["
                            flag_stu_chuer_study_mudi_yysp04_02 = stu_chuer_study_mudi_yysp_randint_04
                            flag_stu_chuer_study_mudi_yysp04_03 = "]"
                            flag_stu_chuer_study_mudi_yysp04_04 = flag_stu_chuer_study_mudi_yysp04_01 +str(flag_stu_chuer_study_mudi_yysp04_02) + flag_stu_chuer_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_chuer_study_mudi_yysp04_04).click()

                            sleep(2)
                    #托福
                    else:

                            stu_chuer_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_chuer_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_chuer_study_mudi_yysp05_01 = "//*[@id='engLevel32']/dd["
                            flag_stu_chuer_study_mudi_yysp05_02 = stu_chuer_study_mudi_yysp_randint_05
                            flag_stu_chuer_study_mudi_yysp05_03 = "]"
                            flag_stu_chuer_study_mudi_yysp05_04 = flag_stu_chuer_study_mudi_yysp05_01 +str(flag_stu_chuer_study_mudi_yysp05_02) + flag_stu_chuer_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_chuer_study_mudi_yysp05_04).click()

                            sleep(2)

                elif flag_stu_chuzhong_text == u"初三":

                    #学习目的(1~5)
                    stu_chusan_study_mudi_randint = random.randint(1,5)
                    # stu_chusan_study_mudi_randint = 5
                    sleep(1)

                    flag_stu_chusan_study_mudi_01 = "//*[@id='purpose11']/dd["
                    flag_stu_chusan_study_mudi_02 = stu_chusan_study_mudi_randint
                    flag_stu_chusan_study_mudi_03 = "]"
                    flag_stu_chusan_study_mudi_04 = flag_stu_chusan_study_mudi_01 +str(flag_stu_chusan_study_mudi_02) + flag_stu_chusan_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_chusan_study_mudi_04).click()

                    flag_stu_chusan_study_mudi_text = driver.find_element_by_xpath(flag_stu_chusan_study_mudi_04).text


                    if  flag_stu_chusan_study_mudi_text == u"提高听说能力":

                            stu_chusan_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_chusan_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_chusan_study_mudi_yysp01_01 = "//*[@id='engLevel33']/dd["
                            flag_stu_chusan_study_mudi_yysp01_02 = stu_chusan_study_mudi_yysp_randint_01
                            flag_stu_chusan_study_mudi_yysp01_03 = "]"
                            flag_stu_chusan_study_mudi_yysp01_04 = flag_stu_chusan_study_mudi_yysp01_01 +str(flag_stu_chusan_study_mudi_yysp01_02) + flag_stu_chusan_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_chusan_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif  flag_stu_chusan_study_mudi_text == u"提高考试成绩":

                            stu_chusan_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_chusan_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_chusan_study_mudi_yysp02_01 = "//*[@id='engLevel34']/dd["
                            flag_stu_chusan_study_mudi_yysp02_02 = stu_chusan_study_mudi_yysp_randint_02
                            flag_stu_chusan_study_mudi_yysp02_03 = "]"
                            flag_stu_chusan_study_mudi_yysp02_04 = flag_stu_chusan_study_mudi_yysp02_01 +str(flag_stu_chusan_study_mudi_yysp02_02) + flag_stu_chusan_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_chusan_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif  flag_stu_chusan_study_mudi_text == u"出国留学":

                            stu_chusan_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_chusan_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_chusan_study_mudi_yysp03_01 = "//*[@id='engLevel35']/dd["
                            flag_stu_chusan_study_mudi_yysp03_02 = stu_chusan_study_mudi_yysp_randint_03
                            flag_stu_chusan_study_mudi_yysp03_03 = "]"
                            flag_stu_chusan_study_mudi_yysp03_04 = flag_stu_chusan_study_mudi_yysp03_01 +str(flag_stu_chusan_study_mudi_yysp03_02) + flag_stu_chusan_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_chusan_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif  flag_stu_chusan_study_mudi_text == u"雅思":

                            stu_chusan_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_chusan_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_chusan_study_mudi_yysp04_01 = "//*[@id='engLevel36']/dd["
                            flag_stu_chusan_study_mudi_yysp04_02 = stu_chusan_study_mudi_yysp_randint_04
                            flag_stu_chusan_study_mudi_yysp04_03 = "]"
                            flag_stu_chusan_study_mudi_yysp04_04 = flag_stu_chusan_study_mudi_yysp04_01 +str(flag_stu_chusan_study_mudi_yysp04_02) + flag_stu_chusan_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_chusan_study_mudi_yysp04_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_chusan_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_chusan_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_chusan_study_mudi_yysp05_01 = "//*[@id='engLevel37']/dd["
                            flag_stu_chusan_study_mudi_yysp05_02 = stu_chusan_study_mudi_yysp_randint_05
                            flag_stu_chusan_study_mudi_yysp05_03 = "]"
                            flag_stu_chusan_study_mudi_yysp05_04 = flag_stu_chusan_study_mudi_yysp05_01 +str(flag_stu_chusan_study_mudi_yysp05_02) + flag_stu_chusan_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_chusan_study_mudi_yysp05_04).click()

                            sleep(2)

                #初四（五四制）
                else:

                    #学习目的(1~5)
                    stu_chusi_study_mudi_randint = random.randint(1,5)
                    # stu_chusi_study_mudi_randint = 5
                    sleep(1)

                    flag_stu_chusi_study_mudi_01 = "//*[@id='purpose12']/dd["
                    flag_stu_chusi_study_mudi_02 = stu_chusi_study_mudi_randint
                    flag_stu_chusi_study_mudi_03 = "]"
                    flag_stu_chusi_study_mudi_04 = flag_stu_chusi_study_mudi_01 +str(flag_stu_chusi_study_mudi_02) + flag_stu_chusi_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_chusi_study_mudi_04).click()

                    flag_stu_chusi_study_mudi_text = driver.find_element_by_xpath(flag_stu_chusi_study_mudi_04).text

                    if  flag_stu_chusi_study_mudi_text == u"提高听说能力":

                            stu_chusi_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_chusi_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_chusi_study_mudi_yysp01_01 = "//*[@id='engLevel38']/dd["
                            flag_stu_chusi_study_mudi_yysp01_02 = stu_chusi_study_mudi_yysp_randint_01
                            flag_stu_chusi_study_mudi_yysp01_03 = "]"
                            flag_stu_chusi_study_mudi_yysp01_04 = flag_stu_chusi_study_mudi_yysp01_01 +str(flag_stu_chusi_study_mudi_yysp01_02) + flag_stu_chusi_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_chusi_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif  flag_stu_chusi_study_mudi_text == u"提高考试成绩":

                            stu_chusi_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_chusi_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_chusi_study_mudi_yysp02_01 = "//*[@id='engLevel39']/dd["
                            flag_stu_chusi_study_mudi_yysp02_02 = stu_chusi_study_mudi_yysp_randint_02
                            flag_stu_chusi_study_mudi_yysp02_03 = "]"
                            flag_stu_chusi_study_mudi_yysp02_04 = flag_stu_chusi_study_mudi_yysp02_01 +str(flag_stu_chusi_study_mudi_yysp02_02) + flag_stu_chusi_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_chusi_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif  flag_stu_chusi_study_mudi_text == u"出国留学":

                            stu_chusi_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_chusi_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_chusi_study_mudi_yysp03_01 = "//*[@id='engLevel40']/dd["
                            flag_stu_chusi_study_mudi_yysp03_02 = stu_chusi_study_mudi_yysp_randint_03
                            flag_stu_chusi_study_mudi_yysp03_03 = "]"
                            flag_stu_chusi_study_mudi_yysp03_04 = flag_stu_chusi_study_mudi_yysp03_01 +str(flag_stu_chusi_study_mudi_yysp03_02) + flag_stu_chusi_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_chusi_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif  flag_stu_chusi_study_mudi_text == u"雅思":

                            stu_chusi_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_chusi_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_chusi_study_mudi_yysp04_01 = "//*[@id='engLevel41']/dd["
                            flag_stu_chusi_study_mudi_yysp04_02 = stu_chusi_study_mudi_yysp_randint_04
                            flag_stu_chusi_study_mudi_yysp04_03 = "]"
                            flag_stu_chusi_study_mudi_yysp04_04 = flag_stu_chusi_study_mudi_yysp04_01 +str(flag_stu_chusi_study_mudi_yysp04_02) + flag_stu_chusi_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_chusi_study_mudi_yysp04_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_chusi_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_chusi_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_chusi_study_mudi_yysp05_01 = "//*[@id='engLevel42']/dd["
                            flag_stu_chusi_study_mudi_yysp05_02 = stu_chusi_study_mudi_yysp_randint_05
                            flag_stu_chusi_study_mudi_yysp05_03 = "]"
                            flag_stu_chusi_study_mudi_yysp05_04 = flag_stu_chusi_study_mudi_yysp05_01 +str(flag_stu_chusi_study_mudi_yysp05_02) + flag_stu_chusi_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_chusi_study_mudi_yysp05_04).click()

                            sleep(2)

        #进入成人身份
        else:

            #您的职业
            stu_occup_randint = random.randint(0,2)
            # stu_occup_randint = 2
            sleep(1)

            flag_stu_occup = driver.find_elements_by_xpath("//*[@id='stuAge2']/dd")

            sleep(2)

            flag_stu_occup[stu_occup_randint].click()

            sleep(2)

            if flag_stu_occup[stu_occup_randint].text == u"上班族":

                    #学习目的(1`6)
                    stu_shangbanzu_study_mudi_randint = random.randint(1,6)
                    # stu_shangbanzu_study_mudi_randint = 6
                    sleep(1)

                    flag_stu_shangbanzu_study_mudi_01 = "//*[@id='purpose6']/dd["
                    flag_stu_shangbanzu_study_mudi_02 = stu_shangbanzu_study_mudi_randint
                    flag_stu_shangbanzu_study_mudi_03 = "]"
                    flag_stu_shangbanzu_study_mudi_04 = flag_stu_shangbanzu_study_mudi_01 + str(flag_stu_shangbanzu_study_mudi_02) + flag_stu_shangbanzu_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_04).click()

                    flag_stu_shangbanzu_study_mudi_text = driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_04).text

                    if flag_stu_shangbanzu_study_mudi_text == u"综合英语能力":

                            stu_shangbanzu_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp01_01 = "//*[@id='engLevel240']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp01_02 = stu_shangbanzu_study_mudi_yysp_randint_01
                            flag_stu_shangbanzu_study_mudi_yysp01_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp01_04 = flag_stu_shangbanzu_study_mudi_yysp01_01 +str(flag_stu_shangbanzu_study_mudi_yysp01_02) + flag_stu_shangbanzu_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif flag_stu_shangbanzu_study_mudi_text == u"商务职场":

                            stu_shangbanzu_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp02_01 = "//*[@id='engLevel241']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp02_02 = stu_shangbanzu_study_mudi_yysp_randint_02
                            flag_stu_shangbanzu_study_mudi_yysp02_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp02_04 = flag_stu_shangbanzu_study_mudi_yysp02_01 +str(flag_stu_shangbanzu_study_mudi_yysp02_02) + flag_stu_shangbanzu_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif flag_stu_shangbanzu_study_mudi_text == u"在职面试":

                            stu_shangbanzu_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp03_01 = "//*[@id='engLevel242']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp03_02 = stu_shangbanzu_study_mudi_yysp_randint_03
                            flag_stu_shangbanzu_study_mudi_yysp03_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp03_04 = flag_stu_shangbanzu_study_mudi_yysp03_01 +str(flag_stu_shangbanzu_study_mudi_yysp03_02) + flag_stu_shangbanzu_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif flag_stu_shangbanzu_study_mudi_text == u"出国旅行":

                            stu_shangbanzu_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp04_01 = "//*[@id='engLevel243']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp04_02 = stu_shangbanzu_study_mudi_yysp_randint_04
                            flag_stu_shangbanzu_study_mudi_yysp04_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp04_04 = flag_stu_shangbanzu_study_mudi_yysp04_01 +str(flag_stu_shangbanzu_study_mudi_yysp04_02) + flag_stu_shangbanzu_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp04_04).click()

                            sleep(2)

                    elif flag_stu_shangbanzu_study_mudi_text == u"雅思":

                            stu_shangbanzu_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp05_01 = "//*[@id='engLevel244']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp05_02 = stu_shangbanzu_study_mudi_yysp_randint_05
                            flag_stu_shangbanzu_study_mudi_yysp05_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp05_04 = flag_stu_shangbanzu_study_mudi_yysp05_01 +str(flag_stu_shangbanzu_study_mudi_yysp05_02) + flag_stu_shangbanzu_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp05_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_shangbanzu_study_mudi_yysp_randint_06 = random.randint(1,4)
                            # stu_shangbanzu_study_mudi_yysp_randint_06 = 1
                            sleep(1)

                            flag_stu_shangbanzu_study_mudi_yysp06_01 = "//*[@id='engLevel245']/dd["
                            flag_stu_shangbanzu_study_mudi_yysp06_02 = stu_shangbanzu_study_mudi_yysp_randint_06
                            flag_stu_shangbanzu_study_mudi_yysp06_03 = "]"
                            flag_stu_shangbanzu_study_mudi_yysp06_04 = flag_stu_shangbanzu_study_mudi_yysp06_01 +str(flag_stu_shangbanzu_study_mudi_yysp06_02) + flag_stu_shangbanzu_study_mudi_yysp06_03

                            driver.find_element_by_xpath(flag_stu_shangbanzu_study_mudi_yysp06_04).click()

                            sleep(2)

            elif flag_stu_occup[stu_occup_randint].text == u"大学生":

                    #大学生(1~6)
                    stu_daxuesheng_study_mudi_randint = random.randint(1,6)
                    # stu_daxuesheng_study_mudi_randint = 6
                    sleep(1)

                    flag_stu_daxuesheng_study_mudi_01 = "//*[@id='purpose7']/dd["
                    flag_stu_daxuesheng_study_mudi_02 = stu_daxuesheng_study_mudi_randint
                    flag_stu_daxuesheng_study_mudi_03 = "]"
                    flag_stu_daxuesheng_study_mudi_04 = flag_stu_daxuesheng_study_mudi_01 + str(flag_stu_daxuesheng_study_mudi_02) + flag_stu_daxuesheng_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_04).click()

                    flag_stu_daxuesheng_study_mudi_text = driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_04).text

                    if flag_stu_daxuesheng_study_mudi_text == u"综合英语能力":

                            stu_daxuesheng_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp01_01 = "//*[@id='engLevel270']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp01_02 = stu_daxuesheng_study_mudi_yysp_randint_01
                            flag_stu_daxuesheng_study_mudi_yysp01_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp01_04 = flag_stu_daxuesheng_study_mudi_yysp01_01 +str(flag_stu_daxuesheng_study_mudi_yysp01_02) + flag_stu_daxuesheng_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp01_04).click()

                            sleep(2)

                    elif flag_stu_daxuesheng_study_mudi_text == u"毕业生找工作":

                            stu_daxuesheng_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp02_01 = "//*[@id='engLevel271']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp02_02 = stu_daxuesheng_study_mudi_yysp_randint_02
                            flag_stu_daxuesheng_study_mudi_yysp02_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp02_04 = flag_stu_daxuesheng_study_mudi_yysp02_01 +str(flag_stu_daxuesheng_study_mudi_yysp02_02) + flag_stu_daxuesheng_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp02_04).click()

                            sleep(2)

                    elif flag_stu_daxuesheng_study_mudi_text == u"商务职场":

                            stu_daxuesheng_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp03_01 = "//*[@id='engLevel272']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp03_02 = stu_daxuesheng_study_mudi_yysp_randint_03
                            flag_stu_daxuesheng_study_mudi_yysp03_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp03_04 = flag_stu_daxuesheng_study_mudi_yysp03_01 +str(flag_stu_daxuesheng_study_mudi_yysp03_02) + flag_stu_daxuesheng_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp03_04).click()

                            sleep(2)

                    elif flag_stu_daxuesheng_study_mudi_text == u"出国旅行":

                            stu_daxuesheng_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp04_01 = "//*[@id='engLevel273']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp04_02 = stu_daxuesheng_study_mudi_yysp_randint_04
                            flag_stu_daxuesheng_study_mudi_yysp04_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp04_04 = flag_stu_daxuesheng_study_mudi_yysp04_01 +str(flag_stu_daxuesheng_study_mudi_yysp04_02) + flag_stu_daxuesheng_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp04_04).click()

                            sleep(2)

                    elif flag_stu_daxuesheng_study_mudi_text == u"雅思":

                            stu_daxuesheng_study_mudi_yysp_randint_05 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_05 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp05_01 = "//*[@id='engLevel274']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp05_02 = stu_daxuesheng_study_mudi_yysp_randint_05
                            flag_stu_daxuesheng_study_mudi_yysp05_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp05_04 = flag_stu_daxuesheng_study_mudi_yysp05_01 +str(flag_stu_daxuesheng_study_mudi_yysp05_02) + flag_stu_daxuesheng_study_mudi_yysp05_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp05_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_daxuesheng_study_mudi_yysp_randint_06 = random.randint(1,4)
                            # stu_daxuesheng_study_mudi_yysp_randint_06 = 1
                            sleep(1)

                            flag_stu_daxuesheng_study_mudi_yysp06_01 = "//*[@id='engLevel275']/dd["
                            flag_stu_daxuesheng_study_mudi_yysp06_02 = stu_daxuesheng_study_mudi_yysp_randint_06
                            flag_stu_daxuesheng_study_mudi_yysp06_03 = "]"
                            flag_stu_daxuesheng_study_mudi_yysp06_04 = flag_stu_daxuesheng_study_mudi_yysp06_01 +str(flag_stu_daxuesheng_study_mudi_yysp06_02) + flag_stu_daxuesheng_study_mudi_yysp06_03

                            driver.find_element_by_xpath(flag_stu_daxuesheng_study_mudi_yysp06_04).click()

                            sleep(2)

            #高中生
            else:

                    #高中生(1~4)
                    stu_gaozhongsheng_study_mudi_randint = random.randint(1,4)
                    # stu_gaozhongsheng_study_mudi_randint = 4
                    sleep(1)

                    flag_stu_gaozhongsheng_study_mudi_01 = "//*[@id='purpose8']/dd["
                    flag_stu_gaozhongsheng_study_mudi_02 = stu_gaozhongsheng_study_mudi_randint
                    flag_stu_gaozhongsheng_study_mudi_03 = "]"
                    flag_stu_gaozhongsheng_study_mudi_04 = flag_stu_gaozhongsheng_study_mudi_01 + str(flag_stu_gaozhongsheng_study_mudi_02) + flag_stu_gaozhongsheng_study_mudi_03

                    driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_04).click()

                    flag_stu_gaozhongsheng_study_mudi_text = driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_04).text

                    if flag_stu_gaozhongsheng_study_mudi_text == u"综合英语能力":

                            stu_gaozhongsheng_study_mudi_yysp_randint_01 = random.randint(1,4)
                            # stu_gaozhongsheng_study_mudi_yysp_randint_01 = 1
                            sleep(1)

                            flag_stu_gaozhongsheng_study_mudi_yysp01_01 = "//*[@id='engLevel300']/dd["
                            flag_stu_gaozhongsheng_study_mudi_yysp01_02 = stu_gaozhongsheng_study_mudi_yysp_randint_01
                            flag_stu_gaozhongsheng_study_mudi_yysp01_03 = "]"
                            flag_stu_gaozhongsheng_study_mudi_yysp01_04 = flag_stu_gaozhongsheng_study_mudi_yysp01_01 +str(flag_stu_gaozhongsheng_study_mudi_yysp01_02) + flag_stu_gaozhongsheng_study_mudi_yysp01_03

                            driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_yysp01_04).click()

                            sleep(2)



                    elif flag_stu_gaozhongsheng_study_mudi_text == u"出国留学":

                            stu_gaozhongsheng_study_mudi_yysp_randint_02 = random.randint(1,4)
                            # stu_gaozhongsheng_study_mudi_yysp_randint_02 = 1
                            sleep(1)

                            flag_stu_gaozhongsheng_study_mudi_yysp02_01 = "//*[@id='engLevel301']/dd["
                            flag_stu_gaozhongsheng_study_mudi_yysp02_02 = stu_gaozhongsheng_study_mudi_yysp_randint_02
                            flag_stu_gaozhongsheng_study_mudi_yysp02_03 = "]"
                            flag_stu_gaozhongsheng_study_mudi_yysp02_04 = flag_stu_gaozhongsheng_study_mudi_yysp02_01 +str(flag_stu_gaozhongsheng_study_mudi_yysp02_02) + flag_stu_gaozhongsheng_study_mudi_yysp02_03

                            driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_yysp02_04).click()

                            sleep(2)



                    elif flag_stu_gaozhongsheng_study_mudi_text == u"雅思":

                            stu_gaozhongsheng_study_mudi_yysp_randint_03 = random.randint(1,4)
                            # stu_gaozhongsheng_study_mudi_yysp_randint_03 = 1
                            sleep(1)

                            flag_stu_gaozhongsheng_study_mudi_yysp03_01 = "//*[@id='engLevel302']/dd["
                            flag_stu_gaozhongsheng_study_mudi_yysp03_02 = stu_gaozhongsheng_study_mudi_yysp_randint_03
                            flag_stu_gaozhongsheng_study_mudi_yysp03_03 = "]"
                            flag_stu_gaozhongsheng_study_mudi_yysp03_04 = flag_stu_gaozhongsheng_study_mudi_yysp03_01 +str(flag_stu_gaozhongsheng_study_mudi_yysp03_02) + flag_stu_gaozhongsheng_study_mudi_yysp03_03

                            driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_yysp03_04).click()

                            sleep(2)

                    #托福
                    else:

                            stu_gaozhongsheng_study_mudi_yysp_randint_04 = random.randint(1,4)
                            # stu_gaozhongsheng_study_mudi_yysp_randint_04 = 1
                            sleep(1)

                            flag_stu_gaozhongsheng_study_mudi_yysp04_01 = "//*[@id='engLevel303']/dd["
                            flag_stu_gaozhongsheng_study_mudi_yysp04_02 = stu_gaozhongsheng_study_mudi_yysp_randint_04
                            flag_stu_gaozhongsheng_study_mudi_yysp04_03 = "]"
                            flag_stu_gaozhongsheng_study_mudi_yysp04_04 = flag_stu_gaozhongsheng_study_mudi_yysp04_01 +str(flag_stu_gaozhongsheng_study_mudi_yysp04_02) + flag_stu_gaozhongsheng_study_mudi_yysp04_03

                            driver.find_element_by_xpath(flag_stu_gaozhongsheng_study_mudi_yysp04_04).click()

                            sleep(2)

        #体验课“完成”按钮
        driver.find_element_by_xpath("//*[@id='moreContent']/div[2]/a[2]").click()

        sleep(4)
