# 一、字符串处理
# salary_str = "15-25k"
# parts = salary_str.split("-")
# min_salary = int(parts[0])
# max_salary = int(parts[1].rstrip('k'))
# avg_salary = (min_salary + max_salary)/2
# print(f"薪资范围：{min_salary}k - {max_salary}k, 平均 {avg_salary}k")
# EX：
# exp_str = "1-3年"
# parts = exp_str.split("-")
# min_exp = int(parts[0])
# max_exp = int(parts[1].rstrip('年'))
# print(f"经验要求:{min_exp}年 - {max_exp}年,至少需要{min_exp}年经验")

# 题目:给定一个字符串 score_str = "85分",提取出数字部分(85),判断是否及格(>=60),打印 成绩: 85 分,及格 或 成绩: 85 分,不及格。
score_str = "35分"
score = int(score_str.rstrip('分'))
# print(f"成绩：{score}分,{'及格' if score >= 60 else '不及格'}")
print(f"成绩：{score}分，{'及格' if score >= 60 else '不及格'} ")