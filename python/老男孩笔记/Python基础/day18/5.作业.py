# 验证码   4位  6位  字母加数字组合6位
import random
# def code(n=6,alpha = True):
#     s = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         if alpha:
#             alpha_upper = chr(random.randint(65,90))
#             alpha_lower = chr(random.randint(97,122))
#             num = random.choice([num,alpha_upper,alpha_lower])
#         s += str(num)
#     return s
# print(code(4,False))
# print(code(6,alpha=False))
# print(code())

# 发红包
def hongbao(money,num):
    lst = []
    for i in range(num):
        s = random.uniform(1,money)
        if money >= 0:
            money -= s
        lst.append(format(s,'0.2f'))
    return lst

print(hongbao(10,10))

# 别人写的参考
# dic = {}
# lis = ['KeLan', 'Monkey', 'Dexter', 'Superman', 'Iron Man', 'Robin']
#
#
# def redpacket(cash, person, index):
#     if cash > 0 and person != 1:
#         n = round(random.uniform(0.01, cash - (0.01 * person)), 2)
#         dic[lis[index]] = n
#         print(str(n).ljust(4, "0"))
#         person -= 1
#         cash -= n
#         index += 1
#         redpacket(cash, person, index)
#     else:
#         dic[lis[index]] = round(cash, 2)
#         print(str(cash).ljust(4, "0"))
#
#
# redpacket(10, len(lis), 0)
# print (dic)
# print ("手气最佳:", max(dic.items(), key=lambda x: x[1]))

# 计算时间差 - 函数
# sys.argv 登录验证
# os模块:
    # 用户登录,登录之后给这个用户创建属于自己的文件夹,已用户名命名
    # 如果用户注销,删除这个文件夹