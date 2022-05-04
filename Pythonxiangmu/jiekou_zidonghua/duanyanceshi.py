#断言测试（断言要和unittest结合一起用）
import requests
import unittest
class EasyBuyLogin(unittest.TestCase):
    #易买网登录
    def test01(self):
        url='http://localhost:8080/EasyBuy/Login'
        data = 'loginName=admin&password=123456&action=login'
        headers={
            'Content-Type': 'application/x-www-from-urlencoded'
        }
        response=requests.post(url,headers=headers,params=data)
        #print(response.text.encode('utf8'))
        #print(response.json())
        #获取返回的结果
        print(response.text)
        #获取状态码
        result=response.json()['status']#status:断言结果
        print(result)
        #断言
        self.assertEqual(1,result)
        self.assertIn('登陆成功',response.text)
        self.assertTrue('操作成功'in response.text)
if __name__ == '__main__':
    unittest.main()