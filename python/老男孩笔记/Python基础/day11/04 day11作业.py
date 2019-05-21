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
