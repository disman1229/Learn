'''
查询的逻辑都在本模块中
'''
from conf import settings
def select():
    condition = input('>>>')
    # 收到命令要处理一下
    # 要到文件中去查
    # 要打开文件
    # 文件名怎么取????
    staff_info = settings.staffinfo
    with open(staff_info) as f:
        for line in f:
            line_lst = line.strip().split(',')
            id = line_lst[0]
            name = line_lst[1]
            age = line_lst[2]
            phone = line_lst[3]
            job = line_lst[4]
    
