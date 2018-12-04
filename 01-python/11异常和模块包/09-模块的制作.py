import first_module  # 导入模块后才可以使用模块里面的代码

print(first_module.g_num)

stu = first_module.Student("张三", 20)
stu.show()

result = first_module.sum_num(1, 2)
print(result)


result = first_module.func_name(2)
print(result)