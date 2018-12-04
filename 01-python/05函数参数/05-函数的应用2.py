# 1. 写一个函数求三个数的和


def sum_num(num1, num2, num3):
    # 函数体里面需要把三个数字的和计算出来
    result = num1 + num2 + num3
    # 把计算的结果返回给函数外，让函数外使用该结果
    return result


# value = sum_num(1, 2, 3)
#
# # 显示计算后的结果信息
# print(value)


# 2. 写一个函数求三个数的平均值
def num_avg(num1, num2, num3):
    # 1. 先计算三个数的和
    value = sum_num(num1, num2, num3)
    # 2. 求平均值
    avg_value = value / 3
    return avg_value

result = num_avg(1, 2, 3)
print(result)