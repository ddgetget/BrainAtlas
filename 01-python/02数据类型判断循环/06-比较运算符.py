# 比较运算符
# ==	检查两个操作数的值是否相等，如果是则条件变为真。	如a=3,b=3，则（a == b) 为 True
# !=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3，则(a != b) 为 True
# >	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a > b) 为 True
# <	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a < b) 为 False
# >=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a >= b) 为 True
# <=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a <= b) 为 True


num1 = 2
num2 = 2

result = (num1 == num2)
print(result)

result = num1 != num2
print(result)

result = num1 > num2
print(result, type(result))

result = num1 < num2
print(result, type(result))

result = num1 >= num2
print(result, type(result))

result = num1 <= num2
print(result, type(result))


# 总结： 比较运算符返回的结果是bool类型， if 语句判断的时候 True表示成立 False表示不成立