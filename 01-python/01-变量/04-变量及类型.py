# 变量： 通俗理解存储程序数据的容器

# 变量的定义格式
# 变量名 = 数据

# 定义了一个变量，名字叫score，存储数据是100
score = 100

# 使用变量
print(score)

# 这里注意：不是定义了一个变量，是对变量进行重新赋值操作
score = 90
print(score)

# 定义了一个变量，名字叫做num，存储数据是10
num1 = 10
print(num1)

# 特点： python定义变量的时候不需要指定变量的类型，根据等号后面的值自动推导数据类型

# 查看数据类型
type_name = type(num1)
print(type_name)

# 定义一个字符串变量
student_name = "张三"
print(student_name)

type_name1 = type(student_name)
print(type_name1)

# 浮点数类型
pi = 3.14
print(type(pi))


# bool类型，只有两个值，True，False

is_ok = False
print(type(is_ok))

# 浮点数和整数进行计算，那么会把整数自动转成浮点数类型
result = num1 + pi
print(result)

result = 10 / 2.0
print(result)

# 了解： 复数分为实部和虚部
#
# num2 = complex(4, 1)
# print(num2)
#
# num3 = 5 - 2j
# 
# result = num2 + num3
# print(result)

int = 10
print(int)