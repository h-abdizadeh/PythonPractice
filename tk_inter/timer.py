from tkinter import *
import time
def counter():
    while True:
        n=label1['text']
        label1['text']=n+1
        app.update()
        time.sleep(0.1)

def counter2():
    n=label1['text']
    label1['text']=n+1
    app.after(100,counter2)

app=Tk()
label1=Label(app,text=0,font='impact 36')
label1.pack()
# counter()
counter2()
app.mainloop()