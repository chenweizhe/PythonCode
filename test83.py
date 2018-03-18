#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 19:45:11 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 19:45:11 
 * @Desc: UDP协议 数据报文包
'''
# UDP是面向无连接的协议
# 只需要知道对方的IP地址和端口号 但是UDP传输数据是不可靠的 但是比TCP协议要快
import socket,threading,time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1',9999))

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
print('bind udp on 9999')
while True:
    # 接收数据
    data,addr = s.recvfrom(1024)
    print('received from %s: %s.' %addr)
    s.sendto(b'hello %s!' %data,addr)
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
s.close()

