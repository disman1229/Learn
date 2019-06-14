# 1.整理函数相关知识点,写博客
# 2.写函数,接收n个数字,求这些参数数字的和.(动态传参)
# def func(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(func(1,2,3,4,6,5,6))

# def func(*args):  # args是元祖,可以迭代
#     return sum(args)
# print(func(1,2,3,4))

# print(sum([1,2,3,4,4,3,7])) # sum中可以直接接收一个可迭代对象.他会把这个可迭代对象进行迭代.把每个元素累加

# 3.读代码,回答:代码中,打印出来的值a,b,c分别是什么?为什么?
# a = 10
# b = 20
# def test5(a,b):
#     print(a,b)
# c = test5(b,a)
# print(c)
# a=20,b=10,c=None


# 4.读代码,回答:代码中,打印出来的值a,b,c分别是什么?为什么?
# a = 10
# b = 20
# def test5(a,b):
#     a = 3
#     b = 5
#     print(a,b)
# c = test5(b,a)
# print(c)
# print(a,b)

# 5.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
# 列如:传入函数两个参数[1,2,3](22)(33),最终args为(1,2,3,22,33)
# def func(*args):
#     print(args)
# func(*[1,2,3],(22),(33))

# 6.写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面
# 例如:传入函数两个参数{'name':'disman'},{'age':34}
# def func(**kwargs):
#     print(kwargs)
# func(**{'name':'disman'},**{'age':34})

# 7.下面代码成立吗?如果不成立为什么报错?怎么解决?
# 7.1
# a = 2
# def wrapper():
#     print(a)
# wrapper()
# 成立  ,结果为2

# 7.2
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()
# 不成立,局部变量不能修改全局变量,需要加入global

# 7.3
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()
# 成立,结果为1

# 7.4
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a # 需要找上次变量a
#         a += 1
#         print(a)
#     inner()
# wrapper()
# 不成立,局部变量内没有找到变量a,需要加入nonlocal,找上一层变量a

# 8.写函数,接收两个参数并把比较小的数返回
# def func(a,b):
#     return a if a < b else b
# print(func(1,2))


# 9.写函数,接受一个参数(此参数类型必须是可迭代对象),将可迭代对象每个元素以"_"相连接,形成新的字符串,并返回
# 例如:传入可迭代对象为[1,"鲁班七号",2,"程咬金"]返回结果为"1_鲁班七号_2_程咬金"

# def func(lst):
#     s = ""
#     for el in lst:
#         s = s + str(el) + "_"
#     return s.rstrip("_")
# print(func([1,"鲁班七号",2,"程咬金"]))

# 10.写函数,传入n个数,返回字典{"max":最大值,"min":最小值}
# 例如:min,max(2,5,7,8,4)返回{"max":8,min:2}(此题用到max(),min()内置函数)
# def func(*args):
#     return {"max":max(args),"min":min(args)}
# print(func(2,3,4,1,567,234,123,6,457435,212,3123))

# 11.写函数,传入一个函数n,返回n的阶乘
# 例如:cal(7) 计算7*6*5*4*3*2*1
# def func(n):
#     sum = 1
#     for i in range(n):
#         sum = sum * (i+1)
#     return sum
# print(func(12))

# def func(n):
#     sum = 1
#     while n >= 1:
#         sum = sum * n
#         n -= 1
#     return sum
# print(func(5))

# 12.写函数,返回一个扑克列表,里面有52项,每一项是一个元祖
# 例如:[("红心",2),("草花",2)...("黑桃",1)]
# def func():
#     result = []
#     huase = ["红心","黑桃","草花","方片"]
#     dianshu = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
#     for hua in huase:
#         for dian in dianshu:
#             result.append((hua,dian))
#     return result
# print(func())


# 13.有如下函数:
# 你可以任意添加代码，用两种或以上方法，执行inner函数
# def wrapper():
#     def inner():
#         print(666)
#     inner()
# wrapper()

# def wrapper():
#     def inner():
#         print(666)
#     return inner()
#ret = wrapper()
# ret()

# def wrapper():
#     def inner():
#         print(666)
#     def func2():
#         inner()
#     func2()
# wrapper()

# 14.相关面试题（先在纸上写好答案，然后在运行）
# 1.函数如下：
# def calc(a,b,c,d=1,e=2):
#     return (a+b)*(c-d)+e
# 请分别写出下列标号代码输出的结果，如果出错请写出Error
# print(calc(1,2,3,4,5))    # 结果2
# print(calc(1,2))    #结果Error
# print(calc(e=4,c=5,a=2,b=3))    # 结果24
# print(calc(1,2,3))  # 结果8
# print(calc(1,2,3,e=4))  # 结果10
# print(calc(1,2,3,d=5,4))    # 结果Error

# 2.(此题有坑)下面代码打印的结果分别是？
# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList("a")
# print("list1%s" %list1)
# print("list2%s" %list2)
# print("list3%s" %list3)

# 3.写代码完成99乘法表（升级题）
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%sx%s=%s" %(i,j,i*j),end=" ")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()