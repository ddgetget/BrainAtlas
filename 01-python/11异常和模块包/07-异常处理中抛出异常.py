def show():
    try:
        try:
            result = 1 / 0
            print(result)
        except Exception as e:
            # 捕获到异常对异常进行处理
            # print(e)
            # 抛出捕获到的异常，这里不进行处理
            # raise e
            # 提示： 简写，表示抛出的是当前异常
            raise

    except Exception as e:
        print("里面的异常我外面捕获着:", e, type(e))


show()