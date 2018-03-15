#!/usr/bin/env python3
# list在执行lower函数时并没有改变原来的值 而是创建一个新的list
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
from functools import reduce
def norsize(name):
     name[0].upper()+name[1:].lower()
     return name

print(list(map(norsize,['adam', 'LISA', 'barT'])))

def prod(a,b):
    return a*b
# reduce 返回的是函数计算的结果
print(reduce(prod,[1,2,3,4]))


d =  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}
def str2int(a):
    def fn(x,y):
       return x*10+y
       
    def gn(s):
       return digits[s]

    return reduce(fn,map(gn,a))

print(str2int('12354'))

def str2float(b):
    def fn(x,y):
        return x*10+y
    n = b.index('.')
    def gn(s):
        return digits[s]
    # s1 = list(map(gn,[x for x in b[:n]]))
    # s2 = list(map(gn,[x for x in b[n+1:]]))
    return reduce(fn,map(gn,[x for x in b[:n]]))+reduce(fn,map(gn,[x for x in b[n+1:]]))/(10**len(b[n+1:]))

print(str2float('123.456'))





