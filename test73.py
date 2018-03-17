#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 14:56:14 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 14:56:14 
 * @Desc: HTMLParser 解析网页用的 比如用爬虫抓取目标网站的页面,第二步就是解析该页面
'''

from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHtmlParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' %tag)
    
    def handle_endtag(self,tag):
        print('</%s>' %tag)

    def handle_startendtag(self,tag,attrs):
        print('<%s/>' %tag)
    
    def handle_data(self,data):
        print(data)
    def handle_comment(self,data):
        print('<!--',data,'-->')
    def handle_entityref(self,name):
        print('&%s;' %name)
    def handle_charref(self,name):
        print('&#%s;' %name)
    
parser = MyHtmlParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

'''feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。'''

