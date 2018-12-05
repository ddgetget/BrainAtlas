def fibonacci(num):
    a = 0
    b = 1
    index = 0
    print("---11--")
    while index < num:
        result = a
        a, b = b, a + b
        index += 1
        print("---22--")
        # 提示： 代码执行到yield会暂停，然后把结果返回给外界，下次启动生成器在暂停的位置继续往下执行
        yield result
        print("---33--")


generator1 = fibonacci(5)

value = next(generator1)
print(value)

value = next(generator1)
print(value)


# for value in generator1:
#     print(value)

# 总结： 在def关键字里面看到yiled关键字表示创建的是一个生成器


