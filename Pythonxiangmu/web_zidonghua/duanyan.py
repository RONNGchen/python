#断言
from selenium import webdriver
import unittest
import time

class test(unittest.TestCase):
    def testduanyan(self):
        self.d = webdriver.Chrome()
        #窗口最大化
        self.d.maximize_window()
        self.d.get('https://www.baidu.com')
        #等等3秒
        time.sleep(3)
        #在搜索框中输入“易烊千玺”
        self.d.find_element_by_id('kw').send_keys('易烊千玺')
        time.sleep(3)
        #点击搜索按钮
        self.d.find_element_by_id('su').click()
        time.sleep(3)
        #断言（断言是unittest自带的方法，必需与unittest一起用）
        self.assertEqual(self.d.find_element_by_xpath('//*[@id="su"]').get_attribute('value'),u'百度','百度失败')
        #判断bool值为True或为False
        self.assertIsNotNone(self.d.find_element_by_xpath('//*[@id="su"]'))
        time.sleep(5)


#判断断言的方法
#断言，判断元素是否对应
        #self.assertEqual(self.driver.find_element_by_name('keyWord').get_attribute('value'),'洗面奶','搜索失败')
#判断bool值为True或为False
        #self.assertTrue(self.driver.find_element_by_class_name('s_btn').is_enabled())
#判断元素是否存在
        #self.assertIsNotNone(self.driver.find_element_by_name('keyWord'))
