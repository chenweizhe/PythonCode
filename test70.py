#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 14:03:35 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 14:03:35 
 * @Desc: urllib
'''

# urllib提供了一系列用于操作URL的功能

# get 
# urllib 的request模块可以非常方便抓取URL内容,也就是发送一个GET请求到指定页面,然后返回http的响应

# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' %(k,v))
#     print('Data:',data.decode('utf-8'))

# 模拟浏览器发送get请求 就需要request对象---添加HTTP头 就可以伪装成浏览器
# 模拟IPhone6
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))
# 这样豆瓣就会返回iPhone的移动版网页

# POST请求
# 模拟微博登录,先读取登录的邮箱和口令,按微博登录页格式传入编码
from urllib import request,parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')


with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' %(k,v))
    print('Data: ',f.read().decode('utf-8'))

'''urllib提供的功能就是利用程序去执行各种HTTP请求。
如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。'''