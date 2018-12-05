import threading


def task1(name, age):
    print(name, age)


if __name__ == '__main__':
    # # 创建子线程
    # sub_thread = threading.Thread(target=task1, args=("西施", 18))
    # # 启动线程执行对应的任务
    # sub_thread.start()

    # # 创建子线程
    # sub_thread = threading.Thread(target=task1, kwargs={"name":"西施", "age":18})
    # # 启动线程执行对应的任务
    # sub_thread.start()

    # 创建子线程
    sub_thread = threading.Thread(target=task1, args=("西施",), kwargs={"age": 18})
    # 启动线程执行对应的任务
    sub_thread.start()