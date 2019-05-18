

# f = open("a1.txt",mode="r",encoding="utf-8")
# f1 = f.read()
# print(f1)
# f.close()

# f = open("a1.txt",mode="r+",encoding="utf-8")
# f1 = f.read()
# f.write("\n信不信由你,反正我信了")
# print(f1)
# f.flush()
# f.close()

# f = open("a1.txt",mode="w",encoding="utf-8")
# f.write("每天坚持一点,\n每天努力一点,\n每天多思考一点,\n你慢慢会发现,\n你的进步越来越大.")
# f.flush()
# f.close()

# import os
# with open("a1.txt",mode='r',encoding='utf-8') as f1,\
#     open('a1.txt_副本',mode='w',encoding='utf-8') as f2:
#     for line in f1:
#         if line == '我说的都是真的。哈哈':
#             f2.write('你们就信吧~\n')
#         f2.write(line)
# os.remove('a1.txt')
# os.rename('a1.txt_副本','a1.txt')

# f = open("a1.txt",mode='r',encoding='utf-8')
# f1 = f.readable()
# f2 = f.writable()
# print(f1,f2)

# f = open("a1.txt",mode='r',encoding='utf-8')
# for line in f:
#     print(line.strip())

# f = open("a1.txt",mode='r',encoding='utf-8')
# f1 = f.readlines()
# print(f1)

# f = open("a1.txt",mode='r',encoding='utf-8')
# f1 = f.read(4)
# print(f1)

# f = open("a1.txt",mode='r',encoding='utf-8')
# f1 = f.readline().strip()
# print(f1)

# f = open("a1.txt",mode='r',encoding='utf-8')
# f.readline()
# f.readline()
# f1 = f.read()
# print(f1)

# f = open("a1.txt",mode='a+',encoding='utf-8')
# f.write("老男孩教育")
# f.seek(0)
# print(f.read())

# f = open("a1.txt",mode='r+',encoding='utf-8')
# f.seek(9)
# f1 = f.truncate()
# f.seek(0)
# print(f.read())



# ls = []
# total = 0
# f = open('a.txt',mode='r',encoding='utf-8')
# for line in f:
#     dic = {}
#     lis = line.strip().split(' ')
#     dic['name'] = lis[0]
#     dic['price'] = lis[1]
#     dic['amount'] = lis[2]
#     ls.append(dic)
#     total = total + int(dic['price']) * int(dic['amount'])
# print(total)
# print(ls)

# import os
# with open('a3.txt',mode='r',encoding='utf-8') as f1,\
#     open('a3.txt_副本',mode='w',encoding='utf-8') as f2:
#     for line in f1:
#         a = line.replace('alex','SB')
#         f2.write(a)
# os.remove('a3.txt')
# os.rename('a3.txt_副本','a3.txt')


# result = []
# f = open('a2.txt',mode='r',encoding='utf-8')
# for line in f:
#     dic = {}
#     lst = line.split(" ")
#     for e in lst:
#         ll = e.split(":")
#         dic[ll[0]] = ll[1]
#     result.append(dic)
# print(result)