''  # 随机输入 半径 求出 圆的面积

radius = int(input('请输入半径：'))
# 定义一个 可以输入 input()函数  用 int() 将其转换 为 int类型 赋值给 radius

def yuan_mianji(radius):  # 定义 函数 yuan_mianji()   radius（半径）
    mianji = 3.14 * radius * radius  # 圆的面积 = 3.14*半径乘2
    return mianji  # 返回结果


mianji = yuan_mianji(radius)  # 传参数
print(f'圆的面积为：{mianji}')  # 打印结果

'''
# 定义函数  接收一个list列表求里面 所有元素的和

def list_sum(L): # 定义函数 list_sum() 括号里面放的是要传进来的参数的名 
    result = 0  # 定义一个变量接收结果，
    for num in L: # for循环 L 将值赋予 num
        result = result + num # 
    return result # 返回结果 
L = [1, 3, 5, 7, 9, 11] # 列出一个 list 
result = list_sum(L) # 将 list 传入上面的函数 list_sum()
print(result) # 打印结果
'''

# 输入一个边长 求 长方形的 周长和面积
''' 
side = int(input('请输入边长：'))  
# 定义一个  可以输入的 input() 函数 用 int() 将其转换成 int(整数) 类型 赋值给 side（边长）
def perimeter_area(side): # 定义 函数 perimeter_area() 
    C = side* 4 # 长方形的  周长 = 边长 * 4
    S = side * side # 长方形的 面积 = 边长 * 边长
    return C,S # 返回 C 和 S 的结果
C,S = perimeter_area(side) # 调用函数 
print(f'已知边长{side}，求得周长等于{C}')
print(f'已知边长{side}，求得面积等于{S}')
'''

# 求 list 列表里面所有元素的平方的和
'''
L = [2,3,5,4,5,6] # 定义一个 list 列表 
def square_of_sum(L): # 定义函数 square_of_sum() 
    summ = 0 # 设置 变量 方便接收结果 和 进行计算
    for num in L: # for 循环 L 将值赋予 num 
        summ = summ + num * num # 计算 表达式
    return summ  # 返回 结果 summ
summ = square_of_sum(L) # 调用函数 
print(summ)
'''
#  定义一个函数 sub_sum() 这个函数接收一个列表作为参数
#  函数返回列表所有奇数项的和以及所有偶数项的和
'''
L = [1,1,3,4,1,3,5,2] # 定义一个 list 列表 作为数据
def sub_sum(L): #  定义一个函数 sub_sum()
    sum1 = 0 # 定义 sum1 变量 来接收 所有 偶数的和 的结果
    sum2 = 0 # 定义 sum2 变量 来接收 所有 奇数的和 的结果
    for num in L: # for 循环 L 这个 list(列表) 将取得的值 给到 num 
        if num % 2 == 0:  # if 条件判断  当 取得的 num %(取模，取余数) 2 ==（等于）0 时就是偶数 
            sum1 = sum1 + num # 当条件成立 就执行 sum1 = sum1 + num
        else: # 否则 就执行 sum2 = sum2 + num
            sum2 = sum2 + num
    return sum1,sum2 # 计算完成 返回 sum1 和 sum2 的 结果
sum1,sum2 = sub_sum(L) #调用函数 
print(f'所有偶数项的和{sum1}') # 打印偶数项结果
print(f'所有奇数项的和{sum2}') # 打印奇数项结果
'''
# 题目：
# 请实现函数func，
# 当参数类型为list时，返回list中所有数字类型元素的和，
# 当参数类型为tuple时，返回tuple中所有数字类型元素的乘积

# 需要使用函数 isinstance(x,y) 这个函数有两个参数 ，
#  x 为要判断的对象（list，变量）
#  y 为要判断的类型（int(整数)，str(字符串),float(小数)）
#  例子：x=100 isinstance(x,int) 结果为 True
#  思路 ： 首先要用 条件判断语句 if 结合 isinstance()函数 判断 传进去的 参数 符合 哪个条件 ，
# 再去写其中的条件表达式
'''
def func(L): #  L 要传进去的参数
    if isinstance(L,list): # 如果 L 为 list（列表） 则执行 if 语句内的代码块
        sum1 = 0 # 设置变量接受结果
        for num in L: # for循环 L  将值 给到 num
            if isinstance(num,int) or isinstance(num,float):
            # 判断 拿到的 num 是否是 int（整数） 或者 float（小数）
            # 如果是 就执行 代码 sum1 = sum1 + num
                sum1 = sum1 + num
        print(f'这个列表为list,所有元素的和={sum1}')
        # 打印结果   f'' 字符串输出格式之一
        return sum1
        # 返回结果
    elif isinstance(L,tuple): # 否则如果 L 为 tuple（元组），则执行 elif 内的代码块
        sum2 = 1 # 定义变量 接收结果
        for num in L : # 循环 L 将值 给到 num 
            if isinstance(num,int) or isinstance(num,float):
            # 判断 拿到的 num 是否是 int（整数） 或者 float（小数）
            # 如果是 就执行 代码 sum2 = sum2 *num
                sum2 = sum2 * num
        print(f'这个列表为tuple,所有元素的乘积={sum2}')
        # 打印结果
        return sum2
        # 返回结果
    else: # 当 L 既不是 list（列表） 也不是 tuple（元组）时 就执行 else 代码块
        print('无法识别数据类型')
L = ['a',2,3,4,5,1,'s'] # 定义list 列表
#L = ('x',1,2,3,4,5,6,7,'a') # 定义 tuple 元组
#L = {'Alice':45,'Bob':60,'Candy':80} # 
func(L)  # 将参数传入上面的 函数 ，调用函数 
'''

# 请定义一个 greet() 函数，
# 它包含一个默认参数，
# 如果没有传入参数，打印 Hello, world.，
# 如果传入参数，打印：Hello, 传入的参数内容
'''
def greet(name='world'):
    print('Hello,'+ name +'.')
greet()
greet('Alice')
'''

'''
def func(*args):
    print(f'args length = {args},args = {args}')
func(4,23,5,'a')
'''
# 请完善average()函数，
# 使得当可变参数长度为0的时候，也能正确返回结果
'''
def average(*args): # 定义函数
    sum = 0 # 设置变量接受结果
    if len(args) == 0: # 如果 参数 args 他的 长度len() ==(等于) 0  len()这个函数用来返回对象的长度
        return sum # 返回 sum 的结果
    for num in args: # 循环 args 将值赋予 num 
        sum += num # sum = sum + num  
    avg = sum / len(args) # avg = 6 / 3
    return avg # 返回 avg 的 结果  
a=average(1,2,3) # 调用函数 
print(a) #  打印结果
'''
# x = [1,23,4,4,1,2,3,12,12,23,4,54,54,5434,53] # len()
# print(len(x))

# 编写一个函数，
# 它接受关键字参数names，gender，age三个list
# 分别包含同学的名字、性别和年龄，
# 请分别把每个同学的名字、性别和年龄打印出来
'''
def info(**kwargs):
    names = kwargs['names']
    gender_list = kwargs['gender']
    age_list = kwargs['age']
    index = 0
    for name in names:1
        gender = gender_list[index]
        age = age_list[index]
        print(f'name:{name},gender:{gender},age:{age}')
        index += 1
info(names = ['Alice', 'Bob', 'Candy'], gender = ['girl', 'boy', 'girl'], age = [16, 17, 15])
'''
''
