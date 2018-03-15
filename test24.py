#! /usr/bin/env python3
# map & reduce

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。

# 比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下
def f(x):
     return x*x

for a in map(f,[1,2,3,4,5,6,7,8,9]):
    print(a)
print(map(f,[1,2,3,4,5,6,7,8,9]))

# map()传入的第一个参数是f，
# 即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。

# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
# 比如，把这个list所有数字转为字符串：

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]的每个元素上上，
# 这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算

# 例如 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def f_1(a,b):
    return a + b

from functools import reduce
print(reduce(f_1,[1,2,3,4]))

# 要注意的是 map 和reduce传入的都是函数名 不需要是函数

# map是对可迭代对象中每一个元素作用 reduce是对可迭代序列中每两个元素进行作用

# 如果考虑到字符串str也是一个序列，
# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

def fn(x,y):
    return x * 10 + y

def gn(s):
    d =  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn,map(gn,'456')))

# 整理成一个str2int的函数就是：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10 +y
    def gn(s):
        return DIGITS[s]
    return reduce(fn,map(gn,s))    



# 还可以用lambda函数进一步简化成：

def char2num(s):
    return DIGITS[s]


def str2int2(s):
    return reduce(lambda x,y:x*10+y , map(char2num,s))

# 也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！



