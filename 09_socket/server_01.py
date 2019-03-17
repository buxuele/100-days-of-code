import socket


# https://www.youtube.com/watch?v=Lbfe3-v7yE0
# 这里2个词分别代表  ipv4, TCP
# (socket_family, socket_type)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主机和端口
s.bind((socket.gethostname(), 1234))

# 5是序列数 ，queue
s.listen(5)

while True:
    # 客户端名称， 客户端的地址
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')

    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()

