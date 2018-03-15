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

# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''在ModelMetaclass中，一共做了几件事情：

排除掉对Model类的修改；

在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

把表名保存到__table__中，这里简化为表名默认为类名。

在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。'''
