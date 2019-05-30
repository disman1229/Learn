
'''
1.让用户输入金额
2.选择要购买的商品,加入购物车
3.当商品的总价超过了你的金额,提示余额不足
4.让用户输入N结算,输入Q退出
5.用户退出后,提示消费多少钱,还剩多少钱
'''

goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':15},
    {'name':'键盘','price':30},
    {'name':'硬盘','price':399},
    {'name':'内存','price':489},
]
fei_yong = 0
shop_car = {}   # 键 == 列表的索引,值 == 商品数量
money = input("请输入你的金额:")

if money.isdigit():
    # 真钱
    while 1:
        for i in range(len(goods)):
            print(i+1,goods[i]["name"],goods[i]["price"])
        # ===================商品展示============================
        choose = input("请输入您要购买的商品(输入n或者N结算,输入q或者Q退出):")
        if choose.isdigit() and 0 < int(choose) <= len(goods):
            # 让用户输入商品序号并判断是不是数字以及在不在正常输入范围内
            int_index = int(choose) - 1
            # 通过用户输入的内容减一,获取到goods的索引
            if shop_car.get(int_index) == None:
                shop_car[int_index] = 1
            else:
                shop_car[int_index] += 1

            # ================让用户把商品加入到购物车中====================
        elif choose.upper() == "N":
            # 结算
            for f in shop_car:
                fei_yong = fei_yong + shop_car[f] * goods[f]["price"]

            if int(money) - fei_yong >= 0:
                for k in shop_car:
                    print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
            else:
                print("余额不足")
                # for i,v in enumerate(shop_car,1): # 枚举
                #     print(f'序号:{i},商品:{goods[v]["name"]},数量:{shop_car[v]}')
                #
                # str_del = int(input("请删除商品对应的序号:"))
                # shop_car[str_del - 1] = shop_car[str_del - 1] - 1
                # if shop_car[str_del - 1] == 0:
                #     shop_car.pop(str_del - 1)

        elif choose.upper() == "Q":
            # 退出
            print(f"您此次共消费{fei_yong},剩余余额{int(money) - fei_yong}")
            break
        else:
            print("输入有误,请重新输入!")
else:
    # 输入非数字
    print("请正确输入!")