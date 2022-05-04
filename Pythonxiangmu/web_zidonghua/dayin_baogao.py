from Lib import HTMLTestRunnerCN
import unittest

#文件路径
Testcase_dir = 'C:\\Pythonxiangmu\\web_zidonghua'
#覆盖该文件路径下的文件                       #运行脚本路径    运行脚本文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'liuluanqi.py')
# 定义报告存放路径
filename = "C:\\Pythonxiangmu\\ceshibaogao\\liuluanqi.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='登录测试', description="用户登录并搜索商品：")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()