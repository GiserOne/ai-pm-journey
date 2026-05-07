# numbers = [1,2,3,4,5]
# squared = [num **2 for num in numbers]
# print(f"平方：{squared}")
# even_squares = [num **2 for num in numbers if num % 2 == 0]
# print(f"偶数的平方：{even_squares}")
# jd_list = [
#     {"公司": "字节", "城市": "重庆", "薪资": "20-30K"},
#     {"公司": "腾讯", "城市": "成都", "薪资": "25-40K"},
#     {"公司": "马上消费", "城市": "重庆", "薪资": "18-28K"},
# ]
# companies = [jd["公司"] for jd in jd_list]
# print(f"公司列表：{companies}")
# cq_companies = [jd["公司"]for jd in jd_list if jd["城市"] == "重庆"and jd["薪资"] >= "20K"]

# 用同样的 jd_list(在抄写代码里那个),用一行列表生成器,筛选出城市是重庆并且薪资里包含 "20" 的岗位。
# 期望结果:返回完整的 JD 字典列表,长这样 [{"公司": "字节", "城市": "重庆", "薪资": "20-30K"}]
# 提示:判断"字符串里包含某个子串"用 in 关键字,比如 "20" in jd["薪资"]
jd_list = [
    {"公司": "字节", "城市": "重庆", "薪资": "20-30K"},
    {"公司": "腾讯", "城市": "成都", "薪资": "25-40K"},
    {"公司": "马上消费", "城市": "重庆", "薪资": "18-28K"},
]
company_info = [jd for jd in jd_list if jd["城市"] == "重庆" and jd["薪资"] == "20-30K"]
print(company_info)