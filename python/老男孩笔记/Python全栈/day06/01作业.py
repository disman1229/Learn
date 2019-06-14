# 一.老男孩好声音选秀比赛评委在打分的时候呢, 可以进行输入. 假设, 老男孩有10个评委.让10个评委进行打分, 要求, 分数必须大于5分, 小于10分.
# count = 1
# while count <= 10:
#     score = input("请输入你的打分:")
#     if score.isdigit() and int(score) > 5 and int(score) <10:
#         print("第 %s 号评委的打分数是:"% count,score)
#         count += 1
#     else:
#         print("请输入正确的评分,分数必须大于5分,小于10分")
#         continue

# 二. 电影投票. 程序先给出一个目前正在上映的电影列表. 由用户给每一个电影投票.最终
# 将该用户投票信息公布出来 lst = ["金某梅", "解救吾先生", "美国往事", "西西里的美丽传说"]
# 结果: {"金某梅": 99, "解救吴先生": 80, "美国往事": 6, "西西里的美丽传说": 23}
# lst = ["金某梅", "解救吾先生", "美国往事", "西西里的美丽传说"]
# dic = {}
# for i in lst:
#     fen = input("请给电影<%s>打分:" % i)
#     dic[i] = int(fen)
# print(dic)

# 三.念数字.  给出一个字典. 在字典中标识出每个数字的发音. 包括相关符号. 然后由
# 用户输入一个数字. 让程序读出相对应的发音(不需要语音输出. 单纯的打印即可)
# dic = {
#     "-":"fu",
#     "0":"ling",
#     "1":"yi",
#     "2":"er",
#     "3":"san",
#     "4":"si",
#     "5":"wu",
#     "6":"liu",
#     "7":"qi",
#     "8":"ba",
#     "9":"jiu",
#     ".":"dian"
# }
# num = input("请输入你的数字:")
# for i in num:
#     print(dic[i] + " ",end="")

# 四.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (升级题)
# cars = ["鲁A32444","鲁B12333","京B8989M","黑C40678","黑C46555","沪B25041"]
# locals = {"沪":"上海","黑":"黑龙江","鲁":"山东","鄂":"湖北","湘":"湖南","京":"北京"}
# result = {}
# for car in cars:
#     location = locals[car[0]]
#     if result.get(location) == None:
#         result[location] = 1
#     else:
#         result[location] += 1
# print(result)

# 五.干掉主播. 现有如下主播收益信息, 按照要求, 完成相应操作:
# zhubo = {"卢本伟":122000,"冯提莫":189999,"金老板":99999,"吴老板":25000000,"alex":126}
# 1.计算各位主播收益的平均值.
# sum = 0
# for i in zhubo:
#     sum = sum + zhubo[i]
# mean = sum / len(zhubo)
# print(mean)
# 2.干掉收益小于平均值的主播.
# for i in list(zhubo):
#     if zhubo[i] < mean:
#         del zhubo[i]
# print(zhubo)
# 3.干掉卢本伟.
# zhubo.pop("卢本伟")
# print(zhubo)

# 六. is和==的区别:
# is 是对比两个值的内存地址是否一致,如果一致那么这两个值得指向的是同一个内存地址
# == 是对比这两个值是否完全相等

# 七. Unicode ,gbk,utf-8的转化.
# s = "鲁班七号"
# ds = (s.encode("gbk"))
# print(ds)
#
# ds1 = (s.encode("utf-8"))
# print(ds1)
#
# a = (ds.decode("gbk"))
# print(a)
#
# b = (ds1.decode("utf-8"))
# print(b)