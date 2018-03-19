#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-19 00:20:30 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-19 00:20:30 
 * @Desc: SQLAlchemy
'''
# 数据库表是一个二维表 包含多行多列 把一个表的内容用Python表示出来的话
# 可以使用一个list表表示多行,每一个list每一个元素是tuple,表示一行记录
# 例如:
[
    ('1','dage'),
    ('2','erge'),
    ('3','sange')
]

# 但是用tuple很难看出表示的结构,如果把一个tuple用[Class实例出来,就更容易看出表的结构
class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

[
    User('1','dage'),
    User('2','erge'),
    User('3','sange')
]

#这就是ORM技术:object-relational Mapping 将关系数据库的表结构映射到对象上
#由ORM框架来做转换,最有名的就是SQLAlchemy
# 第一步:导入SQLAlchemy,并初始化DBSession

# 导入
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base  = declarative_base()

# 定义user对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

'''create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：

'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
你只需要根据需要替换掉用户名、口令等信息即可。

'''
# ORM有了以后 我们向数据库表添加一行记录,可以视为一行记录,可以视为一个user对象
# 创建DBSession对象
session  = DBSession()
# 创建新的user对象
new_user = User(id='5',name='Bob')
# 添加到Session
session.add(new_user)
# 提交保存到数据库
session.commit()
# 关闭session
session.close()


