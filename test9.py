#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

T = (1,2,[4,5])
print(T[1])
print(T[2][1])
T[2][0] = 99
print(T[2][0])