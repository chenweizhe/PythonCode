#!/usr/bin/env python3
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 生产list[] 从1到10 10个数字
print(list(range(1,11)))
# print('cscs')
# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
# 循环太繁琐 而列表生成式可以一行语句代替循环生成上面的list
print([x*x for x in range(1,11)])

# 写列表生成式时，把要生成的元素x * x放到前面，
# 后面跟for循环，就可以把list创建出来，十分有用，
# 多写几次，很快就可以熟悉这种语法。

print(tuple(range(0,11)))

# 可以使用两层循环，可以生成全排列：

print([m+n for m in 'ABC' for n in 'XYZ'])

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os

print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，
# 比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

# 列表生成式也可以使用两个变量来生成list
print([k+'='+v for k,v in d.items()])

# 把一个list中所有字符串变成小写
L1 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L1])

L2 = ['Hello', 'World', 18, 'Apple', None]


L3 = [h.lower()  for h in  L2  if isinstance(h,str)]
print(L3)
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
