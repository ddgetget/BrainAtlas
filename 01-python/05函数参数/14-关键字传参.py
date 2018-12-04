# *后面的参数必须使用关键字方式传参

def show(address, *, name, age):
    print(address, name, age)


# 按照位置方式传参
# show("李四", 20)
# 按照关键字方式传参
show(address="北京", name="王五", age=19)

