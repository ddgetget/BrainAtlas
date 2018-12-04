# 偏函数: 指明函数的参数偏爱某个值，那么这个函数就是偏函数
import functools

# def sum_num(num1, num2=1):
#     result = num1 + num2
#     print(result)
#
#
# sum_num(1, 2)
# sum_num(1)
#
# # 后面再执行这个函数的时候 这个num2参数的值统一想使用3
#
# # 这里的函数就是偏函数
# def new_sum_num(num1, num2=3):
#     sum_num(num1, num2)
#
# new_sum_num(1)
# new_sum_num(2)

# 使用系统的方式生成一个偏函数

def sum_num(num1, num2=1):
    result = num1 + num2
    print(result)

sum_num(1)
sum_num(2)

# 返回的函数就是一个偏函数, 系统的函数也可以进行修改参数偏爱某个值
new_func = functools.partial(sum_num, num2=3)
new_func(1)
new_func(2)

result = int("10")
print(result)
# a=isinstance(result,int)
# print(a)

new_func = functools.partial(int, base=2)
result = new_func("10")
print(result)