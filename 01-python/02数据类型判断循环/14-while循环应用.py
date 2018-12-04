# 1-100的数据累计和

# 1. 获取1-100的数字
# num = 1
#
# # 2. 保存计算后的结果
# result = 0
# while num <= 100:
#     # print(num)
#     result += num
#     num += 1
#
# # 循环后输出计算后的结果
# print(result)


# 计算1~100之间偶数的累积和（包含1和100）

num = 1
# 保存偶数相加后结果
result = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
        result += num
    num += 1

# 输出偶数和
print(result)


