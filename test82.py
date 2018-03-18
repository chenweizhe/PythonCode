#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 10:59:43 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 10:59:43 
 * @Desc: 81匹配客户端
'''
import socket,threading,time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(2048).decode('utf-8'))
s.send(b'exit')
s.close()
