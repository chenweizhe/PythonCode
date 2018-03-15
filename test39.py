#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# 实例属性和类属性
# python是动态语言,根据类创建的实例变量,或者通过self变量:
class Student(object):
    name = 'Student' #类属性
    def __init__(self,name):
        self.name = name
    
s = Student('Bob')
s.score = 90 #实例属性

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class AddDog(object):
    count = 0
    def __init__(self,name):
        self.name =  name
        AddDog.count += 1 #正确写法

        
    def print_cou(self):
        print(self.count)


a = AddDog('a')
print(AddDog.count)
b = AddDog('b')
print(AddDog.count)
c = AddDog('c')
print(AddDog.count)
