# def f(x):
#     return x * x

# result = f(5)
# print(result)

# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normal(name):
#     return name.capitalize()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normal,L1))
# print(L2)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
# def str2float(s):
    # 第一种写法
#     def fn(x,y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     s1 = s.split('.')
#     return reduce(fn,map(char2num,s1[0])) + reduce(fn,map(char2num,s1[1])) / 1000
# 第二种写法
def str2float(s):
    dot_index = s.index('.')    # 找到小数点位置
    s_new = s.replace('.', '')  # 去掉小数点
    # 转成整数 ÷ 10^位数
    return reduce(...) / 10 ** (len(s_new) - dot_index)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

