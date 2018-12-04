def show_info(name, age):
    print(name, age)


# 位置参数： 按照参数定义的顺序去传参, 通俗理解就是按照一定顺序去参数
# 按照位置方式传参
show_info('张三', 18)
# 关键字参数: 按照参数名去给参数传参，提示： 顺序可以不和定义时候的参数顺序一致
# 按照关键字方式传参
show_info(age=19, name='李四')
show_info(name="王五", age=18)