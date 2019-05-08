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
# li[5:] = s
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
# lis[3][2][1][0] = lis[3][2][1][0].replace("tt", "TT")
# print(lis)

# 2)将列表中的数字3变成字符串100（两种方式）
# lis [1]="100"
# lis[3][2][1]="100"
# print(lis)

# 3)将列表中的字符串1变成数字101（两种方式）
# lis[3][2][1][2]=101
# print(lis)

# 4.请用代码实现
# li = ["alex","eric","rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# print("{}_{}_{}".format(li[0],li[1],li[2]))

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

# 9.利用for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然后对列表的元素进⾏筛选，将能被4整除的数留下来。
# lis = []
# for i in range(100,9,-1):
#     if i % 4 == 0:
#         lis.append(i)
# print(lis)

# 10.利用for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个列表，将能被3整除的数改成*。
# lis = []
# index = 0
# for i in range(1,31):
#     lis.append(i)

# 方案一
# for i in lis:
#     if i % 3 == 0:
#         lis[index] = "*"
#     index += 1
# print(lis)

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
#     if c.startswith("A") or c.startswith("a") and c.endswith("c"):
#         lis.append(c)
# for i in lis:
#     print(i)

# 方案二
# for i in li :
#     if (i.strip()[0]=="a" or i.strip()[0]=="A" ) and i.strip()[-1] =="c":
#         lis.append(i)
# for i in lis :
#     print(i)


