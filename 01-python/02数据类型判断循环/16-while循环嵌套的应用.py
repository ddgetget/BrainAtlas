# 打印三角形
# row = 1
#
# while row <= 5:
#     # print("%d" % row)
#     col = 1
#     while col <= row:
#         print("* ", end="")
#         col += 1
#     # 代码执行到此说明每行的星星打印完成，需要换行打印下一行星星
#     print("")
#     row += 1

# 打印九九乘法表
# 行数
row = 1

while row <= 9:
    #print("当前的行数是%d" % row)

    # 列数
    col = 1
    while col <= row:
        print("%d * %d = %d\t" % (col, row, col * row), end="")
        col += 1
    # 代码执行到此说明这一行里面的每一列都打印完成，需要换行打印下一行的数据
    print("")

    row += 1

