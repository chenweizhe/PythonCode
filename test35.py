#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 类和实例

# class Student(object):
#     pass
# Student是类名 (object)表示是从哪个类继承下来的
# 定义好Student类 就可以创建出Student的实例 例如: Student()实现的

# wiezhe = Student()
# # 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
# wiezhe.name = 'bart bis'
# print(wiezhe.name)
# print(wiezhe)
# print(Student)
# # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：(初始化)

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

'''注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去'''

bart =Student('Bart Simpson',59)
print(bart.name)
print(bart.score)

'''和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数'''
# 数据封装
def print_score(std):
    print('%s:%s' %(std.name,std.score))

print_score(bart)
# 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
bart.print_score()
# 我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
# 静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
