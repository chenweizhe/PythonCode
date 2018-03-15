#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
# 面向对象编程
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

    
# 给对象发消息实际上就是调用对象对应的关联函数，
# 我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：
bart = Student('bart simpson',59)
lisa = Student('lisa simpson',87)

bart.print_score()
lisa.print_score()
# 面向对象:封装 继承 多态

