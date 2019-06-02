

# lst = ["鲁班七号","程咬金","花木兰","后裔"]

# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# it = iter(lst)  # 内部封装的就是__iter__()
# print(it.__next__())
# print(next(it)) # 内部封装的是__next__()


# lst = (1,2,3)
# print(id(lst))
# print(hash(lst))    # 目的是为了储存计算后的一个数字,hash值尽量不要重复(在某些特定环境下hash可能会重复)

# print(help(str))    # 帮助文档
#
# a = 10
# print(callable(a))  # 是否被调用执行


# print(bin(5))   # 二进制
# print(oct(8))   # 八进制
# print(hex(15))   # 十六进制

# print(abs(-8))  # 求绝对值
# print(divmod(10,2)) # 计算商和余数
# print(round(3.4))   # 四舍五入
# print(pow(2,3,3)) # 求次幂,第三个参数计算余数
# print(sum([1,2,3,4,5],3)) # 求和
# print(min(55,32,52,56,74))  # 求最小值
# print(max(3,45,62,7,13))    #求最大值


# lst = ['鲁班','安琪拉','后裔','阿珂']
# ll = reversed(lst)  # reversed()反转,返回迭代器
# print(list(ll))

# s = slice(0,3,2)  # 切片
# print(lst[s])

# s = "鲁班七号"
# print(memoryview(s.encode("utf-8")))    # 还不如id

# print(ord("a")) # 查看字符a在编码位置 97
# print(chr(97))  # 通过编码找字符
# print(ascii("a"))
# print(ascii("中"))

# print('小鲁班:"小短腿"')
# print("小鲁班:\"小短腿\"")
# print(repr("小鲁班:\t小短腿\t"))  # 原样输出字符串


# s = "喝酒"
# print(s.center(20))
# print(format(s,"^20"))  # 居中
# print(format(s,">20"))  # 右对齐
# print(format(s,"<20"))  # 左对齐

# print(format(3, 'b'))   # 二进制
# print(format(97, 'c'))
# print(format(11, 'd'))
# print(format(11, 'o'))
# print(format(11, 'x'))
# print(format(11, 'X'))
# print(format(11, 'n'))
# print(format(11)) # 和d⼀一样

# s = "5+6"
# ret = eval(s)   # 动态执行一个代码片段,则重点在返回上
# print(ret)




