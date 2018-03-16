#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-16 10:46:13 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-16 10:46:13 
 * @Desc: 多核CPU
'''
'''如果写一个死循环的话，会出现什么情况呢？

打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。

我们可以监控到一个死循环线程会100%占用一个CPU。

如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。

要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。'''

# 用Python写个死循环...
import threading,multiprocessing
def loop():
    x=0
    while True:
        x = x^1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
    