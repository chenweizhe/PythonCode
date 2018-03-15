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
# 多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放：允许新增Animal子类；

# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。

# 对于动态语言来说 不需要传入的类型严格规定 只要保证传入的对象有一个一样的方法就行

'''这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，
它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。'''

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。