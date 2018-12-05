import socket
import os

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口号
    tcp_server_socket.bind(("", 7890))
    # 设置监听，把主动套接字改成被动套接字，被动套接字就是listen后的套接字
    # 被动套接字只能接收客户端的连接请求，不能收发消息
    tcp_server_socket.listen(128)
    # 可以支持多个人下载文件，但是是同步下载，一个人下载完成以后另外一个人去下载
    while True:
        # 等待接收客户端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端的ip和端口号:", ip_port)
        # 获取客户端的请求数据，请求数据其实就是文件名
        file_name_data = service_client_socket.recv(1024)
        # 对数据进行解码
        file_name = file_name_data.decode("gbk")
        print(file_name)
        # 判断文件是否存在
        if os.path.exists(file_name):

            # print(file_name)
            with open(file_name, "rb") as file:
                while True:
                    # 以二进制方式读取文件中的数据
                    file_data = file.read(1024)
                    if file_data:
                        # 把读取文件的数据发送给客户端
                        service_client_socket.send(file_data)
                    else:
                        break
        else:
            print("文件不存在")

        # 终止和客户端服务
        service_client_socket.close()
    # 停止建立连接的服务
    tcp_server_socket.close()
