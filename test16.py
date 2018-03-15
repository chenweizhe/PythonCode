#!/usr/bin/env python3

# 递归函数 自身调用自身

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
print(fact(6))

# 递归函数的优点是定义简单，逻辑清晰。
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 使用递归需要防止栈溢出
# 解决递归调用栈溢出的方法是通过尾递归优化，
# 事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的。
'''尾递归是指，在函数返回的时候，
调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''
def fact_1(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1,product*num)

print(fact_1(9))

# 练习 
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法


def move(n,a,b,c):
    if n == 1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
print(move(3,'A','B','C'))