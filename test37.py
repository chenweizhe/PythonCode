#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# 继承和多态

class Animal(object):
    def run(self):
        print('animal is running...')

# 当要写狗的时候 直接从Animal类继承
class Dog(Animal):
    def run(self):
        print("Dog is running")
    def eat(self):
        print('Dog is eating')
class Cat(Animal):
    def sleep(self):
        print('cat is sleepping')


# 继承最大的好处就是子类获得了父类的全部功能 比如animal的run方法 cat和dog自动拥有了run方法
dog = Dog()
dog.run()
# 子类还可以增加新方法
# 复写run方法 这就是继承的另一个好处 多态
cat = Cat()
cat.run()
cat.sleep()
dog.eat()


def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())  #因为Dog也是继承自Animal所以可以直接实例