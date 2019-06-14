# 取随机数的模块
import random
# 取随机小数 数学计算
# print(random.random())  # 取0-1之间的小数
print(random.uniform(1,2))  # 取1-2之间的小数

# 取随机整数:彩票,抽奖
# print(random.randint(1,2))  # [1,2]顾头顾尾
# print(random.randrange(1,2)) #  [1,2)顾头不顾尾
# print(random.randrange(1,200,2)) #  按照步长取值

# 从列表中随机抽取值:抽奖
l = ['a','b',(1,2),123]
# print(random.choice(l))
# print(random.sample(l,2))

# 打乱一个列表的顺序,在原列表的基础上直接进行修改,节省内存
# 洗牌
# l = ['a','b',(1,2),123]
# random.shuffle(l)
# print(l)


# 验证码
    # 4位数字验证码
    # 6位数字验证码
# 函数版本
# def code(n=6):
#     s = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         s += str(num)
#     return s
# print(code(4))
# print(code(6))

    # 6位数字+字母验证码
        # 一个位置上,出现的是数字还是字母应该是随机事件
        # 随机字母如何生成
# s = ''
# for i in range(6):
#     # 生成随机的字母,数字各一个
#     num = str(random.randint(0,9))
#     alpha_upper = chr(random.randint(65,90))
#     alpha_lower = chr(random.randint(97,122))
#     res = random.choice([num,alpha_upper,alpha_lower])
#     s += res
# print(s)

# 函数版本
def code(n=6,alpha = True):
    s = ''
    for i in range(n):
        # 生成随机的字母,数字各一个
        num = str(random.randint(0,9))
        if alpha:
            alpha_upper = chr(random.randint(65,90))
            alpha_lower = chr(random.randint(97,122))
            num = random.choice([num,alpha_upper,alpha_lower])
        s += num
    print(s)
code(4,False)
code(alpha=False)
code()
# 发红包