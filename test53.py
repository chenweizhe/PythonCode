#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-15 21:11:57 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-15 21:11:57 
 * @Desc: 序列化
'''
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening
# Python提供了pickle模块来实现序列化
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

import pickle
d = dict(name = 'Bob',age = 20,score = 88)
print(pickle.dumps(d))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，
# 就可以把这个bytes写入文件。或者用另一个方法pickle.dump()
# 直接把对象序列化后写入一个file-like Object

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()




# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)
'''Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系'''

# JSON
# 如果我们要在不同编程语言中传递对象 就必须把对象序列化为标准格式 比如XML
# 更好的办法是用JSON JSON表现出来就是一个字符串 能被所有语言 读取 比XML块

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name = 'Bob',age = 20,score=88)
di = json.dumps(d)
print(di)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"score": 88, "age": 20, "name": "Bob"}'
print(json.loads(json_str))

# json进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def Student2Dirt(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

'''Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
错误的原因是Student对象不是一个可序列化为JSON的对象。
如果连class的实例对象都无法序列化为JSON，这肯定不合理！
别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可'''
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

s = Student('Bob',20,88)
print(json.dumps(s,default=Student2Dirt))

# 下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2Student))