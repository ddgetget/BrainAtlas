def hello():
    print("send_msg:hello")

    
class Student(object):
    @classmethod
    def show(cls):
        print("我是一个学生类:", cls)