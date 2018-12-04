# 异常传递： 就是如果当前代码没有进行异常处理那么异常会往外层传递，如果外层有捕获异常那么不会崩溃，否则没有人捕获异常那么会崩溃

try:
    try:
        name = 10
        del name
        print(name)
    finally:
        print("有没有异常跟哥没有关系")

except Exception as e:
    print("你的异常我来处理")


def show():
    result = 1 / 0
    print(result)

# show()

def show2():
    try:
        show()
    except Exception as e:
        print(e, type(e))


show2()

def show3():
    show()


try:
    show3()
except Exception as e:
    print(e, type(e))

