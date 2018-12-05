import multiprocessing
import time

if __name__ == '__main__':
    # 创建消息队列Queue
    # 3： 表示消息队列的个数，如果不指定默认值:-1, 表示任意多个数据
    queue = multiprocessing.Queue(3)

    # 向队列放入数据
    queue.put("hello")
    queue.put(111)
    queue.put([1, 4, 6])
    # 总结： 队列里面可以放入任意类型数据
    # 如果队列满了，那么会等待，直到队列有空闲位置以后才能放入成功
    # queue.put((1, 3))

    # 如果队列满了, put_nowait 不会等待队列有空闲位置以后再放入，当放入不成功的时候就会崩溃
    # 建议使用put
    # queue.put_nowait((1, 3))

    # 判断队列是否满了
    # result = queue.full()
    # print(result)

    # for i in range(1000000):
    #     pass

    # 解决办法： 1. 代码前面要保证有一定的耗时操作
    # time.sleep(0.0001)
    # 2. 根据个数去判断
    print("队列个数:", queue.qsize())

    # result = queue.empty()  # empty判断队列是否为空不可靠
    # print(result)

    if queue.qsize() == 0:
        print("队列为空")
    else:
        print("队列不为空")


    # 获取队列的数据
    value = queue.get()
    print(value)
    print("队列个数:", queue.qsize())
    value = queue.get()
    print(value)
    value = queue.get()
    print(value)
    # 如果队列空了，那么get方式取值会等待，直到队列有数据才可以获取队列中的数据
    # value = queue.get()
    # print(value)
    # 如果队列空了，那么get_nowait方式取值不会等待
    # 提示： 建议使用get获取值
    # value = queue.get_nowait()
    # print(value)

    if queue.qsize() == 0:
        print("队列为空")
    else:
        print("队列不为空")