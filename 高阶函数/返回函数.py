# from socket import AF_X25


# def calc_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# print(calc_sum(1, 2, 3))
# f = lazy_sum(1, 2, 3)
# print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())

def build(x, y):
    return x*x + y*y
f = build(1, 2)
print(f)