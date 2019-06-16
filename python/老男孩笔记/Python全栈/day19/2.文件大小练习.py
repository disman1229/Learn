import os

# 递归
def func(path):
    size_sum = 0
    namelist = os.listdir(path)
    for name in namelist:
        path_abs = os.path.join(path,name)
        if os.path.isdir(path_abs):
            size = func(path_abs)
            size_sum += size
        else:
            size_sum += os.path.getsize(path_abs)
    return size_sum
ret = func('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈')
print(ret)

# 循环
# lst = ['D:\Learn\python\老男孩笔记\Python基础']
# size_sum = 0
# while lst:
#     path = lst.pop()
#     path_list = os.listdir(path)
#     for name in path_list:
#         abs_path = os.path.join(path,name)
#         if os.path.isdir(abs_path):
#             lst.append(abs_path)
#         else:
#             size_sum += os.path.getsize(abs_path)
# print(size_sum)

