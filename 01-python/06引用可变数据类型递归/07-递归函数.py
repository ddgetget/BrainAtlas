# 递归函数： 函数里面调用函数本身
import sys

# 5! = 5 * 4 * 3 * 2 * 1

# 定义变量保存相乘后的结果
# result = 1
# for value in range(5, 0, -1):
#     print(value)
#     result *= value
#
# print(result)

# 5! = 5 * 4!

# 3! = 3 * 2
# 2! = 2 * 1
# 1! = 1


# 计算数据阶乘
def calc_num(num):
    print(num)
    if num == 1:
        return 1

    return num * calc_num(num - 1)

# 获取递归的最大递归次数, 默认1000次
count = sys.getrecursionlimit()
print(count)

sys.setrecursionlimit(1100)

count = sys.getrecursionlimit()
print(count)

# 求3！数据
# result = calc_num(1000)
# print(result)

# 总结： 递归函数的注意点: 1. 设置结束条件， 2. 提供递归公式


# def show():
#     print("xx")
#     show()
#
# show()
