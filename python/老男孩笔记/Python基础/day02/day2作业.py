'''
1.判断下列语句是True还是False
    1) 1>1 or 3<4 or 4>5 and 2>1 and 9>8 or 7<6
    2) not 2>1 and 3<4 or 4>5 and 2>1 and 9>8 or 7<6
答：1）True； 2）Flase
'''

'''
2.求出下列逻辑语句的值
    1) 8 or 3 and 4 or 2 and 0 or 9 and 7
    2) 0 or 2 and 3 and 4 or 6 and 0 or 3
答：1) 8; 2) 4
'''

'''
3.下列结果是什么？
    1) 6 or 2>1
    2) 3 or 2>1
    3) 0 or 5<4
    4) 5<4 or 3
    5) 2>1 or 6
    6) 3 and 2>1
    7) 0 and 3>1
    8) 2>1 and 3
    9) 3>1 and 0
    10) 3>1 and 2 or 2<3 and 3 and 4 or 3>2
    
答：1) 6; 2) 3; 3) False; 4) 3; 5) True; 6) True; 7) 0; 8) 3; 9) 0; 10) 2
'''

'''
4.while循环语句的基本结构？
while 条件语句:
    循环体（代码块）
'''

'''
5.利用while语句写出猜大小游戏：
    设定一个理想的数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
    如果比66小，则显示猜测的结果小了；
    只有等于66，显示猜测的结果正确，然后退出循环。
答案如下：
n = 66
while True:
    num = int(input("你输入你的数字："))
    if num > n:
        print("你猜的大了")
    elif num < n:
        print("你猜小了")
    else:
        print("你猜对了")
        break
'''
'''
6.在第五题的基础上升级:
    给用户三次猜测机会，如果三次之内猜对了，则显示猜测正确，退出循环；如果三次之内没有猜测真确，则自动退出循环，并显示”太笨了你。“
答案如下：
count = 1
n = 66
while count <= 3:
    num = int(input("你输入你的数字："))
    if num > n:
        print("你猜的大了")
    elif num < n:
        print("你猜小了")
    else:
        print("你猜对了")
        break
    print("你已经猜了%d次了" %count)
    count += 1
else:
    print("太笨了你。")
'''

'''
7.是用while循环输入1,2,3,4,5,6,8,9,10
答案1如下：
count = 1
while count <= 10:
    if count != 7:
        print(count)
    count +=1
答案2如下：  
count = 1
while count <= 10:
    if count == 7:
        count +=1
        continue
    print(count)
    count +=1
'''

'''
8.求1-100所有数的和
答：
count = 1
num = 0
while count <= 100:
    num = num + count
    count += 1
    print(num)
'''

'''
9.输出100以内所有的奇数
答：
count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count += 1
'''

'''
10.输出100以内所有的偶数
答：
count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1
'''

'''
11.求1-2+3-4+5...99的所有数的和
答：
sum = 0
count = 1
while count < 100:
    if count % 2 == 0: #偶数
        sum = sum - count
    if count % 2 == 1: #奇数
        sum =sum + count
    count +=1
print(sum)
'''

'''
12.用户登录（三次输错机会）且每次输错误时会显示剩余错误次数（提示
：使用字符串格式化）
答：
count = 1
while count <= 3:
    name = input("请输入登录名：")
    password = input("请输入密码：")
    if name == "disman" and password =="123":
        print("登录成功！")
        break
    else:
        print("用户名或密码错误！")
        print("剩余输入%s次" % (3 - count))
    count += 1
'''

'''
13.用户输入一个数，判断这个数是否是一个质数（升级题）
'''
num = int(input("请输入你要查的数："))
while num > 1:
    if (num % 2) == 0:
        print(num,'不是质数')
        break
    else:
        print(num,'是质数')
        break
else:
    print(num,'不是质数')
'''
14.输入一个广告标语，判定这个广告是否合法，根本最新的广告法来判断，广告法内容过多，我就判断是否包含‘最’，‘第一’，‘稀缺’，‘国家级’等字样，如果包含。提示，广告不合法
    例如：1.老男孩Python世界第一。  ==>不合法
         2.今年过年不收礼，收礼只收脑白金。  ==>合法
答：
while True:
    ad = input("请输入你的广告标语：")
    if "第一" in ad or "最" in ad or "稀缺" in ad or "国家级" in ad :
        print("你输入的广告标语不合法")
        continue
    else:
        print(ad+" ==>合法")
'''

'''
14.输入一个数，判断这个数是几位数（用算法实现）（升级题）
'''
# c = 0
# a=int(input("the number you want type in:"))
# while a!=0:
#     a = a / 10
#     c += 1
# print(c)

