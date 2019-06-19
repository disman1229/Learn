from core import search

def home():
    print('欢迎来到员工信息查询中心')
    operate_lst = ['查询','修改','删除','添加']
    for index,item in enumerate(operate_lst,1):
        print(index,item)
    try:
        num = int(input('请选择您要做的操作 : '))  # 异常处理
        if num == 1:
            search.select()
    except ValueError:
        print('你输入的内容错误,请重新输入!')
        home()