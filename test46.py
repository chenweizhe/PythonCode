#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# 错误处理
# 程序运行过程中 如果发生错误 事先约定返回一个错误代码 
# try...except..finally 

# try 
try:
    print('try...')
    r = 10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
# finally可以没有
finally:
    print('finally')

print('END')
'''当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕'''

# 错误的种类有很多种.发生不同类型的错误 应该由不同的except语句块处理 可以由多个except来捕获不同类型的错误

try:
    print('try...')
    r = 10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('except:',e)
# 在except语句块后面加上else,当没有错误发生时,会自动执行else语句
else:
    print('no error')
finally:
    print('finally...')
print('END')

'''Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

Python所有的错误都是从BaseException类派生的'''

'''使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：'''
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')

# 调用栈
# 如果错误没有被捕获,他就会一直往上抛出,最后被Python解释器捕获,
# 打印一个错误信息,然后退出

# 记录错误　如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

# Python内置的logging模块可以非常容易地记录错误信息

import logging
def foo2(s):
    return 10/int(s)
def bar2(s):
    return foo2(s)*2

def main():
    try:
        bar2('0')
    except Exception as e:
        logging.exception(e)

main()
print('END') #通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

# 抛出错误 raise语句抛出异常
class FooError(ValueError):
    pass
def foo3(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10/n
foo3('0')

# 新的异常处理
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

'''在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

'''
'''Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。'''
