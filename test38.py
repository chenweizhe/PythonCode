#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
# 获取对象信息
# 如何判断对象类型---使用type函数
# 基本类型都可以用type()函数判断
type(123)
type('str')
type(None)
# 如果一个变量指向函数或者类 也可以用type()判断
type(abs)
import test37
a = test37.Animal()
type(a)
# type()返回的类型是对应的Class类型,
print(type(123)==type(456)) #显然 这里type都返回int类型
print(type('str')==type(456)) #第一个返回str类型 第二个返回int类型

# 如果要判断一个对象是否是函数 可以使用types模块中定义的常量
import types

def fn():
    pass
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType

# 对于class的继承关系 使用type很不方便 要判断class的类型 可以使用isinstance()函数
class Husky(test37.Dog):
    pass

h = Husky()
print(isinstance(h,Husky))
print(isinstance(h,test37.Dog))
print(isinstance(h,test37.Animal))

# 能用type判断的基本类型都可以用isinstance判断 总是优先使用isinstance()判断

# 使用dir()
# 要获得一个对象的所有属性和方法,可以使用dir()函数,它返回一个字符串的list
print(dir('ABC')) # 获得一个str对象的所有属性和方法

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，
# 比如__len__方法返回长度。在Python中，
# 如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
# 所以，下面的代码是等价的：
len('AHJ')
'AHJ'.__len__()

# 如果是自己写的类 也想用len()方法的话 就自己写一个__len__()方法
class Dog(object):
    def __len__(self):
        return 100
    
do = Dog()
print(len(do))

# 仅仅把属性和方法列出来是不够的，
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x

obj = MyObject()
# 紧接着可以测试对象的属性
print(hasattr(obj,'x')) #是否含有属性'x'
print(hasattr(obj,'y')) #是否含有属性'y'
setattr(obj,'y',19)#设置一个属性y
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
# 试图获取不存在的属性，会抛出AttributeError的错误
# getattr(obj,'z')
# 可以传入一个default参数,如果属性不存在 就返回默认值
print(getattr(obj,'z',404))
# 也可以获取对象的方法
hasattr(obj,'power')
print(getattr(obj,'power'))
fn = getattr(obj,'power')
print(fn)
print(fn())

# 通过内置的一系列函数 可以对任意一个Python对象进行剖析 拿到内部数据 要注意的是 只有在不知道对象信息的时候 我们
# 才去获取对象信息
# Python是动态语言 鸭子类型
