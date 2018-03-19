#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-19 09:26:40 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-19 09:26:40 
 * @Desc: 
'''
# 导入:
import mysql.connector
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# 查询数据时,不是吐tuple对象而是user对象
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

# 关系数据库的多个表可以用外键实现一对多 多对多等关联,ORM框架也提供两个对象之间一对多,多对多的等功能 通过relationship()函数
# 如果一个User拥有多个book,就可以定义一对多的关系
class User(Base):
    __tablename__='user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')
class Book(Base):
    __tablename__='book'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # '多'的一方的book表是通过外键关联到user表
    user_id = Column(String(20),ForeignKey('user.id'))

# ORM框架的作用就是把数据库表的一行记录与一个对象互做自动转换