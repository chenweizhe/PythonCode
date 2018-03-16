#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-15 19:41:19 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-15 19:41:19 
 * @Desc: StringIO和BytesIO
'''
# 在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())


# 要读取StringIO,可以用一个str初始化StringIO,然后像文件一样读取:
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    

with open('/home/javazhe/test.txt','w') as g:
    g.write(f.getvalue())
with open('/home/javazhe/test.txt','r') as d:
    print(d.read())


# BytesIO
# StringIO 操作的只能是str 如果操作二进制数据 就需要使用BytesIO 来实现内存中读写bytes

# 例子:
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# StringIO和BytesIO是在内存中操作str和bytes的方法,使得读写文件具有一致的接口
