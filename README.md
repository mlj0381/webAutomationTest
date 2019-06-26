# webAutomationTest
web自动化测试平台

运行步骤配置信息：
1、运行之前先修改configuration_files中：driver_configuration.py文件
   将连接方式修改为：jenkins服务器连接方式

2、用例执行后，需要就发测试报告到相应邮箱里面，不需要可以注释掉发送邮件
   修改all_51talk_1.py文件：

   generate_testreports：生成测试报告并发送邮件
   no_testports：不生成测试报告也不发邮件

   如果需要发送测试报告到个人邮箱，需要更改自己到邮箱地址和账户密码即可
   修改generation_report中：send_Mail.py文件