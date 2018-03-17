#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 09:10:26 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 09:10:26 
 * @Desc: struct
'''
# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

import struct
print(struct.pack('>I',10240099))

'''pack的第一个参数是处理指令，'>I'的意思是：

>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

后面的参数个数要和处理指令一致。

unpack把bytes变成相应的数据类型：'''

# unpack把bytes变成相应的数据类型
s = struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
print(s)

