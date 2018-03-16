#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-15 17:18:18 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-15 17:18:18 
 * @Desc: 二进制文件
'''
# 默认都是读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

# with open('/home/javazhe/图片/111.jpg','rb') as f:
#     print(f.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

# with open('/home/javazhe/test.txt','r',encoding='gbk',errors='ignore') as g:
#     print(g.read())

'''遇到有些编码不规范的文件，
你可能会遇到UnicodeDecodeError，
因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，
表示如果遇到编码错误后如何处理。最简单的方式是直接忽略'''

# 写文件 写文件和读文件一样是调用open() 唯一的区别在于标识符'w' 'wb' 表示写文本文件或二进制文件

with open('/home/javazhe/test.txt','w') as f:
    f.write('hello world!')
    a = "testline"
    f.append(a)
# 以'w'模式写入文件时 如果文件存在就会直接覆盖 
# 如果希望直接在文件末尾追加 可以传入'a'以追加模式append()方法写入
with open('/home/javazhe/test.txt','r') as g:
    print(g.read())