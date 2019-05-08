# 列表-增(append,insert,extend)
# lst = ["麻花藤","林俊杰","周润发","Disman"]
# print(lst)
# lst.append("张杰")
# print(lst)

# lst = []
# while True:
#     content = input("请输入要录入的员工信息，输入Q退出：")
#     if content.upper() == "Q":
#         break
#     lst.append(content)
# print(lst)

# 列表-指定位置插入
# lst = ["麻花藤","林俊杰","周润发","Disman"]
# lst.insert(1,"Disman1") #在指定位置插入元素，原来的元素向后移动一位
# print(lst)

# 迭代添加(list是可以迭代添加的)
# lst = ["王志文", "张一⼭", "苦海无涯"]
# lst.extend(["麻花藤", "麻花不不疼"])
# print(lst)

# 列表-删 （pop,remove,clear,del）
# lst = ["麻花藤", "王剑林", "李嘉诚", "王富贵"]
# deleted = lst.pop(1)  # 如果不填写引索，那么就会删除最后一个
# print(deleted)
# print(lst)

# lst.remove("李嘉诚")
# print(lst)
# lst.remove("哈哈")  # 删除不存在的元素会报错
# print(lst)

# lst.clear() # 清空列表
# print(lst)

# 切片删除
# del lst[1:3]
# print(lst)

# 列表-修改
# lst = ["太⽩", "太⿊", "五⾊", "银王", "⽇天"]
# lst[1] = "太污"
# print(lst)

# lst[1:4:2] = ["麻花藤", "哇靠"] # 切⽚修改也OK. 如果步⻓不是1, 要注意. 元素的个数
# print(lst)

# lst[1:4] = ["李嘉诚个⻳⼉⼦"] # 如果切⽚没有步长或者步长是1. 则不用关心个数
# print(lst)

# 列表是一个可迭代的对象，所以可以for循环
# for el in lst:
#     print(el)


# lst = ["太白", "太黑", "无色", "银王", "日天", "太白", "太黑","太白"]
# c = lst.count("太黑") # 统计"太白"出现的次数
# print(c)

# lst = [1,11,22,2]
# lst.sort() # 排序。默认升序
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = ["太⽩", "太⿊", "五⾊", "银王", "⽇天"]
# print(lst)
# lst.reverse()  # list左右翻转
# print(lst)

# l = len(lst)  # 列表长度
# print(l)

# 三.列表的嵌套
#   采用降维操作，一层一层的看就好
# lst = [1, "太白", "wusir", ["马虎疼", ["可口可乐"], "王剑林"]]
# print(lst)

# 找到wusir
# print(lst[2])

# 找到“太白”,"wusir"
# print(lst[1:3])

# 找到“太白”的“白”字
# print(lst[1][1])

# 将wusir拿到. 然后⾸字⺟⼤写. 再扔回去
# s = lst[2]
# s = s.capitalize()
# lst[2] = s
# print(lst)
# 简写
# lst[2] = lst[2].capitalize()
# print(lst)

# 把太⽩换成太⿊
# lst[1] = lst[1].replace("白","黑")
# print(lst)

# 把马虎疼换成麻花藤
# lst[3][0] = lst[3][0].replace("马虎疼","麻花藤")
# print(lst)

# lst[3][1].append("雪碧")
# print(lst)

# 常用操作
# lst = ["王尼玛","贝克舒塔","黑猫警长","葫芦娃","舒克贝塔","舒克贝塔"]
# # print(len(lst))
# print(lst.count("舒克贝塔"))

lst = [1,2,4,1,53,56,72,21]
# lst = ["王尼玛","贝克舒塔","黑猫警长","葫芦娃","舒克贝塔","舒克贝塔"]
lst.sort()
# lst.sort(reverse=True)
print(lst)



