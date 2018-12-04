# 函数文档说明是给其它公司程序员查看函数功能描述

# 数字和的计算结果 -> 给公司内部的程序员查看的
def sum():
    '''这里完成的是数字和的计算结果 给其它公司的程序员查看'''
    num1 = 1
    num2 = 2
    result = num1 + num2
    print(result)


# help查看函数的功能描述
result = help(sum)

print(result)
