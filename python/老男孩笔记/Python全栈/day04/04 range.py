s = "disman is a good man"
# for c in s:
#     print(c)

# range
# for i in range(10):     # 从0 开始到10结束
#     print(i)

# for i in range(3,7):    # 从3开始,打印到7结束,不能打印7
#     print(i)

# for i in range(3,10,2):     # 从3到10每2个取一个
#     print(i)

# for i in range(10,-10,-1):      #从10开始到-10结束,倒着数
#     print(i)

# 求1-2+3-4...+99-100=?
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum = sum - i
    else:
        sum = sum + i
print(sum)