# encoding: utf-8
from tkinter import *
import re
import sys

root = Tk()

Label(root,text=u'正则表达式:').grid(row=0,column=0)
Label(root,text=u'测试字符串:').grid(row=1,column=0)
Label(root,text=u'是否匹配  :').grid(row=2,column=0)
 
v1=StringVar()
v2=StringVar()
v3=StringVar()

e1 = Entry(root,textvariable=v1)
e2 = Entry(root,textvariable=v2)
e3 = Entry(root,textvariable=v3,state = "readonly")

e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
e3.grid(row=2,column=1,padx=10,pady=5)


def show():
    p1=e1.get()
    str=e2.get()
    pattern1=re.compile(r'' + p1 + '')
    matcher1=re.search(pattern1, str)
    print(u"正则表达式:%s" % e1.get())
    print(u"测试字符串:%s" % e2.get())
    try:
        print(u"测试结果  :%s" % matcher1.group(0))
        v3.set(u"匹配")
    except AttributeError:
        v3.set(u"不匹配")
        print(u"测试结果  :不匹配")

Button(root,text=u'测试',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text=u'退出',width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)

mainloop()