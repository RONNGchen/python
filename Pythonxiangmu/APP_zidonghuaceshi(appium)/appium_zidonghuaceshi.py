#APP自动化测试（以模拟器为例子）
from appium import webdriver
import time

# 启动参数
desired_caps={}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'#手机版本号
desired_caps['deviceName'] = '127.0.0.1:62001'#cmd窗口用"adb devices"获取的信息;手机平台的名称

# app的信息
desired_caps['appPackage'] = 'com.android.settings'#APP包名
#最好输入appActivity的完整名称，有些app不输入完整的名称执行脚本会报错
desired_caps['appActivity']='.Settings'
#unicode设置(允许中文输入)
desired_caps['unicodeKeyboard'] = True
#键盘设置(允许中文输入)
desired_caps['resetKeyboard'] = True
time.sleep(3)
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)               #4723(端口号)  wd(代表驱动)  hub(代表中心节点又叫主节点)
driver.quit()



# from appium import webdriver
# import time
#
# # 启动参数
# desired_caps={}
# # 设备信息
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'#手机版本号
# desired_caps['deviceName'] = '127.0.0.1:62001'#cmd窗口用"adb devices"获取的信息;手机平台的名称
#
# # app的信息
# desired_caps['appPackage'] = 'com.sankuai.meituan'#APP包名
# #最好输入appActivity的完整名称，有些app不输入完整的名称执行脚本会报错
# desired_caps['appActivity']='com.sankuai.meituan.activity.MainActivity'
# #unicode设置(允许中文输入)
# desired_caps['unicodeKeyboard'] = True
# #键盘设置(允许中文输入)
# desired_caps['resetKeyboard'] = True
# time.sleep(3)
# # 声明driver对象
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# time.sleep(3)               #4723(端口号)  wd(代表驱动)  hub(代表中心节点又叫主节点)
# driver.quit()