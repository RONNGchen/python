#认识异常
# SyntaxError：语法错误
#
# NameError：试图访问的变量名不存在
#
# IndexError：索引错误，使用的索引不存在，常索引超出序列范围，什么是索引
#
# KeyError：使用了映射中不存在的关键字（键）时引发的关键字错误
#
# TypeError：类型错误，内建操作或是函数应于在了错误类型的对象时会引发类型错误
#
# ValueError：值错误，传给对象的参数类型不正确，像是给int()函数传入了字符串数据类型
#
# AttributeError：属性错误，特性引用和赋值失败时会引发属性错误
#
# IOError：输出输入错误
#
# 异常不局限于以上八种，这只是很常见的八种异常


# #1.try...except…else组合语法
# try:                 #正常的操作
#     f = open("d:\\test123.txt","r")
#     f.read()
# except IOError:      #发生异常，执行这块代码
#     print('读取文件时出现异常')
# else:                #如果没有异常执行这块代码
#     print("文件写入成功")
#
# #2.try...except组合(不带else也是可以的)
# try:
#     f = open("d:\\test123.txt", "r")
#     f.read()
#     print("文件写入成功")
# except IOError:
#     print("读取文件时出现异常")
#
# #try...except（多个异常处理）
#   #1.try...except…except
# try:
#     f = open("D:\\test123.txt","r")
#     f.read("111")
# except IOError:
#     print("读取文件时出现异常")
# except:
#     print("其它未知异常")
# else:
#     print("文件读取成功")
#
# #如何只打开一次浏览器，执行全部用例，最后关闭浏览器
# #setUp是每次用例都会执行一次
# #setUpClass是当前定义的测试类，只执行一次，必须要@classmethod修饰
# from selenium import webdriver
# import time
# import unittest
#
# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.d = webdriver.Chrome()
#         cls.d.get('https://www.baidu.com')
#         cls.d.implicitly_wait(30)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.d.quit()
#
# aaa = Test()
# aaa.setUpClass()
# aaa.tearDownClass()

#清空cookie
import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d=webdriver.Chrome()
        cls.d.get('https://passport.cnblogs.com/user/signin')
        cls.d.implicitly_wait(30)

    def setUp(self):
        # 每次用例前都清空cookie
        self.d.delete_all_cookies()
        self.d.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.d.quit()
aaa = Test()
aaa.setUpClass()