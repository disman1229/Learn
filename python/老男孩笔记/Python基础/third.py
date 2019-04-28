
# gender = input("你的性别？")
'''
if gender == '男的':
    print("滚蛋！")
print("吓死我了")

if gender == '女的':
    print("请进")
else:
    print("滚蛋")



if gender == '女的':
    age = input("你多大了啊？")
    if int(age) < 60:
        print("请进")
    else:
        print("大妈您去隔壁")
else:
    print("滚蛋！")


# 输入你兜里的钱
# 如果你兜里的钱大于500，喝啤酒吃炸鸡
# 如果你兜里的钱小于500，大于300，吃盖浇饭
# 如果你兜里的钱小于300，大于50，吃泡面
# 如果你兜里的钱小于50，今天减肥
money = input("输入你兜里的钱")
if int(money) > 500:
    print("喝啤酒吃炸鸡")
else:
    if int(money) > 300:
        print("盖浇饭")
    else:
        if int(money) > 50:
            print("泡面")
        else:
            print("减肥")
'''
money = int(input("请出入你兜里的钱："))
if money > 500:
    print("喝啤酒吃炸鸡")
elif money > 300:
    print("盖浇饭")
elif money > 50:
    print("泡面")
else:
    print("减肥")