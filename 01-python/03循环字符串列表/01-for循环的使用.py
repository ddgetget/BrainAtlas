# for循环可以依次遍历对象中的每一个数据， 对象-》 字符串，列表，字典，集合（set）,range，元组
# for循环可以变量的是对象叫做可迭代对象

my_str = "hello"

# value:遍历得到的数据
# my_str: 要遍历的对象
for value in my_str:
    if value == "l":
        print("这一次的数据是%s" % value)
    print(value)




