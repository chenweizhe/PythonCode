#! /usr/bin/env python3
#_*_coding:utf-8 _*_
# 元类使用
# type()
# 动态语言和静态语言最大不同就是 函数和类的定义 不是编译时定义而是运行时创建的

class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.'%name)

from test45 import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))



# type函数可以查看一个类型或者变量的类型 Hello是一个class,它的类型就是type,而h是一个实例 它的类型就是class Hello
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
# 先定义函数
def fn(self,name = 'world'):
    print('Hello,%s.' %name)

Hello2 = type('Hello',(object,),dict(hello2 = fn))  #创建Hello class

h = Hello2()
h.hello2()

print(type(h))

'''要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。'''

# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
# 然后调用type()函数创建出class。

# 正常情况下，我们都用class Xxx...来定义类，
# 但是，type()函数也允许我们动态创建出类来，
# 就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，
# 或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# metaclass 元类
# 当定义类之后 就可以根据这个类创建出实例 所以:先定义类 然后创建实例
# 如果想创建类 就必须根据metaclass创建出类:先定义metaclass 再创建类
# metaclass==>类==>实例
# 例子:定义 ListMetaclass 
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self, value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

# 有了ListMetaclass后 定义类还可以指示使用ListMetaclass来定制类,传入关键字参数 metaclass:
class Mylist(list,metaclass = ListMetaclass):
    pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。

L = Mylist()
L.add(1)
print(L[0])