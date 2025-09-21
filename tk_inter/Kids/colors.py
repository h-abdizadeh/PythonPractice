from tkinter import *
from random import choice

def selectColor():
    list=['red','green','blue','yellow','pink','teal','black']
    c=choice(list)
    app['bg']=c

app=Tk()
app.geometry('300x300')

btn=Button(app,text='color',font='impact 36')
btn.pack()
btn['command']=selectColor

app.mainloop()