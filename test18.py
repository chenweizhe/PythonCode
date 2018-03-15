#! /usr/bin/env python3

# 迭代循环 for...in...
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for n in 'casucsabkjcbsak':
    print(n)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('agb',Iterable))
print(isinstance(12345,Iterable))

# for循环里，同时引用了两个变量，在Python里是很常见的
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)
