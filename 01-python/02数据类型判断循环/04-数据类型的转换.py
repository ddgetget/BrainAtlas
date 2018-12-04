# int(x [,base ])	将x转换为一个整数
# float(x )	将x转换为一个浮点数
# complex(real [,imag ])	创建一个复数，real为实部，imag为虚部
# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
# eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个Unicode字符
# ord(x )	将一个字符转换为它的ASCII整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串
# bin(x )	将一个整数转换为一个二进制字符串

# 为什么要进行数据类型的转换，因为只有数据类型统一才能进行数据的计算

my_str = '1'

my_int = 5
# 把字符串转成整型
num1 = int(my_str)
print(num1, type(num1))
result = num1 + my_int
print(result)


my_float = 3.14
my_str = "4.18"

# 把字符串转成浮点型
num2 = float(my_str)
print(num2, type(num2))

result = my_float + num2
print(result)

num3 = 4.55
num4 = 3
# 把float类型转成int类型, 提示： float转成int类型只取整数部分， 不会四舍五入
result = int(num3) + num4
print(result)

result = num3 + num4
print(result, type(result))

num5 = float(num4)
print(num5, type(num5))

result = num3 + num5
print(result)

num6 = 10
# 把int类型转成字符串
result = str(num6)

print(result, type(result))

num7 = 10.5
# 把float类型转成字符串
result = str(num7)

print(result, type(result))
# eval获取内容里面的原始数据
my_str = "12"
# 获取字符串中原始数据类型并且获取到对应的数据值
result = eval(my_str)

print(result, type(result))

result = chr(97)

print(result)

result = ord('a')

print(result)

num8 = 11
# 把10进制转成16进制
result = hex(num8)

print(result)


# 注意点：如果字符串里面放的是浮点数那么不能使用int类型转换，需要使用float类型转换
my_str = '3.14偏函数嵌套函数推导式'

result = int(float(my_str))
print(result)


# # 如果有格式化占位符，两个百分号表示一个
# print("%d%%" % 10)

