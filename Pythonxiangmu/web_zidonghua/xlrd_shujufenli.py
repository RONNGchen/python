#UI自动化数据分离(数据驱动/关键字驱动)

from selenium import webdriver
import time
import xlrd

d = webdriver.Chrome()
#窗口最大化
d.maximize_window()
#读取文件
data=xlrd.open_workbook("C:\\Pythonxiangmu\\excel_biaoge(shujufenli)\\testcase01.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for i in range(0,table.nrows):#table.nrows代表工作表中的行
    # 读取excel第一行
    list = table.row_values(i)
    break
print(list)
time.sleep(3)
#通过索引在excel表中获取百度URL
d.get(list[0])
time.sleep(3)
#通过索引在列表中获取百度输入框元素并输入要搜索的字段
d.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
#通过索引在列表中获取百度点击“百度一下”元素并点击
d.find_element_by_id(list[7]).click()
time.sleep(3)
list=[]
for i in range(1,table.nrows):
    # 读取excel第二行
    list = table.row_values(i)
    break
print(list)
#跳转到“百度首页”
d.find_element_by_css_selector(list[0]).click()
time.sleep(3)
d.close()