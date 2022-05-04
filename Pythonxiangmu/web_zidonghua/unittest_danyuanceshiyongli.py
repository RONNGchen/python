#  unittest(易买网的单元测试)
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
        self.d.quit()
#添加主方法，可以不用加，不改变运行结果
# if __name__ == '__main__':
#     unittest.main()

#三大框架：1-setup()  2-def test_jik() 用例，这里必须是test开头才能运行，3-teardown()关闭资源