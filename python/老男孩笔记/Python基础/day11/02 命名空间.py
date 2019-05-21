# print("哈哈")
# print("呵呵")


# 1.内置,2.全局,3.局部(函数调用)
# a = 120
# def fn():
#     b = 20
#     def gn():
#         pass
#     print(globals())  # 可以查看全局作用域中的内容
#     print(locals())  # 可以查看当前作用域中的内容
# # def en():
# #     pass
# fn()


# def outer():
#     print("哈哈")
#     def inner_1():
#         print("呵呵")
#         def inner_1_1():
#             print("嘻嘻")
#         inner_1_1()
#         print("吼吼")
#     def inner_2():
#         print("嘿嘿")
#     inner_2()
#     inner_1()
# outer()