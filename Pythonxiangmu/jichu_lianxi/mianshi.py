#面试小问题
# 字典（dict）合并
# d1 = {'name': 'revotu', 'age': 99}
# d2 = {'age': 24, 'sex': 'male'}
# 第一种方法
# d = {}
# d.update(d1)
# d.update(d2)
# print(d)
# 第二种方法  先copy 再更新
# d = d1.copy()
# d.update(d2)
# print(d)
# 第三种方法    方法3，字典构造器
# d = dict(d1)
# d.update(d2)
# print(d)

# 列表（list） 合并
# alist = [1, 2, 3]
# blist = ['zhangsan', 'pythontab', 'lisi']
# 第一种方法
# clist = alist + blist
# print(clist)
# 第二种方法
# alist.extend(blist)
# print(alist)

# 去除字符串空格
a = ' ab c '
# 去掉开头和结尾的空格 strip()  去掉开头的空格 lstrip()
# print(a.strip())
# 去除字符串结尾的空格
# print(a.rstrip())
# 去掉全部空格
# print(a.replace(" ","")

# list 列表排序
a = [1,5,6,8,8,9,2,1,3,5]
x = set(a)   #set集合、去重
c = list(x)  #排序[]
print(c)


