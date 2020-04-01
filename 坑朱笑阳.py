from tkinter import *
import tkinter.messagebox


def qw_qw(q):   
   if q == "朱笑阳":
      i = "是猪"      
   elif q == "刘家朋":
      i = "是天才" 
   elif q == "杨光坤":
      i = "天才他妈"
   else:
      i = "是人"   
   return i
		

def pr():
   label = Label(top,text = qw_qw(w.get()))
   label.pack()

		
top = Tk()
w = Entry(top)
w.pack()
Button(top,text="测试",command=pr).pack()
Button(top,text="退出",command=top.destroy).pack()
top.mainloop() 
xw = Tk()
Label(xw,textvariable="请输入您的意见").pack()
Entry(xw).pack()
Button(xw,text="提交",command=xw.destroy).pack()
xw.mainloop()
tkinter.messagebox.showinfo("关于提示","感谢您的参与！")