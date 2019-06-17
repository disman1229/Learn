
# 什么是模块?
    # 已经写好的一组功能的集合
    # 别人写好的函数,变量,方法放在一个文件里(这个文件可以被我们直接使用),这个文件就是个模块

# 如何自己写一个模块
# 创建一个py文件,给它起一个符合变量名命名规则的名字,这个名字就是模块名

# import my_module    # 报错原因:pycharm认为你的模块导入不进来
# 在导入模块的过程中发生了什么?
# 导入一个模块就是执行一个模块

# 怎么使用my_module模块中的名字
# print(my_module.name)
# print(my_module.read1)
# my_module.read1()

# import 的命名空间
# name = 'disman1'
# def read1():
#     print('main read1')
#
# print(name)
# print(my_module.name)

# 模块是否可以重复导入
# import my_module
# import my_module
# 怎么判断这个模块是否已经导入?
# import sys
# print(sys.modules)

# 模块和当前文件在不同的命名空间中
# 模块导入的过程中发生了什么?
    # 找到这个模块
    # 判断这个模块是否被导入过了
    # 如果没有被导入过,就创建一个属于这个模块的命名空间,让模块的名字指向这个空间
    # 执行这个模块中的代码

# name = 'disman1'
# def read1():
#     print('main read1')
#
# print(name)
# my_module.read2()


# 给模块起别名,起了别名之后,使用这个模块就都使用别名应用变量了
# import my_module as m
# m.read1()

# def func(dic,t = 'json'):
#     if t == 'json':
#         import json
#         return json.dumps(dic)
#     elif t == 'pickle':
#         import pickle
#         return pickle.dumps(dic)

# def func(dic,t = 'json'):
#     if t == 'json':
#         import json as aaa
#     elif t == 'pickle':
#         import pickle as aaa
#     return aaa.dumps(dic)

# 导入多个模块
# import os,time
# import os as o,time as t
# 规范建议模块应该一个一个的导入:自定义模块,第三方模块,内置模块
# 1.内置模块
# 2.扩展(第三方)模块
# 3.自定义模块

