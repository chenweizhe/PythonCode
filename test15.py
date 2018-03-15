#! /usr/bin/env python3

# 位置参数
#计算x^n

def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s

#a = input('please enter a number: ')

#新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数
#导致旧的代码因为缺少一个参数而无法正常调用：
#这个时候，默认参数就排上用场了。由于我们经常计算x2，
# 所以，完全可以把第二个参数n的默认值设定为2
# print(power(int(a)))
#这样，当我们调用power(5)时，相当于调用power(5, 2)：
print(power(5))

'''从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。'''

def enroll(name,gender):
    print('name: ',name)
    print('gender',gender)



# 默认参数的使用 
#  默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
def add_end(L = []):
    L.append('END')
    return L
# >>> add_end([1,2,3])
#[1, 2, 3, 'END']
#>>> add_end()
#['END']
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
# >>> add_end()
# ['END', 'END', 'END', 'END']
# >>> add_end()
# ['END', 'END', 'END', 'END', 'END']
# ，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
'''原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了。
list是可变对象
所以记住：默认参数必须指向不变对象！
'''
# 要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end2(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2([1]))
print(add_end())

# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 可变参数
# 可变参数。顾名思义，
# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 就是在传入的参数前面加个 *

'''数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。'''

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc([1,2,3]))
# 在传入参数时需要传入一个list或者Tuple
# 如果使用可变参数 传入数据会更简单

def calc_2(*number2s):
    sum = 0
    for n in number2s:
        sum = sum + n*n
    return sum


print(calc_2(1,2,3))

'''定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，
因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数：'''

print(calc_2())


# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
# Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去：

num = [1,2,3]
print(calc_2(*num))

# 关键字参数
# 可变参数允许你传入0个或任意个参数，
# 这些可变参数在函数调用时自动组装为一个tuple。、
# 而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数在参数前面加 **
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

# 函数person除了必选参数name和age外，
# 还接受关键字参数kw。在调用该函数时，可以只传入必选参数：

print(person('sds',15))

print(person('boob',16,city = 'beijing'))

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，
# 我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
# 我们也能收到。试想你正在做一个用户注册的功能，
# 除了用户名和年龄是必填项外，其他都是可选项，
# 利用关键字参数来定义这个函数就能满足注册的需求。

# 可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

extra = {'city':'Beijing','job':'farmer'}
print(person('da',15,**extra))

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查。

def person_2(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('success')

# 这样子传入的参数可以不受限制关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 借助特殊分隔符符号 *,

def person_3(name,age,*, city,job):
    print(city,job)
# 命名关键字参数必须传入参数名，
# 这和位置参数不同。如果没有传入参数名，调用将报错：
# 用命名关键字参数时，要特别注意，如果没有可变参数，
# 就必须加一个*作为特殊分隔符。如果缺少*，
# Python解释器将无法识别位置参数和命名关键字参数：


# 参数组合 ：可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 定义一个函数，包含上述若干种参数：

def f1(a,b,c,*args,**kw):
     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

# >>> args = (1, 2, 3, 4)
# >>> kw = {'d': 99, 'x': '#'}
# >>> f1(*args, **kw)
# 所以，对于任意函数，
# 都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


