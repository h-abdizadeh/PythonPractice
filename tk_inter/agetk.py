from tkinter import *

def month():
    age=int(e1.get())
    m=age*12
    from tkinter import messagebox
    messagebox.showinfo(m)

def day():
    age=int(e1.pack())
    d=age*365
    from tkinter import messagebox
    messagebox.showinfo(d)

app=Tk()

e1=Entry(app,font='impact 24',width=5)
e1.pack()

b1=Button(app,text='محاسبه سن به ماه')
b1.pack()
b1['command']=month

b2=Button(app,text='محاسبه سن به روز')
b2.pack()
b2['command']=day

app.mainloop()
