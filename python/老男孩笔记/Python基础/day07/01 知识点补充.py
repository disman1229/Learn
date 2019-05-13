# 将列表转换成字符串,每个元素之间用_拼接
s = "_".join(["disman","disman1","disman2"])
print(s)

ss = "disman_disman1_disman2"
a = ss.split("_")
print(a)

# 字符串转换成列表:split()
# 把列表转换成字符串:join()

s = "_".join("麻花藤")     # join("可迭代对象")
print(s)


