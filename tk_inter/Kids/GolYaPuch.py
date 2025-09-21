from tkinter import *
from random import randint

def gol():
    btnLeft['text']='چپ'
    btnRight['text']='راست'
    n.set(randint(1,2))

def btnClick():
    # print(n)
    if n.get() == 1:
        btnLeft['text']='*'
        btnRight['text']=''
    else:
        btnLeft['text']=''
        btnRight['text']='*'

app=Tk()
app.geometry('300x200')
app.resizable(False,False)
app.title('گل یا پوچ : گل کجاست؟')

btnLeft=Button(app,text='چپ',font='tahoma 32',width=5)
btnLeft.place(x=10,y=20)
btnLeft['command']=btnClick


btnRight=Button(app,text='راست',font='tahoma 32',width=5)
btnRight.place(x=155,y=20)
btnRight['command']=btnClick

btnStart=Button(app,text='شروع مجدد',font='tahoma')
btnStart.place(x=100,y=150)
btnStart['command']=gol

n=IntVar(app)
gol()
app.mainloop()