#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-15 20:05:36 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-15 20:05:36 
 * @Desc: 操作文件和目录
'''

# 用Python完成系统提供的对文件 目录的命令 dir cp等
# 操作系统只是简单调用操作吸引提供的接口函数 Python内置os模块也可以直接调用操作系统提供的
# 接口函数

import os
print(os.name) #得出操作系统类型 得出是啥接口
print(os.uname()) #得出详细的系统信息

# 环境变量 操作系统定义的环境变量 全部保存在os.environ这个变量中 可以直接查看
# print(os.environ)
# 要获得某个环境变量的值 可以调用 os.environ.get('key')
# print(os.environ.get('PATH'))
print(os.environ.get('x','default'))

# 操作文件和目录 这部分函数一些在os模块中,一些在os.path模块中  查看 创建 删除目录可以调用
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录,首先把新目录的完整路径表示出来:
# os.path.join('/home/javazhe','testdir')
# # 然后创建一个目录:
# os.mkdir('/home/javazhe/testdir')
# # 删除一个目录
# os.rmdir('/home/javazhe/testdir')

# 把两个路径合成一个时,不要直接拼字符串 而要通过os.path.join()函数,这样可以正确处理不同操作系统的路径分隔符
# 同样 在拆分路径时 也不要直接去拆字符串 而要通过os.path.split()函数 这样可以把一个路径拆分成两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/home/javazhe/test.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print(os.path.splitext('/home/javazhe/test.txt'))
# 对文件的重命名
# os.rename('/home/javazhe/test.txt','/home/javazhe/test.py')
# # 删除文件
# print(os.remove('/home/javazhe/test.py'))

# 复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L)

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

print(os.listdir())