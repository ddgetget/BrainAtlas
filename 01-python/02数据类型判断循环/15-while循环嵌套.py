# while循环嵌套： 在while循环语句里面在使用一个while循环语句

# while循环嵌套的格式
# while 条件:
#     while 条件:
#         print("xxx")

count = 1
while count <= 3:
    print(count)

    # 内部循环次数
    inner_count = 1

    while inner_count <= 2:
        print("嵌套循环")
        inner_count += 1

    count += 1