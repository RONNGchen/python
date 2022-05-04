#接口自动化数据分离
# import requests
# import xlrd
# #方法一：
# #实时查询天气接口
# #读取文件
# data=xlrd.open_workbook('C:\\Pythonxiangmu\\excel_biaoge(shujufenli)\\testcase03.xls')
# #读取第一个工作表
# table=data.sheet_by_name('Sheet1')
# #新建一个空的list，装数据
# list=[]
# #使用for循环输出所有数据
# for i in range(0,table.nrows):#table.nrows代表工作表中的行
#      # 读取excel表第一行数据
#     list = table.row_values(i)
#     break
# print(list)
# #通过索引获取列表第一个元素
# url = list[0]
# #通过索引获取列表第二个元素
# data = list[1]
# res =requests.get(url=url,params=data)
# print(res.json())

#方法二：
import requests
import xlrd
import json   #有json，表格里的为{"username": "admin", "password": "admin"}需要将字符串转换为字典

#jwt生成token接口
#读取文件
data='C:\\Pythonxiangmu\\excel_biaoge(shujufenli)\\testcase03.xls'
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#新建一个空的list，装数据
list = []
#使用for循环输出所有数据
for i in range(1,table.nrows):
# 读取excel表第二行数据
    list=table.row_values(i)
    break
# 打印第一行
#print(list)
# 获取URL接口地
url=[0]
# 获取接口参数json字符串，并把字符串转成python dict
data = json.locals(list[1])
#print(url,data)
# 提交POST请求
res= requests.post(url=url,data=json)
# 读取返回的JSON
print(res.json())