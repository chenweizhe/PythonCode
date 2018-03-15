#!/usr/bin/env python3
#_*_coding:utf-8 _*_

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zera'
#     return 10/n

# def main():
#     foo('0')

# main()
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：

# logging
# logging不会抛出错误 而且还可以输出到文件:

import logging
s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10/n)

'''这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。'''

# pdb 第四种就是启动Python的调试器pdb,让程序以单步方式运行,可以随时查看运行状态
# err.py
# s = '0'
# n = int(s)
# print(10 / n)
# 然后启动：

# $ python -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
# -> s = '0'
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

# (Pdb) l
#   1     # err.py
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)
# 输入命令n可以单步执行代码：

# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)
# 任何时候都可以输入命令p 变量名来查看变量：

# (Pdb) p s
# '0'
# (Pdb) p n
# 0
# 输入命令q结束调试，退出程序：

# (Pdb) q
# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

# pdb.set_trace()
# 这个方法也是用pdb 但是不需要单步执行
# 只需要 import pdb
# 然后在出错的地方放一个pdb.set_trace(),就可以设置一个断点
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10/n)

