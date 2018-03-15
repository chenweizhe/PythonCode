#! /usr/bin/env python3

# 生成器 
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 与列表生成式的对比如下

L = [x*x for x in range(10)]

G = (x*x for x in range(10))

print(L)
print(G)
'''javazhe@javazhe-X550JX:~/文档/python codes$ python3 test20.py
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
<generator object <genexpr> at 0x7fe9b2b665c8>'''

# 创建generator的方法
# 第一种 也是最简单的一种 只要把列表生成式的[] 改成()，就创建了一个generator
G = (x*x for x in range(10))

'''创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：'''

print(next(G))

'''generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：'''
for  n in G:
    print(n)

# 斐波拉契数列 除第一个和第二个数以外 其他数都是前两个数之和

def fib(max):
   n=0
   a=0
   b=1
   while n < max:
        print(b)
        a , b = b,a+b
        n += 1
   return 'done'

print(fib(4))

'''注意，赋值语句：

a, b = b, a + b
相当于：

t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
但不必显式写出临时变量t就可以赋值。'''

# 面的函数和generator仅一步之遥。
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib1(max):
   n=0
   a=0
   b=1
   while n < max:
        yield b
        a , b = b,a+b
        n += 1
   return 'done'

# yield关键字是定义generator的另一种方法 如果一个函数含有yield关键字 那么这个函数
# 就不再是普通的函数，而是一个generator

print(fib1(6))

'''<generator object fib1 at 0x7f9b8b1f05c8>
javazhe@javazhe-X550JX:~/文档/python codes$'''

'''最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行'''


# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
# 必须捕获StopIteration错误，返回值包含在StopIteration的value中：

g = fib1(6)
while True :
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print(e.value)
        break

'''要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
并在适当的条件结束for循环。对于函数改成的generator来说，
遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，
for循环随之结束。'''




