#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 23:52:17 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 23:52:17 
 * @Desc: MySql
'''
# 导入mysql驱动
import mysql.connector
# 连接数据库
conn = mysql.connector.connect(user='root', password='password', database='test')
# cursor = conn.cursor()
# # 创建user表
# cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# # 插入一行记录,注意Mysql的占位符是%s sqlite的占位符是?
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# conn.commit()
# cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
'''执行INSERT等操作后要调用commit()提交事务；

MySQL的SQL占位符是%s。'''