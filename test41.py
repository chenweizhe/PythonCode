#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# @property的使用
'''有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用'''

class Student(object):
    @property #相当于变成属性score 然后score再创建一个装饰器 score.setter 负责把一个setter方法变成属性
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
    
        if value<0 or value >100:
            raise ValueError('score must be 0~100')
        self._score = value

'''@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作'''

s = Student()
s.score = 60 #OK 实际转化为s.set_score(60)
print(s.score)
s.score = 90

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Studentt(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2018-self._birth

# 以上例子 birth是可读写 age为只读属性

st = Studentt()
st.birth = 1998
print(st.birth)
print(st.age)

# @property 在类的定义中广泛应用 可以写出简短的代码 同时保证对参数进行必要的检查,减少出错的可能性

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError("error num")
        else:
            self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError("value must be an integer")

        else:
            self._height = value
    @property
    def resolution(self):
        return self._width*self._height


sc = Screen()
sc.width = 20
sc.height = 40
print('%d + %d' %(sc.width,sc.height))
print(sc.resolution)