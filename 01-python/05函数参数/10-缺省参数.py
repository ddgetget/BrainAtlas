# 缺省参数: 在定义函数参数的时候，参数已经有值，那么在调用函数的时候如果不给函数传值使用默认值，否则使用传入的指定值


# def sum_num(num1, num2=1):
#     value = num1 + num2
#     return value
#
#
# result = sum_num(1)
# print(result)

# 缺省参数，不能放到普通参数前面
def sum_num(num2=1, num1=1):
    value = num1 + num2
    return value


result = sum_num(2, 2)
print(result)
