def helloworld():
    print("recv_msg:helloworld")


class Teacher(object):
    @classmethod
    def show(cls):
        print("我是一个老师类:", cls)