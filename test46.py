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
        