# from socket import *
#
# sockfd = socket(AF_INET, SOCK_STREAM)
#
# sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#
# sockfd.bind(("0.0.0.0", 8887))
#
# sockfd.listen(5)
#
# connfd, addr = sockfd.accept()
#
# data = connfd.recv(1024)
#
# print(data.decode())
#
# response = """
# HTTP/1.1 200 OK
# Content-Type: text/html
#
# <h1>we are family</h1>
#
# """
#
# connfd.send(response.encode())
#
# connfd.close()
# sockfd.close()

import os
from datetime import datetime

s = 1723737600

c_date = datetime.fromtimestamp(s)

print(c_date)


