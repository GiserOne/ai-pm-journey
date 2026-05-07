# 二、循环+列表
# numbers = [1,2,3,4,5]
# squared = []
# for num in numbers:
#     squared.append(num** 10)
# print(f"原始列表：{numbers}")
# print(f"平方后:{squared}")

# 给定一个名字列表 names = ["alice", "bob", "charlie"],用 for 循环遍历,把每个名字首字母大写后存到新列表 capitalized 里。最后打印 ["Alice", "Bob", "Charlie"]。
# names = ["alice", "bob", "charlie"]
# print(capitalized := [name.capitalize() for name in names])


# 给定一个价格列表 prices = [88, 120, 56, 200, 75],用 for 循环遍历,把所有大于 100 的价格打 8 折(乘以 0.8),其他保持不变,存到新列表 final_prices
prices = [88,120,56,200,75]
# finally_price = []
# for pri in prices:
#     if pri >= 100:
#         finally_price.append(pri*0.8)
#     else:
#         finally_price.append(pri)
# print(finally_price)
finally_price = [pri*0.8 if pri >= 100 else pri for pri in prices]
print(finally_price)
