# 定义函数
# def parse_salary(salary_str):
# 	parts = salary_str.split("-")
# 	min_s = int(parts[0])
# 	max_s = int(parts[1].rstrip('k'))
# 	avg_s = (min_s + max_s)//2
# 	print(f"正在解析：{salary_str}")
# 	return{"min":min_s, "max":max_s,"avg_s":avg_s}
# # 调用函数
# result = parse_salary("15-25k")
# print(result)
# salary_info = parse_salary("18-28k")
# print(f"平均薪资是{salary_info['avg_s']}k")

# 写一个函数 is_in_budget(salary_str, my_budget),接收一个薪资字符串和一个预算数字,返回 True/False,判断这个岗位的最低薪资是否能达到我的预算
def is_in_budget(salary_str, my_budget):
    parts = salary_str.split("-")
    min_s = int(parts[0])
    return min_s >= my_budget
print(is_in_budget("15-25K", 18))   # False(最低 15K,达不到 18K)
print(is_in_budget("20-30K", 18))   # True (最低 20K,达到了)
print(is_in_budget("18-28K", 18))   # True (最低正好 18K)