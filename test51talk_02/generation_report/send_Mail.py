#!/usr/bin/python
#encoding:utf-8


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


#---------------------------------------------查找测试报告---------------------------------------------------------------#

# 发送邮件---附件形式可以发送邮件
def send_mail(file_dir,new_file_name):

    #发送邮箱
    sender= "514571004@qq.com"
    # sender= "xiaocaishenz@sina.com"

    #接收邮箱
    # receiver = "xiaocaishenz@sina.com"
    receiver= "514571004@qq.com"

    # smtpserver = "smtp.sina.com"
    smtpserver = "smtp.qq.com"

    #发送邮箱用户/密码
    # username = u"xiaocaishenz@sina.com"
    # password = u"juedifanjidasini"

    #qq发件人,授权码
    username = u"514571004@qq.com"
    password = u"bcilwjebqilgcaaj"

    #定义发送时间
    #msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')


    #发送邮件附件
    msgRoot = MIMEMultipart('related')
    # 邮件主题
    msgRoot['Subject'] = 'Python email test'
    # msgRoot['Subject'] = Header('Python email test','utf-8')

    #邮件发件人
    msgRoot['From'] = sender

    #邮件收件人
    msgRoot['To']   = receiver


    #只发送文本
    # message = MIMEText('This is content of the email','plain','utf-8')
    #邮件发件人
    # msgRoot['From'] = sender
    #邮件收件人
    # msgRoot['To']   = receiver

    #构造附件
    att = MIMEText(open(file_dir,'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=' + new_file_name
    msgRoot.attach(att)


    try:
        #调用邮件发送方法
        # smtp = smtplib.SMTP()
        # smtp.connect(smtpserver,25)

        #qq:ssl链接方式
        smtp = smtplib.SMTP_SSL(smtpserver,465)

        smtp.login(username, password)
        smtp.sendmail(sender,receiver,msgRoot.as_string())
        print (u"已收到邮件")

    except smtplib.SMTPException as e:

        print "Error: cannot send my email"
        print e

    smtp.quit()

    print 'email has send out !'