#计算1-10的整数求和
# b = [1,2,3,4,5,6,7,8,9,10]
# s = 0
# for i in b:
#     s = s + i
# print(s)

#多个变量赋值
# a = b = c = 1
# print(a,b,c)
# d,e,f =1,2,"hello"
# print(d,e,f)

# 列表转集合（去重）
# a = [6,7,7,8,8,9]
# b = set(a)
# x = list(b)
# print(list(x))

#字符串操作
# s = "hello"
# a = "world"
# print(s+a)
# print(s*3)

##字符串切片
# s1 = "hello world!"
# print(s1[1:4])#索引1至索引4，但不包含索引4
# print(s1[4:])#索引4至最后一个元素，包含最后一个函数
# print(s1[:4])#索引0至索引4，但不包含索引4
# print (s1[4])#取对应第几个字符
# print(s1[1:-1])#索引1至最后一个元素，不包含最后一个元素
# print(s1[::-1])#步长：比如lst[a:b:n]--对于lst序列，从索引a至索引b,但不包含索引b,
#                 #其中间隔为n（步长）
# print(s1[6:3:-1])


#len():求长度
# a = [10,20,30,40,50,60,70]
# print(len(a))

#append():列表末尾添加新的元素
# a = [10,20,30,40,50,60,70]
# a.append(100)
# print(a)

#extend():在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# a = [10,20,30,40,50,60,70]
# a.extend(['a,b,c'])
# print(a)

#insert():
# a = [10,20,30,40,50,60,70]#这里是索引2的位置，插入100
# a.insert(2,100)
# print(a)

#pop:删除，不填写数字默认删除末尾，填写数字删除指定数字
# a = [10,20,30,40,50,60,70]
# a.pop(2)
# print(a)

#remove:删除一个数据,无返回值
# a = [10,20,30,40,50,60,70]
# a.remove(10)
# print(a)

#sort():从小到大排序
# a = [1,2,3,4]
# b = [8,5,7,4]
# b.sort()
# print(b)
#a.sort(reverse = True)#reverse()从大到小排序（打印的结果是倒序）
                     # 解决办法：将a.reverse()改成a.sort(reverse=True)
#print(a)

# #range()函数
# a = range(10)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]从0开始，产出数据到10，不包括10，
#              # 间隔为1（间隔=步长1）
# print(list(a))
# #给个开始的起步的参数1
# a = range(1,10)#设置从1开始，不包括10（也就是结尾），结果为[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(a))
# #间隔或步长为2
# a = range(1,10,2)#设置从1开始，不包括10，间隔为2，结果为[1, 3, 5, 7, 9]
# print(list(a))

#in not in(有就是True,没有就是Flase)
# a = range(1,10,2)#结果为[1, 3, 5, 7, 9]
# print(2 in a)#False
# print(3 in a)#True
# print(2 not in a)#True 因为2不在上面数字结果里，所以假设成立，就为True

#首先我用一个range生成一个列表,其中包含0~9 10个元素
# list1 =list(range(10))
# # #使用range的方式进行遍历：
# for i in range(len(list1)):
#   print(list1[i])
# #当然这种情况我们一般都是直接使用 for value in list1 就可以了，如果使用切片，访问列表的一部分
# for i in range(int(len(list1)/2)):
#   print(list1[i])  #这样我们就可以得到列表中前一半元素，其他部分同理

#字典：key 和value一一对应,Key必须是唯一的
#dict
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name':'john', 'code':6734, 'dept': 'sales'}
# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

#if语句
# age = 30
# if age > 25:
#     print("you are too old!")
#if...else..语句
# age = 10
# if age > 25: #(一个判断条件)
#     print("you are too old!")
# else:
#     print("you are so young!")
# #if...elif...语句
# age = 12
# if age > 25: #(第一个判断条件)
#     print("you are too old!")
# elif age < 10: #(第二个判断条件)
#     print("it's a boy")
# else:
#     print("you are so young!")

#for 语句
# n = "hello world!"
# for i in n:
#     print(i)
# l = ['he','12',12,"hello","22"]
# for i in l:
#     print(i)

#range()    range(1,100,2)起点，终点，步长
# s = 0
# for i in range(10):
#     s+=i #s = s + i
# print(s)
#
# #如何把0-100中的奇数累加？
# s = 0
# for i in range(100):
#     if i % 2:
#         s += i
#     else:
#         continue #continue是跳出本次循环，继续下一个
# print(s)
# #当s大于1000时，如何结束for循环
# s = 0
# for i in range(100):
#     if i % 2:
#         s += i
#         if s > 1000:
#             break
#     else:
#         continue
# print(s)

#while语句
#如何实现1到99中的奇数累加，当总和大于1000时结束循环？
# s = 0
# i = 1
# while i < 100:
#     if i % 2:
#         s = s + i   #当s=0,i=1时，从0加1一直加到奇数63时大于1000跳出整个循环
#         if s > 1000:
#             break
#     i = i + 1
# print(s)
# #占位符：pass   （不起任何作用，只是占个坑）
# # s = 0
# # i = 1
# while i < 100:
#     if i % 2:
#         s = s + i
# #     else:
# #         pass
# #     i = i +1
# # print(s)
# #
# #逻辑运算
# #1.与
# a = 3
# b = 5
# if a > 0 and b >0:
#     print(a+b)
#2.或
# a = 3
# b = 5
# if a < 0 or b < 0:
#     print(a-b)
# #3.非
# a = 3
# b = 5
# c = 0
# if not c: #[当C等于0时，返回true（1）,打印结果；当C不等于0时返回
#           # false没有打印结果]
#     print(c+100)

#随机生成一个整数，如果大于该数提示太大了，如果小于该数提示太小了
# key = 7
# while 1:
#     guess = input("请输入一个1-20的整数：")
#     guess = int(guess)
#     if guess > key:
#         print("输入的太大了")
#     elif guess < key:
#         print("输入的太小了")
#     elif guess == key:
#         print("恭喜猜对了")
#         break

#类的封装
# #例子：
# class People:
#     def hand(self): #self 实例方法，只能被实例对象调用; 不用self 就是普通方法
#                      #def 是函数
#         print("这是我朋友的手")
#     def foot(self):
#         print("这是我朋友的脚")
# if __name__ == '__main__':#主方法
#     #创建一类的实例
#     goodfriend = People()
#     #调用对象里的方法
#     print(goodfriend.hand())
#     print(goodfriend.foot())
# #一个类创建多个实例
# if __name__ == '__main__':
#    # 创建一类的实例：goodfriend
#     goodfriend = People()
#    # 创建一类的实例：boyfriend
#     boyfrind = People()
#    # 调用对象里的方法
#     print(goodfriend.hand())
#     print(goodfriend.foot())
#     print (boyfrind.hand())
#     print (boyfrind.foot())
#
# class Student:
#     def xiaohong(self):
#         print("我叫小红")
#     def xiaoming(self):
#         print("我叫小明")
#     def xiaowang(self):
#         print("我叫小王")
# a = Student()
# print(a.xiaowang())

#self 通用变量
#全局变量：是在函数外引用
#局部变量：是在函数内引用

# class Count():
#     def add(self,a,b):
#         return  a+b
#     def acc(self,a,b):
#         return  a-b
#     def aff(self,a,b):
#         return self.add(a,b)*self.acc(a,b)
# a = Count()
# print(a.aff(3,1))
# print(a.add(4,2))
# print(a.acc(10,11))

# class People():
#     def hand(self):
#         h = "这是我朋友的手"
#         return(h)
#     def foot(self):
#         f ="这是我朋友的脚"
#         return(f)
# a = People()
# print(a.hand())
# print(a.foot())

#类的初始化
# class People():
#    def __init__(self):
#        self.friend = "amy"
#        self.live = "happy"
#        print("start!")
#    def hand(self):
#        h = "这是我朋友的手：%s wants to be %s"%(self.friend, self.live)
#        return(h)
#    def foot(self):
#        f = "这是我朋友：%s wants to be %s"%(self.friend, self.live)
#        return(f)
# a = People()
# print(a.friend)
# print(a.live)
#
# class People():
#     def __init__(self, a="amy", b="happy"):
#         self.friend = a
#         self.live = b
#     def hand(self):
#         h = "这是我朋友的手：%s want to be %s"%(self.friend, self.live)
#         return (h)
#     def foot(self):
#         f = "这是我朋友的脚:%s wants to be %s"%(self.friend, self.live)
#         return(f)
# a = People()
# b = People("boy")
# c = People(b = "live")
# print(a.hand())
# print(b.hand())
# print(c.hand())

#参数作用域
a = 1 #全局作用
class People():
    b = 2  #整个类有效
    def __init__(self):
        self.c = 3 #整个类有效
        d = 4      #本方法有效
        print(d)
    def add(self):
        e = 5      #本方法有效
        self.f = 6 #整个类有效
        return  e+self.f
    def aee(self):
        g = 7
        return  a+self.b+self.c+self.f+g
e = People()
print(e.add())
print(e.aee())