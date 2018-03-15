#! /usr/bin/env python3

dictts = {'dage':88,'erge':77,'sange':66}
print(dictts)

print(dictts['dage'])

if 'erge' in dictts:
    print(dictts.get('erge'))

dictts.pop('dage')
print(dictts)

# dict的key为不可变对象

#set的使用
setts = set([1,2,3])
print(setts)

setts.add(4)
print(setts)

setts.remove(2)
print(setts)
# list是可变对象 所以我们才能改变set元素 但是set是不可变对象
