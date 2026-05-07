# from functools import reduce
# def add (x, y):
#     return x + y
# reduce(add,[1,2,3,4,5,6,7,8,9])
# print(reduce(add,[1,2,3,4,5,6,7,8,9]))

# def fn(x,y):
#     return x * 10 + y
# reduce(fn,[1,3,5,7,9])
# print(reduce(fn,[1,3,5,7,9]))

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce


def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)
print('3*5*7*9=',prod([3,5,7,9]))
if prod([3,5,7,9]) != 945:
    print('测试失败!')
else:    print('测试成功!')