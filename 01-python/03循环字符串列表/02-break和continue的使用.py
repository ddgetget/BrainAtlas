# break和continue

# break和continue只能用在循环语句(while, for)里面,不能单独去使用

# 注意点：不能单独使用，必须在循环语句里面使用
# if 1 == 1:
#     break

# my_str = "hello"

# for value in my_str:
#     if value == "l":
#         # 跳出当前循环，循环执行结束, break后面的代码不会执行
#         break
#     print(value)


# for value in my_str:
#     if value == "l":
#         # 结束本次循环，然后可以继续下一次循环，continue后面的代码不会执行
#         continue
#     print(value)

# for - else 语句

# for value in my_str:
#     if value == "e":
#         # 总结： 如果循环语句里面执行break，那么else语句不会执行
#         break
#     print(value)
# else:
#     print("循环数据结束")


# for value in my_str:
#     if value == "e":
#         # 总结： 如果循环语句里面执行了continue，那么else语句还会执行
#         continue
#     print(value)
# else:
#     print("循环数据结束")
#
# # 提示： 只要循环语句里面不执行break关键字，那么else语句就会执行

# -----------------while循环--------------------------

# count = 3
#
# while count >= 1:
#
#     if count == 2:
#         # 跳出当前循环，循环结束，break后面的代码不会执行
#         break
#
#     print(count)
#     count -= 1


# count = 3
#
# while count >= 1:
#
#     if count == 2:
#         count -= 1
#         continue
#
#
#     print(count)
#     count -= 1


# count = 3
#
# while count >= 1:
#     if count == 2:
#         break
#     print(count)
#     count -= 1
# else:
#     print("循环数据结束")


count = 3

while count >= 1:
    if count == 2:
        count -= 1
        continue
    print(count)
    count -= 1
else:
    print("循环数据结束")


# 提示： while循环也可以使用else语句，要注意while循环语句里面只要执行了break那么else语句就不会执行，否则else语句会执行