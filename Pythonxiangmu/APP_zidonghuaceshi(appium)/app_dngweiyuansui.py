#APP自动化测试（以模拟器为例子）
#元素定位：三种（id，class，xpath)

from appium import webdriver
import time

# 启动参数
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'#手机版本号
desired_caps['deviceName'] = '127.0.0.1:62001'#cmd窗口用"adb devices"获取的信息;手机平台的名称
desired_caps['appPackage'] = 'com.android.settings'#APP包名
#最好输入appActivity的完整名称，有些app不输入完整的名称执行脚本会报错
desired_caps['appActivity'] = '.Settings'
#unicode设置(允许中文输入)
desired_caps['unicodeKeyboard'] = True
#键盘设置(允许中文输入)
desired_caps['resetKeyboard'] = True
time.sleep(3)
# 生成一个driver对象
driver =  webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(3)
#查看WLAN
driver.find_element_by_id('android:id/title').click()
time.sleep(3)
#回退到设置页面
driver.find_element_by_id('android:id/up').click()
time.sleep(3)
#打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
driver.tap([(87,505),(141,542)],500)#500是延续的时间
time.sleep(3)
#返回到设置页面
driver.find_element_by_id('android:id/up').click()
time.sleep(3)
#关闭驱动
driver.quit()
