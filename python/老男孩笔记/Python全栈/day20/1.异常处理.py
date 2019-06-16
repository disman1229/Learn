
# 万能异常
def buy():
    pass
def back():
    pass
def show():
    pass
def main():
    l = [('购物',buy),('退货',back),('查看订单',show)]
    while True:
        for num,i in enumerate(l,1):
            print(num,i[0])
        num = int(input('num >>>'))
        print(l[num - 1])
        print('用户在选择了%s操作之后发生了不可知的异常'%l[num-1][0])
        # func = l[num-1][1]
        # func()
main()
