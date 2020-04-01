from tkinter import Tk,Label,Entry,Menu,Button,Pack,Grid
import tkinter.messagebox
import datetime


global i,cka,ck,w,ck,xm,nl,yw,sx,yy,zzd


def ksxz():
   ksxz = Tk() 
   ksxz.title("登录")
   Label(ksxz,textvariable="请选择您的年级")


def yusuan(xm,nl,yw,sx,yy):
   if xm == "刘家朋":
      a = 0
   elif xm == "朱笑阳":
      a = 10000
   elif xm == "何煜霖":
      a = 10
   else:
      a = nl//5
      a = a+100*3-yw-sx-yy
   return a


def mmpd():
   global i,cka,w
   i = w.get()
   we = open("./mima.txt","r")
   mima = we.read()
   we.close()
   if i == mima:
      wo = open("./record.txt","r")
      q = wo.read()
      wo.close()
      label = Label(cka,text=q)
      label.pack()
      Button(cka,text="完成",command=cka.destroy).pack() 
      cka.mainloop()
   else:    
      cka.quit()
      cka.destroy()
      tkinter.messagebox.showerror("错误","密码输入不正确")


def syjl():
   global i,cka,w
   cka = Tk()
   w = Entry(cka,show="*")
   w.pack()
   Button(cka,text="确认",command=mmpd).pack()
   cka.mainloop()
   
   
def gyjsj():
   tkinter.messagebox.showinfo("关于计算机","此软件可用于windows，linux。PS:试试输入朱笑阳，刘家朋或何煜霖。")
   
   
def gyzzr():
   tkinter.messagebox.showinfo("关于制作人","该软件由刘家朋制作，侵权必究")


def kscs():
   global xm,nl,yw,sx,yy,zzd
   try:
      _xm = xm.get()
      _nl = int(nl.get())
      _yw = int(yw.get())
      _sx = int(sx.get())
      _yy = int(yy.get())
      dt = datetime.datetime.now()
      zzd = yusuan(_xm,_nl,_yw,_sx,_yy)
   except Exception:
      tkinter.messagebox.showerror("错误","请输入全部条件")
   try:
      if zzd <= 10:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，智商极高\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，属于智商极高类",fg="red").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()
      elif zzd <= 50:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，智商较高\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，属于智商较高类",fg="orange").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()
      elif zzd <= 70:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，智商正常\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，属于智商正常类",fg="blue").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()
      elif zzd <= 120:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，智商较低\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，属于智商较低类",fg="green").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()
      elif zzd <= 180:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，智商极低\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，属于智商极低类",fg="black").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()
      else:
         awd = open("./record.txt","a")
         awd.write(f"时间：{dt}，姓名：{_xm}，年龄：{_nl}，语文：{_yw}，数学：{_sx}，英语：{_yy}，非人类\n")
         awd.close()
         ckb = Tk()
         Label(ckb,text=f"{_xm},您的智障度为{zzd}，不属于人类",fg="white",bg="black").pack()
         Button(ckb,text="确定",command=ckb.destroy).pack() 
         ckb.mainloop()	
   except NameError:
      pass	 

 
def cdgui(): 
   global ck     
   cd = Menu(ck)
   ck.config(menu=cd)
   font=("黑体", 30, "bold")
   wj = Menu(cd,tearoff=0,font=font,bg="white",fg="black")
   cd.add_cascade(label="文件",menu=wj)
   wj.add_command(label="退出",command=exit)
   wj.add_separator()
   wj.add_command(label="使用记录",command=syjl)
   gy = Menu(cd,tearoff=0,font=font,bg="white",fg="black")  
   cd.add_cascade(label="关于",menu=gy)
   gy.add_command(label="关于计算机",command=gyjsj)
   gy.add_separator()
   gy.add_command(label="关于制作人",command=gyzzr)


def buju():
   global ck,xm,nl,yw,sx,yy
   Label(ck,text="姓名：").grid(row=0)
   xm = Entry(ck)
   xm.grid(row=0,column=1)
   Label(ck,text="年龄：").grid(row=0,column=2)
   nl = Entry(ck)
   nl.grid(row=0,column=3)
   Label(ck,text="语文：").grid(row=1,column=0)
   yw = Entry(ck)
   yw.grid(row=1,column=1)
   Label(ck,text="数学：").grid(row=1,column=2)
   sx = Entry(ck)
   sx.grid(row=1,column=3)
   Label(ck,text="英语：").grid(row=2,column=0)
   yy = Entry(ck)
   yy.grid(row=2,column=1)
   Button(ck,text="测试",width=19,command=kscs).grid(row=2,column=3)


def rkgui():
   ck.withdraw()
   tkinter.messagebox.showwarning("一封古老的诅咒","据说，当你看到这封诅咒时，你就会变傻！！！")
   tkinter.messagebox.showwarning("一封古老的诅咒","只有通过测试，才能找回你的智商")
   ck.deiconify()
   cdgui()
   buju()
   
 
if __name__ == '__main__':
   ck = Tk()
   ck.title("智障度检测机")
   rkgui()
   ck.mainloop()

