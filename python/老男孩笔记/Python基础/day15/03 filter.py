
# lst = ["张无忌","张铁林","鲁班","安琪拉","程咬金","大乔"]
# def func(el):
#     if el[0] == "张":
#         return False    # 不想要的
#     else:
#         return True

# 筛选,
# f = filter(lambda el : el[0] != "张",lst)    # 将lst中的每一项传递给func,所有返回True的都会保留,所有返回False都会被过滤掉

# print("__iter__" in dir(f)) # 判断是否可迭代
# for e in f:
#     print(e)


# lst = [
#     {"name":"鲁班","score":48},
#     {"name":"程咬金","score":58},
#     {"name":"后裔","score":38},
#     {"name":"花木兰","score":91},
#     {"name":"大乔","score":93},
# ]
#
# f = filter(lambda el:el['score'] > 60,lst)
# print(list(f))