
import pymysql
import random

#使用range（）批量插入数据方法一：
#连接数据库
db=pymysql.connect(host='localhost',user='root',password='123456',database='rongrong')
#使用cursor()方法获取操作游标
cursor=db.cursor()
#sql语句
sql = 'insert into long(age,name) values'
for i in range(10):
    if i == 9:
        sql += '(' + str(i) + ',"麻子");'
    else:
        sql += '(' + str(i) + ',"麻子"),'

print(sql)
try:
    #执行SQL语句
    cursor.execute(sql)
    #执行SQL语句
    db.commit()
    print('成功')
except:
    #发生错误时回滚
    db.rollback()
    print('失败')
cursor.close()
db.close()

# #直接插入数据(插入一次数据）
# #连接数据库
# db=pymysql.connect(host='localhost',user='root',password='root',database='test')
#
# #使用cursor()方法获取操作游标
# cursor=db.cursor()
#
# #SQL插入语句
# sql='insert into test_insert(age,name) value(15,"张三")'
#
# try:
#     #执行SQL语句
#     cursor.execute(sql)
#     #执行SQL语句
#     db.commit()
# except:
#     #发生错误时回滚
#     db.rollback()
# #关闭数据库连接
# db.close()