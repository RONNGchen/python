#用点击qq登录邮箱页面，发送邮件
# from selenium import webdriver#倒包
# import time
# d = webdriver.Chrome()#选择浏览器
# d.maximize_window()#设置浏览器屏幕最大化
# # 先定位到元素再进入
# d.switch_to.frame('login_frame')#因页面是静态只需直接在括号内写入值
# # 定位登录并点击
# d.find_element_by_xpath('//*[@class="face"]').click()
#
# i = 0#定全局变量
# while True:#while循环
#
#     d.switch_to.default_content()#跳回最外层的页面
#     time.sleep(3)
#     # 定位写信并点击
#     d.find_element_by_xpath('//*[@id="composebtn"]').click()
#     # 先定位到元素框架
#     d.switch_to.frame('mainFrame')#因页面是静态只需直接在括号内写入值
#     time.sleep(2)
#     # 定位收件人
#     d.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2275244910@qq.com,2571382543@qq.com')
#     # 定位主题
#     d.find_element_by_xpath('//*[@id="subject"]').send_keys('yuyydgdgdysgdys')
#     time.sleep(2)
#     # 定位添加文件
#     d.find_element_by_xpath('//*[@id="AttachFrame"]/span/input').send_keys('D:\chen\ xiaozhan.jpg')
#     time.sleep(5)
#     # # 定位正文大框架
#     d.switch_to.frame(d.find_element_by_xpath('//iframe[@frameborder="0"]'))
#     # #定位正文输入框
#     d.find_element_by_xpath('/html/body').send_keys('haonanatainanl')
#     # #跳回上层的页面
#     d.switch_to.parent_frame()
#     # #定位发送并点击
#     d.find_element_by_xpath('//*[@id="toolbar"]/div[1]/a[1]').click()
#     if i ==3:
#         break
#     i = i + 1

#封装的文件调用运行
from web_zidonghua.QQfengzhuang import Email
aaa = Email()
aaa.Denglu()







# #用账号密码登录，发送邮件
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.maximize_window()#设置浏览器屏幕最大化
# d.get('https://mail.qq.com/')
# #定位框架在进入
# d.switch_to.frame('login_frame')#因页面是静态只需直接在括号内写入值
# time.sleep(2)
# #定位账号密码登录并点击
# d.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# #定位账号密码输入框
# d.find_element_by_id("u").send_keys('chen.934295135@qq.com')
# d.find_element_by_xpath('//*[@id="p"]').send_keys('********')
# #定位授权登录并点击
# d.find_element_by_xpath('//*[@id="login_button"]').click()
