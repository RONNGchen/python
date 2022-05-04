#自动化接口测试
#方法一：
import requests
import json


url = 'http://localhost:8080/EasyBuy/Login'

data = 'loginName=admin&password=123456&action=login'
#使用data来进行传递
headers = {
     'Content-Type': 'application/x-www-from-urlencoded'
}

#response = requests.request('POST',url,headers=headers,params=data)
response = requests.post(url,headers=headers,params=data)

# print(response.text.encode('utf8'))
#print(response.json())

#indent=4,表示打印的结果缩进2个空格，ensure_ascii=False防止乱码
print(json.dumps(response.json(),indent=4, ensure_ascii=False))

#方法二：
import requests
import json

url = 'http://localhost:8080/EasyBuy/Login'

data = 'loginName=admin&password=123456&action=login'
#响应的请求方式，添加数据
response = requests.post(url,params=data)
#indent=4,表示打印的结果缩进2个空格，ensure_ascii=False防止乱码
print(json.dumps(response.json(),indent=2, ensure_ascii=False))

import requests
import json

url ='http://localhost:8080/EasyBuy/Register'
#填写接口数据,如果有些接口数据不是必要的也需要写上如:'identityCode=&email=&mobile='
data = 'action=saveUserToDatabase&userName=liyan&loginName=wuzhao&sex=0&password=123456&identityCode=&email=&mobile='
#响应的请求方式，添加数据
response = requests.post(url,params=data)
#indent=4,表示打印的结果缩进2个空格，ensure_ascii=False防止乱码
print(json.dumps(response.json(),indent=2,ensure_ascii=False))

