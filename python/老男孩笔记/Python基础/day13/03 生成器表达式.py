

# tu = (i for i in range(10)) # 没有元祖推到式,只有生成器表达式
# print(tu)   # 生成器
# print(tu.__next__())


# def func():
#     print(111)
#     yield 222
# g = func()  # 获取生成器
# g1 = (i for i in g)  # ⽣成器g1. 但是g1的数据来源于g
# g2 = (i for i in g1) # ⽣成器g2. 来源g1
# print(list(g))  # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
# print(list(g1)) # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1也就没有数据了
# print(list(g2))  # 和g1同理

# 求和
def add(a, b):
    return a + b

# 生成器函数 # 0-3
def test():
    for r_i in range(4):
        yield r_i

g = test()  # 获取生成器

for n in [1, 10, 5, 6]:
    g = (add(n, i) for i in g)
print(list(g))
