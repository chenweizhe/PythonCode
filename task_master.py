#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-16 15:14:09 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-16 15:14:09 
 * @Desc: 服务进程
'''
import random,time,queue
from multiprocessing.managers import BaseManager
# 发送任务的队列
task_queue = queue.Queue()
# 接收的结果d队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass
# 把两个Queue都注册到网络上,callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
# 绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('',5000),authkey=b'abc')
# 启动QUeue
manager.start()
# 通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('put task %d' %n)
    task.put(n)
# 从result中=队列读取结果
print('try get results...')
for  i in range (10):
    r = result.get(timeout=10)
    print('Result:%s' %r)
# 关闭
manager.shutdown()
print('master exit..')
# 请注意，当我们在一台机器上写多进程程序时，
# 创建的Queue可以直接拿来用，但是，在分布式多进程环境下，
# 添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，
# 必须通过manager.get_task_queue()获得的Queue接口添加