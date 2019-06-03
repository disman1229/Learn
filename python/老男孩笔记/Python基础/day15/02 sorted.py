

# lst = [2,3,6,8,13,34,12]
# lst.sort()  # list 排序方法
# print(lst)

# 内置函数中提供了一个通用的排序方案,sorted()
# ll = sorted(lst)
# print(ll)


# lst = ["鲁班七号","安琪拉","程咬金","后裔","阿珂"]
# def func(s):
#     return len(s) % 2
# ll = sorted(lst,key=func)
# print(ll)
# key:排序方案,sorted函数内部会把可迭代对象中的每一个元素拿出来交给后面key
# 后面的key计算出一个数字,作为当前这个元素的权重,整个函数根据权重排序


# lst = [
#     {'name':'汪峰','age':48},
#     {'name':'章子怡','age':38},
#     {'name':'鲁班七号','age':23},
#     {'name':'程咬金','age':34},
#     {'name':'后裔','age':32},
#     ]
# # def func(el):
# #     return el['age']
#
# ll = sorted(lst,key=lambda el : len(el['name']),reverse=True)
# print(ll)

# lst = [{'mm':222},{'mm':333},{'mm':111}]
# ll = sorted(lst,key=lambda el:el['mm'])
# print(list(ll))