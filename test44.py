#! /usr/bin/env python3
#_*_ coding:utf-8 _*_
# 枚举类的使用
# 定义常量时 一个办法就是用大写变量通过整数来定义
# 例如月份
JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC =12

# 好处简单 缺点是类型是int 并且仍然是变量
# 更好的办法是为这样的枚举类型定义一个class类型 每个常量都是class的唯一实例  Python
# 提供了Enum类来实现这个功能

from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Setp','Oct','Nov','Dec'))
# 这样就获得了Month的枚举类型,可以使用Month.Jan来引用一个常量
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

# value属性则是自动赋值给成员int变量 默认从1开始计数
from enum import Enum,unique
# 如果需要更精确地控制枚举类型 可以从Enum派生类
@unique
class Weekday(Enum):
    Sun = 0 #sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以检查保证没有重复值

# 访问枚举类型的方法
# 1
day1 = Weekday.Mon
print(day1)

# 2
print(Weekday.Tue)

# 3
print(Weekday['Wed'])

# 4
print(Weekday.Thu.value)

#5
print(Weekday(5))


for n,member in Weekday.__members__.items():
    print(n,'==>',member,'==>',member.value)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student('Bart',Gender.Male)
if bart.gender ==Gender.Male:
    print('test success')

# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
