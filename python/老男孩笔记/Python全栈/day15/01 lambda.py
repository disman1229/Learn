
# 普通正常函数
# def func(n):
#     return n * n
# # ret = func(9)
# # print(ret)
#
# # 匿名函数  语法 lambda 参数:返回值
# a = lambda n : n * n
# ret  = a(9)
# print(ret)
#
# b = lambda x : x+1
#
# print(func.__name__)    # 查看函数名字
# print(a.__name__)   # __name__的值都是lambda
# print(b.__name__)


# 匿名函数,给函数传递2个参数,返回最大值

a = lambda *args : max(args)    # 单行函数
ret = a(7,3,4,5,6,3,4,646,7,323,4,756341,)
print(ret)