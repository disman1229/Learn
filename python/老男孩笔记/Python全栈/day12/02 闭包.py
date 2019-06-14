
# 闭包，在内存函数中访问外层函数的变量
# def outer():
#     a = 10
#     def inner():
#         print(a)
#     inner()
# outer()
# 闭包的作用：
#   1.可以保护你的变量不受侵害
# def outer():
#     a = 10    # 对外界不开放
#     def inner():
#         nonlocal a
#         a = 20
#         print(a)
#         inner()
#   2.可以让一个变量常驻内存
# def outer():
#     a = 10  # 常驻内存，为了inner执行的时候有值
#     def inner():
#         print(a)
#     return inner
# fn = outer()
# fn()

# 超简易爬虫
# from urllib.request import urlopen
#
# def outer():
#     # 常驻内存
#     s = urlopen("http://www.discuz.net/forum.php").read()
#     def getContent():   # 闭包
#         return s
#     return getContent
# print("爬去内容")
# pa = outer()
# ret = pa()
# print(ret)

# def func():
#     a = 10
#     def inner():
#         print(a)
#     print(inner.__closure__) # 如果打印的不是None就是闭包
# func()
