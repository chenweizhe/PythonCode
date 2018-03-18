#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 19:56:03 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 19:56:03 
 * @Desc: 
'''
# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data,('127.0.0.1',9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()
# 服务器接收数据仍然调用recv()方法
