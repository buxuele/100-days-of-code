import socket
import subprocess
import sys
from datetime import datetime

"""
1. 这个文件模仿一个客户端，对一个给定的主机进行端口扫描
2. 这个文件主要表达是一种思想，而不具备实际意义。熟悉语法而已。

"""


subprocess.call('clear', shell=True)

serverName = input("Give me a host to scan eg.[www.baidu.com]: ")
serverIP = socket.gethostbyname(serverName)     # 域名解析

print("-" * 60)
print("Scanning...", serverIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((serverIP, port))
        if res == 0:
            print(f"Port {port} is Open!")
        sock.close()
except KeyboardInterrupt:
    print("Ctrl + C:  to exit")
    sys.exit()
except socket.gaierror:
    print("Hostname error.Exiting.")
    sys.exit()
except socket.error:
    print("connect failed.")
    sys.exit()

t2 = datetime.now()
print(f"Cost time {t2 - t1}")


