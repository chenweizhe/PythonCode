#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 09:25:11 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 09:25:11 
 * @Desc: 摘要算法(哈希算法,散列算法)
'''
# Python的hashlib提供了常见的摘要算法,如MD5,SHA1
'''要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
'''
import hashlib
md5  = hashlib.md5()
md5.update('how to use md5 in Python'.encode('utf-8'))
print(md5.hexdigest())

# 数据量大时,可以多次调用update(),最后计算结果是一样的

md5 = hashlib.md5()
md5.update('how to use md5 in'.encode('utf-8'))
md5.update('python'.encode('utf-8'))
print(md5.hexdigest())

# 另一种摘要算法SHA1 调用MD5类似
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python'.encode('utf-8'))
print(sha1.hexdigest())

sha1.update('how to use sha1'.encode('utf-8'))
sha1.update('in python'.encode('utf-8'))

print(sha1.hexdigest())

'''摘要算法应用
任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：

name	password
michael	123456
bob	abc999
alice	alice2008
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：

username	password
michael	e10adc3949ba59abbe56e057f20f883e
bob	878ef96e86145580c38c87f0410ad153
alice	99b1c2188db85afee403b1536010c2c9
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误'''
