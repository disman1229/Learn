# 1.整理函数相关知识点,写博客
# 2.写函数,检查获取传入列表或者元祖对象的所有奇数位索引对应的元素,并将其作为新的列表返回给调用者.
# li = ['鲁班七号','安琪拉','后裔','程咬金','阿珂','兰陵王','大乔','小乔']

# def func(li):
#     result = []
#     for i in range(len(li)):
#         if i % 2 == 1:
#             result.append(li[i])
#     return result
# ret = func(['鲁班七号','安琪拉','后裔','程咬金','阿珂','兰陵王','大乔','小乔'])
# print(ret)

# def func(li):
#     return li[1::2]
# ret = func(['鲁班七号','安琪拉','后裔','程咬金','阿珂','兰陵王','大乔','小乔'])
# print(ret)

# 3.写函数,判断用户传入的对象(字符串,列表,元祖)长度是否大于5.

# def func(a):
#     return len(a) > 5
# ret = func(['鲁班七号','安琪拉','后裔','程咬金','阿珂','兰陵王','大乔','小乔'])
# print(ret)

# 4.写函数,检查传入的列表长度,如果大于2,将列表的前两项内容返回给调用者.

# def func(a):
#     if len(a) > 2:
#         return a[0:2]
# ret = func([1,2,3,2,34,5])
# print(ret)

# 5.写函数,计算传入函数的字符串中,数字,字母,空格以及其他内容的个数,并返回结果

# def func(s):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for i in s:
#         if i.isdigit():
#             shuzi += 1
#         elif i.isalpha():
#             zimu += 1
#         elif i == " ":
#             kongge += 1
#         else:
#             qita += 1
#     return shuzi,zimu,kongge,qita
# ret = func("asda123123@@@   ")
# print(ret)


# 6.写函数,接受两个数字参数,返回较大的那个数字

# def func(a,b):
#     return a if a > b else b
# ret = func(233,231)
# print(ret)

# 7.写函数,检查传入的字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并将新内容返回给调用者
# dic = {"k1":"v1v2","k2":[11,22,33,44]}
# PS:字典中的value只能是字符串或者列表

# def func(dic):
#     newdic = {}
#     for k,v in dic.items():
#         if len(v) > 2:
#             s = v[0:2]
#             newdic[k] = s
#         else:
#             newdic[k] = v
#     return newdic
# print(func({"太白":"亮","jay":"周杰伦","潘婷":"洗发水","飘柔":"洗头膏","伊卡璐":"卡卡就是甩"}))

# 8.写函数,此函数只接收一个参数且此参数必须是列表数据类型,此函数完成的功能是返回给调用者一个字典,此字典的键值对为此函数的索引及对应的元素.列如传入的列表为:[11,22,33]返回的字典为{0:11,1:22,2:33}.

# def func(lis):
#     dic = {}
#     if type(lis) == list:
#         for i in range(len(lis)):
#             dic[i] = lis[i]
#         return dic
#     else:
#         return "不是个列表"
# print(func([11,22,33,44]))

# 9.写函数,函数接收四个参数分别是:姓名,性别,年龄,学历.用户通过输入这四个内容,然后将这四个内容传入到函数中,此函数接收到这四个内容,将内容追加到一个 student_msg 文件中

# def func(name,gender,age,edu):
#     with open("student_msg.txt",mode="a",encoding="utf-8") as f:
#         f.write(name + "--" + gender + "--" + age + "--" + edu + "\n")
# name = input("请输入姓名:")
# gender = input("请输入性别:")
# age = input("请输入年龄:")
# edu = input("请输入学历:")
# print(func(name,gender,age,edu))

# 10.对第9题升级:支持用户持续输入,Q或者q退出,性别默认是男,如果遇到女学生,则把性别输入女

# def func(name,age,edu,gender="男"):
#     with open("student_msg.txt",mode="a",encoding="utf-8") as f:
#         f.write(name + "--" + gender + "--" + age + "--" + edu + "\n")
# while 1:
#     content = input("是否录入学生信息(输入Q退出):")
#     if content.upper() == "Q":
#         break
#     else:
#         name = input("请输入姓名:")
#         gender = input("请输入性别:")
#         age = input("请输入年龄:")
#         edu = input("请输入学历:")
#         if gender == '':
#             func(name, age, edu)
#         else:
#             func(name,age,edu,gender)

# 11.写函数,用户名传入修改的文件名,与要修改的内容,执行函数,完成整个文件的批量修改操作(升级题)

# import os
# def filename(filename,old,new):
#     with open(filename,mode='r',encoding='utf-8') as f1,\
#         open(filename+'副本',mode='w',encoding='utf-8') as f2:
#         for line in f1:
#             a = line.replace(old,new)
#             f2.write(a)
#     os.remove(filename)
#     os.rename(filename+'副本',filename)
# filename("studynotes.txt","python","python1")

# 12.写一个函数完成三次登录,在写一个函数完成注册功能(升级题)
#   注册:
#       首先,要从文件中读取用户名和密码,匹配用户输入的用户名和文件中的用户名是否一致,如果用户名一致,提示重新输入.
#       其次,如果上面的没有问题,把用户名和密码录入文件



# def login():
#         count = 1
#         while count <= 3:
#             username = input("请输入用户名:")
#             password = input("请输入密码:")
#             with open("db.log", mode="r", encoding="utf-8") as f1:
#                 for line in f1:
#                     a = line.split()
#                     if username == a[0] and password == a[1]:
#                         print("登录成功!")
#                         return
#                 else:
#                     print("用户名或者密码错误!")
#                     print("当前输入错误第 %s 次" % count)
#                     count +=1
# login()


# def regist():
#     print("欢迎进入注册系统")
#     while 1:
#         username = input("请输入用户名:").strip()
#         password = input("请输入密码:").strip()
#         if username == "" or password == "":
#             print("用户名或者密码不合法")
#             continue
#         # 校验用户名是否存在
#         with open("db.log", mode="r+", encoding="utf-8") as f1:
#             for line in f1:
#                 if username == line.split("@@")[0]:
#                     print("该用户名已经注册，请重新注册")
#                     break
#             # 这里确定没注册过
#             else:
#                 f1.write(username + "@@" + password + "\n")
#                 print("注册成功")
#                 return
# regist()
