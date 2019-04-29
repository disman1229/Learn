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

