# def count_up_to(n):
#     i = 0
#     while i <= n:
#         yield i*i  # yield 语句会暂停函数的执行，并返回一个值给调用者，同时保留函数的状态，以便下次继续执行
#         i += 2
# # 使用生成器函数
# for number in count_up_to(10):
#     print(number)

#     # print(list(count_up_to(5)))  # 将生成器转换为列表，输出 [0, 1, 2, 3, 4, 5]
# def even_numbers(n):
#     for i in range(0, n+1, 2):
#         yield i
# for number in even_numbers(10):
#     print(number)

import pandas as pd

# 1. 创建模拟数据
data = {
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [22, 25, 30, 28],
    "薪资": [8000, 12000, 15000, 9000]
}
df = pd.DataFrame(data)

# 2. 查看
print(df.head())

# 3. 筛选薪资 > 10000
result = df[df["薪资"] > 10000]
print("\n高薪人员：")
print(result)

# 4. 统计
print("\n平均薪资：", df["薪资"].mean())
