#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 10:38:02 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 10:38:02 
 * @Desc: TCP 服务器
'''
import socket,threading,time

# 每个连接都必须创建新线程来处理 因为单线程在处理连接过程中,无法接收其他客户端的连接
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' %addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(2048)
        time.sleep(2)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.' %addr)





# 创建一个基于IPv4和TCP协议的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 然后，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接
# 端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：

# 绑定端口
s.bind(('127.0.0.1',9999))
# 监听端口 传入的参数是指定等待连接的最大数量
s.listen(5)
print('wait for connection')
# 服务器程序通过永久循环来接收客户端的连接 accept()会等待并返回一个客户端连接
while True:
    # 接收一个连接
    sock,addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


