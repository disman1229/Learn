s = 'disman and Disman1 And disman2'
# s1 = s.capitalize() # 首字母大写
# print(s) # 原字符串不变
# print(s1)

# s1 = s.upper()
# print(s1)
# s2 = s.lower()
# print(s2)

# 在程序在判断不区分大小写的时候，肯定用上
# while True:
#     content = input("请喷：")
#     if content.upper() == "Q":
#         break
#     else:
#         print("你喷了：",content)

# s = "disMan Disman1 dIsman"
# print(s.swapcase()) #大小写转换

# s2 = "БBß" # 俄美德
# print(s2)
# print(s2.lower())
# print(s2.casefold())

# s = "disman and disman1 or disman2"
# print(s.title())

# s = "麻花藤"
# print(s.center(9,"-"))

# username = input("请输入用户名：").strip() #去掉空格
# password = input("请输入密码：").strip()
# if username == "disman" and password == "123":
#     print("登录成功")
# else:
#     print("登录失败")

# lstrip 去掉左边空格，rstrip 去掉右边空格
# s = "麻花藤马虎疼马虎疼马布里马都不理"
# print(s.strip("马虎疼"))  # strip去掉的是左右两端的内容，中间的不管

# s = "disman disman is good man"
# s1 = s.replace("disman","沙谷地")
# print(s1)
# # 去掉上述字符串中的空格
# s2 = s.replace(" ","")
# print(s2)
# s3 = s.replace("disman","disman1",1)
# print(s3)

# 切割
# s = "disman_diaman1_disman2_disman3"
# lst = s.split("disman_diaman1_disman2_disman3")  # 刀是下划线  切完的东西是列表，列表装的是字符串
# print(lst)


# s = "我叫{}，我今年{}岁了，我喜欢{}".format("disman",28,"电脑")
# print(s)

# 可以定位位置
# s = "我叫{1}，我今年{0}岁了，我喜欢{2}".format("disman",28,"电脑")
# print(s)


# s = "我叫{name}，我今年{age}岁了，我喜欢{hobby}".format(name="disman",age=28,hobby="电脑")
# print(s)

s = "disman is good man good"
# print(s.startswith("disman")) # 是否以disman开头
# print(s.endswith("disman")) # 是否以disman结尾
# print(s.count("disman")) # 计算 xxx 在字符串出现的次数

# print(s.find("goods"))  # 计算xxx字符串出现的位置，如果没有返回-1

# print(s.find("good",11))

# print(s.index("od"))

# s = "123"
# print(s.isdigit())

# s = "disman is a good man"
# print(len(s))   # print(), input(), len()  python的内置函数
#
# i = s.__len__()     #也可以求长度   len()函数执行的时间实际执行的就是它
# print(i)


# 把字符串从头到尾进行遍历

s = "disman is a good mans"

# 1.使用while循环遍历
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1

# 2.用for循环遍历
# 优势：简单
# 劣势：没有索引
for c in s:
    print(c)

# 语法：
#     for 变量 in 可迭代对象：
#         循环体