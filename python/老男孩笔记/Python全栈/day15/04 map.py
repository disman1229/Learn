

# lst = [1,2,4,2,5,6]
# # 计算列表中每个数字的平方
# def func(el):
#     return el ** 2
# m = map(func,lst)
# print(list(m))


lst1 = [1,3,5,7]
lst2 = [2,4,6,8,10]
# 水桶效应,和zip一样
m = map(lambda x,y,z:x+y+z,lst1,lst2,[5,2,3,5,2])
print(list(m))