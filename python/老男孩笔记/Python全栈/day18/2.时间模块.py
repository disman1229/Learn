

import time
# time.sleep(2)
# print(123)

# time 模块主要用来和时间打交道的
# 时间格式
    # '2019-6-12' , '2019.6.12' 字符串时间类型,格式化时间 - 给人看的
    # 结构化时间
    # 1560318780.349285 浮点型数据类型,以 s 为单位,时间戳时间 - 给机器计算用的
# print(time.time())

# 格式化时间
# print(time.strftime('%Y-%m-%d %H:%M:%S'))   # str format time
# print(time.strftime('%c'))   # str format time
# print(time.strftime('%X'))   # str format time
# # print(time.strftime('%Y-%m-%d %X',time.localtime(26000000000)))   # str format time

# 结构化时间
# struct_time = time.localtime() # 北京时间
# tm_isdst=0 是否夏令时
# print(struct_time.tm_hour)
# print(struct_time.tm_mon)

# 时间戳换成字符串时间
# print(time.time())
# print(time.localtime(1560324611))
# print(time.gmtime(1560324611))
# ret = time.strftime('%y/%m/%d %H:%M:%S',time.localtime(150000000))
# print(ret)

# 字符串时间转时间戳时间
# struct_time = time.strptime('2019.5.12','%Y.%m.%d')
# print(struct_time)
# res = time.mktime(struct_time)
# print(res)

# 1.查看一个2000000000时间戳时间表示的年月日

# ret =  time.strftime('%Y-%m-%d',time.localtime(2000000000))
# print(ret)

# 2.将2008-8-8转换成时间戳时间

# struct_time = time.strptime('2008-8-8','%Y-%m-%d')
# ret = time.mktime(struct_time)
# print(ret)

# 3.将当前时间的当前月1号的时间戳时间取出来 - 函数
# def get_time():
#     st = time.localtime()
#     st2 =time.strptime('%s-%s-1'%(st.tm_year,st.tm_mon),'%Y-%m-%d')
#     return time.mktime(st2)
# print(get_time())

# 4.计算时间差
    # 2018-8-19 22:10:8     2018-8-20 11:07:3
    # 进过的时间时分秒

def timec(start_time,end_time):
    start_time = time.strptime(start_time,'%Y-%m-%d %H:%M:%S')
    start_mktime = time.mktime(start_time)
    end_time = time.strptime(end_time,'%Y-%m-%d %H:%M:%S')
    end_mktime = time.mktime(end_time)
    new_mktime = end_mktime - start_mktime
    ret_time = time.gmtime(new_mktime)
    return '过去了%d年%d月%d天%d小时%d分钟%d秒'%(ret_time.tm_year-1970,ret_time.tm_mon-1,ret_time.tm_mday-1,ret_time.tm_hour,ret_time.tm_min,ret_time.tm_sec)
print(timec('2018-8-19 22:10:8','2019-2-21 11:07:3'))