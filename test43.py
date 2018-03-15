#! /usr/bin/env python3
#_*_ coding:utf-8 _*_
# 定制类
'''看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类'''

# __str__
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
    __repr__ = __str__

print(Student('weizhe'))
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：

# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。


class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b = b,a+b
        return a 

f = fib()
print(f[10])

# 但是list有个神奇的切片方法：


# 错误信息很清楚地告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Student2(object):
    def __init__(self):
        self.name = 'Weizhe'
    
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        # 返回函数也是可以的
        if attr == 'age':
            return lambda: 25
        # 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
        raise AttributeError('error')
#当调用不存在的属性时,解释器会试图调用__gertattr__(self,'score')来尝试获得属性,这样就有机会返回score值
s = Student2()
print(s.name)
print(s.score)
print(s.age()) #调用函数
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student3(object):
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print('my name is %s' %self.name)


# 调用方式如下
s = Student3('weizhe')
s()
# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类
