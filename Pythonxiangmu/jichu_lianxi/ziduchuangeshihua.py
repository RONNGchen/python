# 字符串格式化三种方式
# 第一种  %

# print("我叫%s,今年%g岁" % ('小明', 34))
# name = "李四"
# age = 222
# print("我叫%s,今年%d岁" % (name,age))

# 第二种 f ,要先设置参数，直接通过变量名引用
"""
name = '小红'
age = 18
print(f"我叫{name},今年{age}岁")
"""
# 第三种  使用函数 .format() 可以设置参数
# print("我叫{n},今年{a}".format(n='李四', a=66))

# 通过字典（dict）设置参数
dictname = {"name": "张三", "age": 40}
print("我叫{name},今年{age}".format(**dictname))

# 通过列表(list)索引设置参数，'0'是必须的
listname = ["王五", 19]
print("我叫{0[0]},年龄{0[1]}".format(listname))
