# 1.写代码，有如下列表，按照要求实现每一个功能
# li = ["alex","wusir","ritian","barry","wenzhou"]

# 1)计算列表长度并输出
# print(len(li))

# 2)列表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)

# 3)请在列表的第一个位置插入元素"Tony",并输出增加后的列表
# li.insert(0,"Tony")
# print(li)

# 4)请修改列表第二个位置元素为"Kelly"，并输出修改后的列表
# li[1] = "Kelly"
# print(li)

# 5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加
# l2=[1,"a",3,4,"heart"]
# 方法一：
# li.extend(l2)
# print(li)
# 方法二：
# lst = li + l2
# print(lst)

# 6)请将字符串s = "qwert"的每一个元素插入到列表li中，一行代码实现，不允许循环添加
# s = "qwert"
# li.extend(s)
# print(li)

# 7)请删除列表中的元素"alex"，并输出删除后的列表
# li.remove("alex")
# print(li)

# 8)请删除列表中的第2个元素，并输出删的元素和删除后的列表
# lst = li.pop(1)
# print(lst)
# print(li)

# 9)请删除列表中的第2至第4元素，并输出删除后的列表
# li[1:4] = []
# print(li)

# 10)请将列表所有得元素反转，并输出反转后的列表
# li.reverse()
# print(li)

# 11)请计算出"alex"元素在列表li中出现的次数，并输出该次数
# print(li.count("alex"))

# 2.写代码，有如下列表，利用切片实现每一个功能
# li = [1,3,2,"a",4,"b",5,"c"]

# 1)通过对li列表的切片形成新的列表l1，l1=[1,3,2]
# l1 = li[0:3]
# print(l1)

# 2)通过对li列表的切片形成新的列表l2，l2=["a",4,"b"]
# l2 = li[3:6]
# print(l2)

# 3)通过对li列表的切片形成新的列表l3，l3=[1,2,4,5]
# l3 = li[::2]
# print(l3)

# 4)通过对li列表的切片形成新的列表l4，l4=[3,"a","b"]
# l4 = li[1:6:2]
# print(l4)

# 5)通过对li列表的切片形成新的列表l5，l5=["c"]
# l5 = li[7]
# print(l5)

# 6)通过对li列表的切片形成新的列表l6，l6=["b","a",3]
# l6 = li[-3::-2]
# print(l6)

# 3.写代码，有如下列表，按照要求实现每一个功能
# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","adv"]

# 1)将列表lis中的"tt"变成大写（两种方式）
# 方案一
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# 方案二
# lis[3][2][1][0] = "TT"
# print(lis)
# 方案三
# lis[3][2][1][0] = lis[3][2][1][0].replace("t", "T")
# print(lis)

# 2)将列表中的数字3变成字符串100（两种方式）
# 方案一
# lis[1]="100"
# lis[3][2][1][1]="100"
# print(lis)
# 方案二
# lis[1] = str(lis[1] + 97)
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
# print(lis)

# 3)将列表中的字符串1变成数字101（两种方式）
# 方案一
# lis[3][2][1][2]=101
# print(lis)
# 方案二
# lis[3][2][1][2] = int(lis[3][2][1][2] + "01")
# print(lis)

# 4.请用代码实现
# li = ["alex","eric","rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# s = ""
# for el in li:
#     s = s + el + "_"
# print(s[0:-1])

# 5.利用for循环和range打印出下面列表的索引
# li = ["alex","WuSir","ritian","barry","wenzhou"]
# for i in range(len(li)):
#     print(i)

# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中
# lis = []
# for i in range(101):
#     if i % 2 == 0:
#         lis.append(i)
# print(lis)

# 7.利用for循环和range找出50以内能被3整除的数，并将这些数插入到一个新的列表中
# lis = []
# for i in range(51):
#     if i % 3 == 0:
#         lis.append(i)
# print(lis)

# 8.利用for循环和range从100~1，倒序打印
# for i in range(100,0,-1):
#     print(i)
# count = 100
# while count > 0:
#     print(count)
#     count -= 1

# 9.利用for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然后对列表的元素进⾏筛选，将能被4整除的数留下来。
# lis = []
# for i in range(100,9,-1):
#     if i % 2 == 0:
#         lis.append(i)
# new_lis = []
# for i in lis:
#     if i % 4 == 0:
#         new_lis.append(i)
# print(new_lis)

# 10.利用for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个列表，将能被3整除的数改成*。
# lis = []
# for i in range(1,31):
#     lis.append(i)

# 方案一
# new_lis = []
# for i in lis:
#     if i % 3 == 0:
#         i = "*"
#     new_lis.append(i)
# print(new_lis)

# 方案二
# while index < len(lis):
#     if index % 3 == 0:
#         lis[index-1] = "*"
#     index += 1
# print(lis)

# 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并 以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
# lis = []
# 方案一
# for i in li:
#     c = i.replace(" ","")
#     if (c.startswith("A") or c.startswith("a")) and c.endswith("c"):
#         lis.append(c)
# for i in lis:
#     print(i)

# 方案二
# for i in li :
#     if (i.strip()[0]=="a" or i.strip()[0]=="A" ) and i.strip()[-1] =="c":
#         lis.append(i)
# for i in lis :
#     print(i)

# 12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰","波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到这个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

# lst = []
# li = ["苍老师", "东京热", "武藤兰","波多野结衣"]
# comment = input("请输入您的评论:")
# for i in li:
#     if i in comment:
#         comment = comment.replace(i,"*"*len(i))
# lst.append(comment)
# print(lst)

# 13.有如下列表
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7,
# 8
# "taibai"
# 5
# ritian

# for e in li:
#     if type(e) == list:
#         for ee in e:
#             if type(ee) == str:
#                 print(ee.lower())
#             else:
#                 print(ee)
#     elif type(e) == str:
#         print(e.lower())
#     else:
#         print(e)


# 14. 把班级学生数学考试成绩录入到一个列表中:并求平均值. 要求: 录入的时候要带着姓名录入, 例如: 张三_44
# lis = []
# while 1:
#     stu = input("请输入学生的姓名和分数（姓名_分数），输入Q退出录入:")
#     if stu.upper() == "Q":
#         break
#     lis.append(stu)
# sum = 0
# for el in lis:
#     li = el.split("_")
#     sum += int(li[1])
# print(sum / len(lis))

# 15.给出一个任意的数字n,从0开始数,数到n结束,把每个数字都放在列表中,在数的过程中出现7或者7的倍数,则向列表中添加一个"咣"
#例如,输入10
# lst =[1,2,3,4,5,6,"咣",8,9,10]
# lst = []
# index = 0
# num = input("请输入你要查的数:")
# for i in range(1,int(num)+1):
#     if i % 7 == 0:
#         i = "咣" # 两种方法都可以
#         # i = str(i).replace(str(i),"咣")
#     lst.append(i)
# print(lst)

