
# 1.用map来处理字符串列表,把列表中所有的人后面加上_sb
# name = ['luban','chengyaojin','daqiao']
# print(list(map(lambda x:x+'_sb',name)))

# 2.用map来处理下述l,然后用list得到一个新的列表,列表中每个人的名字都是sb处理
# l = [{'name':'luban'},{'name':'daqiao'}]
# print(list(map(lambda x:x['name']+'sb',l)))

# 3.用filter来处理,得到股票的价格大于20的股票名字
# shares = {
#     'IBM':36.6,
#     'Lenovo':23.2,
#     'Asus':21.2,
#     'Sony':18.3,
# }
# print(list(filter(lambda x:x>20,shares.values())))
# print(list(filter(lambda x:shares[x] > 20,shares)))

# 4.有下面字典,得到购买每只股票的总价格,并放在一个迭代器中.
# 结果:list = [9110.0,27161.0,....]
# portfolio = [
#     {'name':'IBM','shares':100,'price':91.1},
#     {'name':'AAPL','shares':50,'price':543.22},
#     {'name':'FB','shares':200,'price':21.09},
#     {'name':'HPQ','shares':35,'price':31.75},
#     {'name':'YHOO','shares':45,'price':16.35},
#     {'name':'YHOO','shares':75,'price':115.65},
# ]
# print(list(map(lambda x:x['shares'] * x['price'],portfolio)))

# 5.还是上面的字典,用filter过滤出单价大于100的股票
# print(list(filter(lambda x:x['price'] > 100,portfolio)))

# 6.有下列三种数据类型
# l1 = [1,2,3,4,5,6]
# l2 = ['luban','daqiao','xiaoqiao','程咬金','后裔']
# tu = ('**','***','****','*****')
# 写代码,最终得到的是(每一个元祖第一个元素>2,第三个*至少是4个)
# [(3,'xiaoqiao','****'),(4,'程咬金','******')]这样的数据
# print(list(filter(lambda x:x[0] > 2 and len(x[2]) > 3,zip(l1,l2,tu))))

# 7.有如下数据类型
# ll = [
#     {'sales_volumn':108},
#     {'sales_volumn':337},
#     {'sales_volumn':475},
#     {'sales_volumn':396},
#     {'sales_volumn':172},
#     {'sales_volumn':9},
#     {'sales_volumn':58},
#     {'sales_volumn':272},
#     {'sales_volumn':456},
#     {'sales_volumn':440},
#     {'sales_volumn':239},
#     {'sales_volumn':0},
# ]
# 将ll按照列表中的每个字典的values大小进行排序,形成一个新的列表
# print(sorted(ll,key=lambda x:x['sales_volumn']))