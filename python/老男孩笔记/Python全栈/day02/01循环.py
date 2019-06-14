# 计数
'''
count = 1
while count <= 2:
    print("你是Disman吗？")
    print("哈哈哈哈")
    count = count + 1
'''

# 让用户尽情喷，输入q退出
'''
while True:
    s = input("请尽情喷：")
    if s == "q":
        break # 停止当前循环

    # 过滤掉马化腾
    if "马化腾" in s: # 在XXX中出现了XX
        print("你输入的内容和草泥马有一拼，不能输出")
        continue #停止本次循环，继续下一循环

    print("喷的内容：" + s)
'''
'''
# 1+2+3+4+5+6+7+8...+100 = ?
count = 1
# 准备一个变量
sum = 0
while count <= 100:
    print(count)
    # 累加到sum中
    sum = sum + count # 把sum中的值（之前运算的结果）和当前数的数相加
    count = count + 1
print(sum)
'''

# 输出0~100奇数
count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1