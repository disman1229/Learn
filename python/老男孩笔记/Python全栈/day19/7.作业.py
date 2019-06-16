# 1、写一个函数，接受一个参数，如果是文件，就执行这个文件，如果是文件夹，就执行这个文件夹下所有的py文件
import os
# def func(path):
#     # 首先判断出入的目录下是否有.py结尾的文件,如果有执行它
#     if os.path.isfile(path) and path.endswith('.py'):
#         os.system('python %s'%path) # 模拟在cmd中执行
#     # 如果不是文件是文件夹
#     elif os.path.isdir(path):
#         # 查看这个文件夹下的文件信息
#         for name in os.listdir(path):
#             abs_path = os.path.join(path,name)
#             if abs_path.endswith('.py'):
#                 print(abs_path)
#                 os.system('python %s' % abs_path) # 执行这个py文件
# func('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day18')


# 2、写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。
# def copy(path1,path2):
#     filename = os.path.basename(path1)
#     # 判断第一个参数是文件,第二个参数是文件夹
#     if os.path.isfile(filename) and os.path.isdir(path2):
#         # 把源文件文件名拼接到目标目录
#         path2 = os.path.join(path2,filename)
#         # 如果目标文件有同名文件则打印已存在
#         if os.path.exists(path2):
#             print('文件已经存在!')
#         # 以bytes读源文件,在以bytes写入到新目录
#         with open(path1,'rb') as f1,open(path2,'wb') as f2:
#             content = f1.read()
#             f2.write(content)
# copy('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/1.os模块.py','/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day18')

# 3、获取某个文件所在目录的上一级目录。
# 例如'D:\sylar\s15\day19\6.序列化模块.py'目录的结果 ：D:\sylar\s15
# 方法一
# path = os.path.dirname('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/6.pickle模块.py')
# basename = os.path.dirname(path)
# print(basename)
# 方法二
# basename = os.path.dirname(os.path.dirname('/Users/zhangjie/Documents/Learn/python/老男孩笔记/Python全栈/day19/6.pickle模块.py'))
# print(basename)

# 4、使用os模块创建如下目录结构
# glance/
#
# ├── __init__.py
#
# ├── api
#
# │   ├── __init__.py
#
# │   ├── policy.py
#
# │   └── versions.py
#
# ├── cmd
#
# │   ├── __init__.py
#
# │   └── manage.py
#
# └── db
#
#     ├── __init__.py
#
#     └── models.py

# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# open('glance/__init__.py','w').close()
# open('glance/api/__init__.py','w').close()
# open('glance/api/policy.py','w').close()
# open('glance/api/versions.py','w').close()
# open('glance/cmd/__init__.py','w').close()
# open('glance/cmd/manage.py','w').close()
# open('glance/db/__init__.py','w').close()
# open('glance/db/models.py','w').close()

# 5、写一个用户注册登陆的程序，每一个用户的注册都要把用户名和密码用字典的格式写入文件userinfo。
# 在登陆的时候，再从文件中读取信息进行验证。

# import pickle
# def register():
#     usr = input('用户名:')
#     pwd = input('密码:')
#     dic = {usr:pwd}
#     with open('userinfo','ab') as f:
#         pickle.dump(dic,f)
#     print('注册成功!')
#
# def login():
#     flag = True
#     usr = input('登录用户名:')
#     pwd = input('登录密码:')
#     with open('userinfo','rb') as f:
#         while flag:
#             try:
#                 dic = pickle.load(f)
#                 for k,v in dic.items():
#                     if k == usr and v == pwd:
#                         print("登录成功")
#                         flag = False
#                         break
#             except EOFError:
#                 print('登录失败')
#                 break
# login()
# register()


# 6、发红包  random
import random
# def hongbao(money,num):
#     money = money * 100
#     ret = random.sample(range(1,money),num-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(money)
#     for i in range(len(ret)-1):
#         yield (ret[i+1] - ret[i]) / 100
# hb = hongbao(200,50)
# for money in hb:
#     print(money)

# def Bonus(person,money):  # 5,200
#     dict_person_money = {}
#     for i in range(person):
#         num = random.randint(1,100)  # 99 99 99 99 99
#         dict_person_money["Person%s"%(i+1)] = num  # person1:99
#     num_sum = 0
#     for i in dict_person_money:
#         num_sum += dict_person_money[i]  # 5 * 99 = 495
#     for i in dict_person_money:    # 99/495 1/5 * 200 = 40
#         x =round(dict_person_money[i]/num_sum*money,2)
#         dict_person_money[i] = '$%s'%x
#     return dict_person_money
#
# result = Bonus(5,10)
# print(result)

# 7、计算器
# '3+4' '5*6' '2-5' '5/2'
# 写函数 计算小字符串的结果

# 1*2+3-4/5
# 乘或者除法先匹配出来

# 小数的 '3.2+4.5' '5.0*6' '2-5' '5/2'

# 默写:
# 计算文件夹的大小 : 递归/循环