# 起始位置默认值是0
# 结束位置不包含
for value in range(3):
    print(value)


print('---------')

# range默认的步长是1
for value in range(1, 4, 1):
    print(value)

print('---------')
for value in range(1, 11, 2):
    print(value)

print('---------')

# -1: 反向取值
for value in range(5, 0, -1):
    print(value)