import multiprocessing
import time


# 拷贝任务
def copy_work():

    print("拷贝中....", multiprocessing.current_process().pid)
    # 查看进程的守护状态
    # 提示： 进程池创建的进程是守护状态的
    print(multiprocessing.current_process().daemon)
    time.sleep(0.00000001)


if __name__ == '__main__':
    # 创建进程池， 根据任务自动创建进程，使用空闲进程执行对应的任务
    # 表示进程池中进程最大个数， 如果不传参数，默认是cpu的核数
    pool = multiprocessing.Pool(3)

    # 使用循环模拟大批量的任务
    for i in range(10):
        # 进程池使用同步的方式执行对应的任务， 同步： 表示一个进程把任务执行完以后另外一个进程才能去执行
        # pool.apply(copy_work)
        # 进程池使用异步的方式执行对应的任务， 异步： 进程池中的进程执行任务的时候，多个进程一起执行，相互不会等待
        pool.apply_async(copy_work)

    # 关闭进程池，表示进程池以后不再接收执行其它任务
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()


    # 总结：　进程池会根据执行任务的情况帮我们自动创建进程，提示：尽量少创建进程。
    # 提示：　千万不要认为上来自动帮我们创建指定进程的个数
