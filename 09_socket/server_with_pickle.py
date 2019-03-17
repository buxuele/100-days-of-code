import socket
import time
import pickle

# # pickle wrap python-objects to some type-data
# d = {1: 'hi', 2: "you"}
# msg = pickle.dumps(d)       # dumps , not dump
# print(msg)
# # b'\x80\x03}q\x00(K\x01X\x02\x00\x00\x00hiq\x01K\x02X\x03\x00\x00\x00youq\x02u.'


HEADERSIZE = 10

# https://www.youtube.com/watch?v=Lbfe3-v7yE0
# 这里2个词分别代表  ipv4, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主机和端口
s.bind((socket.gethostname(), 1235))

# 5是序列数 ，queue
s.listen(5)

while True:
    # 客户端名称， 客户端的地址
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')

    d = {1: 'hi', 2: "you"}
    msg = pickle.dumps(d)  # dumps , not dump # 此时的msg 已经是bytes
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(msg)

    # clientsocket.close()
