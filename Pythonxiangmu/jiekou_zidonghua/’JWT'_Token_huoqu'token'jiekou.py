#关于token：
import requests
import json
import jsonpath
#生成token接口
url = "http://localhost:8000/login"
# python 字典 --》 json
data = {
    "username": "admin",
    "password": "admin"
}
res = requests.post(url=url, json=data)
#使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
# 返回值是个列表 所以要加索引
# print(jsonpath.jsonpath(res.json(), "$..token")[0])

print("*************************************************************")


# #生成token接口(方法二)
# url = 'http://localhost:8000/login'
# #输入登录数据
# data = 'username=admin&password=admin'
# #响应的请求方式，添加数据
# response = requests.post(url,params=data)
# #indent=2,表示打印的结果缩进2个空格，ensure_ascii=False防止乱码
# print(json.dumps(response.json(),indent=2, ensure_ascii=False))
# # 返回值如果是个列表 所以要加索引
# # print(jsonpath.jsonpath(res.json(), "$..token")[0])

print("*************************************************************")

#登录jwt接口(方法一)
urllogin = "http://localhost:8000/auth/hello"
#使用jsonpath来提取
token = "Bearer " + jsonpath.jsonpath(response .json(), "$..token")[0]
headers = {
    "Authorization":token
}
response = requests.get(urllogin,headers=headers)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))

print('************************************************************')

# #登录jwt接口(方法二)
# #生成登录接口
# urllogin = "http://localhost:8000/auth/hello"
# #输入登录数据
# data = 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTExMzQ2NjYsImlkIjoiYWRtaW4iLCJvcmlnX2lhdCI6MTY1MTEzMTA2Nn0.jX4h_WZgVXGEyScMo-TDV_sl1N9EKntwdbiITG2XSeQ'
# #响应的请求方式，添加数据
# response = requests.get(urllogin,params=data)
# print(json.dumps(response.json(),indent=4,ensure_ascii=False))

#上传文件接口
url='http://httpbin.org/post'
# 准备一个文件
file = open("D:\\abc.txt", "rb")
# 参数
files = {
    "file": file
}
res2 = requests.post(url=url, files=files)
#print(res.json())
print(json.dumps(res2.json(), indent=4, ensure_ascii=False))
