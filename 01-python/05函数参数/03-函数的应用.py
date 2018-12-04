# 1. 打印一条横线
def print_one_line():
    print("-" * 30)

# 调用函数
# print_one_line()


# 2. 打印自定义行数的横线
# def print_line(line_num):
#     num = 1
#     while num <= line_num:
#         # 条件成立，打印一条线
#         print_one_line()
#         num += 1

# print_line(5)

# 3. 使用for循环的方式 打印自定义行数的横线
def print_line(line_num):
    for value in range(1, line_num + 1):
        print(value)
        print_one_line()

print_line(3)
