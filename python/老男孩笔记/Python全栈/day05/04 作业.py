# 1.有如下变量（tu是个元祖），请实现要求的功能
# tu = ("alex",[11,22,{"k1":"v1","k2":["age","name"],"k3":(11,22,33)},44])
# a.讲述元祖的特性
#   元素俗称不可变列表，不可以被改变
# b.请问tu变量中的第一个元素"alex"能否被修改？
#   不能
# c.请问tu变量中的"k2"对应的值是什么？是否能被修改？如果可以，请在其中添加一个元素"Seven"
#   可以
# tu[1][2]["k2"].append("Seven")
# print(tu)
# d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以请在其中增加一个"Seven"
#   不可以

# 2.字典dic
# dic = {"k1":"v1","k2":"v2","k3":[11,22,33]}
# a.请循环输出所有的key
# for k in dic.keys():
#     print(k)
# b.请循环输出所有的value
# for v in dic.values():
#     print(v)
# c.请循环输出所有的key,value
# for k,v in dic.items():
#     print(k,v)
# d.请在字典中添加一个键值对，"k4":"v4",输出添加后的字典
# dic["k4"] = "v4"
# print(dic)
# e.请在字典中修改"k1"对应的值为"alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)
# f.请在k3对应的值中追加一个元素44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)
# g.请在k3对应的值的第一位插入一个元素18，输出修改后的字典
# dic["k3"].insert(0,18)
# print(dic)

# 3.
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# a.给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'。

# av_catalog.get("欧美").get("www.youporn.com").insert(1,"量很大")
# av_catalog["欧美"]["www.youporn.com"].insert(1,"量很大")
# print(av_catalog)

# b.将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"]["x-art.com"].pop(1)  # pop删除
# av_catalog["欧美"]["x-art.com"].remove("全部收费,屌丝请绕过")  # remove删除
# print(av_catalog)

# c.将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表中增加"金老板最喜欢这个"。
# av_catalog["欧美"]["x-art.com"].append("金老板最喜欢这个")
# print(av_catalog)

# d.将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# print(av_catalog)

# e.给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"]["1048"] = ['一天就封了']
# av_catalog["大陆"].setdefault("1048","['一天就封了']")
# print(av_catalog)

# f.删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# av_catalog["欧美"].pop("letmedothistoyou.com")
# del av_catalog["欧美"]["letmedothistoyou.com"]
# print(av_catalog)

# g.给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog["大陆"]["1024"].insert(0,'可以爬下来')
# print(av_catalog)

# 4.有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....} （升级题）
# dic = {}
# s = "k:1|k1:2|k2:3|k3:4"
# for kv in s.split("|"):
#     k,v = kv.split(":")
#     dic[k] = int(v)
#     # dic.setdefault(k,int(v))
# print(dic)

# 5.元素分类
# 有如下值li = [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# dic = {"k1":[],"k2":[]}
# li = [11,22,33,44,55,66,77,88,99,90]
# for c in li:
#     if c == 66:
#         continue
#     if c > 66:
#         dic["k1"].append(c)
#     else:
#         dic["k2"].append(c)
# print(dic)

# 6.输出商品列表，用户输入序号，显示用户选中的商品(升级题)
#   商品：
#         good = [
#             {"name":"电脑","price":1999},
#             {"name":"鼠标","price":10},
#             {"name":"游艇","price":20},
#             {"name":"美女","price":998},
#         ]
#   要求：1：页面显示 序号 + 商品名称 + 商品价格，如：
#           1 电脑 1999
#           2 鼠标 10
#           …
#        2：用户输入选择的商品序号，然后打印商品名称及价格
#        3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#        4：用户输入Q或者q，退出程序。
# goods = [
#     {"name":"电脑","price":1999},
#     {"name":"鼠标","price":10},
#     {"name":"游艇","price":20},
#     {"name":"美女","price":998},
# ]
# while 1:
#     for i in goods:
#         print(goods.index(i) + 1,i["name"],i["price"])
#     good = input("请输入你想要的商品编号,输入Q退出:")
#
#     if good.isdigit() and  0 < int(good) < len(goods):
#         i_index = int(good) - 1
#         print(goods[i_index]["name"],goods[i_index]["price"])
#     elif good.upper() == "Q":
#         break
#     else:
#         print("你输入的有误,请重新输入!")
