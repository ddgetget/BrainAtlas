def func1(*args, **kwargs):
    print(args, type(args), kwargs, type(kwargs))
    # 对数据进行拆包
    func2(*args, **kwargs)


def func2(*args, **kwargs):
    print(args, kwargs)


func1(1, 2, a=1, b=2)