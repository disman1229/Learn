# print("disman今年34，是一个中年，爱好是女，性别：男")
# print("disman1今年48，是一个中年，爱好是女，性别：男")
# print("disman3今年40，是一个中年，爱好是不详，性别：诡异")

# name = input("请输入名字：")
# age = input("请出入你的年龄：")
# hobby = input("请出入你的爱好：")
# gender = input("请出入你的性别：")

# print(name + "今年" + age + "岁，是一个中年，爱好是" + hobby + "，性别：" + gender)
# %s:表示字符串的占位符
# print("%s今年%s岁，是一个中年，爱好是%s，性别：%s" %(name,age,hobby,gender))

# a = 108
# s = "梁山水泊有%d个牛B的人物" %(a)
# print(s)

# name = "地球"
# print("%s上%%60都是水" % name) # 如果字符串中有了占位符，那么后面的所有占位的%都是占位符，需要转义
print("地球上%60都是水") # 这就话没有转义符，%还是%
