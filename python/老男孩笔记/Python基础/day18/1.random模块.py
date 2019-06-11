# 取随机数的模块
import random
# 取随机小数 数学计算
# print(random.random())  # 取0-1之间的小数
# print(random.uniform(1,2))  # 取1-2之间的小数

# 取随机整数:彩票,抽奖
# print(random.randint(1,2))  # [1,2]顾头顾尾
# print(random.randrange(1,2)) #  [1,2)顾头不顾尾
# print(random.randrange(1,200,2)) #  按照步长取值

# 从列表中随机抽取值:抽奖
# l = ['a','b',(1,2),123]
# print(random.choice(l))
# print(random.sample(l,2))

# 打乱一个列表的顺序,在原列表的基础上直接进行修改,节省内存
# 洗牌
# l = ['a','b',(1,2),123]
# random.shuffle(l)
# print(l)


# 验证码
    # 4位数字验证码
print(random.randint(1000,9999))
    # 6位数字验证码
print(random.randint(100000,999999))
    # 6位数字+字母验证码
l = ['a','b','c','d','e','f','g']
print(str(random.randrange(100000,999999))+str(random.choice(l)))

# 发红包