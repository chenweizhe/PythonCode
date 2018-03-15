#!/usr/bin/env python3

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
# 于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

# 二进制转十进制
def int2(x,base=2):
    return int(x,base)

# print(int2('8'))
print(int2('111'))

# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3 = functools.partial(int,base = 2)
print(int3('11111'))

# 简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。

# 注意到上面的新的int2函数，
# 仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：

print(int3('100000',base=8))

# 相当于：
# kw = { 'base': 2 }
# int('10010', **kw)

max2 = functools.partial(max,10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(5,6,7))
# max2(5, 6, 7)
# 相当于：

# args = (10, 5, 6, 7)
# max(*args)
# 结果为10。
