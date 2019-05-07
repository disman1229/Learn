'''
1.有变量name="aleX leNb"完成下列操作：
    1）移除 name 变量对应的值两边的空格，并输出结果
    2）移除 name 变量左边的"al"，并输出结果
    3）移除 name 变量右边的"Nb"，并输出结果
    4）移除 name 变量开头的"a"与最后的"b"，并输出出来结果
    5）判断 name 变量是否以"al"开头，并输出结果
    6）判断 name 变量是否以"Nb"结尾，并输出结果
    7）将 name 变量对应值中的所有"l"替换为"p"，并输出结果
    8）将 name 变量对应的之中的第一个"l"替换为"p"，并输出结果
    9）将 name 变量中对应的值根据所有"l"分割，并输出结果
    10）将 name 变量对应的值根据第一个"l"分割，并输出结果
    11）将 name 变量对应的值变成大写，并输出结果
    12）将 name 变量对应的值变成小写，并输出结果
    13）将 name 变量对应的值首字母"a"大写，并输出结果
    14）判断 name 变量对应的值的字母"l"出现几次，并输出结果
    15）如果判断 name 变量对应的值前四位"l"出现几次，并输出结果
    16）从 name 变量对应的值中找到"N"对应的引索（如果找不到则报错），并输出结果
    17）从 name 变量对应的值中找到"N"对应的引索（如果找不到则返回-1），并输出结果
    18）从 name 变量对应的值中找到"X le"对应的引索，并输出结果
    19）请输出 name 变量对应的值的第2个字符？
    20）请输出 name 变量对应的值的前3个字符？
    21）请输出 name 变量对应的值的后2个字符？
    22）请输出 name 变量对应的值中"e"所在引索位置？
2.有字符串s="123a4b5c"
    1）通过对s切片形成新的字符串s1，s1="123"
    2）通过对s切片形成新的字符串s2，s2="a4b"
    3）通过对s切片形成新的字符串s3，s3="1345"
    4）通过对s切片形成字符串s4，s4="2ab"
    5）通过对s切片形成字符串s5，s5="c"
    6）通过对s切片形成字符串s6，s5="ba2"
3.使用while和for循环分别打印字符串s="asdfer"中的每个元素
4.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
5.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字节加上sb，例如：asb,bsb,csb...gsb。
6.使用for循环对s="321"进行循环，打印内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发"
7.实现一个整数的加法计算器（两个数相加）：
    如：content = input("请输入内容：")，用户输入：5+9或者5+ 9或者5 + 9，然后进行分割运算
8.升级题：实现一个整数的加法计算器（多个数相加）：
    如：content = input("请输入内容：")，用户输入：5+9+6 +12+ 13，然后进行分割在进行运算
9.计算用户输入的内容中有几个整数（以个位数为单位）
    如：content = input("请输入内容：") #如fhdal234slfh98769fjdla
10.写代码，完成下列需求：
    用户可持续输入（用while循环），用户使用情况：
    输入A，则显示走大路回家，然后在让用户进一步选择：
        是选择公交车，还是步行？
        选择公交车，显示10分钟到家，并退出整个程序
        选择步行，显示20分钟到家，并退出整个程序
    输入B，则显示走小路回家，并退出整个程序
    输入C，则显示绕道回家，然后在让用户进一步选择：
        是选择在游戏厅玩会，还是网吧？
        选择游戏厅，则显示"一个半小时到家，爸爸在家，拿棍子等你。"并让其重新输入A,B,C选项。
        选择网吧，则显示"两个小时到家，妈妈已经做好战斗准备。"并让其重新输入A,B,C选项。
11.写代码，计算1-2+3...+99中除88以外所有数的总和
12.（升级题）判断一句话是否是回文，回文：正着念和反着念是一样的，例如：上海自来水来自海上
13.输入一个字符串，要求判断在这个字符串中的大写字母，小写字母，数字，其他字符共出现几次，并输出结果
14.制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意实现，如：敬爱可爱的xxx，最喜欢在xxx地方干xxx
15.（升级题）给出百家姓，然后用户输入一个人的名字，判断这个人是否是百家姓中的姓氏

明日默写内容：
    分别用while，for循环输出字符串s = input("你想输入的内容")的每个字符。
'''

#  第一题答案
'''
name = "aleX leNb"
# 1.1
print(name.strip())
#1.2
print(name[2:])
#1.3
print(name[:-2])
#1.4
print(name[1:8])
#1.5
print(name.startswith("al"))
#1.6
print(name.endswith("Nb"))
#1.7
print(name.replace("l","p"))
#1.8
print(name.replace("l","p",1))
#1.9
print(name.split("l"))
#1.10
print(name.split("l",1))
#1.11
print(name.upper())
#1.12
print(name.lower())
#1.13
print(name.capitalize())1229

print(name.replace("a","A")
#1.14
print(name.count("l"))
#1.15
s1 = name[:4]
print(s1.count("l"))
#1.16
print(name.index("N"))
#1.17
print(name.find("N"))
#1.18
print(name.find("X le"))
#1.19
print(name[1])
#1.20
print(name[:3])
#1.21
print(name[-2:])
#1.22
print(name.find("e"))

count = 0
while count < len(name):
    if name[count] == "e":
        print(count)
    count += 1
'''

# 第二题答案
'''
s="123a4b5c"
#2.1
s1 = s[0:3]
print(s1)
#2.2
s2 = s[3:6]
print(s2)
#2.3
s3 = s[::2]
print(s3)
#2.4
s4 = s[1:7:2]
print(s4)
#2.5
s5 = s[-1]
print(s5)
s6 = s[-3:-8:-2]
print(s6)
'''

# 第三题答案
'''
# 3 方法一：while
s="asdfer"
count = 0
while count < len(s):
    print(s[count])
    count += 1
print("-" * 10)
# 3 方法二：for
for i in s:
    print(i)
print("-" * 10)
count = len(s)
for s in s:
    print(s)
'''

'''
第四题答案
s="asdfer"
for c in s:
    print(s)
'''

# 第五题答案
# s="abcdefg"
# for i in s:
#     print(i+"sb")

# 第六题答案
# s = "321"
# for i in s:
#     print("倒计时%s秒" % i)
# else:
#     print("出发！")

# 第七题答案
# content = input("请输入内容：")
# lst = content.split("+")
# s1 = lst[0]
# s2 = lst[1]
# a1 = int(s1)
# a2 = int(s2)
# print(a1+a2)

# 第九题答案
# content = input("请输入内容：")
# count = 0
# for c in content:
#     if c.isdigit():
#         count += 1
# print(count)

# 第十题答案
# while True:
#     gohome = input("请选择A,B,C：").strip().upper()
#     if gohome == "A":
#         print("走大路回家")
#         traffic = input("请输入公交还是走路：")
#         if traffic == "公交":
#             print("十分钟到家")
#             break
#         elif traffic == "走路":
#             print("二十分钟到家")
#             break
#         else:
#             print("我还没想好")
#     elif gohome == "B":
#         print("走小路回家")
#         break
#     elif gohome == "C":
#         print("走小路回家")
#         naughty = input("请输入游戏厅还是网吧：")
#         if naughty == "游戏厅":
#             print("一个半小时到家，爸爸在家，拿棍子等着你")
#         elif naughty == "网吧":
#             print("两个小时到家，妈妈已经做好战斗准备")
#     else:
#         print("按照规矩填写")

# 第十一题答案
# count = 1
# sum = 0
# while count <= 99:
#     if count == 88:
#         count += 1
#         continue
#     if count %2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#     count += 1
# print(sum)

# 第十二题答案：
# s = "上海自来水来自海上"
# s1 = s[::-1]
# if s == s1:
#     print("是回文")
# else:
#     print("不是回文")

# 第十三题答案：
# digit_num = 0
# upper_num = 0
# lower_num = 0
# other = 0
# s = input("请输入内容：")
# for c in s:
#     if c.isupper():
#         digit_num += 1
#     elif c.islower():
#         upper_num += 1
#     elif c.isdigit():
#         lower_num += 1
#     else:
#         other += 1
# print("大写字母有：{digit_num} 个，小写字母有：{upper_num} 个,数字有：{lower_num},其他字符：{other}" .format(digit_num=digit_num,upper_num=upper_num,lower_num=lower_num,other=other))

# 第十四题答案（等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意实现）
# name = input("名字：")
# site = input("地点：")
# hobby = input("爱好：")
# print("敬爱可爱的{name}，最喜欢在{site}，{hobby}".format(name=name,site=site,hobby=hobby))

# 第十五题答案

s = "欧阳娜娜"
ss = " "
name = '''赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。
滕殷罗毕，郝邬安常。
乐于时傅，皮卞齐康。
伍余元卜，顾孟平黄。
和穆萧尹，姚邵湛汪。
祁毛禹狄，米贝明臧。
计伏成戴，谈宋茅庞。
熊纪舒屈，项祝董梁。
杜阮蓝闵，席季麻强。
贾路娄危，江童颜郭。
梅盛林刁，钟徐邱骆。
高夏蔡田，樊胡凌霍。
虞万支柯，昝管卢莫。
经房裘缪，干解应宗。
丁宣贲邓，郁单杭洪。
包诸左石，崔吉钮龚。
程嵇邢滑，裴陆荣翁。
荀羊於惠，甄曲家封。
芮羿储靳，汲邴糜松。
井段富巫，乌焦巴弓。
牧隗山谷，车侯宓蓬。
全郗班仰，秋仲伊宫。
宁仇栾暴，甘钭厉戎。
祖武符刘，景詹束龙。
叶幸司韶，郜黎蓟薄。
印宿白怀，蒲邰从鄂。
索咸籍赖，卓蔺屠蒙。
池乔阴鬱，胥能苍双。
闻莘党翟，谭贡劳逄。
姬申扶堵，冉宰郦雍。
卻璩桑桂，濮牛寿通。
边扈燕冀，郏浦尚农。
温别庄晏，柴瞿阎充。
慕连茹习，宦艾鱼容。
向古易慎，戈廖庾终。
暨居衡步，都耿满弘。
匡国文寇，广禄阙东。
欧殳沃利，蔚越夔隆。
师巩厍聂，晁勾敖融。
冷訾辛阚，那简饶空。
曾毋沙乜，养鞠须丰。
巢关蒯相，查后荆红。
游竺权逯，盖益桓公。
万俟司马，上官欧阳。
夏侯诸葛，闻人东方。
赫连皇甫，尉迟公羊。
澹台公冶，宗政濮阳。
淳于单于，太叔申屠。
公孙仲孙，轩辕令狐。
钟离宇文，长孙慕容。
鲜于闾丘，司徒司空。
丌官司寇，仉督子车。
颛孙端木，巫马公西。
漆雕乐正，壤驷公良。
拓跋夹谷，宰父谷梁。
晋楚闫法，汝鄢涂钦。
段干百里，东郭南门。
呼延归海，羊舌微生。
岳帅缑亢，况郈有琴。
梁丘左丘，东门西门。
商牟佘佴，伯赏南宫。
墨哈谯笪，年爱阳佟。
第五言福，百家姓终。'''
for c in s:
    ss = ss + c
count = 0
while count < len(name):
    n = name[count]
    count += 1
    if n in ss:
        print(n)

