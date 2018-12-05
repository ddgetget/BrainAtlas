import multiprocessing


def show(name, age):
    print("名字:%s 年龄:%d" % (name, age))
    # print(name, age)

if __name__ == '__main__':
    # 创建子进程
    # args: 以元组的方式给指定任务传参数，参数必须按照一定顺序传递
    # kwargs: 以字典的方式给指定任务传参数
    # sub_process = multiprocessing.Process(target=show, args=("李四", 20))
    # sub_process.start()

    sub_process = multiprocessing.Process(target=show, kwargs={"age": 20, "name": '李四'})
    sub_process.start()
