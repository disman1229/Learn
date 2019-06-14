# my_user = "disman"
# my_pwd = "disman"
# my_yzm = "o98K"
# count = 1
# while 1:
#     user = input("请输入用户名：").strip()
#     pwd = input("请输入密 码：").strip()
#     if my_user == user and my_pwd == pwd:
#         print("登录成功！")
#         break
#     elif count == 3:
#         while 1:
#             yzm = input("请输入验证码(o98K)：")
#             if yzm.upper() == my_yzm.upper():
#                 count = 0
#                 break
#             else:
#                 print("验证码错误")
#     else:
#         print("用户名或者密码错误！")
#     count += 1

# 请输入一个数字，检查是否是小数
# num = input("请输入数字：")
# if num.count(".") == 1 and not num.startswith(".") and not num.endswith("."):
#     print("这个小数是：" + num)
# elif num.isdigit():
#     print("这是一个整数")
# else:
#     print("请输入数字")

s = "上海自来水来自海上"
# if s == s[::-1]:

# n = list(s)
# n.reverse()
# s1 = ''.join(n)
# if s == str(s1):
#     print("回文")

# n = list(s)
# s1 = "".join(n[::-1])
# if s == s1:
#     print("回文")

# i = 0
# n = len(s) - 1
# while n >= 0:
#     if s[i] == s[n]:
#         i += 1
#         n -= 1
#     else:
#         print("不是回文")
#         break
# else:
#     print("回文")