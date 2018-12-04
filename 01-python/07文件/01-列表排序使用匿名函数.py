my_student_list = [{"name": "abc", "age": 20}, {"name": "bcd", "age": 32}]
# my_student_list = [1, 2]


# item: 表示遍历列表获取的某一个字典信息
# item["age"]: 根据字典中的某个key对应value值排序
my_student_list.sort(key=lambda item: item["age"], reverse=True)

print(my_student_list)