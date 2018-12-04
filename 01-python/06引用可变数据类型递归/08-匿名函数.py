# 匿名函数: 定义函数的时候不使用def关键字使用lambda关键字表示是匿名函数，提示匿名函数也是函数，调用的时候需要加上'(参数)'

def sum_num(num1, num2):
    result = num1 + num2
    return result

result = sum_num(1, 2)

print(result)

# 匿名函数只适合做一些函数的简单操作
calc_num = lambda x, y: x + y
print(calc_num)

# 执行匿名函数
result = calc_num(4, 5)
print(result)

# 应用场景，判断是否是偶数
func_name = lambda x: True if x % 2 == 0 else False
print("func_name:", func_name)
# result = func_name(5)
#
# print(result)

# 使用普通函数判断是否是偶数
def calc_value(value):
    if value % 2 == 0:
        return True
    else:
        return False

# 使用匿名函数判断num是否是偶数
# 提示： 函数的参数还可以传入匿名函数,当然还可以传入普通函数
def is_oushu(num, function):
    print("is_oushu:", func_name)
    result = function(num)
    print(result)

# is_oushu(2, func_name)

# 把普通函数作为参数传入到指定函数里面
is_oushu(1, calc_value)




