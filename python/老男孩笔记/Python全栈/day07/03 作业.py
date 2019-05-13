# 一.判断一个数是否是水仙花数, 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数, 例如: 153 = 1**3 + 5**3 + 3**3

# num = input("请输入你想查的数:")
# huashu = 0
# for i in num:
#     huashu = huashu + int(i)**3
# if int(num) == huashu:
#     print("这个数是水仙花数")
# else:
#     print("不是水仙花数")


# 二.给出一个纯数字列表. 请对列表进行排序(升级题).
# 思路:
# 1.完成a和b的数据交换. 例如, a = 10, b = 24 交换之后, a = 24, b = 10
# 2.循环列表. 判断a[i]和a[i+1]之间的大小关系, 如果a[i]比a[i+1]大. 则进行互换.循环结束的时候. 当前列表中最大的数据就会被移动到最右端.
# 3.想一想, 如果再次执行一次上面的操作. 最终第二大的数据就移动到了右端. 以此类推.如果反复的进行执行相应的操作. 那这个列表就变成了一个有序列表.
# lst = [6,5,7,1,2,6,4,5]
# a = 10
# b = 5
# a,b = b,a
# print(a,b)

# 冒泡排序
# count = 0
# while count < len(lst):
#     i = 0
#     j = 1
#     while j < len(lst) - i:
#         if lst[i] > lst[i + 1]:
#             lst[i],lst[i + 1] = lst[i+ 1],lst[i]
#         i += 1
#     count += 1
# print(lst)

# 三.完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# 随机数:
# from random import randint
# s = set()
# while len(s) < 7:
# while int(len(s)) < 7:
#     s.add(randint(1,36))
# lst = list(s)
# lst.sort()
# print(lst)

# 四. 税务部门征收所得税. 规定如下:
#         1). 收入在2000以下的. 免征.
#         2). 收入在2000-4000的, 超过2000部分要征收3%的税.
#         3). 收入在4000-6000的, 超过4000部分要征收5%的税.
#         4). 收入在6000-10000的, 超过6000部分要征收8%的税.
#         4). 收入在10000以上的, 超过部分征收20%的税.
#     注, 如果一个人的收入是8000, 那么他要交2000到4000的税加上4000到6000的税加上6000到8000的税.
#         收入 = 8000-(4000-2000)*3%-(6000-4000)*4%-(8000-6000)*8%
# 让用户输入它的工资, 计算最终用户拿到手是多

# salary = int(input("请输入你的工资:"))
# if salary < 2000:
#     print("你的实际到手工资为%s" % salary)
# elif 2000 < salary < 4000:
#     salary = salary - (salary-2000) * 0.03
#     print("扣税后工资: %s" % salary)
# elif 4000 < salary < 6000:
#     salary = salary - (salary-2000) * 0.03 - (salary - 4000) * 0.05
#     print("扣税后工资: %s" % salary)
# elif 6000 < salary <= 10000:
#     salary = salary - (salary-2000) * 0.03 - (salary - 4000) * 0.05 - (salary - 6000) * 0.08
#     print("扣税后工资: %s" % salary)
# else:
#     salary = salary - (salary-2000) * 0.03 - (salary - 4000) * 0.05 - (salary - 6000) * 0.08 - (salary - 10000) * 0.2
#     print("扣税后工资: %s" % salary)