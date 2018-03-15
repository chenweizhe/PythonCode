# 如果将my_abs()函数保存为py文件 可以在该文件目录下启动Python解释器 使用 
# from test13 import my_abs 注意 test13是文件名 不需要加拓展名

from test13 import my_abs
import math

print(my_abs(-999)) 

#练习
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0的两个解。
提示：计算平方根可以调用math.sqrt()函数：
'''
def quadratic(a,b,c):
   nx =  (-b+math.sqrt(b*b-4*a*c))/2*a
   ny = (-b-math.sqrt(b*b-4*a*c))/2*a
   return nx,ny


print(quadratic(1,-2,1))