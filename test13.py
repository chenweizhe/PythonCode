#! /usr/bin/env python3

n1 = 255
n2 = 44
# print(n1,n2)

print(hex(n1),hex(n2))

# python中，定义一个函数要使用def语句，依次写出函数名、括号 括号中的参数和冒号 ：
# 然后在缩进块中编写函数体 函数返回值用 return 返回

def my_abs(x):
    if x > 0 :
        return x
    else:
        return -x

print(my_abs(-88))

# 空函数 想定义一个什么事都不做的空函数 可以用pass语句:
def nonenn():
    pass
# pass实际上可以用来做占位符，比如现在还没想好怎么写 可以先放一个pass 让代码能运行起来
age = 2
if age >= 18 :
    pass  #没有pass这里会有语法错误 

# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
# 修改一下my_abs 的定义 数据类型检查使用内置函数 isinstance() 实现
def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('false type')
    if x >= 0 :
        return x
    else:
        return -x

print(my_abs2(55))

# python函数可以返回多个值 这个有点儿好玩
import math

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)
# 其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100,100,60,math.pi/6)
print(r)
# 由上可知 返回值为tuple
'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''
