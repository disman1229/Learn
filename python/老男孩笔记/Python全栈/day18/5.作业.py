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
# def hongbao(money,num):
#     lst = []
#     for i in range(num):
#         if money > 0 and num != 1:
#             s = round(random.uniform(0.01,money - (0.01*num)),2)
#             num -= 1
#             money -= s
#             lst.append(s)
#     return lst
# print(hongbao(200,5))

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
# import time
# def timec(startTime,endTime):
#     startTime = time.strptime(startTime,'%Y-%m-%d %H:%M:%S')
#     endTime = time.strptime(endTime,'%Y-%m-%d %H:%M:%S')
#     startMktime = time.mktime(startTime)
#     endMktime = time.mktime(endTime)
#     newTime = endMktime - startMktime
#     retime = time.gmtime(newTime)
#     return '时间过去了 %d年%d月%d天 %d时%d分%d秒'%(retime.tm_year-1970,retime.tm_mon-1,retime.tm_mday-1,retime.tm_hour,retime.tm_min,retime.tm_sec)
# print(timec('2019-2-3 13:20:3','2019-2-3 14:20:10'))

# sys.argv 登录验证
# import sys
# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr == 'disman' and pwd == '123':
#     print("登录成功")
# else:
#     print("用户名或者密码错误!")
#     exit()

# os模块:
    # 用户登录,登录之后给这个用户创建属于自己的文件夹,已用户名命名
    # 如果用户注销,删除这个文件夹
import os

usr = input("请输入用户名:")
pwd = input("请输入密码:")
if usr == 'disman' and pwd == '123':
    os.makedirs('user/%s'%usr)
    logout = input("注销请输入1:")
    if int(logout) == 1:
        os.rmdir('user/%s'%usr)

