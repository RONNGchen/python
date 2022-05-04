from Lib import HTMLTestRunnerCN
import unittest

#文件路径
#运行脚本路径
Testcase_dir = 'C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test'
#覆盖该文件路径下的文件                       #运行脚本路径    运行脚本文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'danyuantest.py')
# 定义报告存放路径
filename = "C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\result.html"
    # 定义报告存放路径，如果没有，创建
#打开定义报告
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
# 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()