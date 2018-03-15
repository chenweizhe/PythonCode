#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
# 高级编程 开始
# __slots__的使用
# 正常情况下 我们可以个定义的类的实例绑定任何属性和方法,这就是动态语言的灵活性
class Student(object):
    pass

stu = Student()
stu.name = 'Wizzard'
print(stu.name)

# 还可以给实例绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
stu.set_age = MethodType(set_age,stu)
stu.set_age(25)
print(stu.age)
# 但是给一个实例绑定的方法 对另一个实例不起作用 
# 所以可以给class绑定方法
Student.set_age = set_age
def set_score(self,score):
    self.score = score

Student.set_score = set_score
s = Student()
s.set_score(88)
print(s.score)