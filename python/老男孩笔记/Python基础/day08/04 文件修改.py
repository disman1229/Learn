

# import os
# # 打开文件
# with open("沙谷地2.txt",mode="r",encoding="utf-8") as f1,\
#     open("沙谷地2_副本",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         line = line.replace("disman","沙谷地")
#         f2.write(line)
# # 删除文件
# os.remove("沙谷地2.txt")
# os.rename("沙谷地2_副本","沙谷地2.txt")


# lst = []
# with open("2019-5-16.log",mode="r",encoding="utf-8") as f:
#     first = f.readline().strip().split(",")
#     for line in f:
#         dic = {}
#         ls = line.strip().split(",")
#         for i in range(len(first)):
#             dic[first[i]] = ls[i]
#         lst.append(dic)
# print(lst)

# x = 3
# x //= 3
# print(x)
#
# for i in range(3):
#     print(i)

# a = 1 > 2 and 3 or 6
# print(a)

# l1 = [1,2,3,4,5,6,7,8,9,0]
# l1[1:4] = "abcd"
# print(l1)

# l2 = ["a","b","c"]
# l2.extend("efg")
# print(l2)

# lis = [['k',['qwe',{'k1':['tt',3,'1']},89],'ab']]
# lis[0][1][1]['k1'][0] = lis[0][1][1]['k1'][0].upper()

# lis[0][1][1]["k1"][1] = str(lis[0][1][1]["k1"][1] + 97)

# lis[0][1][1]["k1"][2] = lis[0][1][1]["k1"][2] + "01"
# print(lis)

# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3):{'k3':['2',100,'wer']}}
# dic['k2'].append('23')

# dic['k2'].insert(0,"a")

# dic[(1,2,3)].update({'k4':'v4'})
# dic[(1,2,3)]['k4'] = 'v4'
# print(dic)

# for i in range(100,-1,-1):
#     print(i)

# count = 1
# sum = 0
# for i in range(1,100,2):
#     if count % 2 == 0:
#         sum = sum - i
#     else:
#         sum = sum + i
#     count += 1
# print(sum)

# sum = 0
# fuhao = 1
# for i in range(1, 100, 2):
#     sum = sum + (i*fuhao)
#     fuhao = -fuhao # 关键
# print(sum)

# index = 1
# fuhao = 1
# sum = 0
# while index < 100:
#     index = index + 2
#     sum = sum + (index*fuhao)
#     fuhao = -fuhao
# print(sum)

# dic = {}
# a = "jay:周杰伦|jj:林俊杰|gg:太白|sb:alex"
# lis = a.split("|")
# for i in lis:
#     ll = i.split(":")
#     dic[ll[0]] = ll[1]
# print(dic)