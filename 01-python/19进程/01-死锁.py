import threading

# 创建互斥锁
lock = threading.Lock()


# 根据下标获取列表中的数据，保证同一时刻只能有一个线程去取值
def get_value(index):
    # 上锁
    lock.acquire()
    my_list = [1, 4, 6, 8]

    # 判断下标是否越界
    if index >= len(my_list):
        print("下标越界:", index)
        # 取值不成功的线程也需要把锁释放，否则后面的线程使用不了这个互斥锁
        lock.release()
        return

    # 根据下标获取值
    value = my_list[index]
    print(value)
    # 释放锁
    lock.release()

if __name__ == '__main__':
    # 模拟大量线程去取值
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        #  启动线程执行任务
        sub_thread.start()