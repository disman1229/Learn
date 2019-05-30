

# lst = [1,3,4,1]
# it = lst.__iter__()
# while 1:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         break


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = 20
# for i in range(1,n+1):
#     for k in range(n*2-i*2):
#         print("",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()


# 枚举
# lst = ["鲁班七号","安琪拉","貂蝉","大乔","小乔","程咬金"]
#
# for index,el in enumerate(lst):
#     print(index)
#     print(el)

dic = {"鲁班七号":"小短腿","安琪拉":"213"}
for k,v in dic.items():
    print(k)
    print(v)