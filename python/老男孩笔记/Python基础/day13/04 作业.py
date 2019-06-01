

# 1.整理今天的博客，写课上代码，整理流程图
# 2.用列表推导式做下列小题
#   (1) 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# lst = ["asd","fghj","klasd","zx","cvb"]
# ll = [i.upper() for i in lst if len(i) >= 3]
# print(ll)


#   (2) 求(x,y)其中x中0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# lst = [(x,y) for x in range(5) for y in range(5) if x%2 == 0 and y%2 == 1]
# # y = [y for y in range(6) if y % 2 == 1]
# print(lst)

#   (3) 求M中3,6,9组成的列表 M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([i[2] for i in M])

# print([[i-2,i-1,i-0] for i in [3,6,9]])

#   (4) 求出50以内能被3整除的数的平方，并放入到一个列表中
# lst = [i*i for i in range(1,50) if i % 3 == 0]
# print(lst)

#   (5) 构建一个列表:['python1期'，'python2期'，'python3期'，'python4期'，'python5期'，'python6期'，'python7期'，'python8期'，'python9期'，'python10期']
# lst = ["Python"+str(el)+"期" for el in range(1,11)]
# print(lst)

#   (6) 构建一个列表:[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]
# lst = [(i,i+1) for i in range(6)]
# print(lst)

#   (7) 构建一个列表:[0,2,4,6,8,10,12,14,16,18]
# lst = [i for i in range(20) if i % 2 == 0]
# print(lst)

#   (8) 有一个列表 ll = ['鲁班七号','安琪拉',’程咬金','大乔']将其构造成这种列表,['鲁班七号1','安琪拉2',’程咬金3','大乔4']
# ll = ['鲁班七号','安琪拉','程咬金','大乔']
# lst = [el + str(ll.index(el)) for el in ll]
# print(lst)

# lst = [ll[i]+str(i) for i in range(len(ll))]
# print(lst)

# lst = [el+str(index) for index,el in enumerate(ll)]
# print(lst)

# (9) 有以下数据类型
# x = {
# 'name':'鲁班七号',
# 'values':[
#         {'timestamp':1517991992.94,'value':100,},
#         {'timestamp':1517992000.94,'value':200,},
#         {'timestamp':1517992014.94,'value':300,},
#         {'timestamp':1517992744.94,'value':350,},
#         {'timestamp':1517992844.94,'value':280,}
#     ]
# }
# 将上面的数据通过列表推导式转换成下面的类型:[[1517991992.94,100],[1517992000.94,200],[1517992014.94,300],[1517992744.94,350],[151799844.94,280]]

# lst = [[el['timestamp'],el['value']] for el in x['values']]
# print(lst)
