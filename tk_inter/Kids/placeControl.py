from tkinter import *

def up():
    y1=btnBox.winfo_y()
    y1=y1-5
    btnBox.place(y=y1)

def down():
    y1=btnBox.winfo_y()
    y1=y1+5
    btnBox.place(y=y1)

def left():
    x1=btnBox.winfo_x()
    x1=x1-5
    btnBox.place(x=x1)

def right():
    x1=btnBox.winfo_x()
    x1=x1+5
    btnBox.place(x=x1)

app=Tk()
app.geometry('300x300')

btnUp=Button(app,text='up',command=up)
btnUp.place(x=135,y=10)

btnDown=Button(app,text='down',command=down)
btnDown.place(x=135,y=265)

btnLeft=Button(app,text='left',command=left)
btnLeft.place(x=10,y=140)

btnRight=Button(app,text='right',command=right)
btnRight.place(x=255,y=140)

btnBox=Button(app,width=2,bg='red')
btnBox.place(x=140,y=140)

app.mainloop()