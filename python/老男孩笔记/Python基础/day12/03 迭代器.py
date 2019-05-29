
# s = "你好啊"
# for i in s:
#     print(i)

# print(dir(str)) # dir查看xx类型的数据可以执行哪些方法,__iter__  iterable
# print(dir(list))    # __iter__
# print(dir(int))     # 没有__iter__
# 所有带__iter__可以for循环的,可迭代对象

# 可迭代对象可以使用__iter__()来获取迭代器
# 迭代器里面有__next__()
# s = "鲁班七号程咬金"
# it = s.__iter__()
# print(dir(it))

# 1.只能向前
# 2.几乎不占内存,节省内存
# 3.for循环

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())


# 迭代器模拟for循环
# lst = ["鲁班七号","安琪拉","程咬金","阿珂"]
# for el in lst:    # 底层用的是迭代器
#     print(el)

# it = lst.__iter__() # 获取迭代器
# while 1:
#     try:    # 尝试执行
#         el = it.__next__()  # 获取下一个元素
#         print(el)
#     except StopIteration:   # 处理错误
#         break

lst = ["鲁班七号","安琪拉","程咬金","阿珂"]
it = lst.__iter__()
# 偏方
# print("__iter__" in dir(it))
# print("__next__" in dir(it))
# 可以通过dir来判断数据是否是可迭代的,以及数据是否是迭代器

# 官方方案
from collections import Iterable    # 可迭代对象
from collections import Iterator    # 迭代器

print(isinstance(lst,Iterable))
print(isinstance(lst,Iterator))

print(isinstance(it,Iterable))
print(isinstance(it,Iterator))
