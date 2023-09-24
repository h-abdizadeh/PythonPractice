from tkinter import *
import time
def Counter():
    start=int(entry1.get())

    while start>=0:
        label1['text']=start
        start-=1
        app.update()
        time.sleep(1)



app=Tk()
app.geometry('256x256')

entry1=Entry(app,font=('',21),justify=CENTER)
entry1.insert(INSERT,100)
entry1.pack()

label1=Label(app,font=('',64))
label1.pack()

btn1=Button(app,font=('',21),text='START',command=Counter)
btn1.pack()

app.mainloop()