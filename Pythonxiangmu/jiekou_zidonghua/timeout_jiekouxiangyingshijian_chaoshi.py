
#响应时间
import requests
import json

url = 'https://tianqiapi.com/api'

data = 'version=v6&appid=73691227&appsecret=123456'

#通过timeout设置接口响应的超时时间，单位为s，当请示响应时间大于设置的时间时则抛出异常
#response = requests.request('GET',url,params=data,timeout=0.1)
response = requests.get(url,params=data,timeout=0.1)
#设置SSL证书验证（verify参数）,默认是True，即验证当前网页是否有SSL证书，没有会报错
#response = requests.request('GET',url,params=data,verify=True)

#print(response.text.encode('utf8'))
print(json.dumps(response.json(),indent=4, ensure_ascii=False))

#通过elapsed方法获取接口请示响应时间
print(response.elapsed)

