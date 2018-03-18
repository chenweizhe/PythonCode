#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-18 09:36:17 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-18 09:36:17 
 * @Desc: 图形界面输入文本
'''

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alerButton = Button(self,text='hello',command=self.hello)
        self.alerButton.pack()
        self.quitButton = Button(self,text='quit',command=self.quit)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('message','hello %s' %name)

app = Application()
app.master.title('hello world')
# 主消息循环
app.mainloop()

# 用户点击按钮时 触发hello()