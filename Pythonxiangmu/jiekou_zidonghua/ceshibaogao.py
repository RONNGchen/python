#接口测试报告
import requests
import unittest
import json
from Lib import HTMLTestRunnerCN

class interfacetest01(unittest.TestCase):
    #实时天气查询接口
    url = 'http://localhost:8080/EasyBuy/Login'
    data = 'loginName=admin&password=123456&action=login'
    response=requests.post(url,params=data)
    print(response.json())

#文件路径
#运行脚本路径
aaa = 'C:\\Pythonxiangmu\\jiekou_zidonghua'
#覆盖该文件路径下的文件                  #运行脚本路径 运行脚本文件
dis = unittest.defaultTestLoader.discover(aaa,'ceshibaogao.py')
# 定义报告存放路径
filename = 'C:\\Pythonxiangmu\\ceshibaogao\\jiekou_ceshibaogao.html'
    # 定义报告存放路径，如果没有，创建
#打开定义报告
fp = open(filename, 'wb')
# 定义测试报告
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="天气接口")
# 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()