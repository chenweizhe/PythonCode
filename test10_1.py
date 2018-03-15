#! /usr/bin/env python3
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
#帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：   
'''
多行注释用三引号
'''

h = input('请输入小明的身高：')
w = input('请输入小明的体重：')
height = float(h)
weight = float(w)
BMI = weight/height
if BMI < 18.5 :
    print('小明过轻,%f' %(BMI))
elif  BMI>=18.5 and BMI<25 :
    print('正常，%f' %(BMI))
elif BMI>=25 and BMI<28 :
    print('过重,%f' %(BMI))
elif  BMI >= 28 and BMI<32 :
    print('肥胖,%f' %(BMI))
else:
    print('严重肥胖,%f' %(BMI))