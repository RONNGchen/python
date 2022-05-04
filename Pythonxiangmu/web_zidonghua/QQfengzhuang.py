# from selenium import webdriver
# import time
#
# class QQemail():
#     def __init__(self):
#         #打开浏览器
#         self.d = webdriver.Chrome()
#         self.d.maximize_window()#窗口最大化
#     def Denglu(self):
#         #打开网址
#         self.d.get('https://mail.qq.com/')
#         #选择iframe框架
#         self.d.switch_to.frame('login_frame')
#         self.d.implicitly_wait(30)#隐式等待
#         #点击快速登录
#         self.d.find_element_by_xpath('//*[@id="img_out_934295135"]').click()
#         time.sleep(5)
# #         #调用登录方法实现登录
# # aaa = QQemail()
# # aaa.Denglu()
#     def Write(self):
#         # 点击“写信”按钮
#         self.d.find_element_by_xpath('//*[@id="composebtn"]').click()
#         time.sleep(3)
#         #获取“当前编辑邮件”框架
#         self.d.switch_to.frame('mainFrame')
#         time.sleep(5)
#         # 输入“收件人”
#         self.d.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2275244910@qq.com,2571382543@qq.com')
#         # 输入“主题”
#         self.d.find_element_by_xpath('//*[@id="subject"]').send_keys('小王子')
#         time.sleep(3)
#         # 上传附件
#         self.d.find_element_by_xpath('//*[@id="AttachFrame"]/span/input').send_keys('D:\chen\小王子.jpg')
#         time.sleep(3)
#         #通过xpath元素获取动态的“正文”框架
#         self.d.switch_to.frame(self.d.find_element_by_xpath('//iframe[@frameborder="0"]'))
#         #输入正文内容
#         self.d.find_element_by_xpath('/html/body').send_keys('孤单的小王子来到人类居住的地球')
#         time.sleep(3)
#         #切换到上一级框架(如果当前已是主框架，则无效果)
#         self.d.switch_to.parent_frame()
#         time.sleep(3)
#         #点击“发送”按钮
#         self.d.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
#         time.sleep(3)
# ##调用执行单元测试
# aaa = QQemail()
# aaa.Denglu()
# aaa.Write()

#封装登录邮箱（账号密码登录）
from selenium import webdriver
import time

class Email():
    def __init__(self):
        #打开浏览器
        self.d = webdriver.Chrome()
        self.d.maximize_window()
    def Denglu(self):
        #打开网址
        self.d.get('https://mail.qq.com/')
        #选择iframe框架
        self.d.switch_to.frame('login_frame')
        self.d.implicitly_wait(20)
        #点击帐号密码登录
        self.d.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        time.sleep(3)
        #点击登录输入框并输入
        self.d.find_element_by_xpath('//*[@id="u"]').send_keys('chen.934295135@qq.com')
        self.d.find_element_by_xpath('//*[@id="p"]').send_keys('******')
        time.sleep(3)
        #点击“授权登录”按钮
        self.d.find_element_by_xpath('//*[@id="login_button"]').click()

aaa=Email()
aaa.Denglu()


