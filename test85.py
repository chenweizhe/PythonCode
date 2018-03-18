#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 20:01:28 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 20:01:28 
 * @Desc: 数据库的使用
'''

# sqlite--关系数据库
'''表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。

要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库'''

# 导入数据库驱动
import sqlite3
# 连接到SQLite数据库,数据库文件是db文件 如果文件不存在 会自动在当前目录创建

conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行一条sql语句,创建user表
cursor.execute('create table user (id varchar(20) primary key,name var char(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Conn
conn.close()


# 查询操作
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句 
cursor.execute('select * from user where id=?', ('1',))
# 查看查询结果
value = cursor.fetchall()
print(value)
cursor.close()
conn.close()




'''使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数'''
cursor.execute('select * from user where name=? and pwd=?',('abc','password'))

cursor.close
conn.close()
