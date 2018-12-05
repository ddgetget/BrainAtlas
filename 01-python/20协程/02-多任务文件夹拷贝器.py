import os
import shutil
import multiprocessing
import time


# 拷贝文件的操作
def copy_file(src_dir_path, dst_dir_path, file_name):

    print(multiprocessing.current_process().pid)

    # 源文件的路径
    src_file_path = src_dir_path + "/" + file_name
    # 目标文件的路径
    dst_file_path = dst_dir_path + "/" + file_name

    with open(dst_file_path, "wb") as dst_file:
        # 打开源文件读取源文件中的数据然后写入到目标文件里面
        with open(src_file_path, "rb") as src_file:
            # 循环读取源文件的中数据
            while True:
                src_file_data = src_file.read(1024)
                if src_file_data:
                    # 把源文件中的数据写入到目标文件中
                    dst_file.write(src_file_data)
                else:
                    break



if __name__ == '__main__':
    # 源目录路径
    src_dir_path = "test"
    # 目标目录的路径
    dst_dir_path = "/home/python/Desktop/test"

    # 判断目标目录是否存在
    if os.path.exists(dst_dir_path):
        # 删除指定目标
        shutil.rmtree(dst_dir_path)

    # 创建目标文件夹
    os.mkdir(dst_dir_path)

    # 获取源目录下文件名列表
    file_name_list = os.listdir(src_dir_path)

    # 创建进程池
    pool = multiprocessing.Pool(3)

    # 遍历文件列表
    for file_name in file_name_list:
        print(file_name)

        # 使用进程池异步执行任务
        pool.apply_async(copy_file, args=(src_dir_path, dst_dir_path, file_name))

    # 关闭进程池
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()



        # 源文件的路径
        # src_file_path = src_dir_path + "/" + file_name
        # # 目标文件的路径
        # dst_file_path = dst_dir_path + "/" + file_name
        #
        # with open(dst_file_path, "wb") as dst_file:
        #     # 打开源文件读取源文件中的数据然后写入到目标文件里面
        #     with open(src_file_path, "rb") as src_file:
        #         # 循环读取源文件的中数据
        #         while True:
        #             src_file_data = src_file.read(1024)
        #             if src_file_data:
        #                 # 把源文件中的数据写入到目标文件中
        #                 dst_file.write(src_file_data)
        #             else:
        #                 break