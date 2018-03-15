#! /usr/bin/env python3

L = []
n=1
while n <= 99:
    L.append(n)
    n+=2

print(L)

L_1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取list或者tuple的部分数据
# slice切片操作符
print(L_1[0:3]) 
#如果第一个索引为0还可以省略
print(L_1[:3])

print(L_1[1:3])

# python支持倒数切片
print(L_1[-2:])
print(L_1[-2:-1])

print(L[-10:])
# 每两个取一个
print(L[:10:2])
# 每五个取一个
print(L[::5])
# 啥都不写也可以再复制一个一样的list
print(L[:])

# tuple可以切片 将字符串看成list 字符串也可以切片
print((0,1,2,3,4,5,6,7,8)[0:5])
print('asdfghjkl'[::2])

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(str1):
    n = len(str1)
    str1 = str1[1:n-1]
    return str1
print(trim('sadsadassadasd'))


