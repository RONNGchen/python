from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome()
url = 'http://localhost:8080/EasyBuy'
#数组
object = [{
    'loginNames':'admin',
    'passwords':'123456'
},{
    'loginNames':'admin',
    'passwords':'123456'
}]
def loads():
    try:
        d.maximize_window()
        d.get(url)
        time.sleep(2)
    except Exception:
        print("网页不存在")
def login_test(loginNames,passwords):
    #点击登录
    d.find_element_by_xpath('/html/body/div[1]/div/span[2]/span/a[1]').click()
    time.sleep(3)
    #输入登录账号
    d.find_element_by_xpath('//*[@id="loginName"]').send_keys(loginNames)
    time.sleep(3)
    #输入登录密码
    d.find_element_by_xpath('//*[@id="password"]').send_keys(passwords)
    time.sleep(3)
    #点击登录按钮
    d.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input').click()
    time.sleep(3)
    if d.current_url != url:
        print('进入用户登录页面')
        #退出登录
        d.find_element_by_xpath('/html/body/div[1]/div/span[2]/span[3]/a').click()

loads()

for i in object:
        login_test(i['loginNames'],i['passwords'])

d.quit()
