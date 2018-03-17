#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-16 21:10:05 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-16 21:10:05 
 * @Desc: collections
'''
# collection是Python内建的一个集合模块,提供很多集合类
# nametuple  从tuple派生出来的 
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x,',',p.y)

'''namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素'''
'''这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。'''
# Pont对象是tuple的一种子类
print(isinstance(p,tuple))
print(type(p))

# 类似的坐标和半径表示一个圆 也可以用nametuple定义
Circle = namedtuple('Circle',['x','y','r'])
cir = Circle(2,2,1)

# deque
'''使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈'''
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

'''注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的'''

# OrderedDict
'''使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict'''

from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d) #dict是无序的
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['x'] = 2
od['y'] = 3

print(od)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

# Counter 是一个简单的计数器,例如:统计字符个数
from collections import Counter
c = Counter()
for ch in 'Programming':
    c[ch] = c[ch]+1

print(c)
# Counter实际上也是dict的一个子类
# Collections模块提供了一些有用的集合类


