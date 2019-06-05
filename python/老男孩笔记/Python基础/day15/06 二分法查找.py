

# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
#
# # 使用二分法可以提高效率   前提条件有序序列
# n = 88
# left = 0
# right = len(lst) - 1
#
# while left <= right: # 边界,当右边比左边还小的时候退出循环
#     mid = (left + right) // 2   # 这里必须是整除,应为索引没有小数
#     if lst[mid] > n:
#         right = mid - 1
#     if lst[mid] < n:
#         left = mid + 1
#     if lst[mid] == n:
#         print("找到这个数")
#         break
# else:
#     print("没有这个数!")


# 递归来完成二分法
# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
# def func(n,left,right):
#     if left <= right:
#         mid = (left + right) // 2
#         if n > lst[mid]:
#             left = mid + 1
#             return func(n,left,right)  # 递归,递归入口
#         elif n < lst[mid]:
#             right = mid - 1
#             # 深坑,函数的返回值返回给调用者
#             return func(n,left,right)  # 递归
#         elif lst[mid] == n:
#             # print("找到了")
#             return mid
#     else:
#         print("没找到")
#         return -1   # 避免返回None
#
# # 找66,左边界0,右边界len(lst) - 1
# ret = func(66,0,len(lst) - 1)
# print(ret)


# 递归二分法另一种形式
# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
# def func(lst,target):
#     left = 0
#     right = len(lst) - 1
#     if left > right:
#         print("没有这个数")
#     middle = (left + right)//2
#     if target < lst[middle]:
#         return func(lst[:middle],target)
#     elif target > lst[middle]:
#         return func(lst[middle + 1:],target)
#     elif target == lst[middle]:
#         print("找到这个数了")
# func(lst,101)
