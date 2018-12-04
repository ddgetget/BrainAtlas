# 模块导入的注意点
# from first_module import sum_num  # 注意点： 当前模块如果出现和导入功能代码重复，那么会调用当前模块的功能代码

#
# def sum_num():
#     return 10
#
# result = sum_num()
# print(result)
#
# result = sum_num(1, 2)
# print(result)

# 解决办法： 使用import方式导入，更加安全和通用
# import first_module  # 推荐大家这样导入
#
# def sum_num():
#     return 10
#
# result = sum_num()
# print(result)
#
# result = first_module.sum_num(1, 2)
# print(result)

# 注意点： 自定义的模块名不能和系统的模块名相同
# import random
#
# result = random.randint(1, 3)
# print(result)

# 导入模块的查找搜索路径，默认是当前工程路径
import sys
print(sys.path)

