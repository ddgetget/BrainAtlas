import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    tcp_client_socket.connect(("192.168.167.107", 7890))
    # 接收用户的数据
    file_name = input("请输入您要下载的文件名:")
    # 对字符串进行编码
    file_name_data = file_name.encode("gbk")
    # 发送请求的文件
    tcp_client_socket.send(file_name_data)

    # 打开文件完成数据写入
    with open("/home/python/Desktop/" + file_name, "wb") as file:
        # 循环接收获取服务端发送的二进制数据
        while True:
            # 获取文件的二进制数据
            file_data = tcp_client_socket.recv(1024)
            if file_data:
                # 把服务端发送的文件二进制数据写入到文件中
                file.write(file_data)
            else:
                print("服务端关闭连接了:", len(file_data))
                break

    # 关闭套接字
    tcp_client_socket.close()

