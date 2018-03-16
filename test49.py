#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-15 16:45:20 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-15 16:45:20 
 * @Desc: 文件读写
'''

# 读写文件是最常见的IO操作 读写文件功能都是由操作系统 提供的, 所以读写文件就是请求操作系统
# 打开一个文件 (通常叫做文件描述符)

# 读文件 使用Python内置的open()函数,传入文件名和标示符
f = open('/home/javazhe/文档/第一周学习计划','r')
# r 表示只读 如果文件不存在 open()函数会抛出一个IOerror的错误

# 如果文件被成功打开 接下来调用read()方法可以一次读取文件的全部内容,Python把文件读到内存 用一个str表示
print(f.read()) #read()返回的是一个str文件
# 最后一步是调用close()方法关闭文件 文件使用完毕后关闭 因为文件对象会占用操作系统的资源
# 操作系统同一时间能打开的文件是有限的
f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/home/javazhe/文档/第一周学习计划','r')
    print(f.read())
finally:
    if f:
        f.close()

# Python引入with语句来自动帮我们调用close()方法

with open('/home/javazhe/文档/第一周学习计划','r') as f:
    print(f.read())  #和上述效果一样 而且还不必调用f.close()方法

'''调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：'''
with open('/home/javazhe/文档/第一周学习计划','r') as f:
    for line in f.readline():  #和上述效果一样 而且还不必调用f.close()方法
        print(line.strip())  # 把末尾的'\n'删掉


# file-like Object
'''像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲'''
