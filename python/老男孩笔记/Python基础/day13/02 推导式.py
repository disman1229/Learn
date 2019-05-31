

# lst = []
# for i in range(1,16):
#     lst.append("Python" + str(i))
# print(lst)

# 推导式:用一句话来生成一个列表
# lst = ["Python" + str(i) for i in range(1,16)]
# print(lst)

# 语法:[结果 for循环 判断]

# lst = [i for i in range(100) if i % 2 == 1]
# print(lst)


# 100以内能被3整除的数的平⽅
# lst = [i*i for i in range(100) if i % 3 == 0]
# print(lst)


# 寻找名字中带有两个e的⼈的名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#           ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# 推导式方法
# lst = [name for line in names for name in line if name.count("e")==2]
# print(lst)

# 传统方法
# for line in names:
#     for name in line:
#         if name.count("e") == 2:
#             lst.append(name)
# print(lst)

# [11,22,33,44] => {0:11,1:22,2:33,3:44}
# lst = [11,22,33,44]
# dic = {i:lst[i] for i in range(len(lst)) if i < 2}
# print(dic)
# 语法:{k:v for循环 条件筛选}

# dic = {"jj":"林俊杰","jay":"周杰伦","zs":"赵四","ln":"刘能"}
# new_dic = {v:k for k,v in dic.items()}
# print(new_dic)

# s = {i for i in range(100)}
# print(s)

# 集合推到式
# lst = [1,1,4,6,7,7,4,2,2]
# s = {el for el in lst}
# print(s)
# s = set(lst)
# print(s)