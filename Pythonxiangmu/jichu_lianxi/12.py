# from selenium import webdriver
# import time
# d = webdriver.Chrome()
# d.maximize_window()
# d.get('https://www.baidu.com/')
# d.find_element_by_id('kw').send_keys('肖战身高')
# time.sleep(2)
# d.find_element_by_xpath('//*[@id="su"]').click()
# d.window_handles
# time.sleep(3)
# d.find_element_by_xpath('//*[@id="1"]/div/section/div[2]/div[1]/div/section[2]/div/div[2]/a').click()
# d.find_element_by_xpath('//*[@id="1"]/div/section/div[2]/div[1]/div/section[1]/div/div[2]/a').click()
# time.sleep(2)
# d.switch_to.window(d.window_handles[1])
# d.find_element_by_xpath('//*[@id="kw"]').send_keys('微博')
#
# d.find_element_by_xpath('//*[@id="su"]').click()
# d.switch_to.window(d.window_handles[0])

#案例
# from selenium import webdriver
# import time
# d=webdriver.Chrome()


# try:
#     f = open("d:\\test123.txt","r")
#     f.read()
# except IOError:
#     print('读取文件时出现异常')
# else:
#     print("文件写入成功")

# from selenium import webdriver
# import time
# import xlrd
#
# d = webdriver.Chrome()
# d.maximize_window()
#
# #读取文件
# data = xlrd.open_workbook('C:\\Pythonxiangmu\\excel_biaoge(shujufenli)\\testcase02.xls')
# #读取第一个工作表
# table = data.sheet_by_name('Sheet1')
# #使用for循环输出所有数据
# list=[]
# for i in range(0,table.nrows):
#      # 读取excel第一行
#     list = table.row_values(i)
#     break
# print(list)
# time.sleep(3)
# #通过索引在excel表中获取百度URL
# d.get(list[0])
# time.sleep(3)
# #通过xpath获取点击的字段
# d.find_element_by_xpath(list[2]).click()
# time.sleep(3)
# list=[]
# for i in range(1,table.nrows):
#        # 读取excel第二行
#     list = table.row_values(i)
#     break
# print(list)
# #跳转到清空输入框
# d.find_element_by_xpath(list[0]).clear()
# time.sleep(3)
# #跳转到 "通过索引在列表中获取百度输入框元素并输入要搜索的字段"
# d.find_element_by_xpath(list[1]).send_keys(list[2])
# time.sleep(3)
# #通过索引在列表中获取百度点击“百度一下”元素并点击
# d.find_element_by_xpath(list[3]).click()
# time.sleep(3)

import requests
import json

url = 'http://localhost:8080/EasyBuy/Login'
data = 'loginName=admin&password=123456&action=login'
aaa=requests.post(url,params=data)
print(json.dumps(aaa.json(),indent=2,ensure_ascii=False))

url='http://localhost:8000/login'
data={
    'username':'admin',
    'password':'admin'
}
res=requests.post(url,json=data)
print(json.dumps(res.json(),indent=2,ensure_ascii=False))

