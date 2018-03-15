#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# 访问限制

#  如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self,name,score,gender):
        self.__name = name
        self.__score = score
        self.__gender = gender
    
    def set_gender(self,gender):
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))
    def set_Score(self,score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('wrong score')
    def get_score(self):
        return self.__score


bart = Student('bart',50,'male')
bart.set_Score(90)
print(bart.get_score())
bart.print_score()
bart.set_gender('female')
print(bart.get_gender())

# 样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
'''需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：'''
