#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-17 14:38:30 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-17 14:38:30 
 * @Desc: XML
'''
# 操作XML有两种方法:DOM和SAX DOM会把整个XML读入内存 解析为树 因此占用内存大 解析慢 优点是可以任意遍历树的节点
# SAX是流模式,边读边解析 占用内存小,解析块 缺点是需要自己处理事件
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:end_element:%s' %name)
    def end_element(self,name):
        print('sax:end_element:%s' %name)
    def char_data(self,text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成XML
# L =[]
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# ''.join(L)