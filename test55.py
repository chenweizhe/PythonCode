#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-16 08:49:24 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-16 08:49:24 
 * @Desc: 多进程
'''
# Unix/Linux操作系统提供了fork()函数,普通函数调用一次 返回一次 fork()函数调用一次 返回两次
# 因为操作系统自动把当前的进程(父进程)复制一份(子进程),然后分别在父进程和子进程内返回
# 子进程永远返回0 父进程返回子进程ID 而子进程只需要调用getppid()就可以拿到父进程ID

# Python的os模块封装了常见的系统调用,包括fork()
# 所以可以轻松创建子进程

import os 

print('Process(%s) start...' %os.getpid())
# 只能在unix/linux下运行
pid = os.fork() #返回进程数
if pid == 0:
    print('child process (%s) and my parent is %s ' %(os.getpid,os.getppid))
else:
       print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

