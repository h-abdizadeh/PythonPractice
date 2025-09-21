from tkinter import *

def subtitle():
        lx=label2.winfo_x()
        if lx>400:
            lx=-label2.winfo_width()
        label2.place(x=lx+1)
        app.after(10,subtitle)

def addNews():
      news=entry1.get()
      oldnews=label2['text']
      label2['text']=oldnews +' *** '+ news

app=Tk()
app.geometry('400x100')
app.resizable(False,False)
app.title('شبکه خبر')

entry1=Entry(app,width=50)
entry1.place(x=75,y=10)

btn1=Button(app,text='ثبت',command=addNews)
btn1.place(x=10,y=10)

label2=Label(app,text='hello world, python',font='tahoma 18 italic' )
label2.place(x=10,y=55)

label1=Label(app,text='اخبار',width=5,
             font='tahoma 24',bg='teal',fg='white')
label1.place(x=310,y=55)



subtitle()
app.mainloop()