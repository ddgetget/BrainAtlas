import multiprocessing
import time


# 向队列写入数据
def add_data(current_queue):
    for i in range(5):

        if current_queue.full():
            print("队列满了")
            break

        print("add:", i)
        current_queue.put(i)
        time.sleep(0.2)


# 读取队列里面的数据
def read_data(current_queue):
    while True:
        # 加入数据读取完成，那么就不等待读取队列里面的数据了
        if current_queue.qsize() == 0:
            print("队列的数据读取完成了,队列为空")
            break
        else:
            value = current_queue.get()
            print("read_data:", value)


if __name__ == '__main__':
    # 创建消息队列
    queue = multiprocessing.Queue(3)

    # 创建添加数据进程
    add_process = multiprocessing.Process(target=add_data, args=(queue,))
    # 创建添加数据进程
    read_process = multiprocessing.Process(target=read_data, args=(queue,))

    add_process.start()
    # 保证数据添加完成以后再读取数据
    add_process.join()
    read_process.start()