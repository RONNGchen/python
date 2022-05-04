#创建浏览器
#导入webdriver
# from selenium import webdriver
# import time
#创建浏览器对象，浏览器名首字母大写
# d = webdriver.Chrome()
#设置浏览器最大化
# d.maximize_window()
#获取浏览器尺寸
# r = d.get_window_size()
# print('浏览器大小为：',r)
#设置浏览器大小
# d.set_window_size(800,800)
#获取浏览器位置
# p = d.get_window_position()
# print(p)
#设置浏览器位置
# d.set_window_position(200,200)

# time.sleep(10)
# d.close

#访问浏览器各个网页页面
#导入webdriver（导入包）
# from selenium import webdriver
# import time
#创建浏览器对象，浏览器名首字母大写
# d = webdriver.Chrome()

#访问百度页面
#d.get('https://www.baidu.com/')  # 使用get方法请求网站，不能缺少协议
# time.sleep(10)

# 访问淘宝页面
# d.get('https://www.taobao.com')
#d.refresh()#refresh 用于刷新页面，当我们手动测试有需要刷新操作时可以使用这种方法进行页面的刷新操作
#time.sleep(30)

#返回（后退）到百度首页
# a = d.get('https://www.baidu.com/')
#print(a)
#d.back()
#time.sleep(3)

#前进到淘宝页面
# d.get('https://www.taobao.com')
# d.forward()
# time.sleep(3)
# d.quit()

# #获取断言、截图
# #导入webdriver（导入包）
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# #创建浏览器对象，浏览器名首字母大写
# d = webdriver.Chrome()
# #获取url(百度链接）
# url = 'http://www.baidu.com'
# d.get(url)
# #找到搜索页面
# f = d.find_element(By.ID,'kw')#找到搜索输入框
# f.send_keys('易烊千玺')#输入关键字
# f = d.find_element(By.ID,'su')
# f.click()
# #获取截图，存在内存中
# a = d.get_screenshot_as_file('D:\chen\ yiyangqianxi.jpg')
# time.sleep(10)

#1.元素定位方法的分类
#第一种：d.find_element_by_XXX()
# from selenium import webdriver #倒包
# import time
# d = webdriver.Chrome()#创建浏览器对象
# a = 'https://www.baidu.com/'
# d.get(a)
# d.find_element_by_id('kw').send_keys('易烊千玺')
# d.find_element_by_id('su').click()
# time.sleep(10)
#第二种：By的形式
# from selenium import webdriver  #倒包
# from selenium.webdriver.common.by import By
# import time
# d = webdriver.Chrome()#创建浏览器对象
# d.get('https://www.baidu.com/')#获取url百度链接
# d.find_element(By.ID,'kw').send_keys('肖战身高')#在搜索框中输入关键字
# d.find_element(By.ID,'su').click()#点击搜索
# time.sleep(10)

#元素定位的方式（通过xpath定位）
# from selenium import webdriver #倒包
# import time
# d = webdriver.Chrome()#创建浏览器
# d.get('https://movie.douban.com')#获取url
# d.find_element_by_xpath('//*[@id="screening"]/div[1]/h2/span[1]/a').click()# 通过xpath定位到全部正在热映，并点击
# time.time(5)
# d.quit()

#元素定位的方法（通过css_selector定位）
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.get('https://www.tmall.com/')
# d.find_element_by_css_selector('.inner-con2 > a:nth-child(2) > img:nth-child(1)').click()
# time.sleep(5)
# d.quit()

#元素定位的方法（通过link text定位）--链接文本定位“输入文字”
# from selenium import webdriver
# import time
# d = webdriver.Chrome()#创建浏览器
# d.maximize_window()#浏览器页面最大化
# d.get('https://www.qunar.com/')
# time.sleep(3)
# d.find_element_by_link_text('攻略').click()
# time.sleep(3)

#元素定位的方法（通过name定位）--name属性值定位
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.maximize_window()#浏览器页面最大化
# d.get('http://localhost:8080/EasyBuy/Login?action=toLogin')#浏览器路径
# d.find_element_by_name('loginName').send_keys('admin')#定位到账号输入框，并且输入
# d.find_element_by_name('password').send_keys('123456')#定位到密码输入框，并输入
# #time.sleep(10)
# d.find_element_by_xpath('//*[@class="log_btn"]').click()#用xpath定位

#打开多个窗口（标签、句柄）
from selenium import webdriver
import time                        #倒包
#d = webdriver.Chrome()#选择浏览器
#d.maximize_window()#设置浏览器屏幕最大化
#d.get('https://top.baidu.com/board?platform=pc&sa=pcindex_a_right')#获取url
#定位到'中国航空日',点击
#d.find_element_by_xpath('//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[1]/div[1]/div[2]/div/div').click()
#d.window_handles#获取所有窗口
#定位到'上海31省区市昨增本土“1566+20230'，点击
#d.find_element_by_xpath('//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[2]/div[2]/div[2]/div/div').click()
#定位到'庞宽在箱子上直播14天吃喝拉撒',点击
#d.find_element_by_xpath('//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[8]/div[2]/div[2]/div/div').click()
#d.switch_to.window(d.window_handles[-2])#切换到指定标签
#time.sleep(2)#延迟时间
#d.quit()#退出窗口

#多表单切换(frame/iframe)   通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('http://www.126.com/')#访问126邮箱
# # 直接通过id进入
# #d.switch_to.frame('x-URS-iframe')
# # 先定位到元素再进入
# a = d.find_element_by_xpath('//iframe[@frameborder="0"]')#当页面为动态时，需要用定位元素定位
# d.switch_to.frame(a)
# time.sleep(2)
# # 定位并输入账号
# d.find_element_by_name('email').send_keys('chen123456_rong')
# d.find_element_by_name('password').send_keys('Chen123456')
# d.find_element_by_id('dologin').click()
# #定位到写信页面
# d.find_element_by_xpath('//*[@id="_mail_component_149_149"]/span[2]').click()
# time.sleep(1)


#鼠标&键盘操作   (将这些关于鼠标操作的方法封装在 ActionChains 类提供)
#右击 context_click()
# from selenium import webdriver
# from selenium.webdriver import ActionChains   #导入动作链
# import time
# d = webdriver.Chrome()#创建浏览器
# d.maximize_window()
# d.get('http://www.baidu.com')#获取url
# #创建动作时对象
# aaa=ActionChains(d)
# #定位到百度的logo图片
# d.find_element_by_id('lg')
# time.sleep(2)
# #添加右键点击动作并执行
# aaa.context_click(d.find_element_by_id('lg')).perform()
# time.sleep(3)
# #关闭窗口
# d.close()

#双击 double_click()
# from selenium import webdriver
# #导入动作链
# from selenium.webdriver import ActionChains
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# #获取url
# d.get('http://www.baidu.com')
# #创建动作对象
# aaa = ActionChains(d)
# time.sleep(2)
# #定位到视频元素
# x = d.find_element_by_css_selector('#s-top-left > a:nth-child(5)')
# #执行双击操作
# aaa.double_click(x).perform()
# time.sleep(3)

#鼠标悬停 move_to_element()
# from selenium  import webdriver
# from selenium.webdriver import ActionChains
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('https://www.jd.com/')
# #获取左侧种类元素列表
# mylist = d.find_elements_by_css_selector('li.cate_menu_item')
# # print (mylist)
# # 创建动作动作对象
# aaa = ActionChains(d)
#
# for el in mylist:
#     aaa.move_to_element(el).perform()
#     time.sleep(3)

#键盘事件( send_keys()方法可以用来模拟键盘输入)
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('https://cn.bing.com/')
# #定位输入框的元素并输入
# aa = d.find_element_by_id('sb_form_q')
# aa.send_keys('selenium')
# #全选并删除
# aa.send_keys(Keys.CONTROL,'a')
# time.sleep(3)
# aa.send_keys(Keys.CONTROL,'x')
# #退格并回车
# aa.send_keys('selenium')
# time.sleep(3)
# aa.send_keys(Keys.BACK_SPACE)
# time.sleep(2)
# aa.send_keys(Keys.ENTER)
# time.sleep(5)


#弹出框(警告框)
#1.进入到警告框中
#driver.switch_to.alert             #当出现弹出框的时候，可以使用条语句进入到警告框中
#2.text：返回 alert/confirm/prompt 中的文字信息。
#3.accept()：接受现有警告框。
#4.dismiss()：解散现有警告框。
#5.send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('http://www.baidu.com')#访问百度
# #点击设置
# d.find_element_by_css_selector('#s-usersetting-top').click()
# time.sleep(3)
# # # 点击搜索设置
# d.find_element_by_css_selector('#s-user-setting-menu > div > a.setpref.first > span').click()
# time.sleep(3)
# # # 定位到保存按钮
# d.find_element_by_css_selector('#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary').click()
# time.sleep(3)
# # # 进入到弹出框，执行接受
# d.switch_to.alert.dismiss()
# time.sleep(5)

#下拉框(Select类来处理下拉框)
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('http://www.baidu.com')
# #定位设置按钮
# d.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
# time.sleep(3)
# #定位搜索设置按钮，并点击
# d.find_element_by_css_selector('#s-user-setting-menu > div > a.setpref.first > span').click()
# time.sleep(3)
# #定位高级搜索按钮，并点击
# d. find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
# #定位搜索结果（包含全部关键词）
# d.find_element_by_xpath('//*[@id="adv_keyword"]').send_keys('易烊千玺')
# # 定位下拉框对象
# d.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/i[1]').click()
# time.sleep(3)
# d.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/span').click()
# #定位高级搜索，并点击
# d.find_element_by_xpath('//*[@id="adv-setting-8"]/input').click()

#调用JavaScript代码(提供了execute_script()方法来执行JavaScript代码)
# from selenium import webdriver
# import time
# url = 'https://www.taobao.com/'
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)
#
# for i in range(100):
#     # 滚动到固定位置
#     js = 'window.scrollTo(0,%s)'%(100*i)
#     # 滚动到距离顶部指定长度
#     #js = "var q=document.documentElement.scrollTop=%s"%(100*i)
#     driver.execute_script(js)
#     time.sleep(0.2)
#
# time.sleep(5)

#等待(Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待)
#1.显式等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('http://www.baidu.com')
# #设置显示等待
# aa = WebDriverWait(d,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#kw')))
# d.close()

#2.隐式等待(提供了implicitly_wait()方法来实现隐式等待)
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('https://www.amazon.cn/')
# # 设置隐式等待
# d.implicitly_wait(10)
# d.close()

#cookies(需要验证浏览器中cookie是否正确,提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息)

#WebDriver操作cookie的方法:
# 1.get_cookies()： 获得所有cookie信息
# 2.get_cookie(name)： 返回字典的key为“name”的cookie信息
# 3.add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值
# 4.delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
# 5.delete_all_cookies()： 删除所有cookie信息

#通过get_cookies()来获取当前浏览器的cookie信息
# from selenium import webdriver
#
# d = webdriver.Chrome()
# d.get("http://www.youdao.com")
#
# # 获得cookie信息
# cookie= d.get_cookies()
# # 将获得cookie的信息打印
# print(cookie)
#
# d.quit()

#cookie数据是以字典的形式进行存放的,以按照这种形式向浏览器中写入cookie信息
# from selenium import webdriver
#
# d = webdriver.Chrome()
# d.get("http://www.youdao.com")
#
# # 向cookie的name 和value中添加会话信息
# d.add_cookie({'name': 'itcast', 'value': 'itheima'})
#
# # 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
# for cookie in d.get_cookies():
#     print("%s -> %s" % (cookie['name'], cookie['value']))
#
# d.quit()

#封装
#浏览器操作的封装
# from selenium import webdriver
# import time
# d = webdriver.Chrome()
#
# class Mylib(object):
#     def __init__(self,brower):
#         '''
#             初始化浏览器
#         '''
#         # 根据传入的参数创建对应的浏览器对象，前提是所有的浏览器驱动都已经正确安装
#         if brower == 'Chrome':
#             self.d = webdriver.Chrome()
#         ## 设置浏览器全屏
#         self.d.maximize_window()
#     url = 'http://www.baidu.com'
#     def delay(self):
#         '''
#             延迟等待
#         '''
#         self.d.implicitly_wait(5)
#     def open_url(self, url):
#         '''
#             访问网站
#         '''
#         self.d.get(url)
#         self.delay()
#         print('访问:%s成功'%url)
#
#     def __del__(self):
#         time.sleep(5)
#         self.d.quit()
#
# if __name__ == '__main__':
#     web = Mylib('Chrome')
#     web.open_url('http://www.baidu.com')
#     web.open_url('http://www.renren.com')

#定位操作的封装
# from selenium import webdriver
# import time
#
# class Mylib():
#     def __init__(self):
#         #初始化浏览器对象
#         self.d = webdriver.Chrome()
#         #窗口最大化
#         self.d.maximize_window()
#
#     def delay(self):
#         #延迟等待
#         self.d.implicitly_wait(5)
#     def open_url(self,url):
#         #访问网站
#         self.d.get(url)
#         self.delay()
#         print('访问：%s成功'%url)
#     def locate_element(self,locate_type,value):
#         return self.d.find_element(locate_type,value)
#     #return self.driver.locate_element(locate_type,value)
#
#     #必须调用python自带的__def__方法，不然执行不了close()，除非把close()写到main下面
#     def __del__(self):
#         time.sleep(5)
#         self.d.close()
# if __name__ == '__main__':
#     web = Mylib()
#     web.open_url('http://www.baidu.com')
#     web.locate_element('id','kw').send_keys('itcast')
#     web.locate_element('id','su').click()

#  unittest
from selenium import webdriver
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):#初始化格式
        self.d = webdriver.Chrome()

        self.d.get('http://localhost:8080/EasyBuy')#获取url
        self.d.maximize_window()#窗口最大化
    #@unittest.skip('不执行此用例')
    def test_01_login(self):#写用例(命名需要test开头_后面自定义：如 test_login)
        #点击登录
        self.d.find_element_by_xpath('/html/body/div[1]/div/span[2]/span/a[1]').click()
        time.sleep(3)
        #输入登录账号
        self.d.find_element_by_xpath('//*[@id="loginName"]').send_keys('admin')
        time.sleep(3)
        #输入登录密码
        self.d.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        time.sleep(3)
        #点击登录按钮
        self.d.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input').click()

    @unittest.skip('不执行此用例')

    def test_02_login(self):
        #点击登录
        self.d.find_element_by_xpath('/html/body/div[1]/div/span[2]/span/a[1]').click()
        time.sleep(3)
        #输入登录账号
        self.d.find_element_by_xpath('//*[@id="loginName"]').send_keys('易烊千玺')
        time.sleep(3)
        #输入登录密码
        self.d.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        time.sleep(3)
        #点击登录按钮
        self.d.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input').click()

    #@unittest.skip('不执行此用例')

    def test_seach(self):
        #搜索商品
        self.d.find_element_by_xpath('/html/body/div[4]/div[2]/form/input[1]').send_keys('香奈儿')
        #点击搜索按钮
        self.d.find_element_by_xpath('/html/body/div[4]/div[2]/form/input[2]').click()

    @unittest.skip('不执行此用例')
    def test_registe(self):
        #点击注册
        self.d.find_element_by_xpath('/html/body/div[1]/div/span[2]/span/a[2]').click()
        #输入登录用户名
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[2]/td[2]/input').send_keys('adgfrr')
        #输入密码
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[3]/td[2]/input').send_keys('555666')
        #输入确认密码
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[4]/td[2]/input').send_keys('555666')
        #输入真实姓名
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[5]/td[2]/input').send_keys('zhaozhao')
        #选择性别
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[6]/td[2]/input[2]').click()
        #点击注册
        self.d.find_element_by_xpath('//*[@id="register"]/table/tbody/tr[10]/td[2]/input').click()





    def tearDown(self):#释放缓存
        time.sleep(9)
        pass