#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-16 20:30:21 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-16 20:30:21 
 * @Desc: 常见内建模块
'''
# datetime Python处理时间和日期的标准库

# 获取当前时间和日期
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期或时间

dt = datetime(2015,6,21,12,20)
print(dt)

# datetime转换为timestamp 
'''在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。'''
'''timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的'''
# datetime转换为timestamp只需要简单调用timestamp()方法
from datetime  import datetime
dt  = datetime(2018,3,16,20,40)
print(dt.timestamp())
'''Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法'''

# timestamp也可以直接转换到UTC标准时区时间:
from datetime import datetime
t = 1521204000.0
print(datetime.utcfromtimestamp(t))

# str转datetime 通过datetime.strptime()实现,需要一个日期和时间的格式化字符串
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
# datetime转str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# 需要导入timedelta这个类

from  datetime import datetime,timedelta
now = datetime.now()
n = now + timedelta(hours=10)
print(n)
n = now - timedelta(days=1)
print(n)
n = now + timedelta(days=1,hours=5)
print(n)

# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区

from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换
# 先通过utcnow()拿到当前UTC时间,再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
'''时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。'''

# 要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
