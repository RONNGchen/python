from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/EasyBuy")
        self.driver.maximize_window()
        time.sleep(3)

    def test_login(self):
        #点击登录按钮
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/span[2]/span/a[1]').click()
        time.sleep(3)
        #输入登录帐号
        self.driver.find_element(By.ID,'loginName').send_keys('admin')
        time.sleep(3)
        #输入登录密码
        self.driver.find_element(By.NAME,'password').send_keys('123456')
        time.sleep(3)
        #点击登录按钮登录
        el=self.driver.find_element(By.CLASS_NAME,'log_btn').click()
        #断言
        #self.assertTrue(el.is_enabled(),"登录成功")

    #@unittest.skip('不执行此用例')
    def test_search(self):
        #在搜索内搜索商品
        self.driver.find_element(By.XPATH,'//html/body/div[4]/div[2]/form/input[1]').send_keys('香水',Keys.ENTER)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

#方法一：
# if __name__ == '__main__':
#     unittest.main()

#执行测试套用例不能用右键unittest执行，不然会重复执行所有用例与控制台打印的执行用例条数不对应

#方法二：
#创建一个测试套件，再通过unittest.TestLoader()创建加载对象，加载测试用例类
#suite=unittest.TestLoader().loadTestsFromTestCase(Test)
#使用TextTestRunner执行测试用例,设置verbosity设定对每一个测试方法产生测试结果,run中传入要执行的测试套件
#unittest.TextTestRunner(verbosity=2).run(suite)

#方法三：
# testunit = unittest.TestSuite()
# testunit.addTest(Test("test_search"))
# #添加多个测试用例（列表中为用例方法名）
# #testunit.addTest(Test(["test_search","test_login"]))
# unittest.TextTestRunner().run(testunit)