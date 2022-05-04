from selenium import webdriver
import unittest
import time

class Test(unittest.TestCase):
     #在一个类中只会在所有测试用例运行前调用一次
     @classmethod
     def setUpClass(cls):
         cls.d = webdriver.Chrome()
         cls.d.get('https://www.baidu.com')
         cls.d.maximize_window()
    #@unittest.skip('不执行此用例')
     def test1(self):
        self.d.find_element_by_id('kw').send_keys('china')
        #self.driver.find_element_by_name('wd').send_keys('中国')
        self.d.find_element_by_id('su').click()
        time.sleep(3)
        #回退到上一步
        self.d.back()
        time.sleep(3)
     def test2(self):
         # 获取‘新闻’的元素并打新闻页面
        self.d.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
         #暂停三秒
        time.sleep(3)
         #获取所有窗口
        self.handles=self.d.window_handles
         #切换到新窗口
        self.d.switch_to.window(self.handles[1])
         #暂停三秒
        time.sleep(3)
         #在新闻页面搜索‘国内新闻’
        self.d.find_element_by_id('ww').send_keys('国内新闻')
        self.d.find_element_by_xpath('//*[@id="s_btn_wr"]').click()
         #在所有测试用例运行后调用一次
     @classmethod
     def tearDownClass(cls):
         time.sleep(5)
         cls.d.quit()

if __name__ == '__main__':
    unittest.main()




