# 异常捕获： try-except, 目的就是让程序不会崩溃，并能知道异常信息

# name = "zs"
# del name
# print(name)

try:
    # 提示： try里面放入可能出现异常的代码
    name = "zs"
    del name
    print(name)
except NameError as e:  # 获取异常对象
    # name 'name' is not defined
    # 捕获到异常，并对异常进行处理
    print("哈哈，抓到异常了:", e)


# 提示： 异常多数继承Exception,那么捕获异常可以使用Exception类型
try:
    file = open("1.txt", "r", encoding="utf-8")
    result = file.read()
    print(result)
    file.close()
except Exception as e:
    print(e, type(e))


# 了解捕获多个异常类型
try:
    # 提示： try里面放入可能出现异常的代码
    name = "zs"
    # del name
    print(name)

    result = 1 / 0
    print(result)
except (NameError, ZeroDivisionError) as e:  # 获取异常对象
    # name 'name' is not defined
    # 捕获到异常，并对异常进行处理
    print("哈哈，抓到异常了:", e, type(e))


try:
    # 提示： try里面放入可能出现异常的代码
    name = "zs"
    del name
    print(name)

    result = 1 / 0
    print(result)
except NameError as e:  # 获取异常对象
    # name 'name' is not defined
    # 捕获到异常，并对异常进行处理
    print("名字错误异常抓到了:", e, type(e))

except ZeroDivisionError as e:
    print("除数为0异常抓到了:", e, type(e))


# 提示： 如果在try里面发现了异常代码，则不会再执行try里面的代码，会执行对应的except代码

# 最复杂的异常捕获处理代码
try:
    # 执行可能出现异常的代码
    name = 'zs'
    del name
    print(name)
except Exception as e:
    # 捕获到异常会执行except
    print(e, type(e))
else:
    # 提示：没有捕获到异常会执行else
    print("没有异常会执行else")
finally:
    # 提示： 有没有异常finally必须执行
    print("有没有异常哥必须执行")



