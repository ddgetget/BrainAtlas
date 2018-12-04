# -------------------------import 导入方式-----------------------

# import first_package.recv_msg   ***
# import first_package.send_msg   ***
#
#
# first_package.recv_msg.helloworld()
# first_package.send_msg.hello()

# 给导入的模块起别名
# import first_package.recv_msg as recv_msg
# import first_package.send_msg as send_msg
#
# recv_msg.helloworld()
# send_msg.hello()

# -------------------------from 导入方式-----------------------
# from first_package import recv_msg ***
# from first_package import send_msg ***
#
# recv_msg.helloworld()
# send_msg.hello()

# from first_package import recv_msg as recv
# from first_package import send_msg as send
#
# recv.helloworld()
# send.hello()

#  -------------------------from 导入方式具体的功能-----------------------

# from first_package.send_msg import hello
# from first_package.recv_msg import helloworld
#
# # def hello(msg):
# #     print(msg)
#
#
# hello()
# helloworld()

# ---------------------------from 导入包里面的所有模块 ---------------------
# from first_package import *
#
# recv_msg.helloworld()
# send_msg.hello()

# 扩展：--直接导入包名想要使用模块的时候不报错需要在init文件里面指定导入的模块
import first_package

first_package.send_msg.hello()
first_package.recv_msg.helloworld()




