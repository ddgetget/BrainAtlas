# 其他语言三目运算符: ? :

# python三目运算符: 2 if True else 1, 条件成立使用if左边的值，否则使用else右边的值


def check_age(age):
    result = "成年" if age >= 18 else "未成年"
    return result

value = check_age(19)
print(value)