

# a = 10
# def func():
#     global a    # 1.可以把全局中的内容引入到函数内部,2.在全局创建一个变量
#     a = 20
#     # 在访问func之后把全局中的a换成20
# func()
# print(a)


# def outer():
#     a = 10
#     def inner():    # 在inner中改变a的值
#         nonlocal a # 寻找外层函数中离他最近的那个变量,
#         a = 20
#     inner()
#     print(a)
# outer()


# a=1
# def fun_1():
#     a=2
#     def fun_2():
#         nonlocal a
#         a=3
#         def fun_3():
#             a=4
#             print(a)
#         print(a)
#         fun_3()
#         print(a)
#     print(a)
#     fun_2()
#     print(a)
# print(a)
# fun_1()
# print(a)