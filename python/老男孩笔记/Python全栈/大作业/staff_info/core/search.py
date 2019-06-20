'''
查询的逻辑都在本模块中
'''
from conf import settings
def select():
    find_info = '''
        =*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*=
        本系统支持以下三种查询方法(查询条件分别为：age、dept、enroll_date):
        1、select name, age where age>22
        2、select * where job=IT
        3、select * where phone like 133   
        '''
    condition = input('>>>')
    staff_info = settings.staffinfo
    select_lst = []
    with open(staff_info) as f:
        for line in f:
            line_lst = line.strip().split(',')
            print(line_lst)
    num1 = condition[6:condition.find('where')].strip()
    num2 = condition[condition.find('where')+6:].strip()
    if 'age' in condition:
        num2 = num2.split('>')
        if num2[1] > line_lst[2]:
            num1 = num1.split(',')