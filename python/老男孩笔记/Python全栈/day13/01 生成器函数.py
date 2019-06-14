
# def func():
#     print("哈哈哈")
#     yield 1     # return和yield都可以返回数据
#     print("呵呵呵")
#
#
# gen = func()    # 不会执行你的函数,拿到的是生成器
# ret = gen.__next__()    # 会执行到下一个yield
# print(ret)
# gen.__next__()

# 函数中如果有yield,这个函数就是生成器函数,生成器函数()获取的是生成器,这个时候不执行函数
# yield:相当于return,可以返回数据,但是yield不会彻底中断函数,会分段执行函数
# gen.__next__()执行函数,执行到下一个yield
# gen.__next__()继续执行函数到下一个yield


# def order():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服" + str(i))
#     return lst
# ll = order()


# def order():
#     for i in range(10000):
#         yield "衣服" + str(i)
# g = order() # 获取生成器
# luban = g.__next__()
# print(luban)
# cyj = g.__next__()
# print(cyj)


# send()和 __next__()是一样的,可以执行到下一个yield,可以给上一个yield传值
# def func():
#     print("我是第一段")
#     a = yield "123"
#     print(a)
#     print("鲁班七号是第二段")
#     b = yield "456"
#     print(b)
#     print("程咬金是第三段")
#     c = yield "789"
#     print(c)
#     print("安琪拉最后一段")
#     d = yield "079" # 最后收尾一定是yield
# g = func()
# print(g.__next__())
# print(g.send("大乔"))
# print(g.send("小乔"))
# print(g.send("后裔"))
# print(g.send("阿珂")) # 最后一个yield不能传值


# def eat():
#     print("我吃什么啊")
#     a = yield "馒头"
#     print("a=", a)
#     b = yield "大饼"
#     print("b=", b)
#     c = yield "⾲菜盒⼦"
#     print("c=", c)
#     yield "GAME OVER"
# gen = eat()  # 获取⽣成器
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.send("胡辣汤")
# print(ret2)
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send("猫粮")
# print(ret4)


# def func(): # 再次证明for内部一定有__next__()
#     yield 12
#     yield 23
#     yield 39
#     yield 89
# for i in func():
#     print(i)
#
# print(list(func())) # 内部都有__next__()