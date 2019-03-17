import socket


"""
1. socket.SOCK_DGRAM  UDP连接

2. 
print(socket.gethostbyname('127.0.0.1'))
# fqdn: (fully qualified domain name)
print(socket.getfqdn('127.0.0.1'))
print(socket.gethostname())


"""
print(socket.gethostbyname('www.baidu.com')) # 域名解析成IP
# fqdn: (fully qualified domain name)
print(socket.getfqdn('127.0.0.1'))  # IP 查找对应的域名
print(socket.gethostname())

"""
115.239.211.112
localhost
GSW
"""