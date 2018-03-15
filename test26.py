#! /usr/bin/env python3
# filter过滤函数
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例：在list删去偶数 保留奇数
def is_odd(n):
    return n % 2 ==1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

# 把序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# filter筛选素数

# 构造从3开始的奇数序列
def _odd_iter():
    n=1
    while True:
        n = n+2
        yield n
# 筛选函数
def _not_divisible(n):
    return lambda x:x%n>0
# 生成器 个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 因为odd构建的序列是1000内的奇数，所以不需要从2开始筛选
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # print(n)
        it = filter(_not_divisible(n),it)
 

for n in primes():
    if n<1000:
        print(n)
    else:
         break


def is_palindrome(n):
    nn = str(n)
    return nn == nn[::-1]
print(list(filter(is_palindrome,range(1,1000))))
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，
# 所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

