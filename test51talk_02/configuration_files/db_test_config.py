#!usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from pymysql import connect,cursors


# 连接teanew数据库
conn_teanew = connect(host='172.16.0.20',
                      user='root',
                      password='123456',
                      port=3306,
                      db='teanew',
                      charset='utf8',
                      cursorclass=cursors.DictCursor)

# 连接teanew数据库游标
cursor_teanew = conn_teanew.cursor()



# 连接talk数据库
conn_talk = connect(host='172.16.0.20',
                    user='root',
                    password='123456',
                    port=3306,
                    db='talk',
                    charset='utf8',
                    cursorclass=cursors.DictCursor)

# 连接talk数据库游标
cursor_talk = conn_talk.cursor()
