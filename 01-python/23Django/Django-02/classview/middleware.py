# author        TuringEmmy 
# createtime    18-10-16  下午5:06
# coding=utf-8
# doc           PyCharm

def simple_middleware1(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('func1 init')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('func1 before request')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('func1 after request')
        return response
    return middleware

def simple_middleware2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('func2 init')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('func2 before request')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('func2 after request')
        return response
    return middleware