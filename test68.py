#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 09:44:48 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 09:44:48 
 * @Desc: hmac
'''
'''通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的。

为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。

如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。

这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。

我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：'''
import hmac
message = b'hello world'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
# 消息很长的话 可以多次调用h.update(msg)
print(h.hexdigest())

# itertools 用于操作可迭代对象的函数
import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# cycle()会传入一个序列无限重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)


# repeat()负责把一个元素无限重复下去 不过可以限定重复次数
ns = itertools.repeat('a',5)
for n in ns:
    print(n)

'''无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))

# chain可以把一组迭代对象串联起来,形成更大的迭代器'
for c in itertools.chain('ABC','abc'):
    print(c)

print(list(itertools.chain('ABC','abc')))

# groupby() 把迭代器相邻的重复元素挑在一起
for key,group in itertools.groupby('AABBCCGGDDAAHCCJJS'):
    print(key,list(group))

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
