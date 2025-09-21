from tkinter import *
import time

def start():
    ms=label2['text']
    while ms<99:
        ms=ms+1
        label2['text']=ms
        app.update()
        time.sleep(0.001)
        if stop.get()==True:
            return
    else:
        ms=0
        label2['text']=ms
        se=label1['text']
        se=se+1
        label1['text']=se
        start()

def Reset():
    if stop.get()== False:
        stop.set(True)
    else:
        label1['text']=0
        label2['text']=0
        stop.set(False)

app=Tk()

label1=Label(app,text=0,font='impact 48')
label1.pack()

label2=Label(app,text=0,font='impact 21')
label2.pack()

btnStart=Button(app,text='start',font='impact 32',command=start)
btnStart.pack()

btnreset=Button(app,text='reset',font='impact 21',command=Reset)
btnreset.pack()

stop=BooleanVar(app,False)

app.mainloop()