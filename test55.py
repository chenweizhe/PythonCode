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

# import os 

# print('Process(%s) start...' %os.getpid())
# # 只能在unix/linux下运行
# pid = os.fork() #返回进程数
# if pid == 0:
#     print('child process (%s) and my parent is %s ' %(os.getpid,os.getppid))
# else:
#        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# Windows没有fork调用，上面的代码在Windows上无法运行
# 常见的apache服务器就是由父进程监听端口 有新的请求时 就fork出子进程处理新的http请求

# multiprocessing  由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

# 子进程执行
def run_proc(name):
    print('Run child process %s(%s)' %(name,os.getpid()))

if __name__=='__main__':
    print('Parent Process %s.' %os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()  #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('child process end') 



