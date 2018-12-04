
# *args只能接收不定长位置参数
# def show_info(name, age=18, *args, **kwargs):
#     print(name, age, args, kwargs)

# 按照位置方式传参
# show_info("曹操", 66, "男", "卞夫人")
# 按照关键字方式传参，进行测试
# 提示： 前面使用关键字传参那么后面必须使用关键字传参, 不能使用位置参数
# show_info(name="曹操", age=66, sex="男", wife="卞夫人")

# 错误的使用，缺省参数不能使用默认值
# show_info("孙权", '男', wife='卞夫人')

# 如果不给缺省参数传值使用默认值
# 提示： 缺省参数不能放到**kwargs后面，**kwargs需要放到所有参数的后面
def show_info(name, *args, age=18, **kwargs):
    print(name, age, args, kwargs)

show_info('刘备', "男", '糜夫人', age=64, a=1, b=2)


# 通常使用不定长参数
def show_msg(info, *args, **kwargs):
    print(info, args, kwargs)

show_msg("哈哈，好复杂", 'a', 'b', 'c', a=1, b=2, c=3)